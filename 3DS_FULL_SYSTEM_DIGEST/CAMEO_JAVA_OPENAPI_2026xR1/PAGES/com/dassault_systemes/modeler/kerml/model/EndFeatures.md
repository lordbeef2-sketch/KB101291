# JAVA OPENAPI: EndFeatures (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/EndFeatures.html
- source_path: `com/dassault_systemes/modeler/kerml/model/EndFeatures.html`
- source_sha256: `a82ae3c7ce42e5b297bf0d640fb142276b1132b7d56c4a22ec003163677ae7d7`
- captured_utc: `2026-07-14T16:44:47.436835+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class EndFeatures

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.EndFeatures

@OpenApiAllpublic classEndFeatures
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EndFeatures](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Feature](kerml/Feature.html)`
`[createEndFeature](#createEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Creates a new end feature for the given type.
`static org.eclipse.emf.ecore.EClass`
`[getEndFeatureMembershipEClass](#getEndFeatureMembershipEClass(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the EClass of the end‑feature membership for the given type.
`static [Feature](kerml/Feature.html)`
`[getOtherEnd](#getOtherEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) end)`
Returns the other end of the binary type owning the given end feature.
`static [Feature](kerml/Feature.html)`
`[getOtherEnd](#getOtherEnd(java.util.List,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> endFeatures,
 [Feature](kerml/Feature.html) end)`
Returns the other end of a binary type.
`static boolean`
`[isAlwaysBinary](#isAlwaysBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Checks whether the type is always binary, based on its metaclass.
`static boolean`
`[isAssociationOrConnector](#isAssociationOrConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element is an association or connector.
`static boolean`
`[isBinary](#isBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Checks whether the type is binary (i.e., has exactly two end features).
`static boolean`
`[isEnd](#isEnd(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element is an end feature.
`static boolean`
`[isNary](#isNary(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Checks whether the type is n‑ary (i.e., not binary).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EndFeatures
public EndFeatures()
 ============ METHOD DETAIL ========== 
Method Details
createEndFeature
public static [Feature](kerml/Feature.html) createEndFeature([Type](kerml/Type.html) type)
Creates a new end feature for the given type. The end feature is created
 using the appropriate EClass for the type and wrapped in a corresponding
 [`FeatureMembership`](kerml/FeatureMembership.html). The membership is then added to the type.
Parameters:
`type` - the type for which to create an end feature
Returns:
the created end feature
getEndFeatureMembershipEClass
public static org.eclipse.emf.ecore.EClass getEndFeatureMembershipEClass([Type](kerml/Type.html) type)
Returns the EClass of the end‑feature membership for the given type.
 If the type already has end features, their membership EClass is used.
 Otherwise, a default membership EClass is selected.
Parameters:
`type` - the type
Returns:
membership EClass
isBinary
public static boolean isBinary([Type](kerml/Type.html) type)
Checks whether the type is binary (i.e., has exactly two end features).
Parameters:
`type` - the type
Returns:
true if binary
isNary
public static boolean isNary([Type](kerml/Type.html) type)
Checks whether the type is n‑ary (i.e., not binary).
Parameters:
`type` - the type
Returns:
true if n‑ary
isAlwaysBinary
public static boolean isAlwaysBinary([Type](kerml/Type.html) type)
Checks whether the type is always binary, based on its metaclass.
Parameters:
`type` - the type
Returns:
true if always binary
getOtherEnd
public static [Feature](kerml/Feature.html) getOtherEnd([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> endFeatures,
 [Feature](kerml/Feature.html) end)
Returns the other end of a binary type.
Parameters:
`endFeatures` - list of end features
`end` - one of the ends
Returns:
the opposite end
getOtherEnd
public static [Feature](kerml/Feature.html) getOtherEnd([Feature](kerml/Feature.html) end)
Returns the other end of the binary type owning the given end feature.
Parameters:
`end` - the end feature
Returns:
the opposite end
isAssociationOrConnector
public static boolean isAssociationOrConnector(@CheckForNull
 [Element](kerml/Element.html) element)
Checks whether the element is an association or connector.
Parameters:
`element` - the element
Returns:
true if association or connector
isEnd
public static boolean isEnd([Element](kerml/Element.html) element)
Checks whether the element is an end feature.
Parameters:
`element` - the element
Returns:
true if the element is a feature marked as an end

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class EndFeatures">Class EndFeatures</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.EndFeatures</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">EndFeatures</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EndFeatures</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type)">createEndFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new end feature for the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static org.eclipse.emf.ecore.EClass</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndFeatureMembershipEClass(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getEndFeatureMembershipEClass</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the EClass of the end‑feature membership for the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOtherEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOtherEnd</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the other end of the binary type owning the given end feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOtherEnd(java.util.List,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOtherEnd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; endFeatures,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the other end of a binary type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlwaysBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isAlwaysBinary</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the type is always binary, based on its metaclass.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssociationOrConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isAssociationOrConnector</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is an association or connector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isBinary</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the type is binary (i.e., has exactly two end features).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnd(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isEnd</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is an end feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isNary</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the type is n‑ary (i.e., not binary).</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>EndFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EndFeatures</span>()</div>
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
<section class="detail" id="createEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>createEndFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">createEndFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Creates a new end feature for the given type. The end feature is created
 using the appropriate EClass for the type and wrapped in a corresponding
 <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureMembership</code></a>. The membership is then added to the type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type for which to create an end feature</dd>
<dt>Returns:</dt>
<dd>the created end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndFeatureMembershipEClass(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getEndFeatureMembershipEClass</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">org.eclipse.emf.ecore.EClass</span> <span class="element-name">getEndFeatureMembershipEClass</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the EClass of the end‑feature membership for the given type.
 If the type already has end features, their membership EClass is used.
 Otherwise, a default membership EClass is selected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>membership EClass</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isBinary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBinary</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the type is binary (i.e., has exactly two end features).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>true if binary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isNary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNary</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the type is n‑ary (i.e., not binary).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>true if n‑ary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAlwaysBinary(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isAlwaysBinary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAlwaysBinary</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the type is always binary, based on its metaclass.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>true if always binary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOtherEnd(java.util.List,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOtherEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOtherEnd</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; endFeatures,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns the other end of a binary type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>endFeatures</code> - list of end features</dd>
<dd><code>end</code> - one of the ends</dd>
<dt>Returns:</dt>
<dd>the opposite end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOtherEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOtherEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOtherEnd</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns the other end of the binary type owning the given end feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - the end feature</dd>
<dt>Returns:</dt>
<dd>the opposite end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssociationOrConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isAssociationOrConnector</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAssociationOrConnector</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is an association or connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>true if association or connector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnd(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEnd</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is an end feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>true if the element is a feature marked as an end</dd>
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
