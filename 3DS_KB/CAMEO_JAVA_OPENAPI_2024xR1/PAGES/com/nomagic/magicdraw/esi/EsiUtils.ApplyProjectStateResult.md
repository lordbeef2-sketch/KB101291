# JAVA OPENAPI: EsiUtils.ApplyProjectStateResult (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/esi/EsiUtils.ApplyProjectStateResult.html
- source_path: `com/nomagic/magicdraw/esi/EsiUtils.ApplyProjectStateResult.html`
- source_sha256: `e8e43a285ab6c37ec79bc0827dc96b72047fe2336b88b046d6284911344d2105`
- captured_utc: `2026-07-14T16:51:21.177203+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi](package-summary.html)

## Interface EsiUtils.ApplyProjectStateResult

Enclosing class:
[EsiUtils](EsiUtils.html)

public static interfaceEsiUtils.ApplyProjectStateResult

A structure that is produced by the [`EsiUtils.applyProjectState(Project, Project)`](EsiUtils.html#applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)) and
 which holds information about the result of the operation

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getLockedElements](#getLockedElements())()`
Gets set of elements that were locked during the operation
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[ModuleUsage](../core/modules/ModuleUsage.html)>`
`[getLockedModuleUsages](#getLockedModuleUsages())()`
Gets set of module usages that were locked during the operation

============ METHOD DETAIL ========== 
Method Details
getLockedElements
[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getLockedElements()
Gets set of elements that were locked during the operation
Returns:
the locked elements
getLockedModuleUsages
[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[ModuleUsage](../core/modules/ModuleUsage.html)> getLockedModuleUsages()
Gets set of module usages that were locked during the operation
Returns:
the locked module usages

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi</a></div>
<h1 class="title" title="Interface EsiUtils.ApplyProjectStateResult">Interface EsiUtils.ApplyProjectStateResult</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="EsiUtils.html" title="class in com.nomagic.magicdraw.esi">EsiUtils</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">EsiUtils.ApplyProjectStateResult</span></div>
<div class="block">A structure that is produced by the <a href="EsiUtils.html#applyProjectState(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)"><code>EsiUtils.applyProjectState(Project, Project)</code></a> and
 which holds information about the result of the operation</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedElements()">getLockedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets set of elements that were locked during the operation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLockedModuleUsages()">getLockedModuleUsages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets set of module usages that were locked during the operation</div>
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
<section class="detail" id="getLockedElements()">
<h3>getLockedElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getLockedElements</span>()</div>
<div class="block">Gets set of elements that were locked during the operation</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the locked elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockedModuleUsages()">
<h3>getLockedModuleUsages</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a>&gt;</span> <span class="element-name">getLockedModuleUsages</span>()</div>
<div class="block">Gets set of module usages that were locked during the operation</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the locked module usages</dd>
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
