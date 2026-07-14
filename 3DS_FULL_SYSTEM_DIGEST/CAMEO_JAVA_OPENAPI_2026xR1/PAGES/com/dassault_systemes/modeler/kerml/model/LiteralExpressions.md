# JAVA OPENAPI: LiteralExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/LiteralExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/LiteralExpressions.html`
- source_sha256: `bcc25174b0adc9fb196a99980b64dbd0454d5442626e0342bfc9636f86beeab4`
- captured_utc: `2026-07-14T16:44:47.659837+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class LiteralExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.LiteralExpressions

@OpenApiAllpublic classLiteralExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with single [`LiteralExpression`](kerml/LiteralExpression.html) or multiple ones aggregated with comma [`OperatorExpression`](kerml/OperatorExpression.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[LiteralExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Expression](kerml/Expression.html)`
`[createExpression](#createExpression(java.lang.Object,com.dassault_systemes.modeler.kerml.model.kerml.Element))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Element](kerml/Element.html) context)`
Creates expression representing given value.
`static [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression))([LiteralExpression](kerml/LiteralExpression.html) expression)`
Returns a value of given [`LiteralExpression`](kerml/LiteralExpression.html).
`static [Expression](kerml/Expression.html)`
`[setValue](#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.lang.Object,com.dassault_systemes.modeler.kerml.model.kerml.Element))([Expression](kerml/Expression.html) expression,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Element](kerml/Element.html) context)`
Set a value for given [`Expression`](kerml/Expression.html) or create new [`Expression`](kerml/Expression.html) if value does not match a given one.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
LiteralExpressions
public LiteralExpressions()
 ============ METHOD DETAIL ========== 
Method Details
createExpression
@CheckForNullpublic static [Expression](kerml/Expression.html) createExpression(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Element](kerml/Element.html) context)
Creates expression representing given value.
 Supports [`Integer`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html), [`String`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html), [`Boolean`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html), [`Double`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html) or [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) of those.
Parameters:
`value` - value - either literal or a [`List`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) of literals
`context` - context of expression
Returns:
created expression
setValue
@CheckForNullpublic static [Expression](kerml/Expression.html) setValue(@CheckForNull
 [Expression](kerml/Expression.html) expression,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value,
 [Element](kerml/Element.html) context)
Set a value for given [`Expression`](kerml/Expression.html) or create new [`Expression`](kerml/Expression.html) if value does not match a given one.
Parameters:
`expression` - expression to set value for
`value` - value
`context` - context of new created [`Expression`](kerml/Expression.html)
Returns:
given expression or a new one
getValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([LiteralExpression](kerml/LiteralExpression.html) expression)
Returns a value of given [`LiteralExpression`](kerml/LiteralExpression.html).
 Returns null for unsupported expression like [`LiteralInfinity`](kerml/LiteralInfinity.html).
Parameters:
`expression` - expression
Returns:
value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class LiteralExpressions">Class LiteralExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.LiteralExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">LiteralExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with single <a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralExpression</code></a> or multiple ones aggregated with comma <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OperatorExpression</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">LiteralExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createExpression(java.lang.Object,com.dassault_systemes.modeler.kerml.model.kerml.Element)">createExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates expression representing given value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression)">getValue</a><wbr/>(<a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a value of given <a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralExpression</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setValue(com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.lang.Object,com.dassault_systemes.modeler.kerml.model.kerml.Element)">setValue</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set a value for given <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> or create new <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> if value does not match a given one.</div>
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
<h3>LiteralExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LiteralExpressions</span>()</div>
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
<section class="detail" id="createExpression(java.lang.Object,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>createExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">createExpression</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</span></div>
<div class="block">Creates expression representing given value.
 Supports <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang"><code>Integer</code></a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang"><code>String</code></a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang"><code>Boolean</code></a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang"><code>Double</code></a> or <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> of those.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value - either literal or a <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util"><code>List</code></a> of literals</dd>
<dd><code>context</code> - context of expression</dd>
<dt>Returns:</dt>
<dd>created expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setValue(com.dassault_systemes.modeler.kerml.model.kerml.Expression,java.lang.Object,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">setValue</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> expression,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</span></div>
<div class="block">Set a value for given <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> or create new <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> if value does not match a given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to set value for</dd>
<dd><code>value</code> - value</dd>
<dd><code>context</code> - context of new created <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a></dd>
<dt>Returns:</dt>
<dd>given expression or a new one</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.dassault_systemes.modeler.kerml.model.kerml.LiteralExpression)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">LiteralExpression</a> expression)</span></div>
<div class="block">Returns a value of given <a href="kerml/LiteralExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralExpression</code></a>.
 Returns null for unsupported expression like <a href="kerml/LiteralInfinity.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>LiteralInfinity</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression</dd>
<dt>Returns:</dt>
<dd>value</dd>
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
