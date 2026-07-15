# JAVA OPENAPI: DiagramDifference (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/diff/DiagramDifference.html
- source_path: `com/nomagic/magicdraw/diff/DiagramDifference.html`
- source_sha256: `2c90a4705e3dff37c89217c87f2f3c4944b8fc5628996f93f8f1f88272d930e0`
- captured_utc: `2026-07-14T16:55:13.718991+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface DiagramDifference

All Superinterfaces:
`[Difference](Difference.html)`

@OpenApiAllpublic interfaceDiagramDifferenceextends [Difference](Difference.html)

Difference between two diagrams. Contains diagram information, diagram id, and modification kind.
 If any information in diagram is changed only one [`DiagramDifference`](DiagramDifference.html) is created.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[DiagramData](DiagramData.html)`
`[getAncestorDiagramData](#getAncestorDiagramData())()`
Get ancestor diagram data.
`[DiagramData](DiagramData.html)`
`[getDiagramData](#getDiagramData())()`
Get contributor diagram data.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiagramID](#getDiagramID())()`
Get diagram presentation element id.
`[ModificationKind](ModificationKind.html)`
`[getModificationKind](#getModificationKind())()`
Get modification kind.

============ METHOD DETAIL ========== 
Method Details
getDiagramID
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiagramID()
Get diagram presentation element id.
Returns:
changed diagram presentation element id.
getDiagramData
[DiagramData](DiagramData.html) getDiagramData()
Get contributor diagram data.
Returns:
data of modified diagram.
See Also:
[`DiagramData`](DiagramData.html)
getAncestorDiagramData
@CheckForNull[DiagramData](DiagramData.html) getAncestorDiagramData()
Get ancestor diagram data.
Returns:
data of modified diagram.
See Also:
[`DiagramData`](DiagramData.html)
getModificationKind
[ModificationKind](ModificationKind.html) getModificationKind()
Get modification kind.
Returns:
modification kind.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface DiagramDifference">Interface DiagramDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramDifference</span><span class="extends-implements">
extends <a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></span></div>
<div class="block">Difference between two diagrams. Contains diagram information, diagram id, and modification kind.
 If any information in diagram is changed only one <a href="DiagramDifference.html" title="interface in com.nomagic.magicdraw.diff"><code>DiagramDifference</code></a> is created.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAncestorDiagramData()">getAncestorDiagramData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get ancestor diagram data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramData()">getDiagramData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get contributor diagram data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiagramID()">getDiagramID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get diagram presentation element id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModificationKind()">getModificationKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get modification kind.</div>
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
<section class="detail" id="getDiagramID()">
<h3>getDiagramID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramID</span>()</div>
<div class="block">Get diagram presentation element id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>changed diagram presentation element id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramData()">
<h3>getDiagramData</h3>
<div class="member-signature"><span class="return-type"><a href="DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></span> <span class="element-name">getDiagramData</span>()</div>
<div class="block">Get contributor diagram data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>data of modified diagram.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramData.html" title="interface in com.nomagic.magicdraw.diff"><code>DiagramData</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAncestorDiagramData()">
<h3>getAncestorDiagramData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="DiagramData.html" title="interface in com.nomagic.magicdraw.diff">DiagramData</a></span> <span class="element-name">getAncestorDiagramData</span>()</div>
<div class="block">Get ancestor diagram data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>data of modified diagram.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="DiagramData.html" title="interface in com.nomagic.magicdraw.diff"><code>DiagramData</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationKind()">
<h3>getModificationKind</h3>
<div class="member-signature"><span class="return-type"><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></span> <span class="element-name">getModificationKind</span>()</div>
<div class="block">Get modification kind.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modification kind.</dd>
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
