# JAVA OPENAPI: AbstractMatrixCell (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/datamodel/cell/AbstractMatrixCell.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/cell/AbstractMatrixCell.html`
- source_sha256: `9338263c6590ff41c34fe05696ad58424214987a15435417221aa3acf66aad24`
- captured_utc: `2026-07-14T16:57:53.309483+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.cell](package-summary.html)

## Class AbstractMatrixCell

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell

Direct Known Subclasses:
`[MatrixCell](MatrixCell.html)`

@OpenApiAllpublic abstract classAbstractMatrixCell
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Base cell for all matrix cells

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [AbstractMatrixCell](AbstractMatrixCell.html)`
`[EMPTY_CELL](#EMPTY_CELL)`
Returns static empty matrix cell
`static final [AbstractMatrixCell](AbstractMatrixCell.html)`
`[EMPTY_EDITABLE_CELL](#EMPTY_EDITABLE_CELL)`
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
`static final [AbstractMatrixCell](AbstractMatrixCell.html)`
`[EMPTY_READONLY_CELL](#EMPTY_READONLY_CELL)`
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
`static final [AbstractMatrixCell](AbstractMatrixCell.html)`
`[UNKNOWN_CELL](#UNKNOWN_CELL)`
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractMatrixCell](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`abstract [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)>`
`[getDependencies](#getDependencies())()`
Dependency entry list
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`

`static [AbstractMatrixCell](AbstractMatrixCell.html)`
`[getStaticCell](#getStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags))([ReadOnlyFlags](ReadOnlyFlags.html) readOnlyFlags)`
Deprecated.
deprecated after removal of non-editable cells
`[MatrixCellView](MatrixCellView.html)`
`[getView](#getView())()`
Creates or returns already created matrix view object
`boolean`
`[isEditable](#isEditable())()`
Deprecated.
isEditable is always true, the editable state is checked when trying to create/delete cell value
`static boolean`
`[isStaticCell](#isStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell))([AbstractMatrixCell](AbstractMatrixCell.html) value)`
Deprecated.
deprecated after removal of non-editable cells
`boolean`
`[isUnknownEditableState](#isUnknownEditableState())()`
Deprecated.
unknown editable state is always false, the editable state is checked when trying to create/delete cell value
`static boolean`
`[isUnknownStaticCell](#isUnknownStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell))([AbstractMatrixCell](AbstractMatrixCell.html) cell)`
Deprecated.
deprecated after removal of non-editable cells
`abstract void`
`[setDependencies](#setDependencies(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> dependencies)`
Set new collection with cell dependency list
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
EMPTY_CELL
public static final [AbstractMatrixCell](AbstractMatrixCell.html) EMPTY_CELL
Returns static empty matrix cell
EMPTY_EDITABLE_CELL
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [AbstractMatrixCell](AbstractMatrixCell.html) EMPTY_EDITABLE_CELL
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
EMPTY_READONLY_CELL
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [AbstractMatrixCell](AbstractMatrixCell.html) EMPTY_READONLY_CELL
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
UNKNOWN_CELL
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static final [AbstractMatrixCell](AbstractMatrixCell.html) UNKNOWN_CELL
Deprecated.
use [`EMPTY_CELL`](#EMPTY_CELL)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractMatrixCell
public AbstractMatrixCell()
 ============ METHOD DETAIL ========== 
Method Details
isEditable
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public boolean isEditable()
Deprecated.
isEditable is always true, the editable state is checked when trying to create/delete cell value
to check whether a relation based on dependency criteria can be created/deleted between element nodes use
 [`MatrixDataHelper.isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode, com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)`](../../configuration/MatrixDataHelper.html#isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))
isUnknownEditableState
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public boolean isUnknownEditableState()
Deprecated.
unknown editable state is always false, the editable state is checked when trying to create/delete cell value
getDependencies
public abstract [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> getDependencies()
Dependency entry list
Returns:
dependency entries or empty list if not exits
setDependencies
public abstract void setDependencies([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> dependencies)
Set new collection with cell dependency list
Parameters:
`dependencies` - new dependency list for the cell
getView
public [MatrixCellView](MatrixCellView.html) getView()
Creates or returns already created matrix view object
Returns:
matrix cell view object
getDescription
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDescription()
Returns:
representative text describing this cell
getStaticCell
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static [AbstractMatrixCell](AbstractMatrixCell.html) getStaticCell([ReadOnlyFlags](ReadOnlyFlags.html) readOnlyFlags)
Deprecated.
deprecated after removal of non-editable cells
isUnknownStaticCell
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isUnknownStaticCell([AbstractMatrixCell](AbstractMatrixCell.html) cell)
Deprecated.
deprecated after removal of non-editable cells
isStaticCell
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public static boolean isStaticCell([AbstractMatrixCell](AbstractMatrixCell.html) value)
Deprecated.
deprecated after removal of non-editable cells

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.cell</a></div>
<h1 class="title" title="Class AbstractMatrixCell">Class AbstractMatrixCell</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="MatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCell</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractMatrixCell</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Base cell for all matrix cells</div>
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
<div class="col-first even-row-color"><code>static final <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY_CELL">EMPTY_CELL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Returns static empty matrix cell</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EMPTY_EDITABLE_CELL">EMPTY_EDITABLE_CELL</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY_READONLY_CELL">EMPTY_READONLY_CELL</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNKNOWN_CELL">UNKNOWN_CELL</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractMatrixCell</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDependencies()">getDependencies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Dependency entry list</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags)">getStaticCell</a><wbr/>(<a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a> readOnlyFlags)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated after removal of non-editable cells</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getView()">getView</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates or returns already created matrix view object</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">isEditable is always true, the editable state is checked when trying to create/delete cell value</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">isStaticCell</a><wbr/>(<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated after removal of non-editable cells</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isUnknownEditableState()">isUnknownEditableState</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">unknown editable state is always false, the editable state is checked when trying to create/delete cell value</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isUnknownStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">isUnknownStaticCell</a><wbr/>(<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated after removal of non-editable cells</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDependencies(java.util.Collection)">setDependencies</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt; dependencies)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set new collection with cell dependency list</div>
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
<section class="detail" id="EMPTY_CELL">
<h3>EMPTY_CELL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">EMPTY_CELL</span></div>
<div class="block">Returns static empty matrix cell</div>
</section>
</li>
<li>
<section class="detail" id="EMPTY_EDITABLE_CELL">
<h3>EMPTY_EDITABLE_CELL</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">EMPTY_EDITABLE_CELL</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="EMPTY_READONLY_CELL">
<h3>EMPTY_READONLY_CELL</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">EMPTY_READONLY_CELL</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#EMPTY_CELL"><code>EMPTY_CELL</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="UNKNOWN_CELL">
<h3>UNKNOWN_CELL</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">UNKNOWN_CELL</span></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>AbstractMatrixCell</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractMatrixCell</span>()</div>
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
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">isEditable is always true, the editable state is checked when trying to create/delete cell value</div>
</div>
<div class="block">to check whether a relation based on dependency criteria can be created/deleted between element nodes use
 <a href="../../configuration/MatrixDataHelper.html#isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)"><code>MatrixDataHelper.isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram, com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode, com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)</code></a></div>
</section>
</li>
<li>
<section class="detail" id="isUnknownEditableState()">
<h3>isUnknownEditableState</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUnknownEditableState</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">unknown editable state is always false, the editable state is checked when trying to create/delete cell value</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDependencies()">
<h3>getDependencies</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</span> <span class="element-name">getDependencies</span>()</div>
<div class="block">Dependency entry list</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>dependency entries or empty list if not exits</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDependencies(java.util.Collection)">
<h3>setDependencies</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">setDependencies</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt; dependencies)</span></div>
<div class="block">Set new collection with cell dependency list</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dependencies</code> - new dependency list for the cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getView()">
<h3>getView</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixCellView.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">MatrixCellView</a></span> <span class="element-name">getView</span>()</div>
<div class="block">Creates or returns already created matrix view object</div>
<dl class="notes">
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
<dt>Returns:</dt>
<dd>representative text describing this cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.ReadOnlyFlags)">
<h3>getStaticCell</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">getStaticCell</span><wbr/><span class="parameters">(<a href="ReadOnlyFlags.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">ReadOnlyFlags</a> readOnlyFlags)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated after removal of non-editable cells</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isUnknownStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">
<h3>isUnknownStaticCell</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUnknownStaticCell</span><wbr/><span class="parameters">(<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated after removal of non-editable cells</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isStaticCell(com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">
<h3>isStaticCell</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStaticCell</span><wbr/><span class="parameters">(<a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> value)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">deprecated after removal of non-editable cells</div>
</div>
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
