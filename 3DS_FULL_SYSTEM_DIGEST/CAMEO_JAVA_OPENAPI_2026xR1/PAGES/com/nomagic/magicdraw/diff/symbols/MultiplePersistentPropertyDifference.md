# JAVA OPENAPI: MultiplePersistentPropertyDifference (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/diff/symbols/MultiplePersistentPropertyDifference.html
- source_path: `com/nomagic/magicdraw/diff/symbols/MultiplePersistentPropertyDifference.html`
- source_sha256: `df7a5fc8b09ec6e798cdb5ccd372d1d6f8e6b121b02e049ad355463fa66f4f0b`
- captured_utc: `2026-07-14T16:45:33.613450+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.symbols](package-summary.html)

## Interface MultiplePersistentPropertyDifference<T>

All Superinterfaces:
`[Difference](../Difference.html)`, `[DifferenceLocation](../DifferenceLocation.html)`, `[SymbolDifference](SymbolDifference.html)`

@OpenApiAllpublic interfaceMultiplePersistentPropertyDifference<T>extends [SymbolDifference](SymbolDifference.html)

Difference when persistent property with multiplicity more than one is changed. In case
 persistent property is ordered order change should be reported also.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[T](MultiplePersistentPropertyDifference.html)`
`[getChanged](#getChanged())()`
One object from changed objects collection.
`[ModificationKind](../ModificationKind.html)`
`[getKind](#getKind())()`
Only [`ModificationKind.ADDED`](../ModificationKind.html#ADDED) and [`ModificationKind.REMOVED`](../ModificationKind.html#REMOVED) is used.
`[SymbolFeature](../../uml/symbols/reflect/SymbolFeature.html)`
`[getMetaInfo](#getMetaInfo())()`
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](../DifferenceLocation.html)
`[getModuleURI](../DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.symbols.[SymbolDifference](SymbolDifference.html)
`[getDiagramID](SymbolDifference.html#getDiagramID()), [getProjectID](SymbolDifference.html#getProjectID()), [getSymbolID](SymbolDifference.html#getSymbolID())`

============ METHOD DETAIL ========== 
Method Details
getKind
[ModificationKind](../ModificationKind.html) getKind()
Only [`ModificationKind.ADDED`](../ModificationKind.html#ADDED) and [`ModificationKind.REMOVED`](../ModificationKind.html#REMOVED) is used.
Returns:
kind of modification.
getChanged
[T](MultiplePersistentPropertyDifference.html) getChanged()
One object from changed objects collection.
Returns:
changed element
getMetaInfo
[SymbolFeature](../../uml/symbols/reflect/SymbolFeature.html) getMetaInfo()
Returns:
property meta information - type of property, multiplicity, etc.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.symbols</a></div>
<h1 class="title" title="Interface MultiplePersistentPropertyDifference">Interface MultiplePersistentPropertyDifference&lt;T&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MultiplePersistentPropertyDifference&lt;T&gt;</span><span class="extends-implements">
extends <a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></span></div>
<div class="block">Difference when persistent property with multiplicity more than one is changed. In case
 persistent property is ordered order change should be reported also.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MultiplePersistentPropertyDifference.html" title="type parameter in MultiplePersistentPropertyDifference">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChanged()">getChanged</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">One object from changed objects collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Only <a href="../ModificationKind.html#ADDED"><code>ModificationKind.ADDED</code></a> and <a href="../ModificationKind.html#REMOVED"><code>ModificationKind.REMOVED</code></a> is used.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml/symbols/reflect/SymbolFeature.html" title="interface in com.nomagic.magicdraw.uml.symbols.reflect">SymbolFeature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMetaInfo()">getMetaInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="return-type"><a href="../ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></span> <span class="element-name">getKind</span>()</div>
<div class="block">Only <a href="../ModificationKind.html#ADDED"><code>ModificationKind.ADDED</code></a> and <a href="../ModificationKind.html#REMOVED"><code>ModificationKind.REMOVED</code></a> is used.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>kind of modification.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChanged()">
<h3>getChanged</h3>
<div class="member-signature"><span class="return-type"><a href="MultiplePersistentPropertyDifference.html" title="type parameter in MultiplePersistentPropertyDifference">T</a></span> <span class="element-name">getChanged</span>()</div>
<div class="block">One object from changed objects collection.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>changed element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetaInfo()">
<h3>getMetaInfo</h3>
<div class="member-signature"><span class="return-type"><a href="../../uml/symbols/reflect/SymbolFeature.html" title="interface in com.nomagic.magicdraw.uml.symbols.reflect">SymbolFeature</a></span> <span class="element-name">getMetaInfo</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property meta information - type of property, multiplicity, etc.</dd>
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
