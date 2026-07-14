# JAVA OPENAPI: Change (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/merge/Change.html
- source_path: `com/nomagic/magicdraw/merge/Change.html`
- source_sha256: `a0765d05d00bf3f3f6e56c96d5d753820db0035da6be7052d231f5e4c94731d0`
- captured_utc: `2026-07-14T16:51:24.792251+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.merge](package-summary.html)

## Interface Change

All Known Subinterfaces:
`[MacroChange](macro/MacroChange.html)`

@OpenApipublic interfaceChange

Change denotes the change of the project. Change contains difference with additional information:
 Dependent changes, required changes, State of change (accepted/rejected), Conflicting changes (for 3 way merge).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)>`
`[getConflicts](#getConflicts())()`
Returns the current change conflicting changes.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)>`
`[getDependent](#getDependent())()`
Returns the current change dependent changes - changes that requires current change.
`[Difference](../diff/Difference.html)`
`[getDifference](#getDifference())()`
Returns the difference that caused current change.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)>`
`[getEquivalents](#getEquivalents())()`
Returns the current change equivalent changes.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)>`
`[getRequired](#getRequired())()`
Returns the current change required changes.
`[ChangeState](ChangeState.html)`
`[getState](#getState())()`
Returns the change application state.

============ METHOD DETAIL ========== 
Method Details
getDifference
@OpenApi[Difference](../diff/Difference.html) getDifference()
Returns the difference that caused current change.
Returns:
difference that caused current change.
getState
@OpenApi[ChangeState](ChangeState.html) getState()
Returns the change application state.
Returns:
change application state.
getConflicts
@OpenApi[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)> getConflicts()
Returns the current change conflicting changes.
Returns:
conflicting changes
getEquivalents
@OpenApi[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)> getEquivalents()
Returns the current change equivalent changes.
Returns:
equivalent changes.
getDependent
@OpenApi[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)> getDependent()
Returns the current change dependent changes - changes that requires current change.
Returns:
dependent changes.
getRequired
@OpenApi[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedChange](RelatedChange.html)> getRequired()
Returns the current change required changes.
Returns:
required changes.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.merge</a></div>
<h1 class="title" title="Interface Change">Interface Change</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="macro/MacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">MacroChange</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Change</span></div>
<div class="block">Change denotes the change of the project. Change contains difference with additional information:
 Dependent changes, required changes, State of change (accepted/rejected), Conflicting changes (for 3 way merge).</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConflicts()">getConflicts</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change conflicting changes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDependent()">getDependent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change dependent changes - changes that requires current change.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../diff/Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDifference()">getDifference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the difference that caused current change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEquivalents()">getEquivalents</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change equivalent changes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRequired()">getRequired</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change required changes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ChangeState.html" title="enum class in com.nomagic.magicdraw.merge">ChangeState</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getState()">getState</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the change application state.</div>
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
<section class="detail" id="getDifference()">
<h3>getDifference</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="../diff/Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></span> <span class="element-name">getDifference</span>()</div>
<div class="block">Returns the difference that caused current change.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>difference that caused current change.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getState()">
<h3>getState</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="ChangeState.html" title="enum class in com.nomagic.magicdraw.merge">ChangeState</a></span> <span class="element-name">getState</span>()</div>
<div class="block">Returns the change application state.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>change application state.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConflicts()">
<h3>getConflicts</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</span> <span class="element-name">getConflicts</span>()</div>
<div class="block">Returns the current change conflicting changes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>conflicting changes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEquivalents()">
<h3>getEquivalents</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</span> <span class="element-name">getEquivalents</span>()</div>
<div class="block">Returns the current change equivalent changes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>equivalent changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependent()">
<h3>getDependent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</span> <span class="element-name">getDependent</span>()</div>
<div class="block">Returns the current change dependent changes - changes that requires current change.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>dependent changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequired()">
<h3>getRequired</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedChange.html" title="interface in com.nomagic.magicdraw.merge">RelatedChange</a>&gt;</span> <span class="element-name">getRequired</span>()</div>
<div class="block">Returns the current change required changes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>required changes.</dd>
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
