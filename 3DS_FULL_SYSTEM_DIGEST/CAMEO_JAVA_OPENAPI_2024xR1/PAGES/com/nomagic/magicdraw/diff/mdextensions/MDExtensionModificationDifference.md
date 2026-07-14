# JAVA OPENAPI: MDExtensionModificationDifference (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/diff/mdextensions/MDExtensionModificationDifference.html
- source_path: `com/nomagic/magicdraw/diff/mdextensions/MDExtensionModificationDifference.html`
- source_sha256: `e1ceaaa54c6fbaa810e6bf5943013c49b9c339ca5183c4ce3ba0ee1f238ad4d6`
- captured_utc: `2026-07-14T16:51:18.236163+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.mdextensions](package-summary.html)

## Interface MDExtensionModificationDifference

All Superinterfaces:
`[Difference](../Difference.html)`, `[DifferenceLocation](../DifferenceLocation.html)`, `[ElementDifference](../ElementDifference.html)`, `[MDExtensionDifference](MDExtensionDifference.html)`

@OpenApiAllpublic interfaceMDExtensionModificationDifferenceextends [MDExtensionDifference](MDExtensionDifference.html)

MDExtension modification difference.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[MDExtensionData](MDExtensionData.html)`
`[getAncestorData](#getAncestorData())()`
Ancestor extension data.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](../DifferenceLocation.html)
`[getModuleURI](../DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ElementDifference](../ElementDifference.html)
`[getElementID](../ElementDifference.html#getElementID())`
Methods inherited from interface com.nomagic.magicdraw.diff.mdextensions.[MDExtensionDifference](MDExtensionDifference.html)
`[getData](MDExtensionDifference.html#getData()), [getSource](MDExtensionDifference.html#getSource())`

============ METHOD DETAIL ========== 
Method Details
getAncestorData
[MDExtensionData](MDExtensionData.html) getAncestorData()
Ancestor extension data.
Returns:
extension data.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.mdextensions</a></div>
<h1 class="title" title="Interface MDExtensionModificationDifference">Interface MDExtensionModificationDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="../ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code>, <code><a href="MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MDExtensionModificationDifference</span><span class="extends-implements">
extends <a href="MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></span></div>
<div class="block">MDExtension modification difference.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDExtensionData.html" title="class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAncestorData()">getAncestorData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Ancestor extension data.</div>
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
<section class="detail" id="getAncestorData()">
<h3>getAncestorData</h3>
<div class="member-signature"><span class="return-type"><a href="MDExtensionData.html" title="class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionData</a></span> <span class="element-name">getAncestorData</span>()</div>
<div class="block">Ancestor extension data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>extension data.</dd>
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
