# JAVA OPENAPI: Matrix (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/dependencymatrix/Matrix.html
- source_path: `com/nomagic/reportwizard/tools/dependencymatrix/Matrix.html`
- source_sha256: `9783359de06910292ceae29668126cf32c7b8c506d11da5a190418ae9b6a1e61`
- captured_utc: `2026-07-14T16:46:15.340005+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.dependencymatrix](package-summary.html)

## Class Matrix

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.dependencymatrix.Matrix

@OpenApiAllpublic classMatrix
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Class for getting row elements, column name and relation between row and column elements.

Since:
Feb 1, 2012

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Matrix](#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix))(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Relation](Relation.html)>`
`[getCellDependencies](#getCellDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html) rowNode,
 [ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html) columnNode)`
Get list of relations inside the cell identified row node and column node
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getColumnElements](#getColumnElements())()`
Get all column element.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html)>`
`[getColumnNodes](#getColumnNodes())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getColumns](#getColumns())()`
Deprecated.
use [`getColumnElements()`](#getColumnElements())
`com.nomagic.magicdraw.dependencymatrix.DependencyMatrix`
`[getMatrix](#getMatrix())()`
Gets dependency matrix instance.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Relation](Relation.html)>`
`[getRelation](#getRelation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) columnElement)`
Get list of relation between rowElement and column element.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRowElements](#getRowElements())()`
Get all row elements.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html)>`
`[getRowNodes](#getRowNodes())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRows](#getRows())()`
Deprecated.
use [`getRowElements()`](#getRowElements())
`void`
`[setMatrix](#setMatrix(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix))(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)`
Sets dependency matrix instance.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Matrix
public Matrix(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)
Constructor
Parameters:
`matrix` - Dependency Matrix instance
 ============ METHOD DETAIL ========== 
Method Details
getRowElements
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRowElements()
Get all row elements.
Returns:
list of elements
getColumnElements
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getColumnElements()
Get all column element.
Returns:
list of elements
getRows
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRows()
Deprecated.
use [`getRowElements()`](#getRowElements())
getColumns
@CheckForNull
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getColumns()
Deprecated.
use [`getColumnElements()`](#getColumnElements())
getRowNodes
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html)> getRowNodes()
Returns:
list of nodes that represent matrix rows, in the same order as they are actually displayed in the diagram.
 Grouping packages, that do not belong to the matrix data are skipped.
getColumnNodes
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html)> getColumnNodes()
Returns:
list of nodes that represent matrix rows, in the same order as they are actually displayed in the diagram.
 Grouping packages, that do not belong to the matrix data are skipped.
getCellDependencies
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Relation](Relation.html)> getCellDependencies([ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html) rowNode,
 [ElementNode](../../../magicdraw/dependencymatrix/datamodel/ElementNode.html) columnNode)
Get list of relations inside the cell identified row node and column node
getRelation
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Relation](Relation.html)> getRelation([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) columnElement)
Get list of relation between rowElement and column element.
Parameters:
`rowElement` - row element
`columnElement` - column element
Returns:
list of Relation
getMatrix
public com.nomagic.magicdraw.dependencymatrix.DependencyMatrix getMatrix()
Gets dependency matrix instance.
Returns:
matrix
setMatrix
public void setMatrix(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)
Sets dependency matrix instance.
Parameters:
`matrix` - matrix

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.dependencymatrix</a></div>
<h1 class="title" title="Class Matrix">Class Matrix</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.dependencymatrix.Matrix</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Matrix</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class for getting row elements, column name and relation between row and column elements.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Feb 1, 2012</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix)">Matrix</a><wbr/>(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Relation.html" title="class in com.nomagic.reportwizard.tools.dependencymatrix">Relation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">getCellDependencies</a><wbr/>(<a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> rowNode,
 <a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> columnNode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of relations inside the cell identified row node and column node</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnElements()">getColumnElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all column element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNodes()">getColumnNodes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getColumns()">getColumns</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getColumnElements()"><code>getColumnElements()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.dependencymatrix.DependencyMatrix</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMatrix()">getMatrix</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets dependency matrix instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="Relation.html" title="class in com.nomagic.reportwizard.tools.dependencymatrix">Relation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRelation</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> columnElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get list of relation between rowElement and column element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowElements()">getRowElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all row elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRowNodes()">getRowNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRows()">getRows</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getRowElements()"><code>getRowElements()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMatrix(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix)">setMatrix</a><wbr/>(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets dependency matrix instance.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix)">
<h3>Matrix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Matrix</span><wbr/><span class="parameters">(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - Dependency Matrix instance</dd>
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
<section class="detail" id="getRowElements()">
<h3>getRowElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRowElements</span>()</div>
<div class="block">Get all row elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnElements()">
<h3>getColumnElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getColumnElements</span>()</div>
<div class="block">Get all column element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRows()">
<h3>getRows</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRows</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getRowElements()"><code>getRowElements()</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getColumns()">
<h3>getColumns</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getColumns</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getColumnElements()"><code>getColumnElements()</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRowNodes()">
<h3>getRowNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getRowNodes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of nodes that represent matrix rows, in the same order as they are actually displayed in the diagram.
         Grouping packages, that do not belong to the matrix data are skipped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNodes()">
<h3>getColumnNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getColumnNodes</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of nodes that represent matrix rows, in the same order as they are actually displayed in the diagram.
         Grouping packages, that do not belong to the matrix data are skipped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>getCellDependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Relation.html" title="class in com.nomagic.reportwizard.tools.dependencymatrix">Relation</a>&gt;</span> <span class="element-name">getCellDependencies</span><wbr/><span class="parameters">(<a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> rowNode,
 <a href="../../../magicdraw/dependencymatrix/datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> columnNode)</span></div>
<div class="block">Get list of relations inside the cell identified row node and column node</div>
</section>
</li>
<li>
<section class="detail" id="getRelation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRelation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Relation.html" title="class in com.nomagic.reportwizard.tools.dependencymatrix">Relation</a>&gt;</span> <span class="element-name">getRelation</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> columnElement)</span></div>
<div class="block">Get list of relation between rowElement and column element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rowElement</code> - row element</dd>
<dd><code>columnElement</code> - column element</dd>
<dt>Returns:</dt>
<dd>list of Relation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMatrix()">
<h3>getMatrix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.dependencymatrix.DependencyMatrix</span> <span class="element-name">getMatrix</span>()</div>
<div class="block">Gets dependency matrix instance.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>matrix</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMatrix(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix)">
<h3>setMatrix</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMatrix</span><wbr/><span class="parameters">(com.nomagic.magicdraw.dependencymatrix.DependencyMatrix matrix)</span></div>
<div class="block">Sets dependency matrix instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - matrix</dd>
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
