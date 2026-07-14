# JAVA OPENAPI: ParameterizedExpression (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/expressions/ParameterizedExpression.html
- source_path: `com/nomagic/magicdraw/expressions/ParameterizedExpression.html`
- source_sha256: `6fe4048191c586a14c95b3fda349ca29b74f7214c7535666a43ddde1a6206382`
- captured_utc: `2026-07-14T16:45:36.253484+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions](package-summary.html)

## Interface ParameterizedExpression

All Known Subinterfaces:
`[ElementExpression](ElementExpression.html)`

@OpenApiAllpublic interfaceParameterizedExpression

Expression calculates the value according given parameter values (arguments).

Actual implementation must declare the public method

getValue

with custom number of parameters,

plus additional last parameter

of

ValueContext

type.

E.g.

````java
public class ParameterizedExpressionImpl implements ParameterizedExpression
     {
        /**
          * Value calculation method.
          *
          * @param parameter1   parameter of String type.
          * @param parameter2   parameter of boolean type.
          * @param valueContext context mandatory parameter.
          * @return calculated value.
         */
         public Object getValue(String parameter1, boolean parameter2, ValueContext valueContext)
         {
             // value context is ignored in this implementation
             // construct string using passed arguments
             return "String: " + parameter1 + " boolean: " + parameter2;
         }
     }
````

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?>`
`[getResultType](#getResultType())()`
Returns type of the result.

============ METHOD DETAIL ========== 
Method Details
getResultType
@CheckForNull[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> getResultType()
Returns type of the result. Null means that result type is unknown. If the expression
 returns a collection of objects then the implementation should return a class of single object.
Returns:
result type.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions</a></div>
<h1 class="title" title="Interface ParameterizedExpression">Interface ParameterizedExpression</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ElementExpression.html" title="interface in com.nomagic.magicdraw.expressions">ElementExpression</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ParameterizedExpression</span></div>
<div class="block">Expression calculates the value according given parameter values (arguments).
 <br/>Actual implementation must declare the public method <code>getValue</code> with custom number of parameters,
 <strong>plus additional last parameter</strong> of <a href="ValueContext.html" title="class in com.nomagic.magicdraw.expressions"><code>ValueContext</code></a> type.
 <br/>E.g.
 <pre>
     public class ParameterizedExpressionImpl implements ParameterizedExpression
     {
        /**
          * Value calculation method.
          *
          * @param parameter1   parameter of String type.
          * @param parameter2   parameter of boolean type.
          * @param valueContext context mandatory parameter.
          * @return calculated value.
         */
         public Object getValue(String parameter1, boolean parameter2, ValueContext valueContext)
         {
             // value context is ignored in this implementation
             // construct string using passed arguments
             return "String: " + parameter1 + " boolean: " + parameter2;
         }
     }</pre></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getResultType()">getResultType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns type of the result.</div>
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
<section class="detail" id="getResultType()">
<h3>getResultType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">getResultType</span>()</div>
<div class="block">Returns type of the result. Null means that result type is unknown. If the expression
 returns a collection of objects then the implementation should return a class of single object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>result type.</dd>
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
