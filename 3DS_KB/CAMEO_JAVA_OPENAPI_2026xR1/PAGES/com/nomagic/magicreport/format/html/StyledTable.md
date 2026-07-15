# JAVA OPENAPI: StyledTable (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/format/html/StyledTable.html
- source_path: `com/nomagic/magicreport/format/html/StyledTable.html`
- source_sha256: `2e2c73b3e8c9d9daf5c7aae7d80489d28fd02d924f4bb0f2bf64adac04ab37ad`
- captured_utc: `2026-07-14T16:46:14.361992+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class StyledTable

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.format.html.StyledTable

@OpenApiAllpublic classStyledTable
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Class for keeping shared styles of table, tr, and td.

Since:
July 24, 2013

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TABLE_PROPERTIES](#TABLE_PROPERTIES)`
constants for table properites.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TAG_NAME](#TAG_NAME)`
Constants for tag name.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StyledTable](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addCellStyle](#addCellStyle(com.nomagic.magicreport.format.html.CellStyle))([CellStyle](CellStyle.html) cellStyle)`
Add cell (TD) style to list.
`void`
`[clearCellStyle](#clearCellStyle())()`
Clear cell style.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CellStyle](CellStyle.html)>`
`[getCellStyle](#getCellStyle())()`
Get cell (TD) style list.
`[CellStyle](CellStyle.html)`
`[getCellStyle](#getCellStyle(int))(int index)`
Get cell (TD) style by index.
`[CellStyle](CellStyle.html)`
`[getRowStyle](#getRowStyle())()`
Get row (TR) style.
`[CellStyle](CellStyle.html)`
`[getTableStyle](#getTableStyle())()`
Get table style.
`void`
`[setCellStyle](#setCellStyle(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CellStyle](CellStyle.html)> cellStyles)`
Set cell (TD) style.
`void`
`[setRowStyle](#setRowStyle(com.nomagic.magicreport.format.html.CellStyle))([CellStyle](CellStyle.html) rowStyle)`
Set row (TR) style.
`void`
`[setTableStyle](#setTableStyle(com.nomagic.magicreport.format.html.CellStyle))([CellStyle](CellStyle.html) tableStyle)`
Set table style.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TABLE_PROPERTIES
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TABLE_PROPERTIES
constants for table properites.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledTable.TABLE_PROPERTIES)
TAG_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TAG_NAME
Constants for tag name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledTable.TAG_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StyledTable
public StyledTable()
 ============ METHOD DETAIL ========== 
Method Details
getTableStyle
public [CellStyle](CellStyle.html) getTableStyle()
Get table style.
Returns:
tableStyle
setTableStyle
public void setTableStyle([CellStyle](CellStyle.html) tableStyle)
Set table style.
Parameters:
`tableStyle` - table style
getRowStyle
public [CellStyle](CellStyle.html) getRowStyle()
Get row (TR) style.
Returns:
rowStyle
setRowStyle
public void setRowStyle([CellStyle](CellStyle.html) rowStyle)
Set row (TR) style.
Parameters:
`rowStyle` - row style
getCellStyle
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CellStyle](CellStyle.html)> getCellStyle()
Get cell (TD) style list.
Returns:
cellStyle list
setCellStyle
public void setCellStyle([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[CellStyle](CellStyle.html)> cellStyles)
Set cell (TD) style.
Parameters:
`cellStyles` - list of cell style
addCellStyle
public void addCellStyle([CellStyle](CellStyle.html) cellStyle)
Add cell (TD) style to list.
Parameters:
`cellStyle` - of cell style
getCellStyle
public [CellStyle](CellStyle.html) getCellStyle(int index)
Get cell (TD) style by index.
Parameters:
`index` - index of cell style in list
Returns:
cell style at index
clearCellStyle
public void clearCellStyle()
Clear cell style.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class StyledTable">Class StyledTable</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.format.html.StyledTable</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StyledTable</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for keeping shared styles of table, tr, and td.<br/></div>
<dl class="notes">
<dt>Since:</dt>
<dd>July 24, 2013</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TABLE_PROPERTIES">TABLE_PROPERTIES</a></code></div>
<div class="col-last even-row-color">
<div class="block">constants for table properites.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TAG_NAME">TAG_NAME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for tag name.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">StyledTable</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCellStyle(com.nomagic.magicreport.format.html.CellStyle)">addCellStyle</a><wbr/>(<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a> cellStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add cell (TD) style to list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearCellStyle()">clearCellStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear cell style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellStyle()">getCellStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get cell (TD) style list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellStyle(int)">getCellStyle</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get cell (TD) style by index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowStyle()">getRowStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get row (TR) style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTableStyle()">getTableStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get table style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCellStyle(java.util.List)">setCellStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a>&gt; cellStyles)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set cell (TD) style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRowStyle(com.nomagic.magicreport.format.html.CellStyle)">setRowStyle</a><wbr/>(<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a> rowStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set row (TR) style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTableStyle(com.nomagic.magicreport.format.html.CellStyle)">setTableStyle</a><wbr/>(<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a> tableStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set table style.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="TABLE_PROPERTIES">
<h3>TABLE_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TABLE_PROPERTIES</span></div>
<div class="block">constants for table properites.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledTable.TABLE_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TAG_NAME">
<h3>TAG_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TAG_NAME</span></div>
<div class="block">Constants for tag name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.StyledTable.TAG_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>StyledTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StyledTable</span>()</div>
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
<section class="detail" id="getTableStyle()">
<h3>getTableStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></span> <span class="element-name">getTableStyle</span>()</div>
<div class="block">Get table style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tableStyle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTableStyle(com.nomagic.magicreport.format.html.CellStyle)">
<h3>setTableStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTableStyle</span><wbr/><span class="parameters">(<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a> tableStyle)</span></div>
<div class="block">Set table style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tableStyle</code> - table style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowStyle()">
<h3>getRowStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></span> <span class="element-name">getRowStyle</span>()</div>
<div class="block">Get row (TR) style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rowStyle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRowStyle(com.nomagic.magicreport.format.html.CellStyle)">
<h3>setRowStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRowStyle</span><wbr/><span class="parameters">(<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a> rowStyle)</span></div>
<div class="block">Set row (TR) style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowStyle</code> - row style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellStyle()">
<h3>getCellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a>&gt;</span> <span class="element-name">getCellStyle</span>()</div>
<div class="block">Get cell (TD) style list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>cellStyle list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCellStyle(java.util.List)">
<h3>setCellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCellStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a>&gt; cellStyles)</span></div>
<div class="block">Set cell (TD) style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cellStyles</code> - list of cell style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCellStyle(com.nomagic.magicreport.format.html.CellStyle)">
<h3>addCellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCellStyle</span><wbr/><span class="parameters">(<a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a> cellStyle)</span></div>
<div class="block">Add cell (TD) style to list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cellStyle</code> - of cell style</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellStyle(int)">
<h3>getCellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="CellStyle.html" title="class in com.nomagic.magicreport.format.html">CellStyle</a></span> <span class="element-name">getCellStyle</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Get cell (TD) style by index.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - index of cell style in list</dd>
<dt>Returns:</dt>
<dd>cell style at index</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearCellStyle()">
<h3>clearCellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearCellStyle</span>()</div>
<div class="block">Clear cell style.</div>
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
