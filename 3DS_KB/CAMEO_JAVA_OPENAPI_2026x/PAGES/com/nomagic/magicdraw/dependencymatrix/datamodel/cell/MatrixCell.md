# JAVA OPENAPI: MatrixCell (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/datamodel/cell/MatrixCell.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/cell/MatrixCell.html`
- source_sha256: `97c4ba23560fb03b778863ff4202b64f12fbcd2ecb83e7635cb2b60cc1f28cc2`
- captured_utc: `2026-07-14T16:57:53.343484+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.cell](package-summary.html)

## Class MatrixCell

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell](AbstractMatrixCell.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.cell.MatrixCell

@OpenApiAllpublic classMatrixCell
extends [AbstractMatrixCell](AbstractMatrixCell.html)
Single matrix element representation - holds information about elements and relations according to the criteria

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.dependencymatrix.datamodel.cell.[AbstractMatrixCell](AbstractMatrixCell.html)
`[EMPTY_CELL](AbstractMatrixCell.html#EMPTY_CELL), [EMPTY_EDITABLE_CELL](AbstractMatrixCell.html#EMPTY_EDITABLE_CELL), [EMPTY_READONLY_CELL](AbstractMatrixCell.html#EMPTY_READONLY_CELL), [UNKNOWN_CELL](AbstractMatrixCell.html#UNKNOWN_CELL)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MatrixCell](#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](../ElementNode.html) rowNode,
 [ElementNode](../ElementNode.html) columnNode)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ElementNode](../ElementNode.html)`
`[getColumnNode](#getColumnNode())()`
Column node.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)>`
`[getDependencies](#getDependencies())()`
Dependency entry list
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`

`[ElementNode](../ElementNode.html)`
`[getRowNode](#getRowNode())()`
Row node.
`[MatrixCellView](MatrixCellView.html)`
`[getView](#getView())()`
Creates or returns already created matrix view object
`void`
`[setDependencies](#setDependencies(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> dependencies)`
Set new collection with cell dependency list
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class com.nomagic.magicdraw.dependencymatrix.datamodel.cell.[AbstractMatrixCell](AbstractMatrixCell.html)
`[getStaticCell](AbstractMatrixCell.html#getStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags)), [isEditable](AbstractMatrixCell.html#isEditable()), [isStaticCell](AbstractMatrixCell.html#isStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)), [isUnknownEditableState](AbstractMatrixCell.html#isUnknownEditableState()), [isUnknownStaticCell](AbstractMatrixCell.html#isUnknownStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MatrixCell
public MatrixCell([ElementNode](../ElementNode.html) rowNode,
 [ElementNode](../ElementNode.html) columnNode)
 ============ METHOD DETAIL ========== 
Method Details
getRowNode
public [ElementNode](../ElementNode.html) getRowNode()
Row node.
Returns:
row node.
getColumnNode
public [ElementNode](../ElementNode.html) getColumnNode()
Column node.
Returns:
column node.
getDependencies
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> getDependencies()
Description copied from class: `[AbstractMatrixCell](AbstractMatrixCell.html#getDependencies())`
Dependency entry list
Specified by:
`[getDependencies](AbstractMatrixCell.html#getDependencies())` in class `[AbstractMatrixCell](AbstractMatrixCell.html)`
Returns:
dependency entries or empty list if not exits
setDependencies
public void setDependencies([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> dependencies)
Description copied from class: `[AbstractMatrixCell](AbstractMatrixCell.html#setDependencies(java.util.Collection))`
Set new collection with cell dependency list
Specified by:
`[setDependencies](AbstractMatrixCell.html#setDependencies(java.util.Collection))` in class `[AbstractMatrixCell](AbstractMatrixCell.html)`
Parameters:
`dependencies` - new dependency list for the cell
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
getView
public [MatrixCellView](MatrixCellView.html) getView()
Description copied from class: `[AbstractMatrixCell](AbstractMatrixCell.html#getView())`
Creates or returns already created matrix view object
Overrides:
`[getView](AbstractMatrixCell.html#getView())` in class `[AbstractMatrixCell](AbstractMatrixCell.html)`
Returns:
matrix cell view object
getDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDescription()
Overrides:
`[getDescription](AbstractMatrixCell.html#getDescription())` in class `[AbstractMatrixCell](AbstractMatrixCell.html)`
Returns:
representative text describing this cell

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.cell</a></div>
<h1 class="title" title="Class MatrixCell">Class MatrixCell</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.cell.MatrixCell</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MatrixCell</span>
<span class="extends-implements">extends <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span></div>
<div class="block">Single matrix element representation - holds information about elements and relations according to the criteria</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell">Fields inherited from class com.nomagic.magicdraw.dependencymatrix.datamodel.cell.<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></h3>
<code><a href="AbstractMatrixCell.html#EMPTY_CELL">EMPTY_CELL</a>, <a href="AbstractMatrixCell.html#EMPTY_EDITABLE_CELL">EMPTY_EDITABLE_CELL</a>, <a href="AbstractMatrixCell.html#EMPTY_READONLY_CELL">EMPTY_READONLY_CELL</a>, <a href="AbstractMatrixCell.html#UNKNOWN_CELL">UNKNOWN_CELL</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">MatrixCell</a><wbr/>(<a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> rowNode,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> columnNode)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNode()">getColumnNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Column node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDependencies()">getDependencies</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dependency entry list</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowNode()">getRowNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Row node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getView()">getView</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates or returns already created matrix view object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDependencies(java.util.Collection)">setDependencies</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt; dependencies)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set new collection with cell dependency list</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell">Methods inherited from class com.nomagic.magicdraw.dependencymatrix.datamodel.cell.<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></h3>
<code><a href="AbstractMatrixCell.html#getStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags)">getStaticCell</a>, <a href="AbstractMatrixCell.html#isEditable()">isEditable</a>, <a href="AbstractMatrixCell.html#isStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">isStaticCell</a>, <a href="AbstractMatrixCell.html#isUnknownEditableState()">isUnknownEditableState</a>, <a href="AbstractMatrixCell.html#isUnknownStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">isUnknownStaticCell</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>MatrixCell</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MatrixCell</span><wbr/><span class="parameters">(<a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> rowNode,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> columnNode)</span></div>
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
<section class="detail" id="getRowNode()">
<h3>getRowNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getRowNode</span>()</div>
<div class="block">Row node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>row node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNode()">
<h3>getColumnNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a></span> <span class="element-name">getColumnNode</span>()</div>
<div class="block">Column node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>column node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependencies()">
<h3>getDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</span> <span class="element-name">getDependencies</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="AbstractMatrixCell.html#getDependencies()">AbstractMatrixCell</a></code></span></div>
<div class="block">Dependency entry list</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractMatrixCell.html#getDependencies()">getDependencies</a></code> in class <code><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></dd>
<dt>Returns:</dt>
<dd>dependency entries or empty list if not exits</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDependencies(java.util.Collection)">
<h3>setDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDependencies</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt; dependencies)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="AbstractMatrixCell.html#setDependencies(java.util.Collection)">AbstractMatrixCell</a></code></span></div>
<div class="block">Set new collection with cell dependency list</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractMatrixCell.html#setDependencies(java.util.Collection)">setDependencies</a></code> in class <code><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></dd>
<dt>Parameters:</dt>
<dd><code>dependencies</code> - new dependency list for the cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getView()">
<h3>getView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></span> <span class="element-name">getView</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="AbstractMatrixCell.html#getView()">AbstractMatrixCell</a></code></span></div>
<div class="block">Creates or returns already created matrix view object</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractMatrixCell.html#getView()">getView</a></code> in class <code><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></dd>
<dt>Returns:</dt>
<dd>matrix cell view object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractMatrixCell.html#getDescription()">getDescription</a></code> in class <code><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></dd>
<dt>Returns:</dt>
<dd>representative text describing this cell</dd>
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
