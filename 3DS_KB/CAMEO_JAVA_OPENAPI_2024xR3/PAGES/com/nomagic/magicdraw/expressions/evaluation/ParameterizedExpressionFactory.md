# JAVA OPENAPI: ParameterizedExpressionFactory (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/expressions/evaluation/ParameterizedExpressionFactory.html
- source_path: `com/nomagic/magicdraw/expressions/evaluation/ParameterizedExpressionFactory.html`
- source_sha256: `4e6ce015097b45c763586a78a84dad3515992a82d0f6d2ff0380357e87a2252d`
- captured_utc: `2026-07-14T16:55:21.534079+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions.evaluation](package-summary.html)

## Interface ParameterizedExpressionFactory

@OpenApiAllpublic interfaceParameterizedExpressionFactory

Factory creates a parameterized expression.

See Also:
[`ParameterizedExpression`](../ParameterizedExpression.html)
[`ParameterizedExpressionDescriptor`](ParameterizedExpressionDescriptor.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ParameterizedExpression](../ParameterizedExpression.html)`
`[create](#create(com.nomagic.magicdraw.expressions.evaluation.ParameterizedExpressionDescriptor,com.nomagic.magicdraw.expressions.evaluation.ExpressionContext))([ParameterizedExpressionDescriptor](ParameterizedExpressionDescriptor.html) descriptor,
 [ExpressionContext](ExpressionContext.html) context)`
Create a parameterized expression according expression descriptor.

============ METHOD DETAIL ========== 
Method Details
create
[ParameterizedExpression](../ParameterizedExpression.html) create([ParameterizedExpressionDescriptor](ParameterizedExpressionDescriptor.html) descriptor,
 [ExpressionContext](ExpressionContext.html) context)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Create a parameterized expression according expression descriptor.
Parameters:
`descriptor` - expression descriptor.
`context` - expression context.
Returns:
parameterized expression.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - exception.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions.evaluation</a></div>
<h1 class="title" title="Interface ParameterizedExpressionFactory">Interface ParameterizedExpressionFactory</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ParameterizedExpressionFactory</span></div>
<div class="block">Factory creates a parameterized expression.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions"><code>ParameterizedExpression</code></a></li>
<li><a href="ParameterizedExpressionDescriptor.html" title="class in com.nomagic.magicdraw.expressions.evaluation"><code>ParameterizedExpressionDescriptor</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#create(com.nomagic.magicdraw.expressions.evaluation.ParameterizedExpressionDescriptor,com.nomagic.magicdraw.expressions.evaluation.ExpressionContext)">create</a><wbr/>(<a href="ParameterizedExpressionDescriptor.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ParameterizedExpressionDescriptor</a> descriptor,
 <a href="ExpressionContext.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create a parameterized expression according expression descriptor.</div>
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
<section class="detail" id="create(com.nomagic.magicdraw.expressions.evaluation.ParameterizedExpressionDescriptor,com.nomagic.magicdraw.expressions.evaluation.ExpressionContext)">
<h3>create</h3>
<div class="member-signature"><span class="return-type"><a href="../ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="ParameterizedExpressionDescriptor.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ParameterizedExpressionDescriptor</a> descriptor,
 <a href="ExpressionContext.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionContext</a> context)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Create a parameterized expression according expression descriptor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>descriptor</code> - expression descriptor.</dd>
<dd><code>context</code> - expression context.</dd>
<dt>Returns:</dt>
<dd>parameterized expression.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - exception.</dd>
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
