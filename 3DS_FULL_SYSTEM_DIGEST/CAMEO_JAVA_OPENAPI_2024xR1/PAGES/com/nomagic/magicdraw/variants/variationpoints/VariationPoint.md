# JAVA OPENAPI: VariationPoint (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/variants/variationpoints/VariationPoint.html
- source_path: `com/nomagic/magicdraw/variants/variationpoints/VariationPoint.html`
- source_sha256: `4f4d2222712cb4456c0f8729ef7999222649ce4df5309ee0311f6042fdac7b3f`
- captured_utc: `2026-07-14T16:52:20.541993+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.variationpoints](package-summary.html)

## Class VariationPoint<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.variants.variationpoints.VariationPoint<T>

Direct Known Subclasses:
`[PropertyVariationPoint](PropertyVariationPoint.html)`

@OpenApiAllpublic abstract classVariationPoint<T>
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Marks that element has a variable feature that can be transformed.
 It's evaluator provides concrete value that should be set to the element's variable feature during variant realization

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[VariationPoint](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[T](VariationPoint.html)> evaluator)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`

`protected [Evaluator](../evaluation/Evaluator.html)<[T](VariationPoint.html)>`
`[getEvaluator](#getEvaluator())()`

`[T](VariationPoint.html)`
`[getValue](#getValue(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) currentValue)`
Returns transformed value for the given element
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
VariationPoint
public VariationPoint([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Evaluator](../evaluation/Evaluator.html)<[T](VariationPoint.html)> evaluator)
 ============ METHOD DETAIL ========== 
Method Details
getElement
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
getValue
@CheckForNullpublic [T](VariationPoint.html) getValue(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) currentValue)
Returns transformed value for the given element
Returns:
calculated value to be applied during transformation
getEvaluator
protected [Evaluator](../evaluation/Evaluator.html)<[T](VariationPoint.html)> getEvaluator()
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.variationpoints</a></div>
<h1 class="title" title="Class VariationPoint">Class VariationPoint&lt;T&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.variants.variationpoints.VariationPoint&lt;T&gt;</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="PropertyVariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">PropertyVariationPoint</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">VariationPoint&lt;T&gt;</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Marks that element has a variable feature that can be transformed.
 It's evaluator provides concrete value that should be set to the element's variable feature during variant realization</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">VariationPoint</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="VariationPoint.html" title="type parameter in VariationPoint">T</a>&gt; evaluator)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="VariationPoint.html" title="type parameter in VariationPoint">T</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEvaluator()">getEvaluator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="VariationPoint.html" title="type parameter in VariationPoint">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(java.lang.Object)">getValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> currentValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns transformed value for the given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.variants.evaluation.Evaluator)">
<h3>VariationPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VariationPoint</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="VariationPoint.html" title="type parameter in VariationPoint">T</a>&gt; evaluator)</span></div>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getValue(java.lang.Object)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="VariationPoint.html" title="type parameter in VariationPoint">T</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> currentValue)</span></div>
<div class="block">Returns transformed value for the given element</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>calculated value to be applied during transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEvaluator()">
<h3>getEvaluator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../evaluation/Evaluator.html" title="interface in com.nomagic.magicdraw.variants.evaluation">Evaluator</a>&lt;<a href="VariationPoint.html" title="type parameter in VariationPoint">T</a>&gt;</span> <span class="element-name">getEvaluator</span>()</div>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
