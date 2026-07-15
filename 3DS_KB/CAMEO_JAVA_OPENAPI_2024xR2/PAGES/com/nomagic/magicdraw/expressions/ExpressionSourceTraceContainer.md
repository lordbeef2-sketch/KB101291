# JAVA OPENAPI: ExpressionSourceTraceContainer (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/expressions/ExpressionSourceTraceContainer.html
- source_path: `com/nomagic/magicdraw/expressions/ExpressionSourceTraceContainer.html`
- source_sha256: `293f21dfb4b0c64d7aa8b806e9fac8735dc67468e5ce645f31cf73ac59a04c77`
- captured_utc: `2026-07-14T16:55:19.769062+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions](package-summary.html)

## Interface ExpressionSourceTraceContainer

@OpenApiAllpublic interfaceExpressionSourceTraceContainer
Container of the expression source trace. Allows to track expression origin.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExpressionSource](ExpressionSource.html)>`
`[getExpressionSourceTrace](#getExpressionSourceTrace())()`
Gets contained expression source trace.
`void`
`[setExpressionSourceTrace](#setExpressionSourceTrace(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExpressionSource](ExpressionSource.html)> expressionSourceTrace)`
Sets contained expression source trace.

============ METHOD DETAIL ========== 
Method Details
getExpressionSourceTrace
@CheckForNull[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExpressionSource](ExpressionSource.html)> getExpressionSourceTrace()
Gets contained expression source trace.
Returns:
contained trace.
setExpressionSourceTrace
void setExpressionSourceTrace([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExpressionSource](ExpressionSource.html)> expressionSourceTrace)
Sets contained expression source trace.
Parameters:
`expressionSourceTrace` - contained trace.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions</a></div>
<h1 class="title" title="Interface ExpressionSourceTraceContainer">Interface ExpressionSourceTraceContainer</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ExpressionSourceTraceContainer</span></div>
<div class="block">Container of the expression source trace. Allows to track expression origin.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExpressionSource.html" title="interface in com.nomagic.magicdraw.expressions">ExpressionSource</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExpressionSourceTrace()">getExpressionSourceTrace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets contained expression source trace.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setExpressionSourceTrace(java.util.List)">setExpressionSourceTrace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExpressionSource.html" title="interface in com.nomagic.magicdraw.expressions">ExpressionSource</a>&gt; expressionSourceTrace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets contained expression source trace.</div>
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
<section class="detail" id="getExpressionSourceTrace()">
<h3>getExpressionSourceTrace</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExpressionSource.html" title="interface in com.nomagic.magicdraw.expressions">ExpressionSource</a>&gt;</span> <span class="element-name">getExpressionSourceTrace</span>()</div>
<div class="block">Gets contained expression source trace.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>contained trace.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setExpressionSourceTrace(java.util.List)">
<h3>setExpressionSourceTrace</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setExpressionSourceTrace</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExpressionSource.html" title="interface in com.nomagic.magicdraw.expressions">ExpressionSource</a>&gt; expressionSourceTrace)</span></div>
<div class="block">Sets contained expression source trace.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expressionSourceTrace</code> - contained trace.</dd>
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
