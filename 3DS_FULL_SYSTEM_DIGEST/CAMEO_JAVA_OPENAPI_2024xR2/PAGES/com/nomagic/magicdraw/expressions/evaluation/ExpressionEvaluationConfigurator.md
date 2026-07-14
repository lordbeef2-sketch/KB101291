# JAVA OPENAPI: ExpressionEvaluationConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/expressions/evaluation/ExpressionEvaluationConfigurator.html
- source_path: `com/nomagic/magicdraw/expressions/evaluation/ExpressionEvaluationConfigurator.html`
- source_sha256: `2b11b0bb1f408818ef9dc1b7d4c0131a9dee02d27b970b42492eb6ae256a4df8`
- captured_utc: `2026-07-14T16:55:22.157086+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.expressions.evaluation](package-summary.html)

## Class ExpressionEvaluationConfigurator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.expressions.evaluation.ExpressionEvaluationConfigurator

@OpenApiAllpublic final classExpressionEvaluationConfigurator
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Expression evaluation configurator allows registering expression factories and additional class loaders.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ParameterizedExpressionFactory](ParameterizedExpressionFactory.html)`
`[getFactory](#getFactory(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) language)`
Get expression factory according language.
`static [ExpressionEvaluationConfigurator](ExpressionEvaluationConfigurator.html)`
`[getInstance](#getInstance())()`
Singleton instance getter.
`void`
`[registerClassLoader](#registerClassLoader(java.lang.ClassLoader))([ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) classLoader)`
Register additional class loader, to load classes, implementing custom expressions.
`void`
`[registerFactory](#registerFactory(java.lang.String,com.nomagic.magicdraw.expressions.evaluation.ParameterizedExpressionFactory))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) language,
 [ParameterizedExpressionFactory](ParameterizedExpressionFactory.html) factory)`
Register expression factory according expression language.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [ExpressionEvaluationConfigurator](ExpressionEvaluationConfigurator.html) getInstance()
Singleton instance getter.
Returns:
singleton instance.
registerFactory
public void registerFactory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) language,
 [ParameterizedExpressionFactory](ParameterizedExpressionFactory.html) factory)
Register expression factory according expression language.
Parameters:
`language` - expression language.
`factory` - expression factory to register.
getFactory
@CheckForNullpublic [ParameterizedExpressionFactory](ParameterizedExpressionFactory.html) getFactory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) language)
Get expression factory according language.
Parameters:
`language` - expression language.
Returns:
expression factory.
registerClassLoader
public void registerClassLoader([ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html) classLoader)
Register additional class loader, to load classes, implementing custom expressions.
 It is necessary to register class loader if custom expression implementation comes from plugins.
Parameters:
`classLoader` - classloader to register.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.expressions.evaluation</a></div>
<h1 class="title" title="Class ExpressionEvaluationConfigurator">Class ExpressionEvaluationConfigurator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.expressions.evaluation.ExpressionEvaluationConfigurator</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">ExpressionEvaluationConfigurator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Expression evaluation configurator allows registering expression factories and additional class loaders.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ParameterizedExpressionFactory.html" title="interface in com.nomagic.magicdraw.expressions.evaluation">ParameterizedExpressionFactory</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFactory(java.lang.String)">getFactory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get expression factory according language.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ExpressionEvaluationConfigurator.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionEvaluationConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Singleton instance getter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerClassLoader(java.lang.ClassLoader)">registerClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> classLoader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register additional class loader, to load classes, implementing custom expressions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerFactory(java.lang.String,com.nomagic.magicdraw.expressions.evaluation.ParameterizedExpressionFactory)">registerFactory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 <a href="ParameterizedExpressionFactory.html" title="interface in com.nomagic.magicdraw.expressions.evaluation">ParameterizedExpressionFactory</a> factory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register expression factory according expression language.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ExpressionEvaluationConfigurator.html" title="class in com.nomagic.magicdraw.expressions.evaluation">ExpressionEvaluationConfigurator</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Singleton instance getter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>singleton instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerFactory(java.lang.String,com.nomagic.magicdraw.expressions.evaluation.ParameterizedExpressionFactory)">
<h3>registerFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerFactory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language,
 <a href="ParameterizedExpressionFactory.html" title="interface in com.nomagic.magicdraw.expressions.evaluation">ParameterizedExpressionFactory</a> factory)</span></div>
<div class="block">Register expression factory according expression language.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - expression language.</dd>
<dd><code>factory</code> - expression factory to register.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFactory(java.lang.String)">
<h3>getFactory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ParameterizedExpressionFactory.html" title="interface in com.nomagic.magicdraw.expressions.evaluation">ParameterizedExpressionFactory</a></span> <span class="element-name">getFactory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> language)</span></div>
<div class="block">Get expression factory according language.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - expression language.</dd>
<dt>Returns:</dt>
<dd>expression factory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerClassLoader(java.lang.ClassLoader)">
<h3>registerClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> classLoader)</span></div>
<div class="block">Register additional class loader, to load classes, implementing custom expressions.
 It is necessary to register class loader if custom expression implementation comes from plugins.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classLoader</code> - classloader to register.</dd>
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
