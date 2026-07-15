# JAVA OPENAPI: Associations (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/Associations.html
- source_path: `com/nomagic/magicdraw/uml2/Associations.html`
- source_sha256: `c4ffbb2502783d30dd778a2d50f63666d93e0aa99072847d83ea4cae594e1f40`
- captured_utc: `2026-07-14T16:52:15.989932+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2](package-summary.html)

## Class Associations

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.Associations

public classAssociations
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience utility methods that operate on [`Association`](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) elements.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Associations](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getFirstMemberEnd](#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
Get first property member end of association.
`static [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)`
`[getSecondMemberEnd](#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
Get second property member end of association.
`static boolean`
`[isAggregation](#isAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association,
 [AggregationKind](../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html) aggregationKind)`
Determines if association is of specified aggregation kind.
`static boolean`
`[isDirectedAggregation](#isDirectedAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association,
 [AggregationKind](../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html) aggregationKind)`
Determines if association is of specified aggregation kind and directed.
`static boolean`
`[isDirectedAssociation](#isDirectedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
Check if association is directed
`static boolean`
`[isNonNavigableAssociation](#isNonNavigableAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
Check if association is non navigable
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Associations
public Associations()
 ============ METHOD DETAIL ========== 
Method Details
isAggregation
public static boolean isAggregation([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association,
 [AggregationKind](../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html) aggregationKind)
Determines if association is of specified aggregation kind.
Parameters:
`association` - association element
`aggregationKind` - AggregationKindEnum.SHARED - aggregation, AggregationKindEnum.COMPOSITE - composition
Returns:
true if one of association ends has set specified aggregation kind
isDirectedAggregation
public static boolean isDirectedAggregation([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association,
 [AggregationKind](../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html) aggregationKind)
Determines if association is of specified aggregation kind and directed.
Parameters:
`association` - association element
`aggregationKind` - AggregationKindEnum.SHARED - aggregation, AggregationKindEnum.COMPOSITE - composition
Returns:
true if one of association ends has set specified aggregation kind
isDirectedAssociation
public static boolean isDirectedAssociation([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Check if association is directed
Parameters:
`association` - association
Returns:
true if at least one end is navigable
isNonNavigableAssociation
public static boolean isNonNavigableAssociation([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Check if association is non navigable
Parameters:
`association` - association
Returns:
true if both ends are not navigable
getFirstMemberEnd
public static [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getFirstMemberEnd([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Get first property member end of association.
Parameters:
`association` - association element
Returns:
first property member end of association
getSecondMemberEnd
public static [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) getSecondMemberEnd([Association](../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Get second property member end of association.
Parameters:
`association` - association element
Returns:
second property member end of association

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2</a></div>
<h1 class="title" title="Class Associations">Class Associations</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.Associations</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">Associations</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience utility methods that operate on <a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Association</code></a> elements.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Associations</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getFirstMemberEnd</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get first property member end of association.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getSecondMemberEnd</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get second property member end of association.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">isAggregation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> aggregationKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines if association is of specified aggregation kind.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirectedAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">isDirectedAggregation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> aggregationKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines if association is of specified aggregation kind and directed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirectedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">isDirectedAssociation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if association is directed</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNonNavigableAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">isNonNavigableAssociation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if association is non navigable</div>
</div>
</div>
</div>
</div>
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
<h3>Associations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Associations</span>()</div>
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
<section class="detail" id="isAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">
<h3>isAggregation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAggregation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> aggregationKind)</span></div>
<div class="block">Determines if association is of specified aggregation kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association element</dd>
<dd><code>aggregationKind</code> - AggregationKindEnum.SHARED - aggregation, AggregationKindEnum.COMPOSITE - composition</dd>
<dt>Returns:</dt>
<dd>true if one of association ends has set specified aggregation kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirectedAggregation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.AggregationKind)">
<h3>isDirectedAggregation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDirectedAggregation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/AggregationKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">AggregationKind</a> aggregationKind)</span></div>
<div class="block">Determines if association is of specified aggregation kind and directed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association element</dd>
<dd><code>aggregationKind</code> - AggregationKindEnum.SHARED - aggregation, AggregationKindEnum.COMPOSITE - composition</dd>
<dt>Returns:</dt>
<dd>true if one of association ends has set specified aggregation kind</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirectedAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>isDirectedAssociation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDirectedAssociation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block">Check if association is directed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association</dd>
<dt>Returns:</dt>
<dd>true if at least one end is navigable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNonNavigableAssociation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>isNonNavigableAssociation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNonNavigableAssociation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block">Check if association is non navigable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association</dd>
<dt>Returns:</dt>
<dd>true if both ends are not navigable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>getFirstMemberEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getFirstMemberEnd</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block">Get first property member end of association.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association element</dd>
<dt>Returns:</dt>
<dd>first property member end of association</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSecondMemberEnd(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">
<h3>getSecondMemberEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSecondMemberEnd</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</span></div>
<div class="block">Get second property member end of association.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - association element</dd>
<dt>Returns:</dt>
<dd>second property member end of association</dd>
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
