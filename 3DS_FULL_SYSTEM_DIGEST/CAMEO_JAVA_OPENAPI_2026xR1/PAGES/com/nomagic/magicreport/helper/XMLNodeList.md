# JAVA OPENAPI: XMLNodeList (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/helper/XMLNodeList.html
- source_path: `com/nomagic/magicreport/helper/XMLNodeList.html`
- source_sha256: `506c95fe265f5a65411da53a70ecc3b67ca11830578e0018be68fb4a8fbc15d3`
- captured_utc: `2026-07-14T16:46:14.562995+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper](package-summary.html)

## Class XMLNodeList

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.XMLNodeList

All Implemented Interfaces:
`[NodeList](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html)`

@OpenApiAllpublic classXMLNodeList
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [NodeList](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html)

The `NodeList` interface provides the abstraction of an ordered collection of nodes, without
 defining or constraining how this collection is implemented. `NodeList` objects in the DOM are live.
 The items in the `NodeList` are accessible via an integral index, starting from 0.

Since:
May 23, 2007

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[XMLNodeList](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getLength](#getLength())()`
The number of nodes in the list.
`[Node](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Node.html)`
`[item](#item(int))(int index)`
Returns the `index`th item in the collection.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
XMLNodeList
public XMLNodeList()
 ============ METHOD DETAIL ========== 
Method Details
item
public [Node](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Node.html) item(int index)
Returns the `index`th item in the collection. If `index` is greater than or equal to
 the number of nodes in the list, this returns `null`.
Specified by:
`[item](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html#item(int))` in interface `[NodeList](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html)`
Parameters:
`index` - Index into the collection.
Returns:
The node at the `index`th position in the `NodeList`, or `null` if
 that is not a valid index.
getLength
public int getLength()
The number of nodes in the list. The range of valid child node indices is 0 to `length-1`
 inclusive.
Specified by:
`[getLength](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html#getLength())` in interface `[NodeList](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html)`
Returns:
number of nodes in the list.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper</a></div>
<h1 class="title" title="Class XMLNodeList">Class XMLNodeList</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.XMLNodeList</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html" title="class or interface in org.w3c.dom">NodeList</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">XMLNodeList</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html" title="class or interface in org.w3c.dom">NodeList</a></span></div>
<div class="block">The <code>NodeList</code> interface provides the abstraction of an ordered collection of nodes, without
 defining or constraining how this collection is implemented. <code>NodeList</code> objects in the DOM are live.
 The items in the <code>NodeList</code> are accessible via an integral index, starting from 0.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 23, 2007</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">XMLNodeList</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLength()">getLength</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The number of nodes in the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Node.html" title="class or interface in org.w3c.dom">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#item(int)">item</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the <code>index</code>th item in the collection.</div>
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
<h3>XMLNodeList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XMLNodeList</span>()</div>
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
<section class="detail" id="item(int)">
<h3>item</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Node.html" title="class or interface in org.w3c.dom">Node</a></span> <span class="element-name">item</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Returns the <code>index</code>th item in the collection. If <code>index</code> is greater than or equal to
 the number of nodes in the list, this returns <code>null</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html#item(int)" title="class or interface in org.w3c.dom">item</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html" title="class or interface in org.w3c.dom">NodeList</a></code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - Index into the collection.</dd>
<dt>Returns:</dt>
<dd>The node at the <code>index</code>th position in the <code>NodeList</code>, or <code>null</code> if
         that is not a valid index.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLength()">
<h3>getLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLength</span>()</div>
<div class="block">The number of nodes in the list. The range of valid child node indices is 0 to <code>length-1</code>
 inclusive.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html#getLength()" title="class or interface in org.w3c.dom">getLength</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/NodeList.html" title="class or interface in org.w3c.dom">NodeList</a></code></dd>
<dt>Returns:</dt>
<dd>number of nodes in the list.</dd>
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
