# JAVA OPENAPI: EsiRemoveKeepReferencesService (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/teamwork2/esi/EsiRemoveKeepReferencesService.html
- source_path: `com/nomagic/magicdraw/teamwork2/esi/EsiRemoveKeepReferencesService.html`
- source_sha256: `2ad078bfb021ad878103f100f756f1abd6480b091c2601c37b29270a5a9c928b`
- captured_utc: `2026-07-14T16:58:10.104671+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.teamwork2.esi](package-summary.html)

## Class EsiRemoveKeepReferencesService

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.teamwork2.esi.EsiRemoveKeepReferencesService

@OpenApiAllpublic classEsiRemoveKeepReferencesService
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
A service that is responsible for removing an ESI module with "Keeping References"

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EsiRemoveKeepReferencesService](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[detachModulesKeepAndReferencesOnTask](#detachModulesKeepAndReferencesOnTask(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,java.util.Collection))([Project](../../core/Project.html) project,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> usages)`
Removes usages of modules and keeps references to existing objects from
 modules.
`static boolean`
`[detachModulesKeepAndReferencesOnTask](#detachModulesKeepAndReferencesOnTask(com.nomagic.magicdraw.core.Project,java.util.Collection))([Project](../../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> usages)`
Removes usages of modules and keeps references to existing objects from modules.
`static void`
`[detachModulesKeepReferences](#detachModulesKeepReferences(com.nomagic.magicdraw.core.Project,java.util.Collection,com.nomagic.task.ProgressStatus))([Project](../../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> usages,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)`
Removes usages of modules and keeps references to existing objects from modules.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EsiRemoveKeepReferencesService
public EsiRemoveKeepReferencesService()
 ============ METHOD DETAIL ========== 
Method Details
detachModulesKeepAndReferencesOnTask
public static boolean detachModulesKeepAndReferencesOnTask([Project](../../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> usages)
Removes usages of modules and keeps references to existing objects from modules.
Parameters:
`project` - a project.
`usages` - a collection of usages.
Returns:
true the operation was successful.
detachModulesKeepAndReferencesOnTask
public static boolean detachModulesKeepAndReferencesOnTask([Project](../../core/Project.html) project,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> usages)
Removes usages of modules and keeps references to existing objects from
 modules.
Parameters:
`project` - a project.
`removeConfirmation` - remove confirmation
`usages` - a collection of usages.
Returns:
true the operation was successful.
detachModulesKeepReferences
public static void detachModulesKeepReferences([Project](../../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ModuleUsage](../../core/modules/ModuleUsage.html)> usages,
 [ProgressStatus](../../../task/ProgressStatus.html) monitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Removes usages of modules and keeps references to existing objects from modules.
Parameters:
`project` - a project.
`usages` - a collection of usages.
`monitor` - progress monitor
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.teamwork2.esi</a></div>
<h1 class="title" title="Class EsiRemoveKeepReferencesService">Class EsiRemoveKeepReferencesService</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.teamwork2.esi.EsiRemoveKeepReferencesService</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">EsiRemoveKeepReferencesService</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">A service that is responsible for removing an ESI module with "Keeping References"</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EsiRemoveKeepReferencesService</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesKeepAndReferencesOnTask(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,java.util.Collection)">detachModulesKeepAndReferencesOnTask</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes usages of modules and keeps references to existing objects from
 modules.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesKeepAndReferencesOnTask(com.nomagic.magicdraw.core.Project,java.util.Collection)">detachModulesKeepAndReferencesOnTask</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes usages of modules and keeps references to existing objects from modules.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#detachModulesKeepReferences(com.nomagic.magicdraw.core.Project,java.util.Collection,com.nomagic.task.ProgressStatus)">detachModulesKeepReferences</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes usages of modules and keeps references to existing objects from modules.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>EsiRemoveKeepReferencesService</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EsiRemoveKeepReferencesService</span>()</div>
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
<section class="detail" id="detachModulesKeepAndReferencesOnTask(com.nomagic.magicdraw.core.Project,java.util.Collection)">
<h3>detachModulesKeepAndReferencesOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModulesKeepAndReferencesOnTask</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</span></div>
<div class="block">Removes usages of modules and keeps references to existing objects from modules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dd><code>usages</code> - a collection of usages.</dd>
<dt>Returns:</dt>
<dd>true the operation was successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModulesKeepAndReferencesOnTask(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback,java.util.Collection)">
<h3>detachModulesKeepAndReferencesOnTask</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">detachModulesKeepAndReferencesOnTask</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 com.nomagic.ci.persistence.decomposition.IAttachedProjectRemoverCallback removeConfirmation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages)</span></div>
<div class="block">Removes usages of modules and keeps references to existing objects from
 modules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dd><code>removeConfirmation</code> - remove confirmation</dd>
<dd><code>usages</code> - a collection of usages.</dd>
<dt>Returns:</dt>
<dd>true the operation was successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="detachModulesKeepReferences(com.nomagic.magicdraw.core.Project,java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>detachModulesKeepReferences</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">detachModulesKeepReferences</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt; usages,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span>
                                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Removes usages of modules and keeps references to existing objects from modules.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dd><code>usages</code> - a collection of usages.</dd>
<dd><code>monitor</code> - progress monitor</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
