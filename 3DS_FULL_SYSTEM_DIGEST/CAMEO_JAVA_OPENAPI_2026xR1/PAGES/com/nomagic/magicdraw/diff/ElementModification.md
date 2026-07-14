# JAVA OPENAPI: ElementModification (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/diff/ElementModification.html
- source_path: `com/nomagic/magicdraw/diff/ElementModification.html`
- source_sha256: `7c97fe6fd104e4bb50005ecdbc8b603ef5437b3f9a53d5eb8fe0d96c43df5e15`
- captured_utc: `2026-07-14T16:45:32.863440+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ElementModification

All Superinterfaces:
`[Difference](Difference.html)`, `[DifferenceLocation](DifferenceLocation.html)`, `[ElementDifference](ElementDifference.html)`, `[Modification](Modification.html)`

@OpenApipublic interfaceElementModificationextends [Modification](Modification.html)

Element property is modified. Such property should be accessible using JMI reflection. Only not
 derived and not private properties are analyzed and only for them difference can be created.
 Modification details can be obtain using [`Modification.getModificationInfo()`](Modification.html#getModificationInfo())

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getChangedPropertyName](#getChangedPropertyName())()`
Get modified property/feature name.
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](DifferenceLocation.html)
`[getModuleURI](DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ElementDifference](ElementDifference.html)
`[getElementID](ElementDifference.html#getElementID())`
Methods inherited from interface com.nomagic.magicdraw.diff.[Modification](Modification.html)
`[getModificationInfo](Modification.html#getModificationInfo())`

============ METHOD DETAIL ========== 
Method Details
getChangedPropertyName
@OpenApi[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getChangedPropertyName()
Get modified property/feature name.
Returns:
changed property name.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ElementModification">Interface ElementModification</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code>, <code><a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementModification</span><span class="extends-implements">
extends <a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></span></div>
<div class="block">Element property is modified. Such property should be accessible using JMI reflection. Only not
 derived and not private properties are analyzed and only for them difference can be created.
 Modification details can be obtain using <a href="Modification.html#getModificationInfo()"><code>Modification.getModificationInfo()</code></a></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangedPropertyName()">getChangedPropertyName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get modified property/feature name.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.DifferenceLocation">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></h3>
<code><a href="DifferenceLocation.html#getModuleURI()">getModuleURI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ElementDifference">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></h3>
<code><a href="ElementDifference.html#getElementID()">getElementID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.Modification">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></h3>
<code><a href="Modification.html#getModificationInfo()">getModificationInfo</a></code></div>
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
<section class="detail" id="getChangedPropertyName()">
<h3>getChangedPropertyName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getChangedPropertyName</span>()</div>
<div class="block">Get modified property/feature name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>changed property name.</dd>
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
