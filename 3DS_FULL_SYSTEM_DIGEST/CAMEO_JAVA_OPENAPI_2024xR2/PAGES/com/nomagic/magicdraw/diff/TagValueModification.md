# JAVA OPENAPI: TagValueModification (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/diff/TagValueModification.html
- source_path: `com/nomagic/magicdraw/diff/TagValueModification.html`
- source_sha256: `2d302c89ffbb333819368cbdd5d831fcf939dfb3a1957d3e622d5ce64c778fc7`
- captured_utc: `2026-07-14T16:55:15.676011+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface TagValueModification

All Superinterfaces:
`[Difference](Difference.html)`, `[DifferenceLocation](DifferenceLocation.html)`, `[ElementDifference](ElementDifference.html)`, `[Modification](Modification.html)`

@OpenApipublic interfaceTagValueModificationextends [Modification](Modification.html)

Difference when tagged value is changed in contributor project. Modification details can be
 obtain using [`Modification.getModificationInfo()`](Modification.html#getModificationInfo())

 In case tagged value has non references values, always [`PrimitiveValueModificationInfo`](PrimitiveValueModificationInfo.html) is created.
 In case new value is not set Empty List is used as new value. In other case
 [`ReferenceModificationInfo`](ReferenceModificationInfo.html) is created with [`ModificationKind.ADDED`](ModificationKind.html#ADDED) or [`ModificationKind.REMOVED`](ModificationKind.html#REMOVED) values [`ModificationKind.REPLACED`](ModificationKind.html#REPLACED) is never generated.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTVPropertyID](#getTVPropertyID())()`
Methods inherited from interface com.nomagic.magicdraw.diff.[DifferenceLocation](DifferenceLocation.html)
`[getModuleURI](DifferenceLocation.html#getModuleURI())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ElementDifference](ElementDifference.html)
`[getElementID](ElementDifference.html#getElementID())`
Methods inherited from interface com.nomagic.magicdraw.diff.[Modification](Modification.html)
`[getModificationInfo](Modification.html#getModificationInfo())`

============ METHOD DETAIL ========== 
Method Details
getTVPropertyID
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTVPropertyID()
Returns:
property id of tagged value definition (property is defined by [`Slot.getDefiningFeature()`](../../uml2/ext/magicdraw/classes/mdkernel/Slot.html#getDefiningFeature()).

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface TagValueModification">Interface TagValueModification</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code>, <code><a href="DifferenceLocation.html" title="interface in com.nomagic.magicdraw.diff">DifferenceLocation</a></code>, <code><a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code>, <code><a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TagValueModification</span><span class="extends-implements">
extends <a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></span></div>
<div class="block">Difference when tagged value is changed in contributor project. Modification details can be
 obtain using <a href="Modification.html#getModificationInfo()"><code>Modification.getModificationInfo()</code></a>

 In case tagged value has non references values, always <a href="PrimitiveValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff"><code>PrimitiveValueModificationInfo</code></a> is created.
 In case new value is not set Empty List is used as new value. In other case
 <a href="ReferenceModificationInfo.html" title="interface in com.nomagic.magicdraw.diff"><code>ReferenceModificationInfo</code></a> is created with <a href="ModificationKind.html#ADDED"><code>ModificationKind.ADDED</code></a> or <a href="ModificationKind.html#REMOVED"><code>ModificationKind.REMOVED</code></a> values <a href="ModificationKind.html#REPLACED"><code>ModificationKind.REPLACED</code></a> is never generated.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTVPropertyID()">getTVPropertyID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getTVPropertyID()">
<h3>getTVPropertyID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTVPropertyID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property id of tagged value definition (property is defined by <a href="../../uml2/ext/magicdraw/classes/mdkernel/Slot.html#getDefiningFeature()"><code>Slot.getDefiningFeature()</code></a>.</dd>
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
