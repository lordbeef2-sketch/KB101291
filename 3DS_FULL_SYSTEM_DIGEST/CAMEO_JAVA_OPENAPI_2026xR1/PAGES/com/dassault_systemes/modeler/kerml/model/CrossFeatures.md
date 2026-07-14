# JAVA OPENAPI: CrossFeatures (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/CrossFeatures.html
- source_path: `com/dassault_systemes/modeler/kerml/model/CrossFeatures.html`
- source_sha256: `745e5efb019788a13780c45d784e81ceaa872d8b2a77b5cc579f79fb3c1b04d9`
- captured_utc: `2026-07-14T16:44:47.304836+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class CrossFeatures

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.CrossFeatures

@OpenApiAllpublic final classCrossFeatures
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with cross-features.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CrossFeatures](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Feature](kerml/Feature.html)`
`[createOwnedCrossFeature](#createOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) endFeature)`
Creates a new owned cross feature for the given end feature.
`static void`
`[createOwnedCrossFeatureFromEnd](#createOwnedCrossFeatureFromEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) endFeature)`
Creates an owned cross feature from the given end feature and copies
 relevant properties such as ordering, uniqueness, and multiplicity.
`static [Feature](kerml/Feature.html)`
`[getOrCreateOwnedCrossFeature](#getOrCreateOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns the owned cross feature of the given feature, creating one if necessary.
`static boolean`
`[isAcceptableAsOwnedCrossFeature](#isAcceptableAsOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the given feature is acceptable as an owned cross feature.
`static boolean`
`[isAcceptableAsOwningMembershipOfOwnedCrossFeature](#isAcceptableAsOwningMembershipOfOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership))([OwningMembership](kerml/OwningMembership.html) owningMembership)`
Checks whether the given owning membership is acceptable for an owned cross feature.
`static void`
`[moveCrossFeatureToEnd](#moveCrossFeatureToEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) endFeature)`
Moves the cross feature associated with the given end feature so that it becomes
 owned by the end feature.
`static void`
`[moveCrossFeatureToEndType](#moveCrossFeatureToEndType(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) endFeature)`
Moves the cross feature associated with the given end feature so that it becomes
 owned by the type of the opposite end.
`static void`
`[setCrossFeatureOwningEnd](#setCrossFeatureOwningEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) crossFeature,
 [Feature](kerml/Feature.html) endFeature)`
Sets the owning membership of the cross feature so that it is owned by the end feature.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CrossFeatures
public CrossFeatures()
 ============ METHOD DETAIL ========== 
Method Details
isAcceptableAsOwnedCrossFeature
public static boolean isAcceptableAsOwnedCrossFeature([Feature](kerml/Feature.html) feature)
Checks whether the given feature is acceptable as an owned cross feature.
 Cross features cannot be multiplicities, binding connectors, or metadata features.
Parameters:
`feature` - the feature to check
Returns:
true if the feature can be used as an owned cross feature
isAcceptableAsOwningMembershipOfOwnedCrossFeature
public static boolean isAcceptableAsOwningMembershipOfOwnedCrossFeature(@CheckForNull
 [OwningMembership](kerml/OwningMembership.html) owningMembership)
Checks whether the given owning membership is acceptable for an owned cross feature.
 Cross features cannot be owned by [`FeatureMembership`](kerml/FeatureMembership.html) or [`FeatureValue`](kerml/FeatureValue.html).
Parameters:
`owningMembership` - the membership to check
Returns:
true if acceptable as owning membership of a cross feature
createOwnedCrossFeatureFromEnd
public static void createOwnedCrossFeatureFromEnd([Feature](kerml/Feature.html) endFeature)
Creates an owned cross feature from the given end feature and copies
 relevant properties such as ordering, uniqueness, and multiplicity.
 The end feature is updated to reflect cross‑feature semantics.
Parameters:
`endFeature` - the end feature
createOwnedCrossFeature
public static [Feature](kerml/Feature.html) createOwnedCrossFeature([Feature](kerml/Feature.html) endFeature)
Creates a new owned cross feature for the given end feature.
 The EClass of the cross feature depends on whether the end feature
 belongs to an [`EndFeatureMembership`](kerml/EndFeatureMembership.html).
Parameters:
`endFeature` - the end feature
Returns:
created cross feature
setCrossFeatureOwningEnd
public static void setCrossFeatureOwningEnd([Feature](kerml/Feature.html) crossFeature,
 [Feature](kerml/Feature.html) endFeature)
Sets the owning membership of the cross feature so that it is owned by the end feature.
Parameters:
`crossFeature` - the cross feature
`endFeature` - the end feature
moveCrossFeatureToEnd
public static void moveCrossFeatureToEnd([Feature](kerml/Feature.html) endFeature)
Moves the cross feature associated with the given end feature so that it becomes
 owned by the end feature. The existing cross feature is converted to a new instance.
Parameters:
`endFeature` - the end feature
moveCrossFeatureToEndType
public static void moveCrossFeatureToEndType([Feature](kerml/Feature.html) endFeature)
Moves the cross feature associated with the given end feature so that it becomes
 owned by the type of the opposite end. The cross feature is reused rather than recreated.
Parameters:
`endFeature` - the end feature
getOrCreateOwnedCrossFeature
public static [Feature](kerml/Feature.html) getOrCreateOwnedCrossFeature([Feature](kerml/Feature.html) feature)
Returns the owned cross feature of the given feature, creating one if necessary.
Parameters:
`feature` - the feature
Returns:
existing or newly created cross feature

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class CrossFeatures">Class CrossFeatures</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.CrossFeatures</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">CrossFeatures</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with cross-features.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CrossFeatures</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">createOwnedCrossFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new owned cross feature for the given end feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOwnedCrossFeatureFromEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">createOwnedCrossFeatureFromEnd</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an owned cross feature from the given end feature and copies
 relevant properties such as ordering, uniqueness, and multiplicity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOrCreateOwnedCrossFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned cross feature of the given feature, creating one if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAcceptableAsOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isAcceptableAsOwnedCrossFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is acceptable as an owned cross feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAcceptableAsOwningMembershipOfOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">isAcceptableAsOwningMembershipOfOwnedCrossFeature</a><wbr/>(<a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> owningMembership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given owning membership is acceptable for an owned cross feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#moveCrossFeatureToEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">moveCrossFeatureToEnd</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Moves the cross feature associated with the given end feature so that it becomes
 owned by the end feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#moveCrossFeatureToEndType(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">moveCrossFeatureToEndType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Moves the cross feature associated with the given end feature so that it becomes
 owned by the type of the opposite end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setCrossFeatureOwningEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setCrossFeatureOwningEnd</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> crossFeature,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the owning membership of the cross feature so that it is owned by the end feature.</div>
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
<h3>CrossFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CrossFeatures</span>()</div>
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
<section class="detail" id="isAcceptableAsOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isAcceptableAsOwnedCrossFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAcceptableAsOwnedCrossFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is acceptable as an owned cross feature.
 Cross features cannot be multiplicities, binding connectors, or metadata features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dt>Returns:</dt>
<dd>true if the feature can be used as an owned cross feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAcceptableAsOwningMembershipOfOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">
<h3>isAcceptableAsOwningMembershipOfOwnedCrossFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAcceptableAsOwningMembershipOfOwnedCrossFeature</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> owningMembership)</span></div>
<div class="block">Checks whether the given owning membership is acceptable for an owned cross feature.
 Cross features cannot be owned by <a href="kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureMembership</code></a> or <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureValue</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owningMembership</code> - the membership to check</dd>
