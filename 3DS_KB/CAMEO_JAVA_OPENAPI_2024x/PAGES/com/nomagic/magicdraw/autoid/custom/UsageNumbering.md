# JAVA OPENAPI: UsageNumbering (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/autoid/custom/UsageNumbering.html
- source_path: `com/nomagic/magicdraw/autoid/custom/UsageNumbering.html`
- source_sha256: `6842cd93991cc38c6c6cfa7f2bc885362015859c35e2f224d5ce6d87d5f4e043`
- captured_utc: `2026-07-14T16:51:02.105948+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.autoid.custom](package-summary.html)

## Class UsageNumbering

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
[com.nomagic.magicdraw.autoid.custom.DirectedRelationshipNumbering](DirectedRelationshipNumbering.html)
com.nomagic.magicdraw.autoid.custom.UsageNumbering

All Implemented Interfaces:
`[INumberingAction](../INumberingAction.html)`, `[IRelationshipNumbering](../IRelationshipNumbering.html)`

@OpenApiAllpublic classUsageNumbering
extends [DirectedRelationshipNumbering](DirectedRelationshipNumbering.html)

Numbering elements connected by <> Relationships

 Feb 20, 2012

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
`nInfo`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[UsageNumbering](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [DirectedRelationship](../../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html)>>`
`[getRelationTypes](#getRelationTypes())()`
Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.
Methods inherited from class com.nomagic.magicdraw.autoid.custom.[DirectedRelationshipNumbering](DirectedRelationshipNumbering.html)
`[collectRelations](DirectedRelationshipNumbering.html#collectRelations(java.util.List))`
Methods inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
`generateIds, isSuitableType`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UsageNumbering
public UsageNumbering()
 ============ METHOD DETAIL ========== 
Method Details
getRelationTypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [DirectedRelationship](../../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html)>> getRelationTypes()
Description copied from interface: `[IRelationshipNumbering](../IRelationshipNumbering.html#getRelationTypes())`
Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.
Specified by:
`[getRelationTypes](../IRelationshipNumbering.html#getRelationTypes())` in interface `[IRelationshipNumbering](../IRelationshipNumbering.html)`
Overrides:
`[getRelationTypes](DirectedRelationshipNumbering.html#getRelationTypes())` in class `[DirectedRelationshipNumbering](DirectedRelationshipNumbering.html)`
Returns:
a collection of directed relationship types

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.autoid.custom</a></div>
<h1 class="title" title="Class UsageNumbering">Class UsageNumbering</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
<div class="inheritance"><a href="DirectedRelationshipNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">com.nomagic.magicdraw.autoid.custom.DirectedRelationshipNumbering</a>
<div class="inheritance">com.nomagic.magicdraw.autoid.custom.UsageNumbering</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../INumberingAction.html" title="interface in com.nomagic.magicdraw.autoid">INumberingAction</a></code>, <code><a href="../IRelationshipNumbering.html" title="interface in com.nomagic.magicdraw.autoid">IRelationshipNumbering</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">UsageNumbering</span>
<span class="extends-implements">extends <a href="DirectedRelationshipNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedRelationshipNumbering</a></span></div>
<div class="block">Numbering elements connected by &lt;<usage>&gt; Relationships

 Feb 20, 2012</usage></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">UsageNumbering</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationTypes()">getRelationTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.autoid.custom.DirectedRelationshipNumbering">Methods inherited from class com.nomagic.magicdraw.autoid.custom.<a href="DirectedRelationshipNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedRelationshipNumbering</a></h3>
<code><a href="DirectedRelationshipNumbering.html#collectRelations(java.util.List)">collectRelations</a></code></div>
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
<h3>UsageNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UsageNumbering</span>()</div>
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
<section class="detail" id="getRelationTypes()">
<h3>getRelationTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/DirectedRelationship.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DirectedRelationship</a>&gt;&gt;</span> <span class="element-name">getRelationTypes</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../IRelationshipNumbering.html#getRelationTypes()">IRelationshipNumbering</a></code></span></div>
<div class="block">Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IRelationshipNumbering.html#getRelationTypes()">getRelationTypes</a></code> in interface <code><a href="../IRelationshipNumbering.html" title="interface in com.nomagic.magicdraw.autoid">IRelationshipNumbering</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DirectedRelationshipNumbering.html#getRelationTypes()">getRelationTypes</a></code> in class <code><a href="DirectedRelationshipNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">DirectedRelationshipNumbering</a></code></dd>
<dt>Returns:</dt>
<dd>a collection of directed relationship types</dd>
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
