# JAVA OPENAPI: Directions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Directions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Directions.html`
- source_sha256: `44b0e503c8c90fb19d56518f8a397073482671c680a351455e7b98dd59a365aa`
- captured_utc: `2026-07-14T16:44:47.338834+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Directions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Directions

@OpenApiAllpublic classDirections
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with a direction of [`Feature`](kerml/Feature.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Directions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [FeatureDirectionKind](kerml/FeatureDirectionKind.html)`
`[getDirection](#getDirection(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) context)`
Returns the direction of the feature in the given context.
`static [FeatureDirectionKind](kerml/FeatureDirectionKind.html)`
`[getDirectionByFeatures](#getDirectionByFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Calculates direction by direction of its features [`Type.getFeature()`](kerml/Type.html#getFeature()).
`static [FeatureDirectionKind](kerml/FeatureDirectionKind.html)`
`[getDirectionInOwningType](#getDirectionInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) owningType)`
Returns the direction of the feature within the given owning type.
`static [FeatureDirectionKind](kerml/FeatureDirectionKind.html)`
`[getEffectiveDirection](#getEffectiveDirection(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) context)`
Provides an effective or actual direction for a given [`Feature`](kerml/Feature.html).
`static boolean`
`[isInDirection](#isInDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind))([FeatureDirectionKind](kerml/FeatureDirectionKind.html) direction)`
Returns true if the direction is input or bidirectional.
`static boolean`
`[isInputInOwningType](#isInputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature is an input in its owning type.
`static boolean`
`[isInputInOwningType](#isInputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) owningType)`
Checks whether the feature is an input in the given owning type.
`static boolean`
`[isOutDirection](#isOutDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind))([FeatureDirectionKind](kerml/FeatureDirectionKind.html) direction)`
Returns true if the direction is output or bidirectional.
`static boolean`
`[isOutputInOwningType](#isOutputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature is an output in its owning type.
`static boolean`
`[isOutputInOwningType](#isOutputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type))([Feature](kerml/Feature.html) feature,
 [Type](kerml/Type.html) owningType)`
Checks whether the feature is an output in the given owning type.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Directions
public Directions()
 ============ METHOD DETAIL ========== 
Method Details
getDirectionInOwningType
@CheckForNullpublic static [FeatureDirectionKind](kerml/FeatureDirectionKind.html) getDirectionInOwningType([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Type](kerml/Type.html) owningType)
Returns the direction of the feature within the given owning type.
Parameters:
`feature` - the feature
`owningType` - the type in which direction is evaluated
Returns:
direction of the feature in the owning type, or null
isInputInOwningType
public static boolean isInputInOwningType([Feature](kerml/Feature.html) feature)
Checks whether the feature is an input in its owning type.
Parameters:
`feature` - the feature
Returns:
true if the feature is an input
isInputInOwningType
public static boolean isInputInOwningType([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Type](kerml/Type.html) owningType)
Checks whether the feature is an input in the given owning type.
Parameters:
`feature` - the feature
`owningType` - the type in which direction is evaluated
Returns:
true if the feature is an input
isOutputInOwningType
public static boolean isOutputInOwningType([Feature](kerml/Feature.html) feature)
Checks whether the feature is an output in its owning type.
Parameters:
`feature` - the feature
Returns:
true if the feature is an output
isOutputInOwningType
public static boolean isOutputInOwningType([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Type](kerml/Type.html) owningType)
Checks whether the feature is an output in the given owning type.
Parameters:
`feature` - the feature
`owningType` - the type in which direction is evaluated
Returns:
true if the feature is an output
isInDirection
public static boolean isInDirection(@CheckForNull
 [FeatureDirectionKind](kerml/FeatureDirectionKind.html) direction)
Returns true if the direction is input or bidirectional.
Parameters:
`direction` - the direction
Returns:
true if input-like
isOutDirection
public static boolean isOutDirection(@CheckForNull
 [FeatureDirectionKind](kerml/FeatureDirectionKind.html) direction)
Returns true if the direction is output or bidirectional.
Parameters:
`direction` - the direction
Returns:
true if output-like
getDirectionByFeatures
@CheckForNullpublic static [FeatureDirectionKind](kerml/FeatureDirectionKind.html) getDirectionByFeatures([Feature](kerml/Feature.html) feature)
Calculates direction by direction of its features [`Type.getFeature()`](kerml/Type.html#getFeature()).
Parameters:
`feature` - given feature
Returns:
direction by features or null if all features are non-directional or there are no features
getDirection
@CheckForNullpublic static [FeatureDirectionKind](kerml/FeatureDirectionKind.html) getDirection([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Type](kerml/Type.html) context)
Returns the direction of the feature in the given context. If the feature
 has an explicit direction and the context is non-null, the direction is
 resolved relative to the containing type.
Parameters:
`feature` - the feature
`context` - the context type
Returns:
direction, or null
getEffectiveDirection
@CheckForNullpublic static [FeatureDirectionKind](kerml/FeatureDirectionKind.html) getEffectiveDirection([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Type](kerml/Type.html) context)
Provides an effective or actual direction for a given [`Feature`](kerml/Feature.html).
 Effective direction can be calculated, for example, from owned features.
Parameters:
`feature` - feature
`context` - context of feature
Returns:
direction

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Directions">Class Directions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Directions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Directions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with a direction of <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Directions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirection(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">getDirection</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the direction of the feature in the given context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectionByFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getDirectionByFeatures</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates direction by direction of its features <a href="kerml/Type.html#getFeature()"><code>Type.getFeature()</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectionInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">getDirectionInOwningType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owningType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the direction of the feature within the given owning type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEffectiveDirection(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">getEffectiveDirection</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Provides an effective or actual direction for a given <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">isInDirection</a><wbr/>(<a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the direction is input or bidirectional.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isInputInOwningType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is an input in its owning type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">isInputInOwningType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owningType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is an input in the given owning type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOutDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">isOutDirection</a><wbr/>(<a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> direction)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true if the direction is output or bidirectional.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOutputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOutputInOwningType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is an output in its owning type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOutputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">isOutputInOwningType</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owningType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is an output in the given owning type.</div>
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
<h3>Directions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Directions</span>()</div>
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
<section class="detail" id="getDirectionInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getDirectionInOwningType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getDirectionInOwningType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owningType)</span></div>
<div class="block">Returns the direction of the feature within the given owning type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>owningType</code> - the type in which direction is evaluated</dd>
<dt>Returns:</dt>
<dd>direction of the feature in the owning type, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isInputInOwningType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInputInOwningType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is an input in its owning type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is an input</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isInputInOwningType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInputInOwningType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owningType)</span></div>
<div class="block">Checks whether the feature is an input in the given owning type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>owningType</code> - the type in which direction is evaluated</dd>
<dt>Returns:</dt>
<dd>true if the feature is an input</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOutputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOutputInOwningType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOutputInOwningType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is an output in its owning type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is an output</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOutputInOwningType(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isOutputInOwningType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOutputInOwningType</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> owningType)</span></div>
<div class="block">Checks whether the feature is an output in the given owning type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>owningType</code> - the type in which direction is evaluated</dd>
<dt>Returns:</dt>
<dd>true if the feature is an output</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">
<h3>isInDirection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInDirection</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> direction)</span></div>
<div class="block">Returns true if the direction is input or bidirectional.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - the direction</dd>
<dt>Returns:</dt>
<dd>true if input-like</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOutDirection(com.dassault_systemes.modeler.kerml.model.kerml.FeatureDirectionKind)">
<h3>isOutDirection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOutDirection</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a> direction)</span></div>
<div class="block">Returns true if the direction is output or bidirectional.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - the direction</dd>
<dt>Returns:</dt>
<dd>true if output-like</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectionByFeatures(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getDirectionByFeatures</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getDirectionByFeatures</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Calculates direction by direction of its features <a href="kerml/Type.html#getFeature()"><code>Type.getFeature()</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - given feature</dd>
<dt>Returns:</dt>
<dd>direction by features or null if all features are non-directional or there are no features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirection(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getDirection</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context)</span></div>
<div class="block">Returns the direction of the feature in the given context. If the feature
 has an explicit direction and the context is non-null, the direction is
 resolved relative to the containing type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>context</code> - the context type</dd>
<dt>Returns:</dt>
<dd>direction, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEffectiveDirection(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getEffectiveDirection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureDirectionKind.html" title="class in com.dassault_systemes.modeler.kerml.model.kerml">FeatureDirectionKind</a></span> <span class="element-name">getEffectiveDirection</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context)</span></div>
<div class="block">Provides an effective or actual direction for a given <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Feature</code></a>.
 Effective direction can be calculated, for example, from owned features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - feature</dd>
<dd><code>context</code> - context of feature</dd>
<dt>Returns:</dt>
<dd>direction</dd>
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
