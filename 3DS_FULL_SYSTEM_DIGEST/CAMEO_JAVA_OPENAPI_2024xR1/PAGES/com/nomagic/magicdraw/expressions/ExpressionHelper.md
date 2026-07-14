# JAVA OPENAPI: ExpressionHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/expressions/ExpressionHelper.html
- source_path: `com/nomagic/magicdraw/expressions/ExpressionHelper.html`
- source_sha256: `a741a57c0648845da27872be04e4f608c9f297af091974ac4b278afe1618647a`
- captured_utc: `2026-07-14T16:51:22.243217+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions](package-summary.html)

## Class ExpressionHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.expressions.ExpressionHelper

@OpenApiAllpublic classExpressionHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Various utility methods used for [`ParameterizedExpression`](ParameterizedExpression.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExpressionHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[call](#call(com.nomagic.magicdraw.expressions.ParameterizedExpression,java.lang.Object...))([ParameterizedExpression](ParameterizedExpression.html) expression,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)... arguments)`
Simplified ParametrizedExpression call.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[call](#call(com.nomagic.magicdraw.expressions.ParameterizedExpression,java.util.List,com.nomagic.magicdraw.expressions.ValueContext))([ParameterizedExpression](ParameterizedExpression.html) parameterizedExpression,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 [ValueContext](ValueContext.html) valueContext)`
Call `parameterizedExpression` and returns value.
`static [ParameterizedExpression](ParameterizedExpression.html)`
`[getBehaviorExpression](#getBehaviorExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior))([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior)`
Gets expression represented by a given behavior.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExpressionHelper
public ExpressionHelper()
 ============ METHOD DETAIL ========== 
Method Details
call
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) call([ParameterizedExpression](ParameterizedExpression.html) expression,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)... arguments)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Simplified ParametrizedExpression call. Intended for easier usage from scripts.
 `ValueContext` is `null`.
Parameters:
`expression` - expression to call. If not ParametrizedExpression result will be null
`arguments` - arguments for the expression
Returns:
expression result
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - various exceptions, mostly from java.lang.reflect.Method#invoke(java.lang.Object, java.lang.Object...)
call
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) call([ParameterizedExpression](ParameterizedExpression.html) parameterizedExpression,
 @CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<?> arguments,
 @CheckForNull
 [ValueContext](ValueContext.html) valueContext)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Call `parameterizedExpression` and returns value.
Parameters:
`parameterizedExpression` - expression which should be called
`arguments` - arguments for the expression. If arguments do ot match, then exception will be thrown
`valueContext` - value context for the evaluated value. Usually `null`
Returns:
value of the expression call
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - various exceptions, mostly from java.lang.reflect.Method#invoke(java.lang.Object, java.lang.Object...)
getBehaviorExpression
@CheckForNullpublic static [ParameterizedExpression](ParameterizedExpression.html) getBehaviorExpression([Behavior](../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior)
Gets expression represented by a given behavior.
Parameters:
`behavior` - behavior which represents an expression.
Returns:
parameterized expression.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions</a></div>
<h1 class="title" title="Class ExpressionHelper">Class ExpressionHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.expressions.ExpressionHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ExpressionHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Various utility methods used for <a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions"><code>ParameterizedExpression</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ExpressionHelper</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#call(com.nomagic.magicdraw.expressions.ParameterizedExpression,java.lang.Object...)">call</a><wbr/>(<a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... arguments)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Simplified <call>ParametrizedExpression</call> call.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#call(com.nomagic.magicdraw.expressions.ParameterizedExpression,java.util.List,com.nomagic.magicdraw.expressions.ValueContext)">call</a><wbr/>(<a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a> parameterizedExpression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 <a href="ValueContext.html" title="class in com.nomagic.magicdraw.expressions">ValueContext</a> valueContext)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Call <code>parameterizedExpression</code> and returns value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBehaviorExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">getBehaviorExpression</a><wbr/>(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets expression represented by a given behavior.</div>
</div>
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
<h3>ExpressionHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExpressionHelper</span>()</div>
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
<section class="detail" id="call(com.nomagic.magicdraw.expressions.ParameterizedExpression,java.lang.Object...)">
<h3>call</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">call</span><wbr/><span class="parameters">(<a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a> expression,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... arguments)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Simplified <call>ParametrizedExpression</call> call. Intended for easier usage from scripts.
 <code>ValueContext</code> is <code>null</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - expression to call. If not ParametrizedExpression result will be null</dd>
<dd><code>arguments</code> - arguments for the expression</dd>
<dt>Returns:</dt>
<dd>expression result</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - various exceptions, mostly from java.lang.reflect.Method#invoke(java.lang.Object, java.lang.Object...)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="call(com.nomagic.magicdraw.expressions.ParameterizedExpression,java.util.List,com.nomagic.magicdraw.expressions.ValueContext)">
<h3>call</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">call</span><wbr/><span class="parameters">(<a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a> parameterizedExpression,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;?&gt; arguments,
 @CheckForNull
 <a href="ValueContext.html" title="class in com.nomagic.magicdraw.expressions">ValueContext</a> valueContext)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Call <code>parameterizedExpression</code> and returns value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameterizedExpression</code> - expression which should be called</dd>
<dd><code>arguments</code> - arguments for the expression. If arguments do ot match, then exception will be thrown</dd>
<dd><code>valueContext</code> - value context for the evaluated value. Usually <code>null</code></dd>
<dt>Returns:</dt>
<dd>value of the expression call</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - various exceptions, mostly from java.lang.reflect.Method#invoke(java.lang.Object, java.lang.Object...)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBehaviorExpression(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior)">
<h3>getBehaviorExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></span> <span class="element-name">getBehaviorExpression</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior)</span></div>
<div class="block">Gets expression represented by a given behavior.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - behavior which represents an expression.</dd>
<dt>Returns:</dt>
<dd>parameterized expression.</dd>
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
