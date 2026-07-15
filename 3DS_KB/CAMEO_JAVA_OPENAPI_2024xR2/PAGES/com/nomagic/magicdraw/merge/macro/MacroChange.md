# JAVA OPENAPI: MacroChange (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/merge/macro/MacroChange.html
- source_path: `com/nomagic/magicdraw/merge/macro/MacroChange.html`
- source_sha256: `448b6ff7eded97a25d088bd9e7664ee54bbac3765d39b6296d091092ee752479`
- captured_utc: `2026-07-14T16:55:23.519100+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.merge.macro](package-summary.html)

## Interface MacroChange

All Superinterfaces:
`[Change](../Change.html)`

@OpenApiAllpublic interfaceMacroChangeextends [Change](../Change.html)

Macro change groups several changes into single change.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Change](../Change.html)>`
`[getChanges](#getChanges())()`
Get grouped changes.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedMacroChange](RelatedMacroChange.html)>`
`[getConflicts](#getConflicts())()`
Returns the current change conflicting changes.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedMacroChange](RelatedMacroChange.html)>`
`[getDependent](#getDependent())()`
Returns the current change dependent changes - changes that requires current change.
`[MacroDifference](../../diff/macro/MacroDifference.html)`
`[getDifference](#getDifference())()`
Returns the difference that caused current change.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProjectElementId](#getProjectElementId())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedMacroChange](RelatedMacroChange.html)>`
`[getRequired](#getRequired())()`
Returns the current change required changes.
`[Difference](../../diff/Difference.html)`
`[getVirtualDifference](#getVirtualDifference())()`
Methods inherited from interface com.nomagic.magicdraw.merge.[Change](../Change.html)
`[getEquivalents](../Change.html#getEquivalents()), [getState](../Change.html#getState())`

============ METHOD DETAIL ========== 
Method Details
getChanges
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Change](../Change.html)> getChanges()
Get grouped changes.
Returns:
grouped changes.
getDifference
[MacroDifference](../../diff/macro/MacroDifference.html) getDifference()
Description copied from interface: `[Change](../Change.html#getDifference())`
Returns the difference that caused current change.
Specified by:
`[getDifference](../Change.html#getDifference())` in interface `[Change](../Change.html)`
Returns:
difference that caused current change.
getConflicts
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedMacroChange](RelatedMacroChange.html)> getConflicts()
Description copied from interface: `[Change](../Change.html#getConflicts())`
Returns the current change conflicting changes.
Specified by:
`[getConflicts](../Change.html#getConflicts())` in interface `[Change](../Change.html)`
Returns:
conflicting changes
getDependent
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedMacroChange](RelatedMacroChange.html)> getDependent()
Description copied from interface: `[Change](../Change.html#getDependent())`
Returns the current change dependent changes - changes that requires current change.
Specified by:
`[getDependent](../Change.html#getDependent())` in interface `[Change](../Change.html)`
Returns:
dependent changes.
getRequired
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [RelatedMacroChange](RelatedMacroChange.html)> getRequired()
Description copied from interface: `[Change](../Change.html#getRequired())`
Returns the current change required changes.
Specified by:
`[getRequired](../Change.html#getRequired())` in interface `[Change](../Change.html)`
Returns:
required changes.
getProjectElementId
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProjectElementId()
Returns:
element id of an element which is represented by this MacroChange
getVirtualDifference
@CheckForNull[Difference](../../diff/Difference.html) getVirtualDifference()
Returns:
difference which represents kind of low-level group of differences that make more sense in the gui.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.merge.macro</a></div>
<h1 class="title" title="Interface MacroChange">Interface MacroChange</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MacroChange</span><span class="extends-implements">
extends <a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></span></div>
<div class="block">Macro change groups several changes into single change.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChanges()">getChanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get grouped changes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedMacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">RelatedMacroChange</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getConflicts()">getConflicts</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change conflicting changes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedMacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">RelatedMacroChange</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDependent()">getDependent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change dependent changes - changes that requires current change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../diff/macro/MacroDifference.html" title="interface in com.nomagic.magicdraw.diff.macro">MacroDifference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDifference()">getDifference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the difference that caused current change.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectElementId()">getProjectElementId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedMacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">RelatedMacroChange</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRequired()">getRequired</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the current change required changes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../diff/Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVirtualDifference()">getVirtualDifference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.merge.Change">Methods inherited from interface com.nomagic.magicdraw.merge.<a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></h3>
<code><a href="../Change.html#getEquivalents()">getEquivalents</a>, <a href="../Change.html#getState()">getState</a></code></div>
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
<section class="detail" id="getChanges()">
<h3>getChanges</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a>&gt;</span> <span class="element-name">getChanges</span>()</div>
<div class="block">Get grouped changes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>grouped changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDifference()">
<h3>getDifference</h3>
<div class="member-signature"><span class="return-type"><a href="../../diff/macro/MacroDifference.html" title="interface in com.nomagic.magicdraw.diff.macro">MacroDifference</a></span> <span class="element-name">getDifference</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../Change.html#getDifference()">Change</a></code></span></div>
<div class="block">Returns the difference that caused current change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Change.html#getDifference()">getDifference</a></code> in interface <code><a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></code></dd>
<dt>Returns:</dt>
<dd>difference that caused current change.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConflicts()">
<h3>getConflicts</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedMacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">RelatedMacroChange</a>&gt;</span> <span class="element-name">getConflicts</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../Change.html#getConflicts()">Change</a></code></span></div>
<div class="block">Returns the current change conflicting changes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Change.html#getConflicts()">getConflicts</a></code> in interface <code><a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></code></dd>
<dt>Returns:</dt>
<dd>conflicting changes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependent()">
<h3>getDependent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedMacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">RelatedMacroChange</a>&gt;</span> <span class="element-name">getDependent</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../Change.html#getDependent()">Change</a></code></span></div>
<div class="block">Returns the current change dependent changes - changes that requires current change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Change.html#getDependent()">getDependent</a></code> in interface <code><a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></code></dd>
<dt>Returns:</dt>
<dd>dependent changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequired()">
<h3>getRequired</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RelatedMacroChange.html" title="interface in com.nomagic.magicdraw.merge.macro">RelatedMacroChange</a>&gt;</span> <span class="element-name">getRequired</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../Change.html#getRequired()">Change</a></code></span></div>
<div class="block">Returns the current change required changes.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Change.html#getRequired()">getRequired</a></code> in interface <code><a href="../Change.html" title="interface in com.nomagic.magicdraw.merge">Change</a></code></dd>
<dt>Returns:</dt>
<dd>required changes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectElementId()">
<h3>getProjectElementId</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectElementId</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element id of an element which is represented by this MacroChange</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVirtualDifference()">
<h3>getVirtualDifference</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../diff/Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></span> <span class="element-name">getVirtualDifference</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>difference which represents kind of low-level group of differences that make more sense in the gui.</dd>
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
