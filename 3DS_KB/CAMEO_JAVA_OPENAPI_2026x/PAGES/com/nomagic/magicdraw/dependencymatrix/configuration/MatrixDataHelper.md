# JAVA OPENAPI: MatrixDataHelper (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/configuration/MatrixDataHelper.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/configuration/MatrixDataHelper.html`
- source_sha256: `bb8eb3083804a326b5cb18748d0ebaf20bd9e3bf60e35001bf2c27a0d8c3ae47`
- captured_utc: `2026-07-14T16:57:53.257483+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.configuration](package-summary.html)

## Class MatrixDataHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.configuration.MatrixDataHelper

@OpenApiAllpublic classMatrixDataHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Helper used to get and manage Dependency Matrix Data from external plugins.
 
 Please pay attention, that if the Dependency Matrix diagram is not opened, its data is not collected and
 dependency matrix component needs to be built.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MatrixDataHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MatrixData](../datamodel/MatrixData.html)`
`[buildMatrix](#buildMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)`
Collects all data for provided matrix data component.
`static [MatrixData](../datamodel/MatrixData.html)`
`[getMatrixData](#getMatrixData(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)`
Gets the matrix diagram data object.
`static boolean`
`[isEditable](#isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix,
 [ElementNode](../datamodel/ElementNode.html) rowNode,
 [ElementNode](../datamodel/ElementNode.html) columnNode)`
Checks whether the relation can be created/deleted between row node and column node depending on matrix dependency criteria.
`static boolean`
`[isRebuildNeeded](#isRebuildNeeded(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)`
Checks if the current Dependency Matrix data is up to date or even are collected.
`static void`
`[refreshMatrix](#refreshMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)`
Immediately rebuilds dependency matrix
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MatrixDataHelper
public MatrixDataHelper()
 ============ METHOD DETAIL ========== 
Method Details
getMatrixData
@CheckForNullpublic static [MatrixData](../datamodel/MatrixData.html) getMatrixData([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)
Gets the matrix diagram data object. Pleas note, that if the matrix is not already opened, it will be witout data.
 If you need to manage not opened matrices use `MatrixDataHelper.buildMatrix()` method
Parameters:
`matrix` - diagram of the dependency matrix
Returns:
Dependency Matrix data component for specified diagram or `null` if this
 dependency matrix was not found. Before using data make sure if the matrix data is up to date
 and does not need to be rebuilt
buildMatrix
@CheckForNullpublic static [MatrixData](../datamodel/MatrixData.html) buildMatrix([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)
Collects all data for provided matrix data component. This may be CPU/Time intensive task,
 so use it only in cases, when not opened matrix diagrams have to be used
Parameters:
`matrix` - Dependency Matrix diagram instance
Returns:
Dependency Matrix data component for specified diagram or `null` if this
 dependency matrix was not found
isRebuildNeeded
public static boolean isRebuildNeeded([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)
Checks if the current Dependency Matrix data is up to date or even are collected. If this method
 returns `true` you need to call `MatrixDataHelper.buildMatrix()` in order to
 get correct data
Parameters:
`matrix` - Dependency Matrix diagram instance
Returns:
`true` if rebuild is required
refreshMatrix
public static void refreshMatrix([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix)
Immediately rebuilds dependency matrix
Parameters:
`matrix` - diagram element of dependency matrix to rebuild
isEditable
public static boolean isEditable([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) matrix,
 [ElementNode](../datamodel/ElementNode.html) rowNode,
 [ElementNode](../datamodel/ElementNode.html) columnNode)
Checks whether the relation can be created/deleted between row node and column node depending on matrix dependency criteria.
Parameters:
`matrix` - diagram element of dependency matrix
`rowNode` - row node that needs to be checked
`columnNode` - column node that needs to be checked
Returns:
whether the relation can be created/deleted between given row/column nodes

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.configuration</a></div>
<h1 class="title" title="Class MatrixDataHelper">Class MatrixDataHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.configuration.MatrixDataHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MatrixDataHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helper used to get and manage Dependency Matrix Data from external plugins.
 <p></p>
 Please pay attention, that if the Dependency Matrix diagram is not opened, its data is not collected and
 dependency matrix component needs to be built.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MatrixDataHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../datamodel/MatrixData.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel">MatrixData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#buildMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">buildMatrix</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all data for provided matrix data component.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../datamodel/MatrixData.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel">MatrixData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMatrixData(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getMatrixData</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the matrix diagram data object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">isEditable</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix,
 <a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> rowNode,
 <a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> columnNode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the relation can be created/deleted between row node and column node depending on matrix dependency criteria.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRebuildNeeded(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">isRebuildNeeded</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if the current Dependency Matrix data is up to date or even are collected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#refreshMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">refreshMatrix</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Immediately rebuilds dependency matrix</div>
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
<h3>MatrixDataHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MatrixDataHelper</span>()</div>
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
<section class="detail" id="getMatrixData(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getMatrixData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../datamodel/MatrixData.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel">MatrixData</a></span> <span class="element-name">getMatrixData</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</span></div>
<div class="block">Gets the matrix diagram data object. Pleas note, that if the matrix is not already opened, it will be witout data.
 If you need to manage not opened matrices use <code>MatrixDataHelper.buildMatrix()</code> method</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - diagram of the dependency matrix</dd>
<dt>Returns:</dt>
<dd>Dependency Matrix data component for specified diagram or <code>null</code> if this
         dependency matrix was not found. Before using data make sure if the matrix data is up to date
         and does not need to be rebuilt</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="buildMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>buildMatrix</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../datamodel/MatrixData.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel">MatrixData</a></span> <span class="element-name">buildMatrix</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</span></div>
<div class="block">Collects all data for provided matrix data component. This may be CPU/Time intensive task,
 so use it only in cases, when not opened matrix diagrams have to be used</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - Dependency Matrix diagram instance</dd>
<dt>Returns:</dt>
<dd>Dependency Matrix data component for specified diagram or <code>null</code> if this
         dependency matrix was not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRebuildNeeded(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>isRebuildNeeded</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRebuildNeeded</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</span></div>
<div class="block">Checks if the current Dependency Matrix data is up to date or even are collected. If this method
 returns <code>true</code> you need to call <code>MatrixDataHelper.buildMatrix()</code> in order to
 get correct data</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - Dependency Matrix diagram instance</dd>
<dt>Returns:</dt>
<dd><code>true</code> if rebuild is required</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refreshMatrix(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>refreshMatrix</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">refreshMatrix</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix)</span></div>
<div class="block">Immediately rebuilds dependency matrix</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - diagram element of dependency matrix to rebuild</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>isEditable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEditable</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> matrix,
 <a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> rowNode,
 <a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> columnNode)</span></div>
<div class="block">Checks whether the relation can be created/deleted between row node and column node depending on matrix dependency criteria.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matrix</code> - diagram element of dependency matrix</dd>
<dd><code>rowNode</code> - row node that needs to be checked</dd>
<dd><code>columnNode</code> - column node that needs to be checked</dd>
<dt>Returns:</dt>
<dd>whether the relation can be created/deleted between given row/column nodes</dd>
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
