# JAVA OPENAPI: FeatureReferenceExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/FeatureReferenceExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/FeatureReferenceExpressions.html`
- source_sha256: `357d80fd6bdc97041141f6781fab9068e2ce03f939f771dad6854a52c5eac3fb`
- captured_utc: `2026-07-14T16:44:47.568836+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class FeatureReferenceExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.FeatureReferenceExpressions

@OpenApiAllpublic classFeatureReferenceExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`FeatureReferenceExpression`](kerml/FeatureReferenceExpression.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FeatureReferenceExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [FeatureReferenceExpression](kerml/FeatureReferenceExpression.html)`
`[create](#create(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) referent)`
Creates a feature reference expression for the given feature.
`static [FeatureReferenceExpression](kerml/FeatureReferenceExpression.html)`
`[create](#create(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> referent)`
Creates a feature reference expression for the given list of features.
`static [Membership](kerml/Membership.html)`
`[getReferentMembership](#getReferentMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression))([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression)`
Returns the membership that stores the referenced feature(s)
 for the given feature reference expression.
`static void`
`[setOwnedReferent](#setOwnedReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression,
 [Feature](kerml/Feature.html) referent)`
Sets the referent of the expression using an owned feature membership.
`static void`
`[setReferent](#setReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression,
 [Feature](kerml/Feature.html) referent)`
Sets the referent of the feature reference expression.
`static void`
`[setReferent](#setReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,java.util.List))([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> referent)`
Sets the referent of the expression to the given list of features.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FeatureReferenceExpressions
public FeatureReferenceExpressions()
 ============ METHOD DETAIL ========== 
Method Details
create
public static [FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) create([Feature](kerml/Feature.html) referent)
Creates a feature reference expression for the given feature.
Parameters:
`referent` - the referenced feature
Returns:
created feature reference expression
create
public static [FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) create([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> referent)
Creates a feature reference expression for the given list of features.
 Sets the referent and creates a return parameter.
Parameters:
`referent` - list of referenced features
Returns:
created feature reference expression
setReferent
public static void setReferent([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression,
 [Feature](kerml/Feature.html) referent)
Sets the referent of the feature reference expression.
Parameters:
`expression` - the expression to update
`referent` - the referenced feature
setOwnedReferent
public static void setOwnedReferent([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression,
 [Feature](kerml/Feature.html) referent)
Sets the referent of the expression using an owned feature membership.
Parameters:
`expression` - the expression to update
`referent` - the referenced feature
setReferent
public static void setReferent([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> referent)
Sets the referent of the expression to the given list of features.
Parameters:
`expression` - the expression to update
`referent` - list of referenced features
getReferentMembership
@CheckForNullpublic static [Membership](kerml/Membership.html) getReferentMembership([FeatureReferenceExpression](kerml/FeatureReferenceExpression.html) expression)
Returns the membership that stores the referenced feature(s)
 for the given feature reference expression.
Parameters:
`expression` - the expression
Returns:
referent membership, or null

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class FeatureReferenceExpressions">Class FeatureReferenceExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.FeatureReferenceExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FeatureReferenceExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>FeatureReferenceExpression</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FeatureReferenceExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">create</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a feature reference expression for the given feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.util.List)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a feature reference expression for the given list of features.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReferentMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression)">getReferentMembership</a><wbr/>(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the membership that stores the referenced feature(s)
 for the given feature reference expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwnedReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setOwnedReferent</a><wbr/>(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referent of the expression using an owned feature membership.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setReferent</a><wbr/>(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referent of the feature reference expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,java.util.List)">setReferent</a><wbr/>(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referent of the expression to the given list of features.</div>
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
<h3>FeatureReferenceExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FeatureReferenceExpressions</span>()</div>
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
<section class="detail" id="create(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</span></div>
<div class="block">Creates a feature reference expression for the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referent</code> - the referenced feature</dd>
<dt>Returns:</dt>
<dd>created feature reference expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.util.List)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referent)</span></div>
<div class="block">Creates a feature reference expression for the given list of features.
 Sets the referent and creates a return parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referent</code> - list of referenced features</dd>
<dt>Returns:</dt>
<dd>created feature reference expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setReferent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReferent</span><wbr/><span class="parameters">(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</span></div>
<div class="block">Sets the referent of the feature reference expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the expression to update</dd>
<dd><code>referent</code> - the referenced feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwnedReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setOwnedReferent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOwnedReferent</span><wbr/><span class="parameters">(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</span></div>
<div class="block">Sets the referent of the expression using an owned feature membership.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the expression to update</dd>
<dd><code>referent</code> - the referenced feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferent(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,java.util.List)">
<h3>setReferent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReferent</span><wbr/><span class="parameters">(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; referent)</span></div>
<div class="block">Sets the referent of the expression to the given list of features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the expression to update</dd>
<dd><code>referent</code> - list of referenced features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferentMembership(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression)">
<h3>getReferentMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getReferentMembership</span><wbr/><span class="parameters">(<a href="kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression)</span></div>
<div class="block">Returns the membership that stores the referenced feature(s)
 for the given feature reference expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the expression</dd>
<dt>Returns:</dt>
<dd>referent membership, or null</dd>
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
