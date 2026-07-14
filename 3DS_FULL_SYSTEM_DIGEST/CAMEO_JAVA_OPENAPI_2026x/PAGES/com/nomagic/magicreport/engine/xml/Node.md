# JAVA OPENAPI: Node (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/xml/Node.html
- source_path: `com/nomagic/magicreport/engine/xml/Node.html`
- source_sha256: `8042cc90dbf160d8e7087faaacc6f9afa6a65a4b33413bfbf536d206f2ffd9e4`
- captured_utc: `2026-07-14T16:58:38.170295+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.xml](package-summary.html)

## Interface Node

All Known Implementing Classes:
`[ElementNode](ElementNode.html)`, `[TextNode](TextNode.html)`

@OpenApiAllpublic interfaceNode

The Node interface is the primary data type for the entire Document Object Model. It represents a single node
 in the document tree.

Since:
Jun 1, 2009

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[appendChild](#appendChild(com.nomagic.magicreport.engine.xml.Node))([Node](Node.html) e)`
Adds the node newChild to the end of the list of children of this node.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)>`
`[getChildNodes](#getChildNodes())()`
Return a child.
`[Node](Node.html)`
`[getParentNode](#getParentNode())()`
Return the parent of this node.
`void`
`[insertBefore](#insertBefore(com.nomagic.magicreport.engine.xml.Node,int))([Node](Node.html) newChild,
 int index)`
Inserts the node newChild before the child index.
`[Node](Node.html)`
`[removeChild](#removeChild(com.nomagic.magicreport.engine.xml.Node))([Node](Node.html) oldChild)`
Removes the child node indicated by oldChild from the list of children, and returns it.
`void`
`[setParentNode](#setParentNode(com.nomagic.magicreport.engine.xml.Node))([Node](Node.html) e)`
Set a parent of this node.

============ METHOD DETAIL ========== 
Method Details
setParentNode
void setParentNode([Node](Node.html) e)
Set a parent of this node.
Parameters:
`e` - a node.
getParentNode
[Node](Node.html) getParentNode()
Return the parent of this node.
Returns:
the parent
appendChild
void appendChild([Node](Node.html) e)
Adds the node newChild to the end of the list of children of this node.
Parameters:
`e` - a child element
getChildNodes
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)> getChildNodes()
Return a child.
Returns:
the child
insertBefore
void insertBefore([Node](Node.html) newChild,
 int index)
Inserts the node newChild before the child index.
Parameters:
`newChild` - the node to insert
`index` - the reference child index
removeChild
[Node](Node.html) removeChild([Node](Node.html) oldChild)
Removes the child node indicated by oldChild from the list of children, and returns it.
Parameters:
`oldChild` - The node being removed.
Returns:
the node removed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.xml</a></div>
<h1 class="title" title="Interface Node">Interface Node</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ElementNode.html" title="class in com.nomagic.magicreport.engine.xml">ElementNode</a></code>, <code><a href="TextNode.html" title="class in com.nomagic.magicreport.engine.xml">TextNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Node</span></div>
<div class="block">The Node interface is the primary data type for the entire Document Object Model. It represents a single node
 in the document tree.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 1, 2009</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#appendChild(com.nomagic.magicreport.engine.xml.Node)">appendChild</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds the node newChild to the end of the list of children of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChildNodes()">getChildNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a child.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentNode()">getParentNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the parent of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#insertBefore(com.nomagic.magicreport.engine.xml.Node,int)">insertBefore</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> newChild,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Inserts the node newChild before the child index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeChild(com.nomagic.magicreport.engine.xml.Node)">removeChild</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> oldChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes the child node indicated by oldChild from the list of children, and returns it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setParentNode(com.nomagic.magicreport.engine.xml.Node)">setParentNode</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set a parent of this node.</div>
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
<section class="detail" id="setParentNode(com.nomagic.magicreport.engine.xml.Node)">
<h3>setParentNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setParentNode</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</span></div>
<div class="block">Set a parent of this node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - a node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentNode()">
<h3>getParentNode</h3>
<div class="member-signature"><span class="return-type"><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></span> <span class="element-name">getParentNode</span>()</div>
<div class="block">Return the parent of this node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendChild(com.nomagic.magicreport.engine.xml.Node)">
<h3>appendChild</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">appendChild</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</span></div>
<div class="block">Adds the node newChild to the end of the list of children of this node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - a child element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildNodes()">
<h3>getChildNodes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt;</span> <span class="element-name">getChildNodes</span>()</div>
<div class="block">Return a child.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertBefore(com.nomagic.magicreport.engine.xml.Node,int)">
<h3>insertBefore</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">insertBefore</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> newChild,
 int index)</span></div>
<div class="block">Inserts the node newChild before the child index.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newChild</code> - the node to insert</dd>
<dd><code>index</code> - the reference child index</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeChild(com.nomagic.magicreport.engine.xml.Node)">
<h3>removeChild</h3>
<div class="member-signature"><span class="return-type"><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></span> <span class="element-name">removeChild</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> oldChild)</span></div>
<div class="block">Removes the child node indicated by oldChild from the list of children, and returns it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldChild</code> - The node being removed.</dd>
<dt>Returns:</dt>
<dd>the node removed.</dd>
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
