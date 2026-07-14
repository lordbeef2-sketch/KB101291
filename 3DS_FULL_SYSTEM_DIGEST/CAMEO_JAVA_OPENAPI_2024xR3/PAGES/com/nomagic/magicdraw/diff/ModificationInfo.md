# JAVA OPENAPI: ModificationInfo (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/diff/ModificationInfo.html
- source_path: `com/nomagic/magicdraw/diff/ModificationInfo.html`
- source_sha256: `3d43c0f057ee19e66011700a706895f3748fe339a755734f5c9f19e864064191`
- captured_utc: `2026-07-14T16:55:16.554028+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ModificationInfo

All Known Subinterfaces:
`[ChangeOwnerInfo](ChangeOwnerInfo.html)`, `[GenericOrderModificationInfo](GenericOrderModificationInfo.html)`, `[OrderModificationInfo](OrderModificationInfo.html)`, `[PrimitiveMultiValueModificationInfo](PrimitiveMultiValueModificationInfo.html)`, `[PrimitiveValueModificationInfo](PrimitiveValueModificationInfo.html)`, `[ReferenceModificationInfo](ReferenceModificationInfo.html)`, `[ValueModificationInfo](ValueModificationInfo.html)`, `[ValueOrderModificationInfo](ValueOrderModificationInfo.html)`

@OpenApipublic interfaceModificationInfo

Additional information about difference for [`Modification`](Modification.html).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.diff.ModificationInfoVisitor))(com.nomagic.magicdraw.diff.ModificationInfoVisitor visitor)`

============ METHOD DETAIL ========== 
Method Details
accept
void accept(com.nomagic.magicdraw.diff.ModificationInfoVisitor visitor)
Parameters:
`visitor` - visitor.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ModificationInfo">Interface ModificationInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ChangeOwnerInfo.html" title="interface in com.nomagic.magicdraw.diff">ChangeOwnerInfo</a></code>, <code><a href="GenericOrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">GenericOrderModificationInfo</a></code>, <code><a href="OrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">OrderModificationInfo</a></code>, <code><a href="PrimitiveMultiValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">PrimitiveMultiValueModificationInfo</a></code>, <code><a href="PrimitiveValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">PrimitiveValueModificationInfo</a></code>, <code><a href="ReferenceModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ReferenceModificationInfo</a></code>, <code><a href="ValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueModificationInfo</a></code>, <code><a href="ValueOrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueOrderModificationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModificationInfo</span></div>
<div class="block">Additional information about difference for <a href="Modification.html" title="interface in com.nomagic.magicdraw.diff"><code>Modification</code></a>.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.diff.ModificationInfoVisitor)">accept</a><wbr/>(com.nomagic.magicdraw.diff.ModificationInfoVisitor visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="accept(com.nomagic.magicdraw.diff.ModificationInfoVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(com.nomagic.magicdraw.diff.ModificationInfoVisitor visitor)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visitor</code> - visitor.</dd>
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
