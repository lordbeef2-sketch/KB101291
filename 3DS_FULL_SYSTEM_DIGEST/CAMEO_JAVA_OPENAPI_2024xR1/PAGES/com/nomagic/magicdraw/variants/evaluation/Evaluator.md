# JAVA OPENAPI: Evaluator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/variants/evaluation/Evaluator.html
- source_path: `com/nomagic/magicdraw/variants/evaluation/Evaluator.html`
- source_sha256: `c6382796499f4188b3b691b9b22313469406c522c1e272fdd2df6d0302444f3b`
- captured_utc: `2026-07-14T16:52:20.072987+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.evaluation](package-summary.html)

## Interface Evaluator<T>

All Known Implementing Classes:
`[BooleanEvaluator](BooleanEvaluator.html)`

@OpenApiAllpublic interfaceEvaluator<T>

Evaluates element and returns calculated value. Evaluation can be based on the current value

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[T](Evaluator.html)`
`[evaluate](#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) currentValue)`
Calculates value based on supplied model element

============ METHOD DETAIL ========== 
Method Details
evaluate
@CheckForNull[T](Evaluator.html) evaluate([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) currentValue)
Calculates value based on supplied model element
Parameters:
`element` - model element
`currentValue` - currently existing value of the value that is being re-evaluated
Returns:
calculated value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.evaluation</a></div>
<h1 class="title" title="Interface Evaluator">Interface Evaluator&lt;T&gt;</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="BooleanEvaluator.html" title="class in com.nomagic.magicdraw.variants.evaluation">BooleanEvaluator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Evaluator&lt;T&gt;</span></div>
<div class="block">Evaluates element and returns calculated value. Evaluation can be based on the current value</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Evaluator.html" title="type parameter in Evaluator">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">evaluate</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> currentValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Calculates value based on supplied model element</div>
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
<section class="detail" id="evaluate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>evaluate</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="Evaluator.html" title="type parameter in Evaluator">T</a></span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> currentValue)</span></div>
<div class="block">Calculates value based on supplied model element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - model element</dd>
<dd><code>currentValue</code> - currently existing value of the value that is being re-evaluated</dd>
<dt>Returns:</dt>
<dd>calculated value</dd>
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
