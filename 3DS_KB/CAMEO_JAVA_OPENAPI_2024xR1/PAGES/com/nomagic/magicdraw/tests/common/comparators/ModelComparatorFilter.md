# JAVA OPENAPI: ModelComparatorFilter (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/tests/common/comparators/ModelComparatorFilter.html
- source_path: `com/nomagic/magicdraw/tests/common/comparators/ModelComparatorFilter.html`
- source_sha256: `f2c0c03fb0b0a2835e5ff4f3899bf81cb5ee926d3b51099899216ecf96773e0e`
- captured_utc: `2026-07-14T16:51:47.298550+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests.common.comparators](package-summary.html)

## Interface ModelComparatorFilter

@OpenApiAllpublic interfaceModelComparatorFilter
Base interface of filters used to skip unnecessary model elements during models comparison.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`boolean`
`[needToCompare](#needToCompare(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e)`
Checks if given element should be compared by comparator or skipped.
`default boolean`
`[needToCompareAttribute](#needToCompareAttribute(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e1,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e2)`
Checks if attributes of given element should be compared by comparator or skipped.

============ METHOD DETAIL ========== 
Method Details
needToCompare
boolean needToCompare([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e)
Checks if given element should be compared by comparator or skipped.
Parameters:
`e` - element to check.
Returns:
true if elements should be compared, false if element should be skipped.
needToCompareAttribute
default boolean needToCompareAttribute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e1,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e2)
Checks if attributes of given element should be compared by comparator or skipped. References will be compared in any case.
Parameters:
`name` - attribute name
`e1` - first element to check
`e2` - first element to check
Returns:
true if attribute should be compared, false if element should be skipped.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests.common.comparators</a></div>
<h1 class="title" title="Interface ModelComparatorFilter">Interface ModelComparatorFilter</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelComparatorFilter</span></div>
<div class="block">Base interface of filters used to skip unnecessary model elements during models comparison.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#needToCompare(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">needToCompare</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if given element should be compared by comparator or skipped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#needToCompareAttribute(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">needToCompareAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e1,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Checks if attributes of given element should be compared by comparator or skipped.</div>
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
<section class="detail" id="needToCompare(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>needToCompare</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">needToCompare</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e)</span></div>
<div class="block">Checks if given element should be compared by comparator or skipped.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - element to check.</dd>
<dt>Returns:</dt>
<dd>true if elements should be compared, false if element should be skipped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needToCompareAttribute(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>needToCompareAttribute</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">needToCompareAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e1,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e2)</span></div>
<div class="block">Checks if attributes of given element should be compared by comparator or skipped. References will be compared in any case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - attribute name</dd>
<dd><code>e1</code> - first element to check</dd>
<dd><code>e2</code> - first element to check</dd>
<dt>Returns:</dt>
<dd>true if attribute should be compared, false if element should be skipped.</dd>
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
