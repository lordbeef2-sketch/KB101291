# JAVA OPENAPI: MDExtensionDifference (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/diff/mdextensions/MDExtensionDifference.html
- source_path: `com/nomagic/magicdraw/diff/mdextensions/MDExtensionDifference.html`
- source_sha256: `fd25ec3a93608372df2537a2a65d778e2ab35b95d5e5073a8e66b20388c4c7cf`
- captured_utc: `2026-07-14T16:55:16.869026+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff.mdextensions](package-summary.html)

## Interface MDExtensionDifference

All Superinterfaces:
`[Difference](../Difference.html)`, `[DifferenceLocation](../DifferenceLocation.html)`, `[ElementDifference](../ElementDifference.html)`

All Known Subinterfaces:
`[MDExtensionExistenceDifference](MDExtensionExistenceDifference.html)`, `[MDExtensionModificationDifference](MDExtensionModificationDifference.html)`

@OpenApiAllpublic interfaceMDExtensionDifferenceextends [ElementDifference](../ElementDifference.html)

MDExtension difference.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[MDExtensionData](MDExtensionData.html)`
`[getData](#getData())()`
Extension data.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSource](#getSource())()`
Source string.
Methods inherited from interface com.nomagic.magicdraw.diff.[Difference](../Difference.html)
`[accept](../Difference.html#accept(com.nomagic.magicdraw.diff.DifferenceVisitor))`
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](../DifferenceLocation.html)
`[getModuleURI](../DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ElementDifference](../ElementDifference.html)
`[getElementID](../ElementDifference.html#getElementID())`

============ METHOD DETAIL ========== 
Method Details
getSource
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSource()
Source string.
Returns:
source.
getData
[MDExtensionData](MDExtensionData.html) getData()
Extension data.
Returns:
data.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff.mdextensions</a></div>
<h1 class="title" title="Interface MDExtensionDifference">Interface MDExtensionDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="../ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="MDExtensionExistenceDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference</a></code>, <code><a href="MDExtensionModificationDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionModificationDifference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MDExtensionDifference</span><span class="extends-implements">
extends <a href="../ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></span></div>
<div class="block">MDExtension difference.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="MDExtensionData.html" title="class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getData()">getData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Extension data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Source string.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.Difference">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="../Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></h3>
<code><a href="../Difference.html#accept(com.nomagic.magicdraw.diff.DifferenceVisitor)">accept</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="../DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="../DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ElementDifference">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="../ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></h3>
<code><a href="../ElementDifference.html#getElementID()">getElementID</a></code></div>
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
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSource</span>()</div>
<div class="block">Source string.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>source.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getData()">
<h3>getData</h3>
<div class="member-signature"><span class="return-type"><a href="MDExtensionData.html" title="class in com.nomagic.magicdraw.diff.mdextensions">MDExtensionData</a></span> <span class="element-name">getData</span>()</div>
<div class="block">Extension data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>data.</dd>
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
