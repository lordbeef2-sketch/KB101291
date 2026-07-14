# JAVA OPENAPI: FeatureChainExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/FeatureChainExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/FeatureChainExpressions.html`
- source_sha256: `acc076c13ec3e85d10614ddef82bd1fd62a75f2e2fc1dbeda6d53433b9d64118`
- captured_utc: `2026-07-14T16:44:47.465834+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class FeatureChainExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.FeatureChainExpressions

@OpenApiAllpublic classFeatureChainExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`FeatureChainExpression`](kerml/FeatureChainExpression.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPERATOR](#OPERATOR)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FeatureChainExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [FeatureChainExpression](kerml/FeatureChainExpression.html)`
`[create](#create(com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.util.List))([Expression](kerml/Expression.html) pureExpression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> target)`
Creates a feature chain expression using a pure source expression and a target feature list.
`static [FeatureChainExpression](kerml/FeatureChainExpression.html)`
`[create](#create(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> sourceAndTarget)`
Creates a feature chain expression from a list of source and target features.
`static [Expression](kerml/Expression.html)`
`[createChainOrReferenceExpression](#createChainOrReferenceExpression(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> referenced)`
Creates [`FeatureChainExpression`](kerml/FeatureChainExpression.html) if more than one feature is given or [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html) if one.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getChainingFeatureOfTarget](#getChainingFeatureOfTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression)`
Returns the chaining features of the target feature.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getSourceAndTarget](#getSourceAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression))([FeatureChainExpression](kerml/FeatureChainExpression.html) featureChainExpression)`
Returns the full source-and-target feature path of the chain expression.
`static [Feature](kerml/Feature.html)`
`[getSourceParameter](#getSourceParameter(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression)`
Returns the source parameter of the chain expression.
`static [Membership](kerml/Membership.html)`
`[getTargetFeatureMembership](#getTargetFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression)`
Returns the membership storing the target feature(s).
`static [Expression](kerml/Expression.html)`
`[setSourceExpressionAndTarget](#setSourceExpressionAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.util.List))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [Expression](kerml/Expression.html) pureExpression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> target)`
Updates source and target in the given expression
`static void`
`[setSourceReferent](#setSourceReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [Feature](kerml/Feature.html) referent)`
Sets the source referent of the feature chain expression.
`static [Expression](kerml/Expression.html)`
`[setSourceReferentAndTarget](#setSourceReferentAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,java.util.List))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> sourceAndTarget)`
Updates source and target in the given expression or creates a new [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html)
`static void`
`[setTargetFeature](#setTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,java.util.List))([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> target)`
Sets the target features of the feature chain expression.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPERATOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.FeatureChainExpressions.OPERATOR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FeatureChainExpressions
public FeatureChainExpressions()
 ============ METHOD DETAIL ========== 
Method Details
createChainOrReferenceExpression
public static [Expression](kerml/Expression.html) createChainOrReferenceExpression([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> referenced)
Creates [`FeatureChainExpression`](kerml/FeatureChainExpression.html) if more than one feature is given or [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html) if one.
Parameters:
`referenced` - features
Returns:
created expression
create
public static [FeatureChainExpression](kerml/FeatureChainExpression.html) create([Expression](kerml/Expression.html) pureExpression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> target)
Creates a feature chain expression using a pure source expression and a target feature list.
Parameters:
`pureExpression` - pure expression used as the chain source
`target` - target features
Returns:
created feature chain expression
create
public static [FeatureChainExpression](kerml/FeatureChainExpression.html) create([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> sourceAndTarget)
Creates a feature chain expression from a list of source and target features.
Parameters:
`sourceAndTarget` - list containing source followed by target features
Returns:
created feature chain expression
setSourceReferent
public static void setSourceReferent([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [Feature](kerml/Feature.html) referent)
Sets the source referent of the feature chain expression.
Parameters:
`expression` - expression to update
`referent` - source feature
setTargetFeature
public static void setTargetFeature([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> target)
Sets the target features of the feature chain expression.
Parameters:
`expression` - expression to update
`target` - target features
getTargetFeatureMembership
@CheckForNullpublic static [Membership](kerml/Membership.html) getTargetFeatureMembership([FeatureChainExpression](kerml/FeatureChainExpression.html) expression)
Returns the membership storing the target feature(s).
Parameters:
`expression` - expression
Returns:
membership, or null
setSourceReferentAndTarget
public static [Expression](kerml/Expression.html) setSourceReferentAndTarget([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> sourceAndTarget)
Updates source and target in the given expression or creates a new [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html)
Parameters:
`expression` - expression
`sourceAndTarget` - source used in FeatureReferenceExpressions as referent and target
Returns:
returns given or a new expression
setSourceExpressionAndTarget
public static [Expression](kerml/Expression.html) setSourceExpressionAndTarget([FeatureChainExpression](kerml/FeatureChainExpression.html) expression,
 [Expression](kerml/Expression.html) pureExpression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> target)
Updates source and target in the given expression
Parameters:
`expression` - expression
`pureExpression` - expression used to set FeatureChainExpression source value
`target` - target
Returns:
returns given expression
getSourceParameter
@CheckForNullpublic static [Feature](kerml/Feature.html) getSourceParameter([FeatureChainExpression](kerml/FeatureChainExpression.html) expression)
Returns the source parameter of the chain expression.
Parameters:
`expression` - expression
Returns:
source parameter, or null
getSourceAndTarget
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getSourceAndTarget([FeatureChainExpression](kerml/FeatureChainExpression.html) featureChainExpression)
Returns the full source-and-target feature path of the chain expression.
Parameters:
`featureChainExpression` - chain expression
Returns:
list of source and target features
getChainingFeatureOfTarget
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getChainingFeatureOfTarget([FeatureChainExpression](kerml/FeatureChainExpression.html) expression)
Returns the chaining features of the target feature.
Parameters:
`expression` - chain expression
Returns:
list of chaining features, or empty list

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class FeatureChainExpressions">Class FeatureChainExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.FeatureChainExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeatureChainExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChainExpression</code></a></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPERATOR">OPERATOR</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FeatureChainExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.util.List)">create</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> pureExpression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a feature chain expression using a pure source expression and a target feature list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.util.List)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; sourceAndTarget)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a feature chain expression from a list of source and target features.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createChainOrReferenceExpression(java.util.List)">createChainOrReferenceExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referenced)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChainExpression</code></a> if more than one feature is given or <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a> if one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getChainingFeatureOfTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">getChainingFeatureOfTarget</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the chaining features of the target feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">getSourceAndTarget</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> featureChainExpression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the full source-and-target feature path of the chain expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceParameter(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">getSourceParameter</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source parameter of the chain expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">getTargetFeatureMembership</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the membership storing the target feature(s).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceExpressionAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.util.List)">setSourceExpressionAndTarget</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> pureExpression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates source and target in the given expression</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setSourceReferent</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the source referent of the feature chain expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceReferentAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,java.util.List)">setSourceReferentAndTarget</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; sourceAndTarget)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Updates source and target in the given expression or creates a new <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,java.util.List)">setTargetFeature</a><wbr/>(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the target features of the feature chain expression.</div>
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
<section class="detail" id="OPERATOR">
<h3>OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPERATOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.FeatureChainExpressions.OPERATOR">Constant Field Values</a></li>
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
<h3>FeatureChainExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FeatureChainExpressions</span>()</div>
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
<section class="detail" id="createChainOrReferenceExpression(java.util.List)">
<h3>createChainOrReferenceExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">createChainOrReferenceExpression</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referenced)</span></div>
<div class="block">Creates <a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureChainExpression</code></a> if more than one feature is given or <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a> if one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referenced</code> - features</dd>
<dt>Returns:</dt>
<dd>created expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.util.List)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> pureExpression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; target)</span></div>
<div class="block">Creates a feature chain expression using a pure source expression and a target feature list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pureExpression</code> - pure expression used as the chain source</dd>
<dd><code>target</code> - target features</dd>
<dt>Returns:</dt>
<dd>created feature chain expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.util.List)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; sourceAndTarget)</span></div>
<div class="block">Creates a feature chain expression from a list of source and target features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceAndTarget</code> - list containing source followed by target features</dd>
<dt>Returns:</dt>
<dd>created feature chain expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setSourceReferent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSourceReferent</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</span></div>
<div class="block">Sets the source referent of the feature chain expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to update</dd>
<dd><code>referent</code> - source feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,java.util.List)">
<h3>setTargetFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTargetFeature</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; target)</span></div>
<div class="block">Sets the target features of the feature chain expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to update</dd>
<dd><code>target</code> - target features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetFeatureMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">
<h3>getTargetFeatureMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getTargetFeatureMembership</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression)</span></div>
<div class="block">Returns the membership storing the target feature(s).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
<dt>Returns:</dt>
<dd>membership, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceReferentAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,java.util.List)">
<h3>setSourceReferentAndTarget</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">setSourceReferentAndTarget</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; sourceAndTarget)</span></div>
<div class="block">Updates source and target in the given expression or creates a new <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
<dd><code>sourceAndTarget</code> - source used in FeatureReferenceExpressions as referent and target</dd>
<dt>Returns:</dt>
<dd>returns given or a new expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceExpressionAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression,com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.util.List)">
<h3>setSourceExpressionAndTarget</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">setSourceExpressionAndTarget</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression,
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> pureExpression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; target)</span></div>
<div class="block">Updates source and target in the given expression</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
<dd><code>pureExpression</code> - expression used to set FeatureChainExpression source value</dd>
<dd><code>target</code> - target</dd>
<dt>Returns:</dt>
<dd>returns given expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceParameter(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">
<h3>getSourceParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getSourceParameter</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression)</span></div>
<div class="block">Returns the source parameter of the chain expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
<dt>Returns:</dt>
<dd>source parameter, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceAndTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">
<h3>getSourceAndTarget</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getSourceAndTarget</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> featureChainExpression)</span></div>
<div class="block">Returns the full source-and-target feature path of the chain expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>featureChainExpression</code> - chain expression</dd>
<dt>Returns:</dt>
<dd>list of source and target features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChainingFeatureOfTarget(com.dassault_systemes.modeler.kerml.model.kerml.FeatureChainExpression)">
<h3>getChainingFeatureOfTarget</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getChainingFeatureOfTarget</span><wbr/><span class="parameters">(<a href="kerml/FeatureChainExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureChainExpression</a> expression)</span></div>
<div class="block">Returns the chaining features of the target feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - chain expression</dd>
<dt>Returns:</dt>
<dd>list of chaining features, or empty list</dd>
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
