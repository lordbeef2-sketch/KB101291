# JAVA OPENAPI: ElementTransformationFactory (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/variants/transformation/ElementTransformationFactory.html
- source_path: `com/nomagic/magicdraw/variants/transformation/ElementTransformationFactory.html`
- source_sha256: `8e36db4a1cf3e98414b72174d7a0372cf879d1ef1ac742c9d2a7fb6a947a6d9e`
- captured_utc: `2026-07-14T16:56:08.543605+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.transformation](package-summary.html)

## Class ElementTransformationFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.variants.transformation.ElementTransformationFactory

@OpenApiAllpublic classElementTransformationFactory
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Extendable ElementTransformation factory, used during variant realization transformation.
 Should only be explicitly used to register/unregister custom ElementTransformation objects

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementTransformationFactory](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ElementTransformation](ElementTransformation.html)`
`[getTransformation](#getTransformation(com.nomagic.magicdraw.variants.variationpoints.VariationPoint))([VariationPoint](../variationpoints/VariationPoint.html) variationPoint)`
Creates ElementTransformation based on given element and @see VariationPoint
`static void`
`[registerElementTransformation](#registerElementTransformation(com.nomagic.magicdraw.variants.transformation.ElementTransformation))([ElementTransformation](ElementTransformation.html) transformation)`
Register custom transformation to transform elements during variant realization
 In case several registered transformations can transform some element, then latest registered transformation will be used.
`static void`
`[unregisterElementTransformation](#unregisterElementTransformation(com.nomagic.magicdraw.variants.transformation.ElementTransformation))([ElementTransformation](ElementTransformation.html) transformation)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ElementTransformationFactory
public ElementTransformationFactory()
 ============ METHOD DETAIL ========== 
Method Details
registerElementTransformation
public static void registerElementTransformation([ElementTransformation](ElementTransformation.html) transformation)
Register custom transformation to transform elements during variant realization
 In case several registered transformations can transform some element, then latest registered transformation will be used.
Parameters:
`transformation` - element transformation used during variant realization
unregisterElementTransformation
public static void unregisterElementTransformation([ElementTransformation](ElementTransformation.html) transformation)
getTransformation
@CheckForNullpublic [ElementTransformation](ElementTransformation.html) getTransformation([VariationPoint](../variationpoints/VariationPoint.html) variationPoint)
Creates ElementTransformation based on given element and @see VariationPoint
Parameters:
`variationPoint` - variation point to evaluate given element
Returns:
element transformation for given element or null - no transformation
See Also:
[`ElementTransformation`](ElementTransformation.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.transformation</a></div>
<h1 class="title" title="Class ElementTransformationFactory">Class ElementTransformationFactory</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.variants.transformation.ElementTransformationFactory</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementTransformationFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Extendable ElementTransformation factory, used during variant realization transformation.
 Should only be explicitly used to register/unregister custom ElementTransformation objects</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ElementTransformationFactory</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation">ElementTransformation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformation(com.nomagic.magicdraw.variants.variationpoints.VariationPoint)">getTransformation</a><wbr/>(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates ElementTransformation based on given element and @see VariationPoint</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerElementTransformation(com.nomagic.magicdraw.variants.transformation.ElementTransformation)">registerElementTransformation</a><wbr/>(<a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation">ElementTransformation</a> transformation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register custom transformation to transform elements during variant realization
 In case several registered transformations can transform some element, then latest registered transformation will be used.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterElementTransformation(com.nomagic.magicdraw.variants.transformation.ElementTransformation)">unregisterElementTransformation</a><wbr/>(<a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation">ElementTransformation</a> transformation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<h3>ElementTransformationFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementTransformationFactory</span>()</div>
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
<section class="detail" id="registerElementTransformation(com.nomagic.magicdraw.variants.transformation.ElementTransformation)">
<h3>registerElementTransformation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerElementTransformation</span><wbr/><span class="parameters">(<a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation">ElementTransformation</a> transformation)</span></div>
<div class="block">Register custom transformation to transform elements during variant realization
 In case several registered transformations can transform some element, then latest registered transformation will be used.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformation</code> - element transformation used during variant realization</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterElementTransformation(com.nomagic.magicdraw.variants.transformation.ElementTransformation)">
<h3>unregisterElementTransformation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">unregisterElementTransformation</span><wbr/><span class="parameters">(<a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation">ElementTransformation</a> transformation)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTransformation(com.nomagic.magicdraw.variants.variationpoints.VariationPoint)">
<h3>getTransformation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation">ElementTransformation</a></span> <span class="element-name">getTransformation</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint)</span></div>
<div class="block">Creates ElementTransformation based on given element and @see VariationPoint</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variationPoint</code> - variation point to evaluate given element</dd>
<dt>Returns:</dt>
<dd>element transformation for given element or null - no transformation</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ElementTransformation.html" title="interface in com.nomagic.magicdraw.variants.transformation"><code>ElementTransformation</code></a></li>
</ul>
</dd>
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
