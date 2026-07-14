# JAVA OPENAPI: ElementNode (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/xml/ElementNode.html
- source_path: `com/nomagic/magicreport/engine/xml/ElementNode.html`
- source_sha256: `01e3a5eb5770726f3771df46051dae93a04aaee631136148d6058c802fa93377`
- captured_utc: `2026-07-14T16:46:13.681982+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.xml](package-summary.html)

## Class ElementNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.xml.ElementNode

All Implemented Interfaces:
`[Node](Node.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classElementNode
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Node](Node.html), [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

The Element represents an element in XML document.

Since:
Jun 1, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.xml.ElementNode)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ElementNode](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Create an element with out associated attribute.
`[ElementNode](#%3Cinit%3E(java.lang.String,org.xml.sax.Attributes))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)`
Create an element with associated attributes.
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
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getACustomProperty](#getACustomProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getAttribute](#getAttribute(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)`
Retrieves an attribute value by name.
`[Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html)`
`[getAttributes](#getAttributes())()`
Retrieves XML attributes.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)>`
`[getChildNodes](#getChildNodes())()`
Return a child.
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getContent](#getContent())()`
Return a content.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)>`
`[getCustomProperty](#getCustomProperty())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEndText](#getEndText())()`
Return an end text.
`[Node](Node.html)`
`[getFirstChild](#getFirstChild())()`
The first child of this node.
`[Node](Node.html)`
`[getLastChild](#getLastChild())()`
The last child of this node.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Return a name.
`[Node](Node.html)`
`[getParentNode](#getParentNode())()`
Return the parent of this node.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getStartText](#getStartText())()`
Return a start text.
`boolean`
`[hasTextContent](#hasTextContent(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)> childNodes)`
Return true when `childNodes` contains at least one text node.
`void`
`[insertBefore](#insertBefore(com.nomagic.magicreport.engine.xml.Node,int))([Node](Node.html) newChild,
 int index)`
Inserts the node newChild before the child index.
`[Node](Node.html)`
`[removeChild](#removeChild(com.nomagic.magicreport.engine.xml.Node))([Node](Node.html) oldChild)`
Removes the child node indicated by oldChild from the list of children, and returns it.
`void`
`[setACustomProperty](#setACustomProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`

`void`
`[setAttribute](#setAttribute(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrValue)`
Adds a new attribute.
`void`
`[setAttribute](#setAttribute(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Adds a new attribute.
`void`
`[setCustomProperty](#setCustomProperty(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> customProperty)`

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
ElementNode
public ElementNode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Create an element with out associated attribute.
Parameters:
`name` - an element name.
ElementNode
public ElementNode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) attributes)
Create an element with associated attributes.
Parameters:
`name` - an element name
`attributes` - attributes
 ============ METHOD DETAIL ========== 
Method Details
getContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getContent()
Return a content.
Returns:
the content
hasTextContent
public boolean hasTextContent([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)> childNodes)
Return true when `childNodes` contains at least one text node.
Parameters:
`childNodes` - collection of child node
Returns:
true when `childNodes` contains at least one text node; otherwise false.
appendContent
public void appendContent(char[] str,
 int offset,
 int len)
Append a content.
Parameters:
`str` - the characters to be appended.
`offset` - the index of the first char to append.
`len` - the number of chars to append.
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Return a name.
Returns:
the name
getStartText
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getStartText()
Return a start text.
Returns:
the startText
getEndText
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEndText()
Return an end text.
Returns:
the endText
setAttribute
public void setAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) uri,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) localName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Adds a new attribute. If an attribute with that name is already present in the element, its value is changed
 to be that of the value parameter.
Parameters:
`uri` - The Namespace URI, or the empty string if none is available or Namespace processing is not being
 performed.
`localName` - The local name, or the empty string if Namespace processing is not being performed.
`qName` - The qualified (prefixed) name, or the empty string if qualified names are not available.
`type` - The attribute type as a string.
`value` - The attribute value.
Throws:
`[DOMException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/DOMException.html)` - NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
getAttribute
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) qName)
Retrieves an attribute value by name.
Parameters:
`qName` - The name of the attribute to retrieve.
Returns:
The attribute value as a string, or the empty string.
getAttributes
public [Attributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html) getAttributes()
Retrieves XML attributes.
Returns:
The XML attributes.
setAttribute
public void setAttribute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) attrValue)
 throws [DOMException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/DOMException.html)
Adds a new attribute. If an attribute with that name is already present in the element, its value is changed
 to be that of the value parameter.
