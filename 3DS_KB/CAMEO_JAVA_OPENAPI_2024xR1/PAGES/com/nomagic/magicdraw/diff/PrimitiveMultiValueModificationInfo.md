# JAVA OPENAPI: PrimitiveMultiValueModificationInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/diff/PrimitiveMultiValueModificationInfo.html
- source_path: `com/nomagic/magicdraw/diff/PrimitiveMultiValueModificationInfo.html`
- source_sha256: `ee26e69b3e5ccaf361eadcadf1193a32bb2a6c3610b4221524d8c34636400afb`
- captured_utc: `2026-07-14T16:51:17.873159+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface PrimitiveMultiValueModificationInfo

All Superinterfaces:
`[ModificationInfo](ModificationInfo.html)`, `[ValueModificationInfo](ValueModificationInfo.html)`

@OpenApiAllpublic interfacePrimitiveMultiValueModificationInfoextends [ValueModificationInfo](ValueModificationInfo.html)

Modification of an item in a list of primitive values such as string, integer, boolean.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`int`
`[getIndex](#getIndex())()`
Value is not enough for value identification.
`default boolean`
`[wasChangeFromDefaultValue](#wasChangeFromDefaultValue())()`
Was change made when ancestor value was the default.
Methods inherited from interface com.nomagic.magicdraw.diff.[ValueModificationInfo](ValueModificationInfo.html)
`[getModificationKind](ValueModificationInfo.html#getModificationKind()), [getValue](ValueModificationInfo.html#getValue())`

============ METHOD DETAIL ========== 
Method Details
getIndex
int getIndex()
Value is not enough for value identification.
Returns:
index in the list of primitive type values.
wasChangeFromDefaultValue
default boolean wasChangeFromDefaultValue()
Was change made when ancestor value was the default.
Returns:
`true` if modification kind is changed and ancestor
 property value was default, otherwise - `false`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface PrimitiveMultiValueModificationInfo">Interface PrimitiveMultiValueModificationInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ModificationInfo</a></code>, <code><a href="ValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueModificationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PrimitiveMultiValueModificationInfo</span><span class="extends-implements">
extends <a href="ValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueModificationInfo</a></span></div>
<div class="block">Modification of an item in a list of primitive values such as string, integer, boolean.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIndex()">getIndex</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Value is not enough for value identification.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#wasChangeFromDefaultValue()">wasChangeFromDefaultValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Was change made when ancestor value was the default.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ValueModificationInfo">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="ValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueModificationInfo</a></h3>
<code><a href="ValueModificationInfo.html#getModificationKind()">getModificationKind</a>, <a href="ValueModificationInfo.html#getValue()">getValue</a></code></div>
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
<section class="detail" id="getIndex()">
<h3>getIndex</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getIndex</span>()</div>
<div class="block">Value is not enough for value identification.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>index in the list of primitive type values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="wasChangeFromDefaultValue()">
<h3>wasChangeFromDefaultValue</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">wasChangeFromDefaultValue</span>()</div>
<div class="block">Was change made when ancestor value was the default.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if modification kind is changed and ancestor
         property value was default, otherwise - <code>false</code></dd>
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
