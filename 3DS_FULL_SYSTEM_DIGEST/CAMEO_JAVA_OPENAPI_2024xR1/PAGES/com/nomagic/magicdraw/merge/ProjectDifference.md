# JAVA OPENAPI: ProjectDifference (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/merge/ProjectDifference.html
- source_path: `com/nomagic/magicdraw/merge/ProjectDifference.html`
- source_sha256: `3db89ba24ba3cadbc5825c2a307666907b7474d2fba14dbc04fd874776abc242`
- captured_utc: `2026-07-14T16:51:25.314257+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.merge](package-summary.html)

## Class ProjectDifference

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.merge.ProjectDifference

@OpenApipublic final classProjectDifference
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Project difference data.

See Also:
[`MergeUtil`](MergeUtil.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<? extends [Change](Change.html)>`
`[getChanges](#getChanges())()`
Get all changes - changes between both contributors and the ancestor project.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[ModuleInfo](../diff/ModuleInfo.html),[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[RwMergeModeConstraint](../diff/RwMergeModeConstraint.html)>>`
`[getRejectedModules](#getRejectedModules())()`
Deprecated, for removal: This API element is subject to removal in a future version.
do not use this method, it always returns empty collection
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)>`
`[getSourceChanges](#getSourceChanges())()`
Get source changes - changes between ancestor and source.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)>`
`[getTargetChanges](#getTargetChanges())()`
Get target changes - changes between ancestor and target.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getSourceChanges
@OpenApipublic [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> getSourceChanges()
Get source changes - changes between ancestor and source.
Returns:
source changes.
getTargetChanges
@OpenApipublic [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Change](Change.html)> getTargetChanges()
Get target changes - changes between ancestor and target.
 There are changes nn the case of 2-way merge, as ancestor and target are the same.
Returns:
target changes.
getChanges
@OpenApipublic [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<? extends [Change](Change.html)> getChanges()
Get all changes - changes between both contributors and the ancestor project.
Returns:
all changes.
getRejectedModules
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2022xRefresh2",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)
@OpenApipublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[ModuleInfo](../diff/ModuleInfo.html),[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[RwMergeModeConstraint](../diff/RwMergeModeConstraint.html)>> getRejectedModules()
Deprecated, for removal: This API element is subject to removal in a future version.
do not use this method, it always returns empty collection
Gets modules that were requested but did not qualify for read-write merge mode.
Returns:
target project [`ModuleInfo`](../diff/ModuleInfo.html) to [`RwMergeModeConstraint`](../diff/RwMergeModeConstraint.html) map

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.merge</a></div>
<h1 class="title" title="Class ProjectDifference">Class ProjectDifference</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.merge.ProjectDifference</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ProjectDifference</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Project difference data.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="MergeUtil.html" title="class in com.nomagic.magicdraw.merge"><code>MergeUtil</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;? extends <a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChanges()">getChanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all changes - changes between both contributors and the ancestor project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../diff/ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../diff/RwMergeModeConstraint.html" title="enum class in com.nomagic.magicdraw.diff">RwMergeModeConstraint</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRejectedModules()">getRejectedModules</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">do not use this method, it always returns empty collection</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceChanges()">getSourceChanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get source changes - changes between ancestor and source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetChanges()">getTargetChanges</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get target changes - changes between ancestor and target.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getSourceChanges()">
<h3>getSourceChanges</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</span> <span class="element-name">getSourceChanges</span>()</div>
<div class="block">Get source changes - changes between ancestor and source.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetChanges()">
<h3>getTargetChanges</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</span> <span class="element-name">getTargetChanges</span>()</div>
<div class="block">Get target changes - changes between ancestor and target.
 There are changes nn the case of 2-way merge, as ancestor and target are the same.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChanges()">
<h3>getChanges</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;? extends <a href="Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</span> <span class="element-name">getChanges</span>()</div>
<div class="block">Get all changes - changes between both contributors and the ancestor project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRejectedModules()">
<h3>getRejectedModules</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2022xRefresh2",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../diff/ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../diff/RwMergeModeConstraint.html" title="enum class in com.nomagic.magicdraw.diff">RwMergeModeConstraint</a>&gt;&gt;</span> <span class="element-name">getRejectedModules</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">do not use this method, it always returns empty collection</div>
</div>
<div class="block">Gets modules that were requested but did not qualify for read-write merge mode.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>target project <a href="../diff/ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff"><code>ModuleInfo</code></a> to <a href="../diff/RwMergeModeConstraint.html" title="enum class in com.nomagic.magicdraw.diff"><code>RwMergeModeConstraint</code></a> map</dd>
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
