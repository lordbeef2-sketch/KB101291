# JAVA OPENAPI: BinaryEvaluator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/evaluation/BinaryEvaluator.html
- source_path: `com/nomagic/magicdraw/evaluation/BinaryEvaluator.html`
- source_sha256: `1298732b17a725bc5fbb47f8652dea66e3cbba795db5ca7ba4e8a3309dc614c9`
- captured_utc: `2026-07-14T16:51:21.625207+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.evaluation](package-summary.html)

## Interface BinaryEvaluator

All Superinterfaces:
`[Evaluator](Evaluator.html)`

@OpenApipublic interfaceBinaryEvaluatorextends [Evaluator](Evaluator.html)

Specialization of evaluator for binary expressions.
 Allows additional configuration - contributing expression implementations
 from separate classloaders - e.g. coming from plugins.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[registerAdditionalImplementers](#registerAdditionalImplementers(java.lang.ClassLoader))([ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) implementorClasses)`
Method allows registering additional classloaders, to load classes,
 implementing binary expressions.
Methods inherited from interface com.nomagic.magicdraw.evaluation.[Evaluator](Evaluator.html)
`[evaluate](Evaluator.html#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [evaluate](Evaluator.html#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List)), [getExpressionCachingKey](Evaluator.html#getExpressionCachingKey(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)), [isExpressionGlobal](Evaluator.html#isExpressionGlobal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression))`

============ METHOD DETAIL ========== 
Method Details
registerAdditionalImplementers
@OpenApivoid registerAdditionalImplementers([ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) implementorClasses)
Method allows registering additional classloaders, to load classes,
 implementing binary expressions. This is especially necessary
 for expression implementations, coming from plugins (otherwise
 these implementation classes will not be found - since they are in a
 separate classloader - plugin classloader).
Parameters:
`implementorClasses` - classloader, supplying additional classes, implementing expressions

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.evaluation</a></div>
<h1 class="title" title="Interface BinaryEvaluator">Interface BinaryEvaluator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Evaluator.html" title="interface in com.nomagic.magicdraw.evaluation">Evaluator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BinaryEvaluator</span><span class="extends-implements">
extends <a href="Evaluator.html" title="interface in com.nomagic.magicdraw.evaluation">Evaluator</a></span></div>
<div class="block">Specialization of evaluator for binary expressions.
 Allows additional configuration - contributing expression implementations
 from separate classloaders - e.g. coming from plugins.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#registerAdditionalImplementers(java.lang.ClassLoader)">registerAdditionalImplementers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> implementorClasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method allows registering additional classloaders, to load classes,
 implementing binary expressions.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.evaluation.Evaluator">Methods inherited from interface com.nomagic.magicdraw.evaluation.<a href="Evaluator.html" title="interface in com.nomagic.magicdraw.evaluation">Evaluator</a></h3>
<code><a href="Evaluator.html#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">evaluate</a>, <a href="Evaluator.html#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List)">evaluate</a>, <a href="Evaluator.html#getExpressionCachingKey(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">getExpressionCachingKey</a>, <a href="Evaluator.html#isExpressionGlobal(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.OpaqueExpression)">isExpressionGlobal</a></code></div>
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
<section class="detail" id="registerAdditionalImplementers(java.lang.ClassLoader)">
<h3>registerAdditionalImplementers</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">registerAdditionalImplementers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> implementorClasses)</span></div>
<div class="block">Method allows registering additional classloaders, to load classes,
 implementing binary expressions. This is especially necessary
 for expression implementations, coming from plugins (otherwise
 these implementation classes will not be found - since they are in a
 separate classloader - plugin classloader).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>implementorClasses</code> - classloader, supplying additional classes, implementing expressions</dd>
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
