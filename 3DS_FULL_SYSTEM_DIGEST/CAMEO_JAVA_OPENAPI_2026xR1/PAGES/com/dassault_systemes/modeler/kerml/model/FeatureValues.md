# JAVA OPENAPI: FeatureValues (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/FeatureValues.html
- source_path: `com/dassault_systemes/modeler/kerml/model/FeatureValues.html`
- source_sha256: `7720820a46e9f449d6fbd4eaa744fa1caddaf1fbaa11b5d78fc08b5f8fc045c8`
- captured_utc: `2026-07-14T16:44:47.595837+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class FeatureValues

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.FeatureValues

@OpenApiAllpublic classFeatureValues
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`FeatureValue`](kerml/FeatureValue.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FeatureValues](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [FeatureValue](kerml/FeatureValue.html)`
`[getOwnedFeatureValue](#getOwnedFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns the owned feature value of the given feature.
`static [Expression](kerml/Expression.html)`
`[getOwnedFeatureValueExpression](#getOwnedFeatureValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns the value expression of the owned feature value.
`static [Expression](kerml/Expression.html)`
`[getValueExpression](#getValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns the effective value expression of the feature,
 considering redefinitions.
`static boolean`
`[hasBindingFeatureValue](#hasBindingFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature has a binding (non‑initial, non‑default) feature value.
`static boolean`
`[hasInitialFeatureValue](#hasInitialFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature has an initial feature value.
`static boolean`
`[hasOwnedFeatureValue](#hasOwnedFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature has any owned feature value.
`static boolean`
`[isApplicable](#isApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the feature is allowed to have a feature value.
`static [FeatureValue](kerml/FeatureValue.html)`
`[setValue](#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object))([Feature](kerml/Feature.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Sets or clears the feature value of the given feature.
`static [FeatureValue](kerml/FeatureValue.html)`
`[setValue](#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object))([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Sets a feature value by creating or reusing a redefining feature.
`static [FeatureValue](kerml/FeatureValue.html)`
`[setValue](#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Supplier,java.lang.Object))([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) feature,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.eclipse.emf.ecore.EClass> redefiningECLassSupplier,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Sets a feature value using a custom redefining feature class supplier.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FeatureValues
public FeatureValues()
 ============ METHOD DETAIL ========== 
Method Details
getOwnedFeatureValue
@CheckForNullpublic static [FeatureValue](kerml/FeatureValue.html) getOwnedFeatureValue([Feature](kerml/Feature.html) feature)
Returns the owned feature value of the given feature.
Parameters:
`feature` - the feature
Returns:
owned feature value, or null
hasBindingFeatureValue
public static boolean hasBindingFeatureValue([Feature](kerml/Feature.html) feature)
Checks whether the feature has a binding (non‑initial, non‑default) feature value.
Parameters:
`feature` - the feature
Returns:
true if a binding feature value exists
hasOwnedFeatureValue
public static boolean hasOwnedFeatureValue([Feature](kerml/Feature.html) feature)
Checks whether the feature has any owned feature value.
Parameters:
`feature` - the feature
Returns:
true if an owned feature value exists
getValueExpression
@CheckForNullpublic static [Expression](kerml/Expression.html) getValueExpression([Feature](kerml/Feature.html) feature)
Returns the effective value expression of the feature,
 considering redefinitions.
Parameters:
`feature` - the feature
Returns:
value expression, or null
getOwnedFeatureValueExpression
@CheckForNullpublic static [Expression](kerml/Expression.html) getOwnedFeatureValueExpression([Feature](kerml/Feature.html) feature)
Returns the value expression of the owned feature value.
Parameters:
`feature` - the feature
Returns:
value expression, or null
isApplicable
public static boolean isApplicable([Feature](kerml/Feature.html) feature)
Checks whether the feature is allowed to have a feature value.
Parameters:
`feature` - the feature
Returns:
true if applicable
hasInitialFeatureValue
public static boolean hasInitialFeatureValue([Feature](kerml/Feature.html) feature)
Checks whether the feature has an initial feature value.
Parameters:
`feature` - the feature
Returns:
true if the feature value is initial
setValue
@CheckForNullpublic static [FeatureValue](kerml/FeatureValue.html) setValue([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Sets a feature value by creating or reusing a redefining feature.
Parameters:
`type` - the owning type
`feature` - the feature being redefined
`value` - value to assign
Returns:
created or updated feature value, or null
setValue
@CheckForNullpublic static [FeatureValue](kerml/FeatureValue.html) setValue([Type](kerml/Type.html) type,
 [Feature](kerml/Feature.html) feature,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<org.eclipse.emf.ecore.EClass> redefiningECLassSupplier,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Sets a feature value using a custom redefining feature class supplier.
Parameters:
`type` - the owning type
`feature` - the feature being redefined
`redefiningECLassSupplier` - supplier for redefining feature class
`value` - value to assign
Returns:
created or updated feature value, or null
setValue
@CheckForNullpublic static [FeatureValue](kerml/FeatureValue.html) setValue([Feature](kerml/Feature.html) feature,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Sets or clears the feature value of the given feature.
 Creates a new FeatureValue if needed.
Parameters:
`feature` - the feature
`value` - literal value or expression
Returns:
created or updated feature value, or null if removed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class FeatureValues">Class FeatureValues</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.FeatureValues</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeatureValues</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureValue</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FeatureValues</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOwnedFeatureValue</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned feature value of the given feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedFeatureValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getOwnedFeatureValueExpression</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the value expression of the owned feature value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getValueExpression</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the effective value expression of the feature,
 considering redefinitions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasBindingFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">hasBindingFeatureValue</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature has a binding (non‑initial, non‑default) feature value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasInitialFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">hasInitialFeatureValue</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature has an initial feature value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasOwnedFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">hasOwnedFeatureValue</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature has any owned feature value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isApplicable</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the feature is allowed to have a feature value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">setValue</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets or clears the feature value of the given feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">setValue</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets a feature value by creating or reusing a redefining feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Supplier,java.lang.Object)">setValue</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.eclipse.emf.ecore.EClass&gt; redefiningECLassSupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets a feature value using a custom redefining feature class supplier.</div>
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
<h3>FeatureValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FeatureValues</span>()</div>
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
<section class="detail" id="getOwnedFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOwnedFeatureValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">getOwnedFeatureValue</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns the owned feature value of the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>owned feature value, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasBindingFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>hasBindingFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasBindingFeatureValue</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature has a binding (non‑initial, non‑default) feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if a binding feature value exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasOwnedFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>hasOwnedFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasOwnedFeatureValue</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature has any owned feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if an owned feature value exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getValueExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getValueExpression</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns the effective value expression of the feature,
 considering redefinitions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>value expression, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedFeatureValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getOwnedFeatureValueExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOwnedFeatureValueExpression</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns the value expression of the owned feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>value expression, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isApplicable(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isApplicable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isApplicable</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature is allowed to have a feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if applicable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasInitialFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>hasInitialFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasInitialFeatureValue</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the feature has an initial feature value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature value is initial</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets a feature value by creating or reusing a redefining feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the owning type</dd>
<dd><code>feature</code> - the feature being redefined</dd>
<dd><code>value</code> - value to assign</dd>
<dt>Returns:</dt>
<dd>created or updated feature value, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.function.Supplier,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;org.eclipse.emf.ecore.EClass&gt; redefiningECLassSupplier,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets a feature value using a custom redefining feature class supplier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the owning type</dd>
<dd><code>feature</code> - the feature being redefined</dd>
<dd><code>redefiningECLassSupplier</code> - supplier for redefining feature class</dd>
<dd><code>value</code> - value to assign</dd>
<dt>Returns:</dt>
<dd>created or updated feature value, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.lang.Object)">
<h3>setValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureValue.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureValue</a></span> <span class="element-name">setValue</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Sets or clears the feature value of the given feature.
 Creates a new FeatureValue if needed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dd><code>value</code> - literal value or expression</dd>
<dt>Returns:</dt>
<dd>created or updated feature value, or null if removed</dd>
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
