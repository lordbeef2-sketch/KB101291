# JAVA OPENAPI: MDExtensionExistenceDifference (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/diff/mdextensions/MDExtensionExistenceDifference.html
- source_path: `com/nomagic/magicdraw/diff/mdextensions/MDExtensionExistenceDifference.html`
- source_sha256: `657b84aa7e04e1b8fc45107e2e644b618d05692c2cd4ade20e7256a70443fd04`
- captured_utc: `2026-07-14T16:57:55.518507+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.mdextensions](package-summary.html)

## Interface MDExtensionExistenceDifference

All Superinterfaces:
`[Difference](../Difference.html)`, `[DifferenceLocation](../DifferenceLocation.html)`, `[ElementDifference](../ElementDifference.html)`, `[MDExtensionDifference](MDExtensionDifference.html)`

@OpenApiAllpublic interfaceMDExtensionExistenceDifferenceextends [MDExtensionDifference](MDExtensionDifference.html)

MDExtension existence difference.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static enum`
`[MDExtensionExistenceDifference.Type](MDExtensionExistenceDifference.Type.html)`
Existence difference type.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[MDExtensionExistenceDifference.Type](MDExtensionExistenceDifference.Type.html)`
`[getType](#getType())()`
Difference tyoe.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](../DifferenceLocation.html)
`[getModuleURI](../DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ElementDifference](../ElementDifference.html)
`[getElementID](../ElementDifference.html#getElementID())`
Methods inherited from interface com.nomagic.magicdraw.diff.mdextensions.[MDExtensionDifference](MDExtensionDifference.html)
`[getData](MDExtensionDifference.html#getData()), [getSource](MDExtensionDifference.html#getSource())`

============ METHOD DETAIL ========== 
Method Details
getType
[MDExtensionExistenceDifference.Type](MDExtensionExistenceDifference.Type.html) getType()
Difference tyoe.
Returns:
type of difference.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.mdextensions</a></div>
<h1 class="title" title="Interface MDExtensionExistenceDifference">Interface MDExtensionExistenceDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="../ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code>, <code><a href="MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MDExtensionExistenceDifference</span><span class="extends-implements">
extends <a href="MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></span></div>
<div class="block">MDExtension existence difference.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MDExtensionExistenceDifference.Type.html" title="enum class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference.Type</a></code></div>
<div class="col-last even-row-color">
<div class="block">Existence difference type.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDExtensionExistenceDifference.Type.html" title="enum class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference.Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Difference tyoe.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="../DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ElementDifference">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="../ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></h3>
<code><a href="../ElementDifference.html#getElementID()">getElementID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.mdextensions.MDExtensionDifference">Methods inherited from interface com.nomagic.magicdraw.diff.mdextensions.<a href="MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></h3>
<code><a href="MDExtensionDifference.html#getData()">getData</a>, <a href="MDExtensionDifference.html#getSource()">getSource</a></code></div>
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
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="return-type"><a href="MDExtensionExistenceDifference.Type.html" title="enum class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference.Type</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Difference tyoe.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of difference.</dd>
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
