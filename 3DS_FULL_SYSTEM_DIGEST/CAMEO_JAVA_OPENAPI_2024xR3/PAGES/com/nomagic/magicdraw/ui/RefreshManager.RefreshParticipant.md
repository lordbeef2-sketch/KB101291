# JAVA OPENAPI: RefreshManager.RefreshParticipant (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/RefreshManager.RefreshParticipant.html
- source_path: `com/nomagic/magicdraw/ui/RefreshManager.RefreshParticipant.html`
- source_sha256: `a9ef6eb8a470b17ebade3eb42d28087974bf27e113e02399a94485fe4aee60fa`
- captured_utc: `2026-07-14T16:55:50.666408+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Interface RefreshManager.RefreshParticipant

All Superinterfaces:
`[PriorityProvider](../utils/PriorityProvider.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`

Enclosing class:
[RefreshManager](RefreshManager.html)

public static interfaceRefreshManager.RefreshParticipantextends [PriorityProvider](../utils/PriorityProvider.html)

Refresh participant

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default int`
`[getPriority](#getPriority())()`
Returns priority of this object.
`void`
`[refresh](#refresh(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus))([Project](../core/Project.html) project,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)`

============ METHOD DETAIL ========== 
Method Details
refresh
void refresh([Project](../core/Project.html) project,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)
getPriority
default int getPriority()
Description copied from interface: `[PriorityProvider](../../utils/PriorityProvider.html#getPriority())`
Returns priority of this object.
Specified by:
`[getPriority](../../utils/PriorityProvider.html#getPriority())` in interface `[PriorityProvider](../../utils/PriorityProvider.html)`
Returns:
priority of this object.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Interface RefreshManager.RefreshParticipant">Interface RefreshManager.RefreshParticipant</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="RefreshManager.html" title="class in com.nomagic.magicdraw.ui">RefreshManager</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">RefreshManager.RefreshParticipant</span><span class="extends-implements">
extends <a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></span></div>
<div class="block">Refresh participant</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns priority of this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#refresh(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus)">refresh</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="refresh(com.nomagic.magicdraw.core.Project,com.nomagic.task.ProgressStatus)">
<h3>refresh</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">refresh</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../utils/PriorityProvider.html#getPriority()">PriorityProvider</a></code></span></div>
<div class="block">Returns priority of this object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../utils/PriorityProvider.html#getPriority()">getPriority</a></code> in interface <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
<dt>Returns:</dt>
<dd>priority of this object.</dd>
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
