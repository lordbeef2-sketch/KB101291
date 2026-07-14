# JAVA OPENAPI: ProjectEventListener (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/core/project/ProjectEventListener.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectEventListener.html`
- source_sha256: `790ed88119f9ec8c7a81e7d3db3c9732b0f090c8c135541f67cbb8d6ac30f460`
- captured_utc: `2026-07-14T16:57:52.847478+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Interface ProjectEventListener

All Known Subinterfaces:
`[ProjectPartListener](ProjectPartListener.html)`, `[ProjectPartLoadedListener](ProjectPartLoadedListener.html)`

All Known Implementing Classes:
`[ProjectEventListenerAdapter](ProjectEventListenerAdapter.html)`, `[ProjectEventListenerAdapter2](ProjectEventListenerAdapter2.html)`, `[ProjectPartListenerAdapter](ProjectPartListenerAdapter.html)`, `com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter`, `[SpecificationDialogManager](../../ui/dialogs/specifications/SpecificationDialogManager.html)`

@OpenApiAllpublic interfaceProjectEventListener

Event listener for project events.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[projectActivated](#projectActivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called when inactive project became active project.
`void`
`[projectActivatedFromGUI](#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called when inactive project became active project by user action, not from code.
`void`
`[projectClosed](#projectClosed(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called after closing the project.
`void`
`[projectCreated](#projectCreated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called when project is created, but before activating and opening it.
`void`
`[projectDeActivated](#projectDeActivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called when active project becomes not active.
`void`
`[projectOpened](#projectOpened(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called when project was opened, created or loaded from teamwork server.
`void`
`[projectOpenedFromGUI](#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called when project was opened, created or loaded from teamwork server by user action, not from code.
`void`
`[projectPreActivated](#projectPreActivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called before inactive project will become an active project.
`void`
`[projectPreClosed](#projectPreClosed(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called before closing the project.
`void`
`[projectPreClosedFinal](#projectPreClosedFinal(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called before closing the project.
`void`
`[projectPreDeActivated](#projectPreDeActivated(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called before active project will become not active.
`default void`
`[projectPreOpenedFromGUI](#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project))([Project](../Project.html) project)`
Method is called before (method #projectOpenedFromGUI) project was opened, created or loaded from teamwork server by user action, not from code.
`void`
`[projectPreSaved](#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean))([Project](../Project.html) project,
 boolean savedInServer)`
Method is called when project is going to be saved.
`void`
`[projectReplaced](#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))([Project](../Project.html) oldProject,
 [Project](../Project.html) newProject)`
The method is called when one project is replaced with
 (logically equivalent) another project.
`void`
`[projectSaved](#projectSaved(com.nomagic.magicdraw.core.Project,boolean))([Project](../Project.html) project,
 boolean savedInServer)`
Method is called when project is saved or exported in Unisys format.
`default void`
`[projectUsedFromGUI](#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)`
Method is called when some project was used from GUI

============ METHOD DETAIL ========== 
Method Details
projectOpened
void projectOpened([Project](../Project.html) project)
Method is called when project was opened, created or loaded from teamwork server.
 Opened project is active project and no projectActivated(Project) is called for this project.
Parameters:
`project` - project which was opened.
See Also:
[`projectActivated(Project)`](#projectActivated(com.nomagic.magicdraw.core.Project))
projectClosed
void projectClosed([Project](../Project.html) project)
Method is called after closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "projectClosed" in this step.
Parameters:
`project` - project which was closed.
See Also:
`Project.isProjectClosed()`
projectSaved
void projectSaved([Project](../Project.html) project,
 boolean savedInServer)
Method is called when project is saved or exported in Unisys format.
 This method is not called when saving project module.
Parameters:
`project` - project which was saved.
`savedInServer` - true if project was sent to teamwork server.
projectActivated
void projectActivated([Project](../Project.html) project)
Method is called when inactive project became active project.
Parameters:
`project` - new active project.
projectDeActivated
void projectDeActivated([Project](../Project.html) project)
Method is called when active project becomes not active.
Parameters:
`project` - inactive project.
projectReplaced
void projectReplaced([Project](../Project.html) oldProject,
 [Project](../Project.html) newProject)
The method is called when one project is replaced with
 (logically equivalent) another project.
 Such situation occurs, for example, when local project is added to teamwork.
 In this case the local project is added to teamwork, local project is closed
 and teamwork project is opened. This results in the notification about old
 project replacement with the new project
Parameters:
`oldProject` - the project, which was replaced
`newProject` - the project, which replaced the old project
projectCreated
void projectCreated([Project](../Project.html) project)
Method is called when project is created, but before activating and opening it.
Parameters:
`project` - project which was created.
projectPreClosed
void projectPreClosed([Project](../Project.html) project)
Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is not marked as "closing" in this step.
Parameters:
`project` - project which will be closed.
See Also:
`Project.isClosing()`
projectPreClosedFinal
void projectPreClosedFinal([Project](../Project.html) project)
Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "closing" in this step.
Parameters:
`project` - project which will be closed.
See Also:
`Project.isClosing()`
projectPreSaved
void projectPreSaved([Project](../Project.html) project,
 boolean savedInServer)
Method is called when project is going to be saved.
 This method is not called when saving project module.
Parameters:
`project` - project which will be saved.
`savedInServer` - true if project will be sent to a teamwork server.
projectPreActivated
void projectPreActivated([Project](../Project.html) project)
Method is called before inactive project will become an active project.
Parameters:
`project` - a new active project.
projectPreDeActivated
void projectPreDeActivated([Project](../Project.html) project)
Method is called before active project will become not active.
Parameters:
`project` - an inactive project.
projectOpenedFromGUI
void projectOpenedFromGUI([Project](../Project.html) project)
Method is called when project was opened, created or loaded from teamwork server by user action, not from code.
 It is very useful if you want to show any dialog, which can be shown only if user itself open project.
Parameters:
`project` - project which was opened.
projectPreOpenedFromGUI
default void projectPreOpenedFromGUI([Project](../Project.html) project)
Method is called before (method #projectOpenedFromGUI) project was opened, created or loaded from teamwork server by user action, not from code.
Parameters:
`project` - project which was opened.
projectActivatedFromGUI
void projectActivatedFromGUI([Project](../Project.html) project)
Method is called when inactive project became active project by user action, not from code.
Parameters:
`project` - new active project.
projectUsedFromGUI
default void projectUsedFromGUI([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)
Method is called when some project was used from GUI
Parameters:
`project` - in witch project was used
`using` - project
`used` - project

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Interface ProjectEventListener">Interface ProjectEventListener</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></code>, <code><a href="ProjectPartLoadedListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartLoadedListener</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></code>, <code><a href="ProjectEventListenerAdapter2.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter2</a></code>, <code><a href="ProjectPartListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectPartListenerAdapter</a></code>, <code>com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter</code>, <code><a href="../../ui/dialogs/specifications/SpecificationDialogManager.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationDialogManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectEventListener</span></div>
<div class="block">Event listener for project events.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when inactive project became active project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when inactive project became active project by user action, not from code.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called after closing the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when project is created, but before activating and opening it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when active project becomes not active.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when project was opened, created or loaded from teamwork server.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when project was opened, created or loaded from teamwork server by user action, not from code.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called before inactive project will become an active project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called before closing the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called before closing the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called before active project will become not active.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method is called before (method #projectOpenedFromGUI) project was opened, created or loaded from teamwork server by user action, not from code.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when project is going to be saved.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> oldProject,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> newProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The method is called when one project is replaced with
 (logically equivalent) another project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called when project is saved or exported in Unisys format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method is called when some project was used from GUI</div>
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
<section class="detail" id="projectOpened(com.nomagic.magicdraw.core.Project)">
<h3>projectOpened</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectOpened</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called when project was opened, created or loaded from teamwork server.
 Opened project is active project and no projectActivated(Project) is called for this project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#projectActivated(com.nomagic.magicdraw.core.Project)"><code>projectActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectClosed(com.nomagic.magicdraw.core.Project)">
<h3>projectClosed</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectClosed</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called after closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "projectClosed" in this step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>Project.isProjectClosed()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectSaved(com.nomagic.magicdraw.core.Project,boolean)">
<h3>projectSaved</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectSaved</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</span></div>
<div class="block">Method is called when project is saved or exported in Unisys format.
 This method is not called when saving project module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was saved.</dd>
<dd><code>savedInServer</code> - true if project was sent to teamwork server.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectActivated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called when inactive project became active project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - new active project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectDeActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectDeActivated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectDeActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called when active project becomes not active.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - inactive project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>projectReplaced</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectReplaced</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> oldProject,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> newProject)</span></div>
<div class="block">The method is called when one project is replaced with
 (logically equivalent) another project.
 Such situation occurs, for example, when local project is added to teamwork.
 In this case the local project is added to teamwork, local project is closed
 and teamwork project is opened. This results in the notification about old
 project replacement with the new project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldProject</code> - the project, which was replaced</dd>
<dd><code>newProject</code> - the project, which replaced the old project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectCreated(com.nomagic.magicdraw.core.Project)">
<h3>projectCreated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectCreated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called when project is created, but before activating and opening it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreClosed(com.nomagic.magicdraw.core.Project)">
<h3>projectPreClosed</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPreClosed</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is not marked as "closing" in this step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>Project.isClosing()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">
<h3>projectPreClosedFinal</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPreClosedFinal</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "closing" in this step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>Project.isClosing()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">
<h3>projectPreSaved</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPreSaved</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</span></div>
<div class="block">Method is called when project is going to be saved.
 This method is not called when saving project module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be saved.</dd>
<dd><code>savedInServer</code> - true if project will be sent to a teamwork server.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectPreActivated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPreActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called before inactive project will become an active project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a new active project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreDeActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectPreDeActivated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPreDeActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called before active project will become not active.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - an inactive project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>projectOpenedFromGUI</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectOpenedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called when project was opened, created or loaded from teamwork server by user action, not from code.
 It is very useful if you want to show any dialog, which can be shown only if user itself open project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>projectPreOpenedFromGUI</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">projectPreOpenedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called before (method #projectOpenedFromGUI) project was opened, created or loaded from teamwork server by user action, not from code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>projectActivatedFromGUI</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectActivatedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Method is called when inactive project became active project by user action, not from code.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - new active project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">
<h3>projectUsedFromGUI</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">projectUsedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject using,
 com.nomagic.ci.persistence.IAttachedProject used)</span></div>
<div class="block">Method is called when some project was used from GUI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - in witch project was used</dd>
<dd><code>using</code> - project</dd>
<dd><code>used</code> - project</dd>
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
