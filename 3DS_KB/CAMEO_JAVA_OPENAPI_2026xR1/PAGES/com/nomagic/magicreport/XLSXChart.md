# JAVA OPENAPI: XLSXChart (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/XLSXChart.html
- source_path: `com/nomagic/magicreport/XLSXChart.html`
- source_sha256: `2af6f16540d7d1338ea3b39f82bb0bcc0df56115717dec4853eda44f4fef5a3e`
- captured_utc: `2026-07-14T16:46:11.687957+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class XLSXChart

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicreport.Chart](Chart.html)
com.nomagic.magicreport.XLSXChart

@OpenApiAllpublic classXLSXChart
extends [Chart](Chart.html)

An bean represent a chart object for xlsx template.

Since:
Jan 12, 2022

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.magicreport.[Chart](Chart.html)
`[Chart.Series](Chart.Series.html)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[XLSXChart](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType)`

`[XLSXChart](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle)`

`[XLSXChart](#%3Cinit%3E(java.lang.String,java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle,
 int columnSize,
 int rowSize)`

`[XLSXChart](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) startCell,
 int columnSize,
 int rowSize)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getColumnSize](#getColumnSize())()`

`int`
`[getRowSize](#getRowSize())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getStartCell](#getStartCell())()`

`void`
`[setColumnSize](#setColumnSize(int))(int columnSize)`

`void`
`[setRowSize](#setRowSize(int))(int rowSize)`

`void`
`[setStartCell](#setStartCell(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) startCell)`
Methods inherited from class com.nomagic.magicreport.[Chart](Chart.html)
`[createSeries](Chart.html#createSeries(java.lang.String)), [getCategories](Chart.html#getCategories()), [getChartStyle](Chart.html#getChartStyle()), [getChartType](Chart.html#getChartType()), [getSeriesList](Chart.html#getSeriesList()), [getTitle](Chart.html#getTitle()), [setCategories](Chart.html#setCategories(java.util.Collection)), [setChartStyle](Chart.html#setChartStyle(java.lang.String)), [setChartType](Chart.html#setChartType(java.lang.String)), [setSeriesList](Chart.html#setSeriesList(java.util.List)), [setTitle](Chart.html#setTitle(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
XLSXChart
public XLSXChart([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType)
XLSXChart
public XLSXChart([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle)
XLSXChart
public XLSXChart([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle,
 int columnSize,
 int rowSize)
XLSXChart
public XLSXChart([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) chartStyle,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) startCell,
 int columnSize,
 int rowSize)
 ============ METHOD DETAIL ========== 
Method Details
getStartCell
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getStartCell()
setStartCell
public void setStartCell([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) startCell)
getColumnSize
public int getColumnSize()
setColumnSize
public void setColumnSize(int columnSize)
getRowSize
public int getRowSize()
setRowSize
public void setRowSize(int rowSize)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class XLSXChart">Class XLSXChart</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="Chart.html" title="class in com.nomagic.magicreport">com.nomagic.magicreport.Chart</a>
<div class="inheritance">com.nomagic.magicreport.XLSXChart</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">XLSXChart</span>
<span class="extends-implements">extends <a href="Chart.html" title="class in com.nomagic.magicreport">Chart</a></span></div>
<div class="block">An bean represent a chart object for xlsx template.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 12, 2022</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.Chart">Nested classes/interfaces inherited from class com.nomagic.magicreport.<a href="Chart.html" title="class in com.nomagic.magicreport">Chart</a></h2>
<code><a href="Chart.Series.html" title="class in com.nomagic.magicreport">Chart.Series</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">XLSXChart</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">XLSXChart</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,int,int)">XLSXChart</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle,
 int columnSize,
 int rowSize)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,int,int)">XLSXChart</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> startCell,
 int columnSize,
 int rowSize)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnSize()">getColumnSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowSize()">getRowSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartCell()">getStartCell</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnSize(int)">setColumnSize</a><wbr/>(int columnSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowSize(int)">setRowSize</a><wbr/>(int rowSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStartCell(java.lang.String)">setStartCell</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> startCell)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.Chart">Methods inherited from class com.nomagic.magicreport.<a href="Chart.html" title="class in com.nomagic.magicreport">Chart</a></h3>
<code><a href="Chart.html#createSeries(java.lang.String)">createSeries</a>, <a href="Chart.html#getCategories()">getCategories</a>, <a href="Chart.html#getChartStyle()">getChartStyle</a>, <a href="Chart.html#getChartType()">getChartType</a>, <a href="Chart.html#getSeriesList()">getSeriesList</a>, <a href="Chart.html#getTitle()">getTitle</a>, <a href="Chart.html#setCategories(java.util.Collection)">setCategories</a>, <a href="Chart.html#setChartStyle(java.lang.String)">setChartStyle</a>, <a href="Chart.html#setChartType(java.lang.String)">setChartType</a>, <a href="Chart.html#setSeriesList(java.util.List)">setSeriesList</a>, <a href="Chart.html#setTitle(java.lang.String)">setTitle</a></code></div>
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
<h3>XLSXChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXChart</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>XLSXChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXChart</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,int,int)">
<h3>XLSXChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXChart</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle,
 int columnSize,
 int rowSize)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,int,int)">
<h3>XLSXChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXChart</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> chartStyle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> startCell,
 int columnSize,
 int rowSize)</span></div>
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
<section class="detail" id="getStartCell()">
<h3>getStartCell</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStartCell</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setStartCell(java.lang.String)">
<h3>setStartCell</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartCell</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> startCell)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnSize()">
<h3>getColumnSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getColumnSize</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setColumnSize(int)">
<h3>setColumnSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnSize</span><wbr/><span class="parameters">(int columnSize)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRowSize()">
<h3>getRowSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getRowSize</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setRowSize(int)">
<h3>setRowSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowSize</span><wbr/><span class="parameters">(int rowSize)</span></div>
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
