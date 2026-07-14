# JAVA OPENAPI: Evaluator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/evaluation/Evaluator.html
- source_path: `com/nomagic/magicdraw/evaluation/Evaluator.html`
- source_sha256: `b2c4a1298ec5161c2d48aa58e16a53080180600e1ef4f5426f1ffa1d42c53940`
- captured_utc: `2026-07-14T16:55:19.555056+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.evaluation](package-summary.html)

## Interface Evaluator

All Known Subinterfaces:
`[BinaryEvaluator](BinaryEvaluator.html)`

@OpenApipublic interfaceEvaluator

A basic expression evaluator interface. Implementers should realize
 the method to evaluate expression

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[evaluate](#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) object)`
Entry method for expression evaluation.
`default [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[evaluate](#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List))([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) object,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NamedArgument](NamedArgument.html)> arguments)`
Entry method for expression evaluation.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getExpressionCachingKey](#getExpressionCachingKey(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression))([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression)`
Calculates a string identifier of the expression.
`boolean`
`[isExpressionGlobal](#isExpressionGlobal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression))([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression)`
Determines if the supplied expression is "global", i.e.

============ METHOD DETAIL ========== 
Method Details
evaluate
@OpenApi[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) evaluate([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) object)
Entry method for expression evaluation. Takes expression, contextual object and produces result.
Parameters:
`expression` - expression to be called
`object` - contextual object of expression call
Returns:
expression evaluation result
evaluate
@OpenApidefault [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) evaluate([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) object,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NamedArgument](NamedArgument.html)> arguments)
Entry method for expression evaluation. Takes expression, contextual object, additional arguments and produces result.
Parameters:
`expression` - expression to be called
`object` - contextual object of expression call
Returns:
expression evaluation result
isExpressionGlobal
@OpenApiboolean isExpressionGlobal([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression)
Determines if the supplied expression is "global", i.e. if it needs
 contextual object to be evaluated. If expression does not need contextual object,
 then this expression is considered to be "global" or "static"
Parameters:
`expression` - expression to be inspected
Returns:
true if expression does not need the contextual object
getExpressionCachingKey
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getExpressionCachingKey([OpaqueExpression](../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html) expression)
Calculates a string identifier of the expression.
 Expression evaluation results of objects are cached under this key
 return null if result should not be cached.
Parameters:
`expression` - expression, results of which are to be cached
Returns:
identifier of the expression

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.evaluation</a></div>
<h1 class="title" title="Interface Evaluator">Interface Evaluator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="BinaryEvaluator.html" title="interface in com.nomagic.magicdraw.evaluation">BinaryEvaluator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Evaluator</span></div>
<div class="block">A basic expression evaluator interface. Implementers should realize
 the method to evaluate expression</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">evaluate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Entry method for expression evaluation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List)">evaluate</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NamedArgument.html" title="interface in com.nomagic.magicdraw.evaluation">NamedArgument</a>&gt; arguments)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Entry method for expression evaluation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExpressionCachingKey(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">getExpressionCachingKey</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Calculates a string identifier of the expression.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isExpressionGlobal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">isExpressionGlobal</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Determines if the supplied expression is "global", i.e.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>evaluate</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> object)</span></div>
<div class="block">Entry method for expression evaluation. Takes expression, contextual object and produces result.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to be called</dd>
<dd><code>object</code> - contextual object of expression call</dd>
<dt>Returns:</dt>
<dd>expression evaluation result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List)">
<h3>evaluate</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="NamedArgument.html" title="interface in com.nomagic.magicdraw.evaluation">NamedArgument</a>&gt; arguments)</span></div>
<div class="block">Entry method for expression evaluation. Takes expression, contextual object, additional arguments and produces result.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to be called</dd>
<dd><code>object</code> - contextual object of expression call</dd>
<dt>Returns:</dt>
<dd>expression evaluation result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExpressionGlobal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">
<h3>isExpressionGlobal</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isExpressionGlobal</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression)</span></div>
<div class="block">Determines if the supplied expression is "global", i.e. if it needs
 contextual object to be evaluated. If expression does not need contextual object,
 then this expression is considered to be "global" or "static"</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to be inspected</dd>
<dt>Returns:</dt>
<dd>true if expression does not need the contextual object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExpressionCachingKey(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">
<h3>getExpressionCachingKey</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExpressionCachingKey</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/OpaqueExpression.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">OpaqueExpression</a> expression)</span></div>
<div class="block">Calculates a string identifier of the expression.
 Expression evaluation results of objects are cached under this key
 return null if result should not be cached.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression, results of which are to be cached</dd>
<dt>Returns:</dt>
<dd>identifier of the expression</dd>
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
