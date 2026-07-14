# JAVA OPENAPI: AggregationCompositionNumbering (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/autoid/custom/AggregationCompositionNumbering.html
- source_path: `com/nomagic/magicdraw/autoid/custom/AggregationCompositionNumbering.html`
- source_sha256: `04e576f27ab67aa788f7371ddd7621e12a02b7c3ffa082255a9abf1b35adf19c`
- captured_utc: `2026-07-14T16:55:03.109871+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.autoid.custom](package-summary.html)

## Class AggregationCompositionNumbering

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
[com.nomagic.magicdraw.autoid.custom.DirectedAssociationNumbering](DirectedAssociationNumbering.html)
com.nomagic.magicdraw.autoid.custom.AggregationCompositionNumbering

All Implemented Interfaces:
`com.nomagic.magicdraw.autoid.IAssociationNumbering`, `[INumberingAction](../INumberingAction.html)`

@OpenApiAllpublic classAggregationCompositionNumbering
extends [DirectedAssociationNumbering](DirectedAssociationNumbering.html)

Numbering Elements connected by aggregation or composition

 Feb 21, 2012

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
`nInfo`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AggregationCompositionNumbering](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getAssociationTarget](#getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
If the Association is directed, determine the Target element
Methods inherited from class com.nomagic.magicdraw.autoid.custom.[DirectedAssociationNumbering](DirectedAssociationNumbering.html)
`[collectRelations](DirectedAssociationNumbering.html#collectRelations(java.util.List)), [getAssociationTypes](DirectedAssociationNumbering.html#getAssociationTypes())`
Methods inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
`generateIds, isSuitableType`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AggregationCompositionNumbering
public AggregationCompositionNumbering()
 ============ METHOD DETAIL ========== 
Method Details
getAssociationTarget
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getAssociationTarget([Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Description copied from interface: `com.nomagic.magicdraw.autoid.IAssociationNumbering`
If the Association is directed, determine the Target element
Specified by:
`getAssociationTarget` in interface `com.nomagic.magicdraw.autoid.IAssociationNumbering`
Overrides:
`[getAssociationTarget](DirectedAssociationNumbering.html#getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))` in class `[DirectedAssociationNumbering](DirectedAssociationNumbering.html)`
Parameters:
`association` - the Association
Returns:
the target or null if not found

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.autoid.custom</a></div>
<h1 class="title" title="Class AggregationCompositionNumbering">Class AggregationCompositionNumbering</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
<div class="inheritance"><a href="DirectedAssociationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">com.nomagic.magicdraw.autoid.custom.DirectedAssociationNumbering</a>
<div class="inheritance">com.nomagic.magicdraw.autoid.custom.AggregationCompositionNumbering</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.autoid.IAssociationNumbering</code>, <code><a href="../INumberingAction.html" title="interface in com.nomagic.magicdraw.autoid">INumberingAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AggregationCompositionNumbering</span>
<span class="extends-implements">extends <a href="DirectedAssociationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedAssociationNumbering</a></span></div>
<div class="block">Numbering Elements connected by aggregation or composition

 Feb 21, 2012</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering">Fields inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering</h3>
<code>nInfo</code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AggregationCompositionNumbering</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getAssociationTarget</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If the Association is directed, determine the Target element</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.autoid.custom.DirectedAssociationNumbering">Methods inherited from class com.nomagic.magicdraw.autoid.custom.<a href="DirectedAssociationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedAssociationNumbering</a></h3>
<code><a href="DirectedAssociationNumbering.html#collectRelations(java.util.List)">collectRelations</a>, <a href="DirectedAssociationNumbering.html#getAssociationTypes()">getAssociationTypes</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering">Methods inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering</h3>
<code>generateIds, isSuitableType</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>AggregationCompositionNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AggregationCompositionNumbering</span>()</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>getAssociationTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getAssociationTarget</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.autoid.IAssociationNumbering</code></span></div>
<div class="block">If the Association is directed, determine the Target element</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getAssociationTarget</code> in interface <code>com.nomagic.magicdraw.autoid.IAssociationNumbering</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DirectedAssociationNumbering.html#getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getAssociationTarget</a></code> in class <code><a href="DirectedAssociationNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedAssociationNumbering</a></code></dd>
<dt>Parameters:</dt>
<dd><code>association</code> - the Association</dd>
<dt>Returns:</dt>
<dd>the target or null if not found</dd>
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