<dt>Returns:</dt>
<dd>true if acceptable as owning membership of a cross feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOwnedCrossFeatureFromEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>createOwnedCrossFeatureFromEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createOwnedCrossFeatureFromEnd</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</span></div>
<div class="block">Creates an owned cross feature from the given end feature and copies
 relevant properties such as ordering, uniqueness, and multiplicity.
 The end feature is updated to reflect cross‑feature semantics.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>endFeature</code> - the end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>createOwnedCrossFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">createOwnedCrossFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</span></div>
<div class="block">Creates a new owned cross feature for the given end feature.
 The EClass of the cross feature depends on whether the end feature
 belongs to an <a href="kerml/EndFeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>EndFeatureMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>endFeature</code> - the end feature</dd>
<dt>Returns:</dt>
<dd>created cross feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCrossFeatureOwningEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setCrossFeatureOwningEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setCrossFeatureOwningEnd</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> crossFeature,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</span></div>
<div class="block">Sets the owning membership of the cross feature so that it is owned by the end feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>crossFeature</code> - the cross feature</dd>
<dd><code>endFeature</code> - the end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveCrossFeatureToEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>moveCrossFeatureToEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">moveCrossFeatureToEnd</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</span></div>
<div class="block">Moves the cross feature associated with the given end feature so that it becomes
 owned by the end feature. The existing cross feature is converted to a new instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>endFeature</code> - the end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveCrossFeatureToEndType(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>moveCrossFeatureToEndType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">moveCrossFeatureToEndType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> endFeature)</span></div>
<div class="block">Moves the cross feature associated with the given end feature so that it becomes
 owned by the type of the opposite end. The cross feature is reused rather than recreated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>endFeature</code> - the end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOwnedCrossFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOrCreateOwnedCrossFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateOwnedCrossFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns the owned cross feature of the given feature, creating one if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>existing or newly created cross feature</dd>
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
