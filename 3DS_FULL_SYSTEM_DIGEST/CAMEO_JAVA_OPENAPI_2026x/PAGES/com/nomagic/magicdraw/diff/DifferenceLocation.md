# JAVA OPENAPI: DifferenceLocation (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/diff/DifferenceLocation.html
- source_path: `com/nomagic/magicdraw/diff/DifferenceLocation.html`
- source_sha256: `e41c2358d81958137ab62567610814fac67fe9da3145d901eb8b841baa9ee91b`
- captured_utc: `2026-07-14T16:57:53.986492+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface DifferenceLocation

All Known Subinterfaces:
`[ElementAddition](ElementAddition.html)`, `[ElementDeletion](ElementDeletion.html)`, `[ElementDifference](ElementDifference.html)`, `[ElementModification](ElementModification.html)`, `[MDExtensionDifference](mdextensions/MDExtensionDifference.html)`, `[MDExtensionExistenceDifference](mdextensions/MDExtensionExistenceDifference.html)`, `[MDExtensionModificationDifference](mdextensions/MDExtensionModificationDifference.html)`, `[Modification](Modification.html)`, `[ModuleUsageDifference](ModuleUsageDifference.html)`, `[MultiplePersistentPropertyDifference](symbols/MultiplePersistentPropertyDifference.html)<T>`, `[PersistentPropertyOrderDifference](symbols/PersistentPropertyOrderDifference.html)<T>`, `[StereotypeModification](StereotypeModification.html)`, `[SymbolAddition](symbols/SymbolAddition.html)`, `[SymbolDeletion](symbols/SymbolDeletion.html)`, `[SymbolDifference](symbols/SymbolDifference.html)`, `[SymbolPersistentPropertyDifference](symbols/SymbolPersistentPropertyDifference.html)<T>`, `[TagValueModification](TagValueModification.html)`

@OpenApiAllpublic interfaceDifferenceLocation

This kind of difference may detected in the main project as well in module (attached project)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.emf.common.util.URI`
`[getModuleURI](#getModuleURI())()`
Return the URI of containing module.

============ METHOD DETAIL ========== 
Method Details
getModuleURI
@CheckForNullorg.eclipse.emf.common.util.URI getModuleURI()
Return the URI of containing module.
Returns:
module URI if element is owned by module, null - element is owned directly by project.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface DifferenceLocation">Interface DifferenceLocation</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ElementAddition.html" title="interface in com.nomagic.magicdraw.diff">ElementAddition</a></code>, <code><a href="ElementDeletion.html" title="interface in com.nomagic.magicdraw.diff">ElementDeletion</a></code>, <code><a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code>, <code><a href="ElementModification.html" title="interface in com.nomagic.magicdraw.diff">ElementModification</a></code>, <code><a href="mdextensions/MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></code>, <code><a href="mdextensions/MDExtensionExistenceDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference</a></code>, <code><a href="mdextensions/MDExtensionModificationDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionModificationDifference</a></code>, <code><a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></code>, <code><a href="ModuleUsageDifference.html" title="interface in com.nomagic.magicdraw.diff">ModuleUsageDifference</a></code>, <code><a href="symbols/MultiplePersistentPropertyDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">MultiplePersistentPropertyDifference</a>&lt;T&gt;</code>, <code><a href="symbols/PersistentPropertyOrderDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">PersistentPropertyOrderDifference</a>&lt;T&gt;</code>, <code><a href="StereotypeModification.html" title="interface in com.nomagic.magicdraw.diff">StereotypeModification</a></code>, <code><a href="symbols/SymbolAddition.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolAddition</a></code>, <code><a href="symbols/SymbolDeletion.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDeletion</a></code>, <code><a href="symbols/SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></code>, <code><a href="symbols/SymbolPersistentPropertyDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolPersistentPropertyDifference</a>&lt;T&gt;</code>, <code><a href="TagValueModification.html" title="interface in com.nomagic.magicdraw.diff">TagValueModification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DifferenceLocation</span></div>
<div class="block">This kind of difference may detected in the main project as well in module (attached project)</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.URI</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModuleURI()">getModuleURI</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the URI of containing module.</div>
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
<section class="detail" id="getModuleURI()">
<h3>getModuleURI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">getModuleURI</span>()</div>
<div class="block">Return the URI of containing module.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>module URI if element is owned by module, null - element is owned directly by project.</dd>
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
