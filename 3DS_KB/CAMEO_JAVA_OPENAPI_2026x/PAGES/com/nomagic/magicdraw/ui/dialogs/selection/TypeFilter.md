# JAVA OPENAPI: TypeFilter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/dialogs/selection/TypeFilter.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/selection/TypeFilter.html`
- source_sha256: `a5c100af8063ac2769ebb4826b1f156ae142cdbf3c9b83a32663afa4db6f17ff`
- captured_utc: `2026-07-14T16:58:25.558151+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.selection](package-summary.html)

## Interface TypeFilter

All Superinterfaces:
`com.nomagic.magicdraw.ui.ElementFilter`

All Known Implementing Classes:
`[TypeFilterImpl](TypeFilterImpl.html)`

@OpenApiAllpublic interfaceTypeFilterextends com.nomagic.magicdraw.ui.ElementFilter

Type element filter. Implementation filters element according the element type.
 Override `ElementFilter.accept(com.nomagic.magicdraw.uml.BaseElement)` method to change the filtering.

See Also:
[`TypeFilterImpl`](TypeFilterImpl.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[accept](#accept(com.nomagic.magicdraw.uml.BaseElement,boolean))([BaseElement](../../../uml/BaseElement.html) obj,
 boolean checkType)`
Tests element to satisfy filter condition.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?>`
`[getTypes](#getTypes())()`
Get the acceptable element types.
Methods inherited from interface com.nomagic.magicdraw.ui.ElementFilter
`accept`

============ METHOD DETAIL ========== 
Method Details
getTypes
@CheckForNull[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> getTypes()
Get the acceptable element types.
Returns:
acceptable element types. If null - all element types are accepted.
accept
boolean accept([BaseElement](../../../uml/BaseElement.html) obj,
 boolean checkType)
Tests element to satisfy filter condition.
Parameters:
`obj` - element.
`checkType` - check object type
Returns:
true if obj satisfies filter condition otherwise false.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.selection</a></div>
<h1 class="title" title="Interface TypeFilter">Interface TypeFilter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.nomagic.magicdraw.ui.ElementFilter</code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="TypeFilterImpl.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">TypeFilterImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TypeFilter</span><span class="extends-implements">
extends com.nomagic.magicdraw.ui.ElementFilter</span></div>
<div class="block">Type element filter. Implementation filters element according the element type.
 Override <code>ElementFilter.accept(com.nomagic.magicdraw.uml.BaseElement)</code> method to change the filtering.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="TypeFilterImpl.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection"><code>TypeFilterImpl</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.uml.BaseElement,boolean)">accept</a><wbr/>(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj,
 boolean checkType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Tests element to satisfy filter condition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTypes()">getTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get the acceptable element types.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.ElementFilter">Methods inherited from interface com.nomagic.magicdraw.ui.ElementFilter</h3>
<code>accept</code></div>
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
<section class="detail" id="getTypes()">
<h3>getTypes</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt;</span> <span class="element-name">getTypes</span>()</div>
<div class="block">Get the acceptable element types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>acceptable element types. If null - all element types are accepted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.magicdraw.uml.BaseElement,boolean)">
<h3>accept</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> obj,
 boolean checkType)</span></div>
<div class="block">Tests element to satisfy filter condition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - element.</dd>
<dd><code>checkType</code> - check object type</dd>
<dt>Returns:</dt>
<dd>true if obj satisfies filter condition otherwise false.</dd>
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
