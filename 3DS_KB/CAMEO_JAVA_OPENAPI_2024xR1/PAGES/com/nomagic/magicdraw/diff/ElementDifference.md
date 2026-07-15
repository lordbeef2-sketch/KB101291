# JAVA OPENAPI: ElementDifference (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/diff/ElementDifference.html
- source_path: `com/nomagic/magicdraw/diff/ElementDifference.html`
- source_sha256: `b78e8c73baf735d7b0489b7f543301ba053b4c9f48363fa092485788034b4cf5`
- captured_utc: `2026-07-14T16:51:17.831159+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ElementDifference

All Superinterfaces:
`[Difference](Difference.html)`, `[DifferenceLocation](DifferenceLocation.html)`

All Known Subinterfaces:
`[ElementAddition](ElementAddition.html)`, `[ElementDeletion](ElementDeletion.html)`, `[ElementModification](ElementModification.html)`, `[MDExtensionDifference](mdextensions/MDExtensionDifference.html)`, `[MDExtensionExistenceDifference](mdextensions/MDExtensionExistenceDifference.html)`, `[MDExtensionModificationDifference](mdextensions/MDExtensionModificationDifference.html)`, `[Modification](Modification.html)`, `[StereotypeModification](StereotypeModification.html)`, `[TagValueModification](TagValueModification.html)`

@OpenApiAllpublic interfaceElementDifferenceextends [Difference](Difference.html), [DifferenceLocation](DifferenceLocation.html)

Difference for model element. This difference provides information about which element was changed.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementID](#getElementID())()`
Get affected element id.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](DifferenceLocation.html)
`[getModuleURI](DifferenceLocation.html#getModuleURI())`

============ METHOD DETAIL ========== 
Method Details
getElementID
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementID()
Get affected element id.
Returns:
id of element.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ElementDifference">Interface ElementDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ElementAddition.html" title="interface in com.nomagic.magicdraw.diff">ElementAddition</a></code>, <code><a href="ElementDeletion.html" title="interface in com.nomagic.magicdraw.diff">ElementDeletion</a></code>, <code><a href="ElementModification.html" title="interface in com.nomagic.magicdraw.diff">ElementModification</a></code>, <code><a href="mdextensions/MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></code>, <code><a href="mdextensions/MDExtensionExistenceDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference</a></code>, <code><a href="mdextensions/MDExtensionModificationDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionModificationDifference</a></code>, <code><a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></code>, <code><a href="StereotypeModification.html" title="interface in com.nomagic.magicdraw.diff">StereotypeModification</a></code>, <code><a href="TagValueModification.html" title="interface in com.nomagic.magicdraw.diff">TagValueModification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementDifference</span><span class="extends-implements">
extends <a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a>, <a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></span></div>
<div class="block">Difference for model element. This difference provides information about which element was changed.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementID()">getElementID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get affected element id.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
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
<section class="detail" id="getElementID()">
<h3>getElementID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementID</span>()</div>
<div class="block">Get affected element id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>id of element.</dd>
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
