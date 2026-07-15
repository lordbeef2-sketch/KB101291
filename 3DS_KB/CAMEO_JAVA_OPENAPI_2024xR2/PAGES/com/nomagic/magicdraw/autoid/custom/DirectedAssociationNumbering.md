# JAVA OPENAPI: DirectedAssociationNumbering (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/autoid/custom/DirectedAssociationNumbering.html
- source_path: `com/nomagic/magicdraw/autoid/custom/DirectedAssociationNumbering.html`
- source_sha256: `aa5d421b1dfe59a56eb061ebe553730b432688ba787bb7d5f2b84e7c2bcbd883`
- captured_utc: `2026-07-14T16:55:03.139872+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.autoid.custom](package-summary.html)

## Class DirectedAssociationNumbering

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
com.nomagic.magicdraw.autoid.custom.DirectedAssociationNumbering

All Implemented Interfaces:
`com.nomagic.magicdraw.autoid.IAssociationNumbering`, `[INumberingAction](../INumberingAction.html)`

Direct Known Subclasses:
`[AggregationCompositionNumbering](AggregationCompositionNumbering.html)`

@OpenApiAllpublic classDirectedAssociationNumbering
extends com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
implements com.nomagic.magicdraw.autoid.IAssociationNumbering

Numbering for Elements connected by directed Associations

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
`[DirectedAssociationNumbering](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[collectRelations](#collectRelations(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Collecting the Elements that are connected through given DirectedRelationship
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getAssociationTarget](#getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association))([Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)`
If the Association is directed, determine the Target element
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html)>>`
`[getAssociationTypes](#getAssociationTypes())()`
Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.
Methods inherited from class com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
`generateIds, isSuitableType`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DirectedAssociationNumbering
public DirectedAssociationNumbering()
 ============ METHOD DETAIL ========== 
Method Details
getAssociationTarget
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getAssociationTarget([Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html) association)
Description copied from interface: `com.nomagic.magicdraw.autoid.IAssociationNumbering`
If the Association is directed, determine the Target element
Specified by:
`getAssociationTarget` in interface `com.nomagic.magicdraw.autoid.IAssociationNumbering`
Parameters:
`association` - the Association
Returns:
the target or null if not found
getAssociationTypes
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Association](../../../uml2/ext/magicdraw/classes/mdkernel/Association.html)>> getAssociationTypes()
Description copied from interface: `com.nomagic.magicdraw.autoid.IAssociationNumbering`
Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.
Specified by:
`getAssociationTypes` in interface `com.nomagic.magicdraw.autoid.IAssociationNumbering`
Returns:
a collection of directed relationship types
collectRelations
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html),[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> collectRelations([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Description copied from class: `com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering`
Collecting the Elements that are connected through given DirectedRelationship
Specified by:
`collectRelations` in class `com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering`
Parameters:
`elements` - the elements to test
Returns:
a map of source-target connected by DirectedRelationship

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.autoid.custom</a></div>
<h1 class="title" title="Class DirectedAssociationNumbering">Class DirectedAssociationNumbering</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
<div class="inheritance">com.nomagic.magicdraw.autoid.custom.DirectedAssociationNumbering</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.autoid.IAssociationNumbering</code>, <code><a href="../INumberingAction.html" title="interface in com.nomagic.magicdraw.autoid">INumberingAction</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AggregationCompositionNumbering.html" title="class in com.nomagic.magicdraw.autoid.custom">AggregationCompositionNumbering</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DirectedAssociationNumbering</span>
<span class="extends-implements">extends com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering
implements com.nomagic.magicdraw.autoid.IAssociationNumbering</span></div>
<div class="block">Numbering for Elements connected by directed Associations

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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DirectedAssociationNumbering</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#collectRelations(java.util.List)">collectRelations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collecting the Elements that are connected through given DirectedRelationship</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationTarget(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Association)">getAssociationTarget</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">If the Association is directed, determine the Target element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationTypes()">getAssociationTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.</div>
</div>
</div>
</div>
</div>
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
<h3>DirectedAssociationNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DirectedAssociationNumbering</span>()</div>
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
<dt>Parameters:</dt>
<dd><code>association</code> - the Association</dd>
<dt>Returns:</dt>
<dd>the target or null if not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationTypes()">
<h3>getAssociationTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Association.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Association</a>&gt;&gt;</span> <span class="element-name">getAssociationTypes</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.nomagic.magicdraw.autoid.IAssociationNumbering</code></span></div>
<div class="block">Which types of directedRelationships should be taken into consideration
 for element sthat are eithe rsource or target of the given relation types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getAssociationTypes</code> in interface <code>com.nomagic.magicdraw.autoid.IAssociationNumbering</code></dd>
<dt>Returns:</dt>
<dd>a collection of directed relationship types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectRelations(java.util.List)">
<h3>collectRelations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>,<wbr/><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">collectRelations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering</code></span></div>
<div class="block">Collecting the Elements that are connected through given DirectedRelationship</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>collectRelations</code> in class <code>com.nomagic.magicdraw.autoid.AbstractRelationshipNumbering</code></dd>
<dt>Parameters:</dt>
<dd><code>elements</code> - the elements to test</dd>
<dt>Returns:</dt>
<dd>a map of source-target connected by DirectedRelationship</dd>
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
