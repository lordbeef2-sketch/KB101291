# JAVA OPENAPI: Chart (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/Chart.html
- source_path: `com/nomagic/magicreport/Chart.html`
- source_sha256: `51480f14747c0f5ef391978e6d91cb0f916bcf8bf12acd3c95197ae862a2783e`
- captured_utc: `2026-07-14T16:46:11.287949+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class Chart

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.Chart

Direct Known Subclasses:
`[XLSXChart](XLSXChart.html)`

@OpenApiAllpublic classChart
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

An bean represent a chart object for template.

Since:
Nov 22, 2021

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`class`
`[Chart.Series](Chart.Series.html)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Chart](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType)`

`[Chart](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Chart.Series](Chart.Series.html)`
`[createSeries](#createSeries(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getCategories](#getCategories())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getChartStyle](#getChartStyle())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getChartType](#getChartType())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Chart.Series](Chart.Series.html)>`
`[getSeriesList](#getSeriesList())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getTitle](#getTitle())()`

`void`
`[setCategories](#setCategories(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> categories)`

`void`
`[setChartStyle](#setChartStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle)`

`void`
`[setChartType](#setChartType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType)`

`void`
`[setSeriesList](#setSeriesList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Chart.Series](Chart.Series.html)> seriesList)`

`void`
`[setTitle](#setTitle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) title)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Chart
public Chart([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType)
Chart
public Chart([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle)
 ============ METHOD DETAIL ========== 
Method Details
getChartType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getChartType()
setChartType
public void setChartType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType)
getChartStyle
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getChartStyle()
setChartStyle
public void setChartStyle([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle)
getTitle
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getTitle()
setTitle
public void setTitle([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) title)
getSeriesList
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Chart.Series](Chart.Series.html)> getSeriesList()
setSeriesList
public void setSeriesList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Chart.Series](Chart.Series.html)> seriesList)
getCategories
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getCategories()
setCategories
public void setCategories([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> categories)
createSeries
public [Chart.Series](Chart.Series.html) createSeries([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class Chart">Class Chart</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.Chart</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="XLSXChart.html" title="class in com.nomagic.magicreport">XLSXChart</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Chart</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">An bean represent a chart object for template.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Nov 22, 2021</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">Chart</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">Chart</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSeries(java.lang.String)">createSeries</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategories()">getCategories</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChartStyle()">getChartStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChartType()">getChartType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeriesList()">getSeriesList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitle()">getTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCategories(java.util.Collection)">setCategories</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categories)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChartStyle(java.lang.String)">setChartStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChartType(java.lang.String)">setChartType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeriesList(java.util.List)">setSeriesList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a>&gt; seriesList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitle(java.lang.String)">setTitle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>Chart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Chart</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>Chart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Chart</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle)</span></div>
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
<section class="detail" id="getChartType()">
<h3>getChartType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getChartType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setChartType(java.lang.String)">
<h3>setChartType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChartType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType)</span></div>
</section>
</li>
<li>
<section class="detail" id="getChartStyle()">
<h3>getChartStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getChartStyle</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setChartStyle(java.lang.String)">
<h3>setChartStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChartStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTitle(java.lang.String)">
<h3>setTitle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> title)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSeriesList()">
<h3>getSeriesList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a>&gt;</span> <span class="element-name">getSeriesList</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSeriesList(java.util.List)">
<h3>setSeriesList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeriesList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a>&gt; seriesList)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCategories()">
<h3>getCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getCategories</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCategories(java.util.Collection)">
<h3>setCategories</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCategories</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categories)</span></div>
</section>
</li>
<li>
<section class="detail" id="createSeries(java.lang.String)">
<h3>createSeries</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a></span> <span class="element-name">createSeries</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
