# JAVA OPENAPI: MatrixCellView (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/dependencymatrix/datamodel/cell/MatrixCellView.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/cell/MatrixCellView.html`
- source_sha256: `ce4376e1aa2f707a9191e3b5da833ce36ba4a87ce5afc2995dd34d6247a530fd`
- captured_utc: `2026-07-14T16:55:13.778996+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.cell](package-summary.html)

## Class MatrixCellView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.cell.MatrixCellView

@OpenApiAllpublic classMatrixCellView
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents one cell element in the matrix

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [MatrixCellView](MatrixCellView.html)`
`[EMPTY_CELL](#EMPTY_CELL)`
Display empty but editable cell
`static final [MatrixCellView](MatrixCellView.html)`
`[EMPTY_EDITABLE](#EMPTY_EDITABLE)`
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
`static final [MatrixCellView](MatrixCellView.html)`
`[EMPTY_READONLY](#EMPTY_READONLY)`
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
`static final [MatrixCellView](MatrixCellView.html)`
`[NULL_CELL](#NULL_CELL)`
Static value to represent null valued cell view
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MatrixCellView](#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell))([AbstractMatrixCell](AbstractMatrixCell.html) cell)`
Creates new cell view
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[AbstractMatrixCell](AbstractMatrixCell.html)`
`[getCell](#getCell())()`

`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Returns representation icon for this cell
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getToolTipText](#getToolTipText())()`

`boolean`
`[isEditable](#isEditable())()`

`void`
`[setToolTipText](#setToolTipText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Sets tooltip text describing the content of the cell
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
NULL_CELL
public static final [MatrixCellView](MatrixCellView.html) NULL_CELL
Static value to represent null valued cell view
EMPTY_CELL
public static final [MatrixCellView](MatrixCellView.html) EMPTY_CELL
Display empty but editable cell
EMPTY_EDITABLE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [MatrixCellView](MatrixCellView.html) EMPTY_EDITABLE
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
EMPTY_READONLY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [MatrixCellView](MatrixCellView.html) EMPTY_READONLY
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MatrixCellView
public MatrixCellView(@CheckForNull
 [AbstractMatrixCell](AbstractMatrixCell.html) cell)
Creates new cell view
Parameters:
`cell` - matrix cell
 ============ METHOD DETAIL ========== 
Method Details
getCell
@CheckForNullpublic [AbstractMatrixCell](AbstractMatrixCell.html) getCell()
Returns:
matrix cell.
isEditable
public boolean isEditable()
Returns:
is cell editable
getIcon
@CheckForNullpublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Returns representation icon for this cell
Returns:
cell representation icon
getToolTipText
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getToolTipText()
Returns:
tooltip text describing the content of the cell
setToolTipText
public void setToolTipText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Sets tooltip text describing the content of the cell

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.cell</a></div>
<h1 class="title" title="Class MatrixCellView">Class MatrixCellView</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.cell.MatrixCellView</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MatrixCellView</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Represents one cell element in the matrix</div>
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
<div class="col-first even-row-color"><code>static final <a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY_CELL">EMPTY_CELL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Display empty but editable cell</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EMPTY_EDITABLE">EMPTY_EDITABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY_READONLY">EMPTY_READONLY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NULL_CELL">NULL_CELL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Static value to represent null valued cell view</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">MatrixCellView</a><wbr/>(<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates new cell view</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCell()">getCell</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns representation icon for this cell</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getToolTipText()">getToolTipText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setToolTipText(java.lang.String)">setToolTipText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets tooltip text describing the content of the cell</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="NULL_CELL">
<h3>NULL_CELL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></span> <span class="element-name">NULL_CELL</span></div>
<div class="block">Static value to represent null valued cell view</div>
</section>
</li>
<li>
<section class="detail" id="EMPTY_CELL">
<h3>EMPTY_CELL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></span> <span class="element-name">EMPTY_CELL</span></div>
<div class="block">Display empty but editable cell</div>
</section>
</li>
<li>
<section class="detail" id="EMPTY_EDITABLE">
<h3>EMPTY_EDITABLE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></span> <span class="element-name">EMPTY_EDITABLE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="EMPTY_READONLY">
<h3>EMPTY_READONLY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></span> <span class="element-name">EMPTY_READONLY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">
<h3>MatrixCellView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MatrixCellView</span><wbr/><span class="parameters">(@CheckForNull
 <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</span></div>
<div class="block">Creates new cell view</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cell</code> - matrix cell</dd>
</dl>
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
<section class="detail" id="getCell()">
<h3>getCell</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">getCell</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>matrix cell.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>is cell editable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Returns representation icon for this cell</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>cell representation icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getToolTipText()">
<h3>getToolTipText</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getToolTipText</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tooltip text describing the content of the cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setToolTipText(java.lang.String)">
<h3>setToolTipText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setToolTipText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Sets tooltip text describing the content of the cell</div>
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
