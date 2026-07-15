# JAVA OPENAPI: ValueModificationInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/diff/ValueModificationInfo.html
- source_path: `com/nomagic/magicdraw/diff/ValueModificationInfo.html`
- source_sha256: `ae4782ea2abcb1b7963f56606a5a12ee90501ff51174c0be7e7e74f3afd8a6a9`
- captured_utc: `2026-07-14T16:55:15.700012+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ValueModificationInfo

All Superinterfaces:
`[ModificationInfo](ModificationInfo.html)`

All Known Subinterfaces:
`[ChangeOwnerInfo](ChangeOwnerInfo.html)`, `[PrimitiveMultiValueModificationInfo](PrimitiveMultiValueModificationInfo.html)`, `[PrimitiveValueModificationInfo](PrimitiveValueModificationInfo.html)`, `[ReferenceModificationInfo](ReferenceModificationInfo.html)`

@OpenApiAllpublic interfaceValueModificationInfoextends [ModificationInfo](ModificationInfo.html)

Modification which can have several types - addition, removing, changing(replacing).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ModificationKind](ModificationKind.html)`
`[getModificationKind](#getModificationKind())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue())()`

============ METHOD DETAIL ========== 
Method Details
getModificationKind
[ModificationKind](ModificationKind.html) getModificationKind()
Returns:
modification kind.
getValue
[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getValue()
Returns:
changed value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ValueModificationInfo">Interface ValueModificationInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ModificationInfo</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ChangeOwnerInfo.html" title="interface in com.nomagic.magicdraw.diff">ChangeOwnerInfo</a></code>, <code><a href="PrimitiveMultiValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">PrimitiveMultiValueModificationInfo</a></code>, <code><a href="PrimitiveValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">PrimitiveValueModificationInfo</a></code>, <code><a href="ReferenceModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ReferenceModificationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ValueModificationInfo</span><span class="extends-implements">
extends <a href="ModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ModificationInfo</a></span></div>
<div class="block">Modification which can have several types - addition, removing, changing(replacing).</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModificationKind()">getModificationKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getValue()">getValue</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getModificationKind()">
<h3>getModificationKind</h3>
<div class="member-signature"><span class="return-type"><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></span> <span class="element-name">getModificationKind</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modification kind.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue()">
<h3>getValue</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>changed value.</dd>
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
