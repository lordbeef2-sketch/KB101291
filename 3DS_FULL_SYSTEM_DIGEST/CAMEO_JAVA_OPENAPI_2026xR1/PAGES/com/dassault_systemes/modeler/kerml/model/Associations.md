# JAVA OPENAPI: Associations (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Associations.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Associations.html`
- source_sha256: `aba1476636c3a66c02cb76caaa52ba620701809e11fc563aae2ec4122846493a`
- captured_utc: `2026-07-14T16:44:47.253833+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Associations

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Associations

@OpenApiAllpublic classAssociations
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Association`](kerml/Association.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[SOURCE_INDEX](#SOURCE_INDEX)`
Index of the source end feature in the association’s ordered end list
`static final int`
`[TARGET_INDEX](#TARGET_INDEX)`
Index of the target end feature in the association’s ordered end list
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
`static [Feature](kerml/Feature.html)`
`[getAssociationEndSourceFeature](#getAssociationEndSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association))([Association](kerml/Association.html) association)`
Returns the source feature of the association end.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getAssociationEndTargetFeature](#getAssociationEndTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association))([Association](kerml/Association.html) association)`
Returns the target features of the association end.
`static [Feature](kerml/Feature.html)`
`[getOrCreateSourceEndFeature](#getOrCreateSourceEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association))([Association](kerml/Association.html) association)`
Returns the source end feature of the association, creating it if necessary.
`static [Feature](kerml/Feature.html)`
`[getOrCreateTargetEndFeature](#getOrCreateTargetEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association))([Association](kerml/Association.html) association)`
Returns the target end feature of the association, creating it if necessary.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SOURCE_INDEX
public static final int SOURCE_INDEX
Index of the source end feature in the association’s ordered end list
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Associations.SOURCE_INDEX)
TARGET_INDEX
public static final int TARGET_INDEX
Index of the target end feature in the association’s ordered end list
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Associations.TARGET_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Associations
public Associations()
 ============ METHOD DETAIL ========== 
Method Details
getOrCreateSourceEndFeature
public static [Feature](kerml/Feature.html) getOrCreateSourceEndFeature([Association](kerml/Association.html) association)
Returns the source end feature of the association, creating it if necessary.
Parameters:
`association` - the association
Returns:
existing or newly created source end feature
getOrCreateTargetEndFeature
public static [Feature](kerml/Feature.html) getOrCreateTargetEndFeature([Association](kerml/Association.html) association)
Returns the target end feature of the association, creating it if necessary.
Parameters:
`association` - the association
Returns:
existing or newly created target end feature
getAssociationEndSourceFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getAssociationEndSourceFeature([Association](kerml/Association.html) association)
Returns the source feature of the association end.
Parameters:
`association` - the association
Returns:
source end feature, or null
getAssociationEndTargetFeature
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getAssociationEndTargetFeature([Association](kerml/Association.html) association)
Returns the target features of the association end.
Parameters:
`association` - the association
Returns:
list of target end features

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Associations">Class Associations</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Associations</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Associations</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Association</code></a></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_INDEX">SOURCE_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the source end feature in the association’s ordered end list</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_INDEX">TARGET_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the target end feature in the association’s ordered end list</div>
</div>
</div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationEndSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">getAssociationEndSourceFeature</a><wbr/>(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source feature of the association end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAssociationEndTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">getAssociationEndTargetFeature</a><wbr/>(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target features of the association end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateSourceEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">getOrCreateSourceEndFeature</a><wbr/>(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source end feature of the association, creating it if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateTargetEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">getOrCreateTargetEndFeature</a><wbr/>(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target end feature of the association, creating it if necessary.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="SOURCE_INDEX">
<h3>SOURCE_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SOURCE_INDEX</span></div>
<div class="block">Index of the source end feature in the association’s ordered end list</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Associations.SOURCE_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_INDEX">
<h3>TARGET_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TARGET_INDEX</span></div>
<div class="block">Index of the target end feature in the association’s ordered end list</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Associations.TARGET_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
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
<section class="detail" id="getOrCreateSourceEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">
<h3>getOrCreateSourceEndFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateSourceEndFeature</span><wbr/><span class="parameters">(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</span></div>
<div class="block">Returns the source end feature of the association, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - the association</dd>
<dt>Returns:</dt>
<dd>existing or newly created source end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateTargetEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">
<h3>getOrCreateTargetEndFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateTargetEndFeature</span><wbr/><span class="parameters">(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</span></div>
<div class="block">Returns the target end feature of the association, creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - the association</dd>
<dt>Returns:</dt>
<dd>existing or newly created target end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationEndSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">
<h3>getAssociationEndSourceFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getAssociationEndSourceFeature</span><wbr/><span class="parameters">(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</span></div>
<div class="block">Returns the source feature of the association end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - the association</dd>
<dt>Returns:</dt>
<dd>source end feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAssociationEndTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Association)">
<h3>getAssociationEndTargetFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getAssociationEndTargetFeature</span><wbr/><span class="parameters">(<a href="kerml/Association.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Association</a> association)</span></div>
<div class="block">Returns the target features of the association end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>association</code> - the association</dd>
<dt>Returns:</dt>
<dd>list of target end features</dd>
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
