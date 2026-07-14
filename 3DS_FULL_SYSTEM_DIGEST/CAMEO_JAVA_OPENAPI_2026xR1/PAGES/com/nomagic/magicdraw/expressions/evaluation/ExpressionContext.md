# JAVA OPENAPI: ExpressionContext (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/expressions/evaluation/ExpressionContext.html
- source_path: `com/nomagic/magicdraw/expressions/evaluation/ExpressionContext.html`
- source_sha256: `0cf7fa58a76b5f1a6d5ffa06c921b0ef41d260a69303519f755153a7d97b9eae`
- captured_utc: `2026-07-14T16:45:36.277485+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions.evaluation](package-summary.html)

## Class ExpressionContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.expressions.evaluation.ExpressionContext

@OpenApiAllpublic classExpressionContext
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Expression context used to create expressions.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_METACLASS](#CONTEXT_METACLASS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[EVALUATION_STEREOTYPE](#EVALUATION_STEREOTYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[EXPRESSION_SOURCE](#EXPRESSION_SOURCE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROJECT](#PROJECT)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[THIS](#THIS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExpressionContext](#%3Cinit%3E(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Constructor.
`[ExpressionContext](#%3Cinit%3E(com.nomagic.magicdraw.expressions.evaluation.ExpressionContext))([ExpressionContext](ExpressionContext.html) parent)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[add](#add(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Add value to the current context.
`[ExpressionContext](ExpressionContext.html)`
`[copy](#copy())()`
Create this context copy.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Get the value from current context, or parent context if current context has no value.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getKeys](#getKeys())()`
Context keys.
`[Project](../../core/Project.html)`
`[getProject](#getProject())()`
Get project - identical to `get(PROJECT)`.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
THIS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) THIS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.THIS)
PROJECT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROJECT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.PROJECT)
CONTEXT_METACLASS
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONTEXT_METACLASS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.CONTEXT_METACLASS)
EXPRESSION_SOURCE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) EXPRESSION_SOURCE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.EXPRESSION_SOURCE)
EVALUATION_STEREOTYPE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) EVALUATION_STEREOTYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.EVALUATION_STEREOTYPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExpressionContext
public ExpressionContext(@CheckForNull
 [ExpressionContext](ExpressionContext.html) parent)
Constructor.
Parameters:
`parent` - parent context.
ExpressionContext
public ExpressionContext([Project](../../core/Project.html) project)
Constructor.
Parameters:
`project` - project.
 ============ METHOD DETAIL ========== 
Method Details
add
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) add([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Add value to the current context.
Parameters:
`key` - key.
`value` - value.
Returns:
the previous value associated with key.
get
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Get the value from current context, or parent context if current context has no value.
Parameters:
`key` - key.
Returns:
the value associated with key.
copy
public [ExpressionContext](ExpressionContext.html) copy()
Create this context copy.
Returns:
copy.
getProject
public [Project](../../core/Project.html) getProject()
Get project - identical to `get(PROJECT)`.
Returns:
project.
getKeys
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getKeys()
Context keys.
Returns:
keys.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions.evaluation</a></div>
<h1 class="title" title="Class ExpressionContext">Class ExpressionContext</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.expressions.evaluation.ExpressionContext</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ExpressionContext</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Expression context used to create expressions.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_METACLASS">CONTEXT_METACLASS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EVALUATION_STEREOTYPE">EVALUATION_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXPRESSION_SOURCE">EXPRESSION_SOURCE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROJECT">PROJECT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#THIS">THIS</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project)">ExpressionContext</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.expressions.evaluation.ExpressionContext)">ExpressionContext</a><wbr/>(<a href="ExpressionContext.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionContext</a> parent)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(java.lang.String,java.lang.Object)">add</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add value to the current context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ExpressionContext.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionContext</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy()">copy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create this context copy.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the value from current context, or parent context if current context has no value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getKeys()">getKeys</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Context keys.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project - identical to  <code>get(PROJECT)</code>.</div>
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
<section class="detail" id="THIS">
<h3>THIS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">THIS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.THIS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROJECT">
<h3>PROJECT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROJECT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.PROJECT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONTEXT_METACLASS">
<h3>CONTEXT_METACLASS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_METACLASS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.CONTEXT_METACLASS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXPRESSION_SOURCE">
<h3>EXPRESSION_SOURCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXPRESSION_SOURCE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.EXPRESSION_SOURCE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVALUATION_STEREOTYPE">
<h3>EVALUATION_STEREOTYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EVALUATION_STEREOTYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.expressions.evaluation.ExpressionContext.EVALUATION_STEREOTYPE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.expressions.evaluation.ExpressionContext)">
<h3>ExpressionContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExpressionContext</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ExpressionContext.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionContext</a> parent)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project)">
<h3>ExpressionContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExpressionContext</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project.</dd>
</dl>
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
<section class="detail" id="add(java.lang.String,java.lang.Object)">
<h3>add</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">add</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Add value to the current context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - key.</dd>
<dd><code>value</code> - value.</dd>
<dt>Returns:</dt>
<dd>the previous value associated with key.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Get the value from current context, or parent context if current context has no value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - key.</dd>
<dt>Returns:</dt>
<dd>the value associated with key.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy()">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ExpressionContext.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionContext</a></span> <span class="element-name">copy</span>()</div>
<div class="block">Create this context copy.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>copy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Get project - identical to  <code>get(PROJECT)</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getKeys()">
<h3>getKeys</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getKeys</span>()</div>
<div class="block">Context keys.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>keys.</dd>
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
