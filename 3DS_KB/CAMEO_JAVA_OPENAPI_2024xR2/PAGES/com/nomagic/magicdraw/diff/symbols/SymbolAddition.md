# JAVA OPENAPI: SymbolAddition (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/diff/symbols/SymbolAddition.html
- source_path: `com/nomagic/magicdraw/diff/symbols/SymbolAddition.html`
- source_sha256: `0ef73abc703d36d70a1036fccb815845290e44f7d887723d9bfdc6bd95a30c09`
- captured_utc: `2026-07-14T16:55:15.912014+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.symbols](package-summary.html)

## Interface SymbolAddition

All Superinterfaces:
`[Difference](../Difference.html)`, `[DifferenceLocation](../DifferenceLocation.html)`, `[SymbolDifference](SymbolDifference.html)`

@OpenApiAllpublic interfaceSymbolAdditionextends [SymbolDifference](SymbolDifference.html)

New symbol added difference. All symbol properties is reported as
 [`SymbolPersistentPropertyDifference`](SymbolPersistentPropertyDifference.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)>`
`[getSymbolType](#getSymbolType())()`
Created symbol type.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](../DifferenceLocation.html)
`[getModuleURI](../DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.symbols.[SymbolDifference](SymbolDifference.html)
`[getDiagramID](SymbolDifference.html#getDiagramID()), [getProjectID](SymbolDifference.html#getProjectID()), [getSymbolID](SymbolDifference.html#getSymbolID())`

============ METHOD DETAIL ========== 
Method Details
getSymbolType
[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<[PresentationElement](../../uml/symbols/PresentationElement.html)> getSymbolType()
Created symbol type.
Returns:
created symbol type.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.symbols</a></div>
<h1 class="title" title="Interface SymbolAddition">Interface SymbolAddition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SymbolAddition</span><span class="extends-implements">
extends <a href="SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></span></div>
<div class="block">New symbol added difference. All symbol properties is reported as
 <a href="SymbolPersistentPropertyDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols"><code>SymbolPersistentPropertyDifference</code></a></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSymbolType()">getSymbolType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Created symbol type.</div>
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
<section class="detail" id="getSymbolType()">
<h3>getSymbolType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;<a href="../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSymbolType</span>()</div>
<div class="block">Created symbol type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created symbol type.</dd>
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
