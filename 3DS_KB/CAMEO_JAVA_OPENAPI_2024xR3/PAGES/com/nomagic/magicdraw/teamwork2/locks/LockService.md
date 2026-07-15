# JAVA OPENAPI: LockService (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/teamwork2/locks/LockService.html
- source_path: `com/nomagic/magicdraw/teamwork2/locks/LockService.html`
- source_sha256: `fbb41fa27d96b36724f66c9b6951322f2749c8ef814edeb304a801474c4548bf`
- captured_utc: `2026-07-14T16:55:39.044274+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2.locks](package-summary.html)

## Class LockService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[Project](../../core/Project.html)>
com.nomagic.magicdraw.core.project.service.ProjectService
com.nomagic.magicdraw.teamwork2.locks.LockService

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`, `[ILockProjectService](ILockProjectService.html)`

@OpenApiAllpublic abstract classLockService
extends com.nomagic.magicdraw.core.project.service.ProjectService
implements [ILockProjectService](ILockProjectService.html)

Project related lock service. Provides api to check, request and release locks on various project data.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicdraw.teamwork2.locks.[ILockProjectService](ILockProjectService.html)
`[ILockProjectService.LockOptions](ILockProjectService.LockOptions.html)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[LockService](#%3Cinit%3E(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ILockProjectService](ILockProjectService.html)`
`[getLockService](#getLockService(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Return and instance of lock service for a given project
`protected boolean`
`[hasAutomaticUsages](#hasAutomaticUsages(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages)`

`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[selectElementsForLock](#selectElementsForLock(java.util.Collection,java.util.function.Predicate))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collection,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> canBeLocked)`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.teamwork2.locks.[ILockProjectService](ILockProjectService.html)
`[canBeDecompositionLocked](ILockProjectService.html#canBeDecompositionLocked(com.nomagic.ci.persistence.IProject)), [canBeDecompositionUnlocked](ILockProjectService.html#canBeDecompositionUnlocked(com.nomagic.ci.persistence.IProject)), [canBeLocked](ILockProjectService.html#canBeLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)), [canBeLocked](ILockProjectService.html#canBeLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [canBeOptionsLocked](ILockProjectService.html#canBeOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)), [canBeOptionsUnlocked](ILockProjectService.html#canBeOptionsUnlocked(com.nomagic.ci.persistence.IProject,java.lang.String)), [canBeUnlocked](ILockProjectService.html#canBeUnlocked(com.nomagic.magicdraw.core.modules.ModuleUsage)), [canBeUnlocked](ILockProjectService.html#canBeUnlocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getDecompositionLock](ILockProjectService.html#getDecompositionLock(com.nomagic.ci.persistence.IProject)), [getLockedBy](ILockProjectService.html#getLockedBy(java.lang.String)), [getLockedByMe](ILockProjectService.html#getLockedByMe()), [getLockedElements](ILockProjectService.html#getLockedElements()), [getLockedElementUsers](ILockProjectService.html#getLockedElementUsers()), [getLockedModules](ILockProjectService.html#getLockedModules()), [getLockInfo](ILockProjectService.html#getLockInfo(com.nomagic.magicdraw.core.modules.ModuleUsage)), [getLockInfo](ILockProjectService.html#getLockInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [getModulesLockedBy](ILockProjectService.html#getModulesLockedBy(java.lang.String)), [getModulesLockedByMe](ILockProjectService.html#getModulesLockedByMe()), [getOptionsLock](ILockProjectService.html#getOptionsLock(com.nomagic.ci.persistence.IProject,java.lang.String)), [hasLockedBy](ILockProjectService.html#hasLockedBy(java.lang.String)), [hasLockedElements](ILockProjectService.html#hasLockedElements()), [hasPermissionToLock](ILockProjectService.html#hasPermissionToLock(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDecompositionLocked](ILockProjectService.html#isDecompositionLocked(com.nomagic.ci.persistence.IProject)), [isDecompositionLockedByMe](ILockProjectService.html#isDecompositionLockedByMe(com.nomagic.ci.persistence.IProject)), [isLocked](ILockProjectService.html#isLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)), [isLocked](ILockProjectService.html#isLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isLockedBy](ILockProjectService.html#isLockedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [isLockedByMe](ILockProjectService.html#isLockedByMe(com.nomagic.magicdraw.core.modules.ModuleUsage)), [isLockedByMe](ILockProjectService.html#isLockedByMe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isOptionsLocked](ILockProjectService.html#isOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)), [isOptionsLockedByMe](ILockProjectService.html#isOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String)), [lockElements](ILockProjectService.html#lockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)), [lockElements](ILockProjectService.html#lockElements(java.util.Collection,com.nomagic.magicdraw.teamwork2.locks.ILockProjectService.LockOptions,com.nomagic.task.ProgressStatus)), [lockElements](ILockProjectService.html#lockElements(java.util.Collection,com.nomagic.task.ProgressStatus)), [lockModules](ILockProjectService.html#lockModules(java.util.Collection,boolean,boolean,com.nomagic.task.ProgressStatus)), [lockModules](ILockProjectService.html#lockModules(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)), [setCacheOptionsLock](ILockProjectService.html#setCacheOptionsLock(boolean)), [setDecompositionLockedByMe](ILockProjectService.html#setDecompositionLockedByMe(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus)), [setOptionsLockedByMe](ILockProjectService.html#setOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String,boolean,com.nomagic.task.ProgressStatus)), [unlockElements](ILockProjectService.html#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)), [unlockElements](ILockProjectService.html#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,boolean)), [unlockElements](ILockProjectService.html#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,java.util.Collection,boolean)), [unlockElements](ILockProjectService.html#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus)), [unlockElements](ILockProjectService.html#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus,boolean)), [unlockModules](ILockProjectService.html#unlockModules(java.util.Collection,com.nomagic.task.ProgressStatus)), [updateLocks](ILockProjectService.html#updateLocks(com.nomagic.task.ProgressStatus))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
LockService
protected LockService([Project](../../core/Project.html) project)
Constructor
Parameters:
`project` - project
 ============ METHOD DETAIL ========== 
Method Details
getLockService
@CheckForNullpublic static [ILockProjectService](ILockProjectService.html) getLockService(@CheckForNull
 [Project](../../core/Project.html) project)
Return and instance of lock service for a given project
Parameters:
`project` - project
Returns:
lock service
selectElementsForLock
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> selectElementsForLock(@Nonnull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collection,
 [Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> canBeLocked)
hasAutomaticUsages
protected boolean hasAutomaticUsages([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> moduleUsages)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2.locks</a></div>
<h1 class="title" title="Class LockService">Class LockService</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.core.project.service.ProjectService
<div class="inheritance">com.nomagic.magicdraw.teamwork2.locks.LockService</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code>, <code><a href="ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">LockService</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.project.service.ProjectService
implements <a href="ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></span></div>
<div class="block">Project related lock service. Provides api to check, request and release locks on various project data.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicdraw.teamwork2.locks.ILockProjectService">Nested classes/interfaces inherited from interface com.nomagic.magicdraw.teamwork2.locks.<a href="ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></h2>
<code><a href="ILockProjectService.LockOptions.html" title="class in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService.LockOptions</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project)">LockService</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockService(com.nomagic.magicdraw.core.Project)">getLockService</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return and instance of lock service for a given project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAutomaticUsages(java.util.Collection)">hasAutomaticUsages</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#selectElementsForLock(java.util.Collection,java.util.function.Predicate)">selectElementsForLock</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; canBeLocked)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.teamwork2.locks.ILockProjectService">Methods inherited from interface com.nomagic.magicdraw.teamwork2.locks.<a href="ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></h3>
<code><a href="ILockProjectService.html#canBeDecompositionLocked(com.nomagic.ci.persistence.IProject)">canBeDecompositionLocked</a>, <a href="ILockProjectService.html#canBeDecompositionUnlocked(com.nomagic.ci.persistence.IProject)">canBeDecompositionUnlocked</a>, <a href="ILockProjectService.html#canBeLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">canBeLocked</a>, <a href="ILockProjectService.html#canBeLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canBeLocked</a>, <a href="ILockProjectService.html#canBeOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)">canBeOptionsLocked</a>, <a href="ILockProjectService.html#canBeOptionsUnlocked(com.nomagic.ci.persistence.IProject,java.lang.String)">canBeOptionsUnlocked</a>, <a href="ILockProjectService.html#canBeUnlocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">canBeUnlocked</a>, <a href="ILockProjectService.html#canBeUnlocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canBeUnlocked</a>, <a href="ILockProjectService.html#getDecompositionLock(com.nomagic.ci.persistence.IProject)">getDecompositionLock</a>, <a href="ILockProjectService.html#getLockedBy(java.lang.String)">getLockedBy</a>, <a href="ILockProjectService.html#getLockedByMe()">getLockedByMe</a>, <a href="ILockProjectService.html#getLockedElements()">getLockedElements</a>, <a href="ILockProjectService.html#getLockedElementUsers()">getLockedElementUsers</a>, <a href="ILockProjectService.html#getLockedModules()">getLockedModules</a>, <a href="ILockProjectService.html#getLockInfo(com.nomagic.magicdraw.core.modules.ModuleUsage)">getLockInfo</a>, <a href="ILockProjectService.html#getLockInfo(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getLockInfo</a>, <a href="ILockProjectService.html#getModulesLockedBy(java.lang.String)">getModulesLockedBy</a>, <a href="ILockProjectService.html#getModulesLockedByMe()">getModulesLockedByMe</a>, <a href="ILockProjectService.html#getOptionsLock(com.nomagic.ci.persistence.IProject,java.lang.String)">getOptionsLock</a>, <a href="ILockProjectService.html#hasLockedBy(java.lang.String)">hasLockedBy</a>, <a href="ILockProjectService.html#hasLockedElements()">hasLockedElements</a>, <a href="ILockProjectService.html#hasPermissionToLock(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hasPermissionToLock</a>, <a href="ILockProjectService.html#isDecompositionLocked(com.nomagic.ci.persistence.IProject)">isDecompositionLocked</a>, <a href="ILockProjectService.html#isDecompositionLockedByMe(com.nomagic.ci.persistence.IProject)">isDecompositionLockedByMe</a>, <a href="ILockProjectService.html#isLocked(com.nomagic.magicdraw.core.modules.ModuleUsage)">isLocked</a>, <a href="ILockProjectService.html#isLocked(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isLocked</a>, <a href="ILockProjectService.html#isLockedBy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isLockedBy</a>, <a href="ILockProjectService.html#isLockedByMe(com.nomagic.magicdraw.core.modules.ModuleUsage)">isLockedByMe</a>, <a href="ILockProjectService.html#isLockedByMe(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isLockedByMe</a>, <a href="ILockProjectService.html#isOptionsLocked(com.nomagic.ci.persistence.IProject,java.lang.String)">isOptionsLocked</a>, <a href="ILockProjectService.html#isOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String)">isOptionsLockedByMe</a>, <a href="ILockProjectService.html#lockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">lockElements</a>, <a href="ILockProjectService.html#lockElements(java.util.Collection,com.nomagic.magicdraw.teamwork2.locks.ILockProjectService.LockOptions,com.nomagic.task.ProgressStatus)">lockElements</a>, <a href="ILockProjectService.html#lockElements(java.util.Collection,com.nomagic.task.ProgressStatus)">lockElements</a>, <a href="ILockProjectService.html#lockModules(java.util.Collection,boolean,boolean,com.nomagic.task.ProgressStatus)">lockModules</a>, <a href="ILockProjectService.html#lockModules(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">lockModules</a>, <a href="ILockProjectService.html#setCacheOptionsLock(boolean)">setCacheOptionsLock</a>, <a href="ILockProjectService.html#setDecompositionLockedByMe(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.task.ProgressStatus)">setDecompositionLockedByMe</a>, <a href="ILockProjectService.html#setOptionsLockedByMe(com.nomagic.ci.persistence.IProject,java.lang.String,boolean,com.nomagic.task.ProgressStatus)">setOptionsLockedByMe</a>, <a href="ILockProjectService.html#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus)">unlockElements</a>, <a href="ILockProjectService.html#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,boolean)">unlockElements</a>, <a href="ILockProjectService.html#unlockElements(java.util.Collection,boolean,com.nomagic.task.ProgressStatus,java.util.Collection,boolean)">unlockElements</a>, <a href="ILockProjectService.html#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus)">unlockElements</a>, <a href="ILockProjectService.html#unlockElements(java.util.Collection,com.nomagic.task.ProgressStatus,boolean)">unlockElements</a>, <a href="ILockProjectService.html#unlockModules(java.util.Collection,com.nomagic.task.ProgressStatus)">unlockModules</a>, <a href="ILockProjectService.html#updateLocks(com.nomagic.task.ProgressStatus)">updateLocks</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project)">
<h3>LockService</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">LockService</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
</dl>
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
<section class="detail" id="getLockService(com.nomagic.magicdraw.core.Project)">
<h3>getLockService</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ILockProjectService.html" title="interface in com.nomagic.magicdraw.teamwork2.locks">ILockProjectService</a></span> <span class="element-name">getLockService</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Return and instance of lock service for a given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>lock service</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selectElementsForLock(java.util.Collection,java.util.function.Predicate)">
<h3>selectElementsForLock</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">selectElementsForLock</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; canBeLocked)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasAutomaticUsages(java.util.Collection)">
<h3>hasAutomaticUsages</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasAutomaticUsages</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; moduleUsages)</span></div>
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
