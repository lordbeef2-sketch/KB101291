# JAVA OPENAPI: InvocationExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/InvocationExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/InvocationExpressions.html`
- source_sha256: `b02a9310244bc1011e1c845f083c54fc529892183ab43a8d42e9aedc8abce862`
- captured_utc: `2026-07-14T16:44:47.635836+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class InvocationExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.InvocationExpressions

@OpenApiAllpublic classInvocationExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`InvocationExpression`](kerml/InvocationExpression.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[InvocationExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [InvocationExpression](kerml/InvocationExpression.html)`
`[createInvocationExpression](#createInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.Type,int))([Type](kerml/Type.html) instantiatedType,
 int numberOfInputParameters)`
Creates an [`InvocationExpression`](kerml/InvocationExpression.html) with a specified number of input parameters.
`static [InvocationExpression](kerml/InvocationExpression.html)`
`[createInvocationExpression](#createInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Object...))([Type](kerml/Type.html) instantiatedType,
 [Type](kerml/Type.html) resultType,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputParameterValues)`
Creates an [`InvocationExpression`](kerml/InvocationExpression.html) with a specified arguments an optional result type.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
InvocationExpressions
public InvocationExpressions()
 ============ METHOD DETAIL ========== 
Method Details
createInvocationExpression
public static [InvocationExpression](kerml/InvocationExpression.html) createInvocationExpression([Type](kerml/Type.html) instantiatedType,
 int numberOfInputParameters)
Creates an [`InvocationExpression`](kerml/InvocationExpression.html) with a specified number of input parameters.
Parameters:
`instantiatedType` - instantiated type
`numberOfInputParameters` - number of input parameters to create
Returns:
created expression
createInvocationExpression
public static [InvocationExpression](kerml/InvocationExpression.html) createInvocationExpression([Type](kerml/Type.html) instantiatedType,
 @CheckForNull
 [Type](kerml/Type.html) resultType,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputParameterValues)
Creates an [`InvocationExpression`](kerml/InvocationExpression.html) with a specified arguments an optional result type.
Parameters:
`instantiatedType` - instantiated type
`resultType` - expression result type
`inputParameterValues` - values of arguments
Returns:
created expression

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class InvocationExpressions">Class InvocationExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.InvocationExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">InvocationExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">InvocationExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.Type,int)">createInvocationExpression</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> instantiatedType,
 int numberOfInputParameters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a> with a specified number of input parameters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Object...)">createInvocationExpression</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> instantiatedType,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> resultType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputParameterValues)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a> with a specified arguments an optional result type.</div>
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
<h3>InvocationExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">InvocationExpressions</span>()</div>
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
<section class="detail" id="createInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.Type,int)">
<h3>createInvocationExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></span> <span class="element-name">createInvocationExpression</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> instantiatedType,
 int numberOfInputParameters)</span></div>
<div class="block">Creates an <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a> with a specified number of input parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instantiatedType</code> - instantiated type</dd>
<dd><code>numberOfInputParameters</code> - number of input parameters to create</dd>
<dt>Returns:</dt>
<dd>created expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInvocationExpression(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Object...)">
<h3>createInvocationExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">InvocationExpression</a></span> <span class="element-name">createInvocationExpression</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> instantiatedType,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> resultType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputParameterValues)</span></div>
<div class="block">Creates an <a href="kerml/InvocationExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>InvocationExpression</code></a> with a specified arguments an optional result type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>instantiatedType</code> - instantiated type</dd>
<dd><code>resultType</code> - expression result type</dd>
<dd><code>inputParameterValues</code> - values of arguments</dd>
<dt>Returns:</dt>
<dd>created expression</dd>
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
