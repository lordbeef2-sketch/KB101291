# JAVA OPENAPI: RendererHelper (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/ui/table/renderer/RendererHelper.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/ui/table/renderer/RendererHelper.html`
- source_sha256: `96c4517e2d51fce1873d1b832b9455638a0bbb1188b21eeea24154cc8649904d`
- captured_utc: `2026-07-14T16:57:53.932490+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.ui.table.renderer](package-summary.html)

## Class RendererHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.ui.table.renderer.RendererHelper

@OpenApiAllpublic classRendererHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Helper methods used in the Dependency Matrix renderer components

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RendererHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ElementNode](../../../datamodel/ElementNode.html)`
`[getColumnElementNode](#getColumnElementNode(javax.swing.JTable,int))([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int column)`
ElementNode represented by given column.
`static [Element](../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getHeaderElement](#getHeaderElement(javax.swing.JTable,int,int))([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int row,
 int column)`
Gets element from row or column header according to the row and column indexes
 This method because custom column header components do not return exact element as value of the column
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getNameExtension](#getNameExtension(javax.swing.JTable,int,int,java.lang.String))([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int row,
 int column,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) currentText)`
Returns name of the column in regard to its hierarchy (collapsed package names in compact tree mode)
`static [ElementNode](../../../datamodel/ElementNode.html)`
`[getRowElementNode](#getRowElementNode(javax.swing.JTable,int))([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int row)`
ElementNode represented by given row.
`static boolean`
`[isExpandedColumnGroupHeader](#isExpandedColumnGroupHeader(int))(int column)`
Checks if this column is one of the expanded group headers (e.g.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RendererHelper
public RendererHelper()
 ============ METHOD DETAIL ========== 
Method Details
getRowElementNode
@CheckForNullpublic static [ElementNode](../../../datamodel/ElementNode.html) getRowElementNode([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int row)
ElementNode represented by given row.
Parameters:
`table` - main table component
`row` - row index
Returns:
row element node
getColumnElementNode
@CheckForNullpublic static [ElementNode](../../../datamodel/ElementNode.html) getColumnElementNode([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int column)
ElementNode represented by given column.
Parameters:
`table` - main table component
`column` - row index
Returns:
column element node
getHeaderElement
@CheckForNullpublic static [Element](../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getHeaderElement([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int row,
 int column)
Gets element from row or column header according to the row and column indexes
 This method because custom column header components do not return exact element as value of the column
Parameters:
`table` - main table component
`row` - row index
`column` - column index
Returns:
column element instance
getNameExtension
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getNameExtension([JTable](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html) table,
 int row,
 int column,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) currentText)
Returns name of the column in regard to its hierarchy (collapsed package names in compact tree mode)
Parameters:
`table` - main table component
`row` - row index
`column` - column index
`currentText` - text to add extension to
Returns:
full text of the column element
isExpandedColumnGroupHeader
public static boolean isExpandedColumnGroupHeader(int column)
Checks if this column is one of the expanded group headers (e.g. package)
Parameters:
`column` - column index
Returns:
true if it is column group header

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.ui.table.renderer</a></div>
<h1 class="title" title="Class RendererHelper">Class RendererHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.ui.table.renderer.RendererHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RendererHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helper methods used in the Dependency Matrix renderer components</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RendererHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnElementNode(javax.swing.JTable,int)">getColumnElementNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int column)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">ElementNode represented by given column.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeaderElement(javax.swing.JTable,int,int)">getHeaderElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int row,
 int column)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets element from row or column header according to the row and column indexes
 This method because custom column header components do not return exact element as value of the column</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameExtension(javax.swing.JTable,int,int,java.lang.String)">getNameExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int row,
 int column,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currentText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns name of the column in regard to its hierarchy (collapsed package names in compact tree mode)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowElementNode(javax.swing.JTable,int)">getRowElementNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int row)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">ElementNode represented by given row.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExpandedColumnGroupHeader(int)">isExpandedColumnGroupHeader</a><wbr/>(int column)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if this column is one of the expanded group headers (e.g.</div>
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
<h3>RendererHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RendererHelper</span>()</div>
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
<section class="detail" id="getRowElementNode(javax.swing.JTable,int)">
<h3>getRowElementNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getRowElementNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int row)</span></div>
<div class="block">ElementNode represented by given row.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>table</code> - main table component</dd>
<dd><code>row</code> - row index</dd>
<dt>Returns:</dt>
<dd>row element node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnElementNode(javax.swing.JTable,int)">
<h3>getColumnElementNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getColumnElementNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int column)</span></div>
<div class="block">ElementNode represented by given column.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>table</code> - main table component</dd>
<dd><code>column</code> - row index</dd>
<dt>Returns:</dt>
<dd>column element node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHeaderElement(javax.swing.JTable,int,int)">
<h3>getHeaderElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getHeaderElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int row,
 int column)</span></div>
<div class="block">Gets element from row or column header according to the row and column indexes
 This method because custom column header components do not return exact element as value of the column</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>table</code> - main table component</dd>
<dd><code>row</code> - row index</dd>
<dd><code>column</code> - column index</dd>
<dt>Returns:</dt>
<dd>column element instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNameExtension(javax.swing.JTable,int,int,java.lang.String)">
<h3>getNameExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getNameExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/JTable.html" title="class or interface in javax.swing">JTable</a> table,
 int row,
 int column,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> currentText)</span></div>
<div class="block">Returns name of the column in regard to its hierarchy (collapsed package names in compact tree mode)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>table</code> - main table component</dd>
<dd><code>row</code> - row index</dd>
<dd><code>column</code> - column index</dd>
<dd><code>currentText</code> - text to add extension to</dd>
<dt>Returns:</dt>
<dd>full text of the column element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExpandedColumnGroupHeader(int)">
<h3>isExpandedColumnGroupHeader</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExpandedColumnGroupHeader</span><wbr/><span class="parameters">(int column)</span></div>
<div class="block">Checks if this column is one of the expanded group headers (e.g. package)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>column</code> - column index</dd>
<dt>Returns:</dt>
<dd>true if it is column group header</dd>
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