Parameters:
`attrName` - The name of the attribute to create or alter.
`attrValue` - Value to set in string form.
Throws:
`[DOMException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/DOMException.html)` - NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Return string represents this object.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a string represents this object
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
getChildNodes
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Node](Node.html)> getChildNodes()
Return a child.
Specified by:
`[getChildNodes](Node.html#getChildNodes())` in interface `[Node](Node.html)`
Returns:
the child
getLastChild
public [Node](Node.html) getLastChild()
The last child of this node. If there is no such node, this returns null.
Returns:
last child of this node.
getFirstChild
public [Node](Node.html) getFirstChild()
The first child of this node. If there is no such node, this returns null.
Returns:
first child of this node.
getParentNode
public [Node](Node.html) getParentNode()
Return the parent of this node.
Specified by:
`[getParentNode](Node.html#getParentNode())` in interface `[Node](Node.html)`
Returns:
the parent
setParentNode
public void setParentNode([Node](Node.html) e)
Set a parent of this node.
Specified by:
`[setParentNode](Node.html#setParentNode(com.nomagic.magicreport.engine.xml.Node))` in interface `[Node](Node.html)`
Parameters:
`e` - a node.
getCustomProperty
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> getCustomProperty()
setCustomProperty
public void setCustomProperty([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> customProperty)
getACustomProperty
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getACustomProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
setACustomProperty
public void setACustomProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.xml</a></div>
<h1 class="title" title="Class ElementNode">Class ElementNode</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.xml.ElementNode</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ElementNode</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">The Element represents an element in XML document.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 1, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.xml.ElementNode">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">ElementNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color">
<div class="block">Create an element with out associated attribute.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,org.xml.sax.Attributes)">ElementNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create an element with associated attributes.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getACustomProperty(java.lang.String)">getACustomProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttribute(java.lang.String)">getAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves an attribute value by name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttributes()">getAttributes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves XML attributes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildNodes()">getChildNodes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a child.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContent()">getContent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a content.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomProperty()">getCustomProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndText()">getEndText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an end text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstChild()">getFirstChild</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The first child of this node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastChild()">getLastChild</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The last child of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentNode()">getParentNode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the parent of this node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStartText()">getStartText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a start text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasTextContent(java.util.Collection)">hasTextContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt; childNodes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return true when <code>childNodes</code> contains at least one text node.</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setACustomProperty(java.lang.String,java.lang.Object)">setACustomProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttribute(java.lang.String,java.lang.String)">setAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new attribute.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttribute(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">setAttribute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a new attribute.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomProperty(java.util.Map)">setCustomProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; customProperty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>ElementNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Create an element with out associated attribute.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - an element name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,org.xml.sax.Attributes)">
<h3>ElementNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElementNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a> attributes)</span></div>
<div class="block">Create an element with associated attributes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - an element name</dd>
<dd><code>attributes</code> - attributes</dd>
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
<section class="detail" id="hasTextContent(java.util.Collection)">
<h3>hasTextContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasTextContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a>&gt; childNodes)</span></div>
<div class="block">Return true when <code>childNodes</code> contains at least one text node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>childNodes</code> - collection of child node</dd>
<dt>Returns:</dt>
<dd>true when <code>childNodes</code> contains at least one text node; otherwise false.</dd>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Return a name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStartText()">
<h3>getStartText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStartText</span>()</div>
<div class="block">Return a start text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the startText</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndText()">
<h3>getEndText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEndText</span>()</div>
<div class="block">Return an end text.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the endText</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAttribute(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>setAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> localName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Adds a new attribute. If an attribute with that name is already present in the element, its value is changed
 to be that of the value parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - The Namespace URI, or the empty string if none is available or Namespace processing is not being
           performed.</dd>
<dd><code>localName</code> - The local name, or the empty string if Namespace processing is not being performed.</dd>
<dd><code>qName</code> - The qualified (prefixed) name, or the empty string if qualified names are not available.</dd>
<dd><code>type</code> - The attribute type as a string.</dd>
<dd><code>value</code> - The attribute value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/DOMException.html" title="class or interface in org.w3c.dom">DOMException</a></code> - NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttribute(java.lang.String)">
<h3>getAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> qName)</span></div>
<div class="block">Retrieves an attribute value by name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>qName</code> - The name of the attribute to retrieve.</dd>
<dt>Returns:</dt>
<dd>The attribute value as a string, or the empty string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttributes()">
<h3>getAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/Attributes.html" title="class or interface in org.xml.sax">Attributes</a></span> <span class="element-name">getAttributes</span>()</div>
<div class="block">Retrieves XML attributes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The XML attributes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAttribute(java.lang.String,java.lang.String)">
<h3>setAttribute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttribute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> attrValue)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/DOMException.html" title="class or interface in org.w3c.dom">DOMException</a></span></div>
<div class="block">Adds a new attribute. If an attribute with that name is already present in the element, its value is changed
 to be that of the value parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attrName</code> - The name of the attribute to create or alter.</dd>
<dd><code>attrValue</code> - Value to set in string form.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/DOMException.html" title="class or interface in org.w3c.dom">DOMException</a></code> - NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.</dd>
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
<section class="detail" id="getLastChild()">
<h3>getLastChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></span> <span class="element-name">getLastChild</span>()</div>
<div class="block">The last child of this node. If there is no such node, this returns null.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last child of this node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstChild()">
<h3>getFirstChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Node.html" title="interface in com.nomagic.magicreport.engine.xml">Node</a></span> <span class="element-name">getFirstChild</span>()</div>
<div class="block">The first child of this node. If there is no such node, this returns null.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first child of this node.</dd>
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
<section class="detail" id="getCustomProperty()">
<h3>getCustomProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getCustomProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCustomProperty(java.util.Map)">
<h3>setCustomProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; customProperty)</span></div>
</section>
</li>
<li>
<section class="detail" id="getACustomProperty(java.lang.String)">
<h3>getACustomProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getACustomProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
</section>
</li>
<li>
<section class="detail" id="setACustomProperty(java.lang.String,java.lang.Object)">
<h3>setACustomProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setACustomProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
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
