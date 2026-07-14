# JAVA OPENAPI: TextNode (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/xml/TextNode.html
- source_path: `com/nomagic/magicreport/engine/xml/TextNode.html`
- source_sha256: `d553cdfa99a322d1d0c38b40d3be53705667d8d99a114e39ebeadfd79e09d1c3`
- captured_utc: `2026-07-14T16:58:38.197295+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.xml](package-summary.html)

## Class TextNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.xml.TextNode

All Implemented Interfaces:
`[Node](Node.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classTextNode
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Node](Node.html), [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

The Text node represents the textual content (termed character data in XML) of an Element or Attribute.

Since:
Jun 1, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.xml.TextNode)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TextNode](#%3Cinit%3E())()`
Create a text node.
`[TextNode](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Create a text node with text content.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[appendChild](#appendChild(com.nomagic.magicreport.engine.xml.Node))([Node](Node.html) e)`
Adds the node newChild to the end of the list of children of this node.
`void`
`[appendContent](#appendContent(char%5B%5D,int,int))(char[] str,
 int offset,
 int len)`
Append a content.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)>`
`[getChildNodes](#getChildNodes())()`
Return a child.
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getContent](#getContent())()`
Return a content.
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
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Return string represents this object.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TextNode
public TextNode()
Create a text node.
TextNode
public TextNode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Create a text node with text content.
Parameters:
`text` - text content.
 ============ METHOD DETAIL ========== 
Method Details
getContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getContent()
Return a content.
Returns:
the content
appendContent
public void appendContent(char[] str,
 int offset,
 int len)
Append a content.
Parameters:
`str` - the characters to be appended.
`offset` - the index of the first char to append.
`len` - the number of chars to append.
getChildNodes
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)> getChildNodes()
Return a child.
Specified by:
`[getChildNodes](Node.html#getChildNodes())` in interface `[Node](Node.html)`
Returns:
the child
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Return string represents this object.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a string represents this object
setParentNode
public void setParentNode([Node](Node.html) e)
Set a parent of this node.
Specified by:
`[setParentNode](Node.html#setParentNode(com.nomagic.magicreport.engine.xml.Node))` in interface `[Node](Node.html)`
Parameters:
`e` - a node.
getParentNode
public [Node](Node.html) getParentNode()
Return the parent of this node.
Specified by:
`[getParentNode](Node.html#getParentNode())` in interface `[Node](Node.html)`
Returns:
the parent
appendChild
public void appendChild([Node](Node.html) e)
Adds the node newChild to the end of the list of children of this node.
Specified by:
`[appendChild](Node.html#appendChild(com.nomagic.magicreport.engine.xml.Node))` in interface `[Node](Node.html)`
Parameters:
`e` - a child element
removeChild
public [Node](Node.html) removeChild([Node](Node.html) oldChild)
Removes the child node indicated by oldChild from the list of children, and returns it.
Specified by:
`[removeChild](Node.html#removeChild(com.nomagic.magicreport.engine.xml.Node))` in interface `[Node](Node.html)`
Parameters:
`oldChild` - The node being removed.
Returns:
the node removed.
insertBefore
public void insertBefore([Node](Node.html) newChild,
 int index)
Inserts the node newChild before the child index.
Specified by:
`[insertBefore](Node.html#insertBefore(com.nomagic.magicreport.engine.xml.Node,int))` in interface `[Node](Node.html)`
Parameters:
`newChild` - the node to insert
`index` - the reference child index

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.xml</a></div>
<h1 class="title" title="Class TextNode">Class TextNode</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.xml.TextNode</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TextNode</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">The Text node represents the textual content (termed character data in XML) of an Element or Attribute.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 1, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.xml.TextNode">Serialized Form</a></li>
</ul>
</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TextNode</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create a text node.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">TextNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a text node with text content.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendChild(com.nomagic.magicreport.engine.xml.Node)">appendChild</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the node newChild to the end of the list of children of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#appendContent(char%5B%5D,int,int)">appendContent</a><wbr/>(char[] str,
 int offset,
 int len)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Append a content.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildNodes()">getChildNodes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a child.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContent()">getContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a content.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentNode()">getParentNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the parent of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#insertBefore(com.nomagic.magicreport.engine.xml.Node,int)">insertBefore</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> newChild,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Inserts the node newChild before the child index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeChild(com.nomagic.magicreport.engine.xml.Node)">removeChild</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> oldChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the child node indicated by oldChild from the list of children, and returns it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentNode(com.nomagic.magicreport.engine.xml.Node)">setParentNode</a><wbr/>(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a parent of this node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return string represents this object.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>TextNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TextNode</span>()</div>
<div class="block">Create a text node.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>TextNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TextNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Create a text node with text content.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text content.</dd>
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
<section class="detail" id="getContent()">
<h3>getContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getContent</span>()</div>
<div class="block">Return a content.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the content</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendContent(char[],int,int)">
<h3>appendContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">appendContent</span><wbr/><span class="parameters">(char[] str,
 int offset,
 int len)</span></div>
<div class="block">Append a content.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - the characters to be appended.</dd>
<dd><code>offset</code> - the index of the first char to append.</dd>
<dd><code>len</code> - the number of chars to append.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildNodes()">
<h3>getChildNodes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt;</span> <span class="element-name">getChildNodes</span>()</div>
<div class="block">Return a child.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Node.html#getChildNodes()">getChildNodes</a></code> in interface <code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></dd>
<dt>Returns:</dt>
<dd>the child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Return string represents this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a string represents this object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentNode(com.nomagic.magicreport.engine.xml.Node)">
<h3>setParentNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentNode</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</span></div>
<div class="block">Set a parent of this node.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Node.html#setParentNode(com.nomagic.magicreport.engine.xml.Node)">setParentNode</a></code> in interface <code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - a node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentNode()">
<h3>getParentNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></span> <span class="element-name">getParentNode</span>()</div>
<div class="block">Return the parent of this node.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Node.html#getParentNode()">getParentNode</a></code> in interface <code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></dd>
<dt>Returns:</dt>
<dd>the parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="appendChild(com.nomagic.magicreport.engine.xml.Node)">
<h3>appendChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">appendChild</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> e)</span></div>
<div class="block">Adds the node newChild to the end of the list of children of this node.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Node.html#appendChild(com.nomagic.magicreport.engine.xml.Node)">appendChild</a></code> in interface <code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - a child element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeChild(com.nomagic.magicreport.engine.xml.Node)">
<h3>removeChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></span> <span class="element-name">removeChild</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> oldChild)</span></div>
<div class="block">Removes the child node indicated by oldChild from the list of children, and returns it.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Node.html#removeChild(com.nomagic.magicreport.engine.xml.Node)">removeChild</a></code> in interface <code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></dd>
<dt>Parameters:</dt>
<dd><code>oldChild</code> - The node being removed.</dd>
<dt>Returns:</dt>
<dd>the node removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertBefore(com.nomagic.magicreport.engine.xml.Node,int)">
<h3>insertBefore</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">insertBefore</span><wbr/><span class="parameters">(<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a> newChild,
 int index)</span></div>
<div class="block">Inserts the node newChild before the child index.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Node.html#insertBefore(com.nomagic.magicreport.engine.xml.Node,int)">insertBefore</a></code> in interface <code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></dd>
<dt>Parameters:</dt>
<dd><code>newChild</code> - the node to insert</dd>
<dd><code>index</code> - the reference child index</dd>
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
