# JAVA OPENAPI: MatrixData (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/dependencymatrix/datamodel/MatrixData.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/MatrixData.html`
- source_sha256: `118b24a10e5eb42352c206a69f443f3d25ff150fe203d5e53648235c0a577c5b`
- captured_utc: `2026-07-14T16:51:16.657142+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel](package-summary.html)

## Interface MatrixData

@OpenApiAllpublic interfaceMatrixData
Interface used to access dependency matrix data structure.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getColumnElements](#getColumnElements())()`
Returns only model elements used in columns without group elements
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)>`
`[getColumnNodes](#getColumnNodes())()`
Returns all column nodes used in matrix
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)>`
`[getColumnNodes](#getColumnNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return all column nodes which contain specified element
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRowElements](#getRowElements())()`
Returns only model elements used in rows without group elements
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)>`
`[getRowNodes](#getRowNodes())()`
Returns all row nodes used in matrix
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)>`
`[getRowNodes](#getRowNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Return all row nodes which contain specified element
`[AbstractMatrixCell](cell/AbstractMatrixCell.html)`
`[getValue](#getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](ElementNode.html) row,
 [ElementNode](ElementNode.html) column)`
Get Matrix Cell value from the model
`[AbstractMatrixCell](cell/AbstractMatrixCell.html)`
`[getValue](#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) row,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) column)`
Deprecated.
use [`getValue(ElementNode, ElementNode)`](#getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))
`boolean`
`[isEmpty](#isEmpty())()`
If there is any data inside this dependency matrix

============ METHOD DETAIL ========== 
Method Details
getRowElements
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRowElements()
Returns only model elements used in rows without group elements
Returns:
row elements
getRowNodes
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)> getRowNodes()
Returns all row nodes used in matrix
Returns:
row element nodes
getRowNodes
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)> getRowNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return all row nodes which contain specified element
Parameters:
`element` - to search for row nodes
Returns:
all of element row nodes used in matrix
getColumnElements
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getColumnElements()
Returns only model elements used in columns without group elements
Returns:
column elements
getColumnNodes
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)> getColumnNodes()
Returns all column nodes used in matrix
Returns:
column element nodes
getColumnNodes
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](ElementNode.html)> getColumnNodes([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Return all column nodes which contain specified element
Parameters:
`element` - to search for column nodes
Returns:
all of element column nodes used in matrix
getValue
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)[AbstractMatrixCell](cell/AbstractMatrixCell.html) getValue([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) row,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) column)
Deprecated.
use [`getValue(ElementNode, ElementNode)`](#getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))
getValue
[AbstractMatrixCell](cell/AbstractMatrixCell.html) getValue([ElementNode](ElementNode.html) row,
 [ElementNode](ElementNode.html) column)
Get Matrix Cell value from the model
Parameters:
`row` - row node
`column` - column node
Returns:
matrix data cell
isEmpty
boolean isEmpty()
If there is any data inside this dependency matrix
Returns:
`true` if empty

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel</a></div>
<h1 class="title" title="Interface MatrixData">Interface MatrixData</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MatrixData</span></div>
<div class="block">Interface used to access dependency matrix data structure.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getColumnElements()">getColumnElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns only model elements used in columns without group elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getColumnNodes()">getColumnNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all column nodes used in matrix</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getColumnNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getColumnNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return all column nodes which contain specified element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRowElements()">getRowElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns only model elements used in rows without group elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRowNodes()">getRowNodes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all row nodes used in matrix</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRowNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getRowNodes</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return all row nodes which contain specified element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">getValue</a><wbr/>(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get Matrix Cell value from the model</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a href="cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getValue</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> row,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> column)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)"><code>getValue(ElementNode, ElementNode)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If there is any data inside this dependency matrix</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="getRowElements()">
<h3>getRowElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRowElements</span>()</div>
<div class="block">Returns only model elements used in rows without group elements</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>row elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowNodes()">
<h3>getRowNodes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getRowNodes</span>()</div>
<div class="block">Returns all row nodes used in matrix</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>row element nodes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRowNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getRowNodes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getRowNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return all row nodes which contain specified element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - to search for row nodes</dd>
<dt>Returns:</dt>
<dd>all of element row nodes used in matrix</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnElements()">
<h3>getColumnElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getColumnElements</span>()</div>
<div class="block">Returns only model elements used in columns without group elements</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>column elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNodes()">
<h3>getColumnNodes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getColumnNodes</span>()</div>
<div class="block">Returns all column nodes used in matrix</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>column element nodes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNodes(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getColumnNodes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt;</span> <span class="element-name">getColumnNodes</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Return all column nodes which contain specified element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - to search for column nodes</dd>
<dt>Returns:</dt>
<dd>all of element column nodes used in matrix</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getValue</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type"><a href="cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> row,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> column)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)"><code>getValue(ElementNode, ElementNode)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getValue(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>getValue</h3>
<div class="member-signature"><span class="return-type"><a href="cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a></span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column)</span></div>
<div class="block">Get Matrix Cell value from the model</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>row</code> - row node</dd>
<dd><code>column</code> - column node</dd>
<dt>Returns:</dt>
<dd>matrix data cell</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
<div class="block">If there is any data inside this dependency matrix</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if empty</dd>
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
