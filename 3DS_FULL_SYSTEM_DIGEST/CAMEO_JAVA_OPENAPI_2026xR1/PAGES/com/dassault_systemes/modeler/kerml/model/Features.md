# JAVA OPENAPI: Features (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Features.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Features.html`
- source_sha256: `83a160afbe3fc8c461e586db83183d7d4f8a61e38288847526256023d581c768`
- captured_utc: `2026-07-14T16:44:47.607838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Features

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Features

@OpenApiAllpublic classFeatures
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Feature`](kerml/Feature.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Features](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static <T extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)>> 
T`
`[collectAllFeaturingTypes](#collectAllFeaturingTypes(com.dassault_systemes.modeler.kerml.model.kerml.Feature,T))([Feature](kerml/Feature.html) feature,
 T collected)`
Collects all featuring types of the feature recursively.
`static [Type](kerml/Type.html)`
`[getContainingTypeOrContext](#getContainingTypeOrContext(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Type](kerml/Type.html) context,
 [Feature](kerml/Feature.html) feature)`
Extracts a type containing a given feature from a given context.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEffectiveName](#getEffectiveName(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Function))([Feature](kerml/Feature.html) feature,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Feature](kerml/Feature.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> nameFunction)`
Returns the effective name of the feature using the given name function.
`static [Feature](kerml/Feature.html)`
`[getOwningFeatureOfAnonymousFeature](#getOwningFeatureOfAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) anonymousFeature)`
Returns the owning feature of an anonymous feature.
`static [Feature](kerml/Feature.html)`
`[getRedefiningFeatureInType](#getRedefiningFeatureInType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) type)`
Get Feature of the given type that is the same or redefined that is provided.
`static boolean`
`[isAnonymousFeature](#isAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature is anonymous.
`static boolean`
`[isInheritedFromType](#isInheritedFromType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) type)`
Checks whether the feature is inherited from the given type.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Features
public Features()
 ============ METHOD DETAIL ========== 
Method Details
getEffectiveName
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEffectiveName([Feature](kerml/Feature.html) feature,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Feature](kerml/Feature.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> nameFunction)
Returns the effective name of the feature using the given name function.
Parameters:
`feature` - the feature
`nameFunction` - function extracting a name from the feature
Returns:
effective name, or null if none found
getContainingTypeOrContext
public static [Type](kerml/Type.html) getContainingTypeOrContext([Type](kerml/Type.html) context,
 [Feature](kerml/Feature.html) feature)
Extracts a type containing a given feature from a given context.
 It is either one of Feature::type if context is a Feature, or passed context itself.
 (must-precondition - given feature belong to "context.feature")
Parameters:
`context` - context
`feature` - feature
Returns:
type of context to which the given feature belongs
isInheritedFromType
public static boolean isInheritedFromType([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) type)
Checks whether the feature is inherited from the given type.
Parameters:
`feature` - the feature
`type` - the type to check against
Returns:
true if the feature is inherited from the type
collectAllFeaturingTypes
public static <T extends [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)>> T collectAllFeaturingTypes([Feature](kerml/Feature.html) feature,
 T collected)
Collects all featuring types of the feature recursively.
Type Parameters:
`T` - collection type
Parameters:
`feature` - the feature
`collected` - collection to populate
Returns:
the populated collection
getRedefiningFeatureInType
@CheckForNullpublic static [Feature](kerml/Feature.html) getRedefiningFeatureInType([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) type)
Get Feature of the given type that is the same or redefined that is provided.
 Example: Have Calc defined: Inc { in x; x+1} and call attribute my = Inc(5); Feature is x defined in Inc calc
 Type is InvocationExpression calling it, it has x feature as input (value 5).
 Methods returns if Invocation x (feature) is sameOrRedefined as calc x (feature).
Parameters:
`feature` - feature to look for
`type` - type in which to look for provided feature
Returns:
feature of a type
isAnonymousFeature
public static boolean isAnonymousFeature([Feature](kerml/Feature.html) feature)
Checks whether the feature is anonymous.
 A feature is anonymous if it is a plain Feature and its owning relationship
 is not an OwningMembership.
Parameters:
`feature` - the feature
Returns:
true if anonymous
getOwningFeatureOfAnonymousFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getOwningFeatureOfAnonymousFeature([Feature](kerml/Feature.html) anonymousFeature)
Returns the owning feature of an anonymous feature.
Parameters:
`anonymousFeature` - anonymous feature
Returns:
owning feature, or null

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Features">Class Features</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Features</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Features</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Features</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectAllFeaturingTypes(com.dassault_systemes.modeler.kerml.model.kerml.Feature,T)">collectAllFeaturingTypes</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 T collected)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all featuring types of the feature recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainingTypeOrContext(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getContainingTypeOrContext</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extracts a type containing a given feature from a given context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEffectiveName(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Function)">getEffectiveName</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; nameFunction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the effective name of the feature using the given name function.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwningFeatureOfAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOwningFeatureOfAnonymousFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> anonymousFeature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owning feature of an anonymous feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefiningFeatureInType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">getRedefiningFeatureInType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Feature of the given type that is the same or redefined that is provided.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isAnonymousFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is anonymous.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInheritedFromType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">isInheritedFromType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is inherited from the given type.</div>
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
<h3>Features</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Features</span>()</div>
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
<section class="detail" id="getEffectiveName(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Function)">
<h3>getEffectiveName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEffectiveName</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; nameFunction)</span></div>
<div class="block">Returns the effective name of the feature using the given name function.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>nameFunction</code> - function extracting a name from the feature</dd>
<dt>Returns:</dt>
<dd>effective name, or null if none found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainingTypeOrContext(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getContainingTypeOrContext</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getContainingTypeOrContext</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Extracts a type containing a given feature from a given context.
 It is either one of Feature::type if context is a Feature, or passed context itself.
 (must-precondition - given feature belong to "context.feature")</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - context</dd>
<dd><code>feature</code> - feature</dd>
<dt>Returns:</dt>
<dd>type of context to which the given feature belongs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInheritedFromType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isInheritedFromType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInheritedFromType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the feature is inherited from the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>type</code> - the type to check against</dd>
<dt>Returns:</dt>
<dd>true if the feature is inherited from the type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectAllFeaturingTypes(com.dassault_systemes.modeler.kerml.model.kerml.Feature,T)">
<h3 id="collectAllFeaturingTypes(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.Collection)">collectAllFeaturingTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;&gt;</span> <span class="return-type">T</span> <span class="element-name">collectAllFeaturingTypes</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 T collected)</span></div>
<div class="block">Collects all featuring types of the feature recursively.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - collection type</dd>
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>collected</code> - collection to populate</dd>
<dt>Returns:</dt>
<dd>the populated collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefiningFeatureInType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getRedefiningFeatureInType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefiningFeatureInType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Get Feature of the given type that is the same or redefined that is provided.
 Example: Have Calc defined: Inc { in x; x+1} and call attribute my = Inc(5); Feature is x defined in Inc calc
 Type is InvocationExpression calling it, it has x feature as input (value 5).
 Methods returns if Invocation x (feature) is sameOrRedefined as calc x (feature).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature to look for</dd>
<dd><code>type</code> - type in which to look for provided feature</dd>
<dt>Returns:</dt>
<dd>feature of a type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isAnonymousFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAnonymousFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is anonymous.
 A feature is anonymous if it is a plain Feature and its owning relationship
 is not an OwningMembership.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if anonymous</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningFeatureOfAnonymousFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOwningFeatureOfAnonymousFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwningFeatureOfAnonymousFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> anonymousFeature)</span></div>
<div class="block">Returns the owning feature of an anonymous feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>anonymousFeature</code> - anonymous feature</dd>
<dt>Returns:</dt>
<dd>owning feature, or null</dd>
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
