# JAVA OPENAPI: ElementExpression (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/expressions/ElementExpression.html
- source_path: `com/nomagic/magicdraw/expressions/ElementExpression.html`
- source_sha256: `0db7954e284b43b93d347bc42a3e2071a10bd4ae426c53f4057e8d54de9fb22c`
- captured_utc: `2026-07-14T16:45:36.309486+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions](package-summary.html)

## Interface ElementExpression

All Superinterfaces:
`[ParameterizedExpression](ParameterizedExpression.html)`

@OpenApiAllpublic interfaceElementExpressionextends [ParameterizedExpression](ParameterizedExpression.html)

Expression executed with [`Element`](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) as argument

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getValue](#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.expressions.ValueContext))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [ValueContext](ValueContext.html) valueContext)`
Methods inherited from interface com.nomagic.magicdraw.expressions.[ParameterizedExpression](ParameterizedExpression.html)
`[getResultType](ParameterizedExpression.html#getResultType())`

============ METHOD DETAIL ========== 
Method Details
getValue
@CheckForNull[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getValue([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [ValueContext](ValueContext.html) valueContext)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions</a></div>
<h1 class="title" title="Interface ElementExpression">Interface ElementExpression</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementExpression</span><span class="extends-implements">
extends <a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></span></div>
<div class="block">Expression executed with <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a> as argument</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.expressions.ValueContext)">getValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ValueContext.html" title="class in com.nomagic.magicdraw.expressions">ValueContext</a> valueContext)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.expressions.ParameterizedExpression">Methods inherited from interface com.nomagic.magicdraw.expressions.<a href="ParameterizedExpression.html" title="interface in com.nomagic.magicdraw.expressions">ParameterizedExpression</a></h3>
<code><a href="ParameterizedExpression.html#getResultType()">getResultType</a></code></div>
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
<section class="detail" id="getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.expressions.ValueContext)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="ValueContext.html" title="class in com.nomagic.magicdraw.expressions">ValueContext</a> valueContext)</span></div>
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
