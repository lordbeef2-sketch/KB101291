# JAVA OPENAPI: OrderModificationInfo (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/diff/OrderModificationInfo.html
- source_path: `com/nomagic/magicdraw/diff/OrderModificationInfo.html`
- source_sha256: `1e7ca298927e5c990a9025c44c71ba46a60199dbff9aa835410c8a2a63a2710a`
- captured_utc: `2026-07-14T16:45:33.187444+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface OrderModificationInfo

All Superinterfaces:
`[GenericOrderModificationInfo](GenericOrderModificationInfo.html)`, `[ModificationInfo](ModificationInfo.html)`

@OpenApiAllpublic interfaceOrderModificationInfoextends [GenericOrderModificationInfo](GenericOrderModificationInfo.html)

Difference for multiple ordered references. Any ordered reference modification will cause
 [`OrderModificationInfo`](OrderModificationInfo.html).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getOrder](#getOrder())()`

============ METHOD DETAIL ========== 
Method Details
getOrder
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getOrder()
Specified by:
`[getOrder](GenericOrderModificationInfo.html#getOrder())` in interface `[GenericOrderModificationInfo](GenericOrderModificationInfo.html)`
Returns:
list of references ids in contributor project element.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface OrderModificationInfo">Interface OrderModificationInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="GenericOrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">GenericOrderModificationInfo</a></code>, <code><a href="ModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ModificationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">OrderModificationInfo</span><span class="extends-implements">
extends <a href="GenericOrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">GenericOrderModificationInfo</a></span></div>
<div class="block">Difference for multiple ordered references. Any ordered reference modification will cause
 <a href="OrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff"><code>OrderModificationInfo</code></a>.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOrder()">getOrder</a>()</code></div>
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
<section class="detail" id="getOrder()">
<h3>getOrder</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getOrder</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="GenericOrderModificationInfo.html#getOrder()">getOrder</a></code> in interface <code><a href="GenericOrderModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">GenericOrderModificationInfo</a></code></dd>
<dt>Returns:</dt>
<dd>list of references ids in contributor project element.</dd>
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
