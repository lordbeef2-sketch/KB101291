# JAVA OPENAPI: ProjectEventListenerAdapter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/project/ProjectEventListenerAdapter.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectEventListenerAdapter.html`
- source_sha256: `0db016a0a8aee71bf7f22ff8e5416f10902b1b5977e64ebc0ba2d29c3eb46dcf`
- captured_utc: `2026-07-14T16:45:31.739424+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Class ProjectEventListenerAdapter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter

All Implemented Interfaces:
`[ProjectEventListener](ProjectEventListener.html)`

Direct Known Subclasses:
`[ProjectEventListenerAdapter2](ProjectEventListenerAdapter2.html)`, `com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter`, `[SpecificationDialogManager](../../ui/dialogs/specifications/SpecificationDialogManager.html)`

@OpenApiAllpublic classProjectEventListenerAdapter
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [ProjectEventListener](ProjectEventListener.html)

Event listener for project events.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectEventListenerAdapter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
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
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](ProjectEventListener.html)
`[projectPreOpenedFromGUI](ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectUsedFromGUI](ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectEventListenerAdapter
public ProjectEventListenerAdapter()
 ============ METHOD DETAIL ========== 
Method Details
projectOpened
public void projectOpened([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project))`
Method is called when project was opened, created or loaded from teamwork server.
 Opened project is active project and no projectActivated(Project) is called for this project.
Specified by:
`[projectOpened](ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which was opened.
See Also:
[`ProjectEventListener.projectActivated(Project)`](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))
projectClosed
public void projectClosed([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project))`
Method is called after closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "projectClosed" in this step.
Specified by:
`[projectClosed](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which was closed.
See Also:
[`ProjectEventListener.projectClosed(Project)`](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project))
projectSaved
public void projectSaved([Project](../Project.html) project,
 boolean savedInServer)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))`
Method is called when project is saved or exported in Unisys format.
 This method is not called when saving project module.
Specified by:
`[projectSaved](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which was saved.
`savedInServer` - true if project was sent to teamwork server.
See Also:
[`ProjectEventListener.projectSaved(Project, boolean)`](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))
projectActivated
public void projectActivated([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))`
Method is called when inactive project became active project.
Specified by:
`[projectActivated](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - new active project.
See Also:
[`ProjectEventListener.projectActivated(Project)`](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project))
projectDeActivated
public void projectDeActivated([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project))`
Method is called when active project becomes not active.
Specified by:
`[projectDeActivated](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - inactive project.
See Also:
[`ProjectEventListener.projectDeActivated(Project)`](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project))
projectReplaced
public void projectReplaced([Project](../Project.html) oldProject,
 [Project](../Project.html) newProject)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))`
The method is called when one project is replaced with
 (logically equivalent) another project.
 Such situation occurs, for example, when local project is added to teamwork.
 In this case the local project is added to teamwork, local project is closed
 and teamwork project is opened. This results in the notification about old
 project replacement with the new project
Specified by:
`[projectReplaced](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`oldProject` - the project, which was replaced
`newProject` - the project, which replaced the old project
See Also:
[`ProjectEventListener.projectReplaced(Project, Project)`](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))
projectPreClosed
public void projectPreClosed([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project))`
Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is not marked as "closing" in this step.
Specified by:
`[projectPreClosed](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which will be closed.
See Also:
[`ProjectEventListener.projectPreClosed(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project))
projectPreClosedFinal
public void projectPreClosedFinal([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project))`
Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "closing" in this step.
Specified by:
`[projectPreClosedFinal](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which will be closed.
See Also:
[`ProjectEventListener.projectPreClosedFinal(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project))
projectPreSaved
public void projectPreSaved([Project](../Project.html) project,
 boolean savedInServer)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean))`
Method is called when project is going to be saved.
 This method is not called when saving project module.
Specified by:
`[projectPreSaved](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which will be saved.
`savedInServer` - true if project will be sent to a teamwork server.
See Also:
[`ProjectEventListener.projectPreSaved(com.nomagic.magicdraw.core.Project, boolean)`](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean))
projectPreActivated
public void projectPreActivated([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project))`
Method is called before inactive project will become an active project.
Specified by:
`[projectPreActivated](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - a new active project.
See Also:
[`ProjectEventListener.projectPreActivated(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project))
projectPreDeActivated
public void projectPreDeActivated([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project))`
Method is called before active project will become not active.
Specified by:
`[projectPreDeActivated](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - an inactive project.
See Also:
[`ProjectEventListener.projectPreDeActivated(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project))
projectCreated
public void projectCreated([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project))`
Method is called when project is created, but before activating and opening it.
Specified by:
`[projectCreated](ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which was created.
See Also:
[`ProjectEventListener.projectClosed(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project))
projectActivatedFromGUI
public void projectActivatedFromGUI([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project))`
Method is called when inactive project became active project by user action, not from code.
Specified by:
`[projectActivatedFromGUI](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - new active project.
See Also:
[`ProjectEventListener.projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project))
projectOpenedFromGUI
public void projectOpenedFromGUI([Project](../Project.html) project)
Description copied from interface: `[ProjectEventListener](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project))`
Method is called when project was opened, created or loaded from teamwork server by user action, not from code.
 It is very useful if you want to show any dialog, which can be shown only if user itself open project.
Specified by:
`[projectOpenedFromGUI](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project))` in interface `[ProjectEventListener](ProjectEventListener.html)`
Parameters:
`project` - project which was opened.
See Also:
[`ProjectEventListener.projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)`](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Class ProjectEventListenerAdapter">Class ProjectEventListenerAdapter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ProjectEventListenerAdapter2.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter2</a></code>, <code>com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter</code>, <code><a href="../../ui/dialogs/specifications/SpecificationDialogManager.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationDialogManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectEventListenerAdapter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></span></div>
<div class="block">Event listener for project events.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectEventListenerAdapter</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when inactive project became active project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when inactive project became active project by user action, not from code.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called after closing the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when project is created, but before activating and opening it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when active project becomes not active.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when project was opened, created or loaded from teamwork server.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when project was opened, created or loaded from teamwork server by user action, not from code.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called before inactive project will become an active project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called before closing the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called before closing the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called before active project will become not active.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when project is going to be saved.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> oldProject,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> newProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method is called when one project is replaced with
 (logically equivalent) another project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method is called when project is saved or exported in Unisys format.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></h3>
<code><a href="ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a></code></div>
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
<h3>ProjectEventListenerAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectEventListenerAdapter</span>()</div>
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
<section class="detail" id="projectOpened(com.nomagic.magicdraw.core.Project)">
<h3>projectOpened</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectOpened</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when project was opened, created or loaded from teamwork server.
 Opened project is active project and no projectActivated(Project) is called for this project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectClosed(com.nomagic.magicdraw.core.Project)">
<h3>projectClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectClosed</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called after closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "projectClosed" in this step.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which was closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectClosed(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectSaved(com.nomagic.magicdraw.core.Project,boolean)">
<h3>projectSaved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectSaved</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when project is saved or exported in Unisys format.
 This method is not called when saving project module.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which was saved.</dd>
<dd><code>savedInServer</code> - true if project was sent to teamwork server.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)"><code>ProjectEventListener.projectSaved(Project, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when inactive project became active project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - new active project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectDeActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectDeActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectDeActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when active project becomes not active.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - inactive project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectDeActivated(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>projectReplaced</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectReplaced</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> oldProject,
 <a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> newProject)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">The method is called when one project is replaced with
 (logically equivalent) another project.
 Such situation occurs, for example, when local project is added to teamwork.
 In this case the local project is added to teamwork, local project is closed
 and teamwork project is opened. This results in the notification about old
 project replacement with the new project</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>oldProject</code> - the project, which was replaced</dd>
<dd><code>newProject</code> - the project, which replaced the old project</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectReplaced(Project, Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreClosed(com.nomagic.magicdraw.core.Project)">
<h3>projectPreClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPreClosed</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is not marked as "closing" in this step.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectPreClosed(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">
<h3>projectPreClosedFinal</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPreClosedFinal</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called before closing the project. Close operation has three steps - preClose, preCloseFinal and projectClosed.
 Project is marked as "closing" in this step.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectPreClosedFinal(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">
<h3>projectPreSaved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPreSaved</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean savedInServer)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when project is going to be saved.
 This method is not called when saving project module.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which will be saved.</dd>
<dd><code>savedInServer</code> - true if project will be sent to a teamwork server.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)"><code>ProjectEventListener.projectPreSaved(com.nomagic.magicdraw.core.Project, boolean)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectPreActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPreActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called before inactive project will become an active project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - a new active project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectPreActivated(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPreDeActivated(com.nomagic.magicdraw.core.Project)">
<h3>projectPreDeActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPreDeActivated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called before active project will become not active.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - an inactive project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectPreDeActivated(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectCreated(com.nomagic.magicdraw.core.Project)">
<h3>projectCreated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectCreated</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when project is created, but before activating and opening it.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which was created.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectClosed(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>projectActivatedFromGUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectActivatedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when inactive project became active project by user action, not from code.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - new active project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">
<h3>projectOpenedFromGUI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectOpenedFromGUI</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">ProjectEventListener</a></code></span></div>
<div class="block">Method is called when project was opened, created or loaded from teamwork server by user action, not from code.
 It is very useful if you want to show any dialog, which can be shown only if user itself open project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a></code> in interface <code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project which was opened.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)"><code>ProjectEventListener.projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)</code></a></li>
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
