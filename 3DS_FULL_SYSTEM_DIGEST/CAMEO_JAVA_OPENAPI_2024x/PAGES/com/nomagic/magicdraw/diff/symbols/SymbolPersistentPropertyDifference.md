# JAVA OPENAPI: SymbolPersistentPropertyDifference (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/diff/symbols/SymbolPersistentPropertyDifference.html
- source_path: `com/nomagic/magicdraw/diff/symbols/SymbolPersistentPropertyDifference.html`
- source_sha256: `2ddf9d5160521f34fab5d0992c34841b301c8baa39894c7954a9f30ecb8e14b0`
- captured_utc: `2026-07-14T16:51:18.146163+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.symbols](package-summary.html)

## Interface SymbolPersistentPropertyDifference<T>

Type Parameters:
`T` - type for persistent property.

All Superinterfaces:
`[Difference](../Difference.html)`, `[DifferenceLocation](../DifferenceLocation.html)`, `[SymbolDifference](SymbolDifference.html)`

All Known Subinterfaces:
`[PersistentPropertyOrderDifference](PersistentPropertyOrderDifference.html)<T>`

@OpenApiAllpublic interfaceSymbolPersistentPropertyDifference<T>extends [SymbolDifference](SymbolDifference.html)

Persistent symbol property changed.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[PersistentProperty](../../uml/symbols/reflect/PersistentProperty.html)<[T](SymbolPersistentPropertyDifference.html)>`
`[getChangedProperty](#getChangedProperty())()`
Changed property.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](../DifferenceLocation.html)
`[getModuleURI](../DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.symbols.[SymbolDifference](SymbolDifference.html)
`[getDiagramID](SymbolDifference.html#getDiagramID()), [getProjectID](SymbolDifference.html#getProjectID()), [getSymbolID](SymbolDifference.html#getSymbolID())`

============ METHOD DETAIL ========== 
Method Details
getChangedProperty
[PersistentProperty](../../uml/symbols/reflect/PersistentProperty.html)<[T](SymbolPersistentPropertyDifference.html)> getChangedProperty()
Changed property.
Returns:
changed property.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.symbols</a></div>
<h1 class="title" title="Interface SymbolPersistentPropertyDifference">Interface SymbolPersistentPropertyDifference&lt;T&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - type for persistent property.</dd>
</dl>
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="PersistentPropertyOrderDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">PersistentPropertyOrderDifference</a>&lt;T&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SymbolPersistentPropertyDifference&lt;T&gt;</span><span class="extends-implements">
extends <a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></span></div>
<div class="block">Persistent symbol property changed.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml/symbols/reflect/PersistentProperty.html" title="interface in com.nomagic.magicdraw.uml.symbols.reflect">PersistentProperty</a>&lt;<a href="SymbolPersistentPropertyDifference.html" title="type parameter in SymbolPersistentPropertyDifference">T</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangedProperty()">getChangedProperty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Changed property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="../DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.symbols.SymbolDifference">Methods inherited from interface com.nomagic.magicdraw.diff.symbols.<a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></h3>
<code><a href="SymbolDifference.html#getDiagramID()">getDiagramID</a>, <a href="SymbolDifference.html#getProjectID()">getProjectID</a>, <a href="SymbolDifference.html#getSymbolID()">getSymbolID</a></code></div>
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
<section class="detail" id="getChangedProperty()">
<h3>getChangedProperty</h3>
<div class="member-signature"><span class="return-type"><a href="../../uml/symbols/reflect/PersistentProperty.html" title="interface in com.nomagic.magicdraw.uml.symbols.reflect">PersistentProperty</a>&lt;<a href="SymbolPersistentPropertyDifference.html" title="type parameter in SymbolPersistentPropertyDifference">T</a>&gt;</span> <span class="element-name">getChangedProperty</span>()</div>
<div class="block">Changed property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>changed property.</dd>
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
