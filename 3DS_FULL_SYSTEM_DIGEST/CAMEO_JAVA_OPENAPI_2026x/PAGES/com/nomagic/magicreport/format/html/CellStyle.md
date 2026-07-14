# JAVA OPENAPI: CellStyle (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/CellStyle.html
- source_path: `com/nomagic/magicreport/format/html/CellStyle.html`
- source_sha256: `65779899eaa58a44030cc86677103aa1742047215352e070c08c5fb7c77e886d`
- captured_utc: `2026-07-14T16:58:38.687298+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class CellStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.text.SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
[com.nomagic.magicreport.format.html.SimpleStyle](SimpleStyle.html)
com.nomagic.magicreport.format.html.CellStyle

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)`, `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`, `[Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)`

@OpenApiAllpublic classCellStyle
extends [SimpleStyle](SimpleStyle.html)

A collection of attributes, represent cell styles.

Since:
Jun 1, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.format.html.CellStyle)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ALIGN](#ALIGN)`
Constants for align attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CELL_BORDER](#CELL_BORDER)`
Constants for cellborder attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CELL_PADDING](#CELL_PADDING)`
Constants for cellpadding attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLOR](#COLOR)`
Constants for color attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLSPAN](#COLSPAN)`
Constants for colspan attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MARGIN_LEFT](#MARGIN_LEFT)`
Constants for marginLeft attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MARGIN_RIGHT](#MARGIN_RIGHT)`
Constants for marginRight attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROWSPAN](#ROWSPAN)`
Constants for rowspan attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[VALIGN](#VALIGN)`
Constants for valign attribute.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[WIDTH](#WIDTH)`
Constants for width attribute.
Fields inherited from class com.nomagic.magicreport.format.html.[SimpleStyle](SimpleStyle.html)
`[changeEvent](SimpleStyle.html#changeEvent), [listenerList](SimpleStyle.html#listenerList)`
Fields inherited from class javax.swing.text.[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
`[EMPTY](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#EMPTY)`
Fields inherited from interface javax.swing.text.[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)
`[NameAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#NameAttribute), [ResolveAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#ResolveAttribute)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CellStyle](#%3Cinit%3E())()`
Creates a new style, with a null name and parent.
`[CellStyle](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Creates a new style.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Compares this object to the specified object.
`int`
`[hashCode](#hashCode())()`
Returns a hashcode for this set of attributes.
`boolean`
`[isHeader](#isHeader())()`
Return a header.
`void`
`[setHeader](#setHeader(boolean))(boolean header)`
Set a header.
Methods inherited from class com.nomagic.magicreport.format.html.[SimpleStyle](SimpleStyle.html)
`[addAttribute](SimpleStyle.html#addAttribute(java.lang.Object,java.lang.Object)), [addAttributes](SimpleStyle.html#addAttributes(javax.swing.text.AttributeSet)), [addChangeListener](SimpleStyle.html#addChangeListener(javax.swing.event.ChangeListener)), [fireStateChanged](SimpleStyle.html#fireStateChanged()), [getChangeListeners](SimpleStyle.html#getChangeListeners()), [getListeners](SimpleStyle.html#getListeners(java.lang.Class)), [getName](SimpleStyle.html#getName()), [removeAttribute](SimpleStyle.html#removeAttribute(java.lang.Object)), [removeAttributes](SimpleStyle.html#removeAttributes(java.util.Enumeration)), [removeAttributes](SimpleStyle.html#removeAttributes(javax.swing.text.AttributeSet)), [removeChangeListener](SimpleStyle.html#removeChangeListener(javax.swing.event.ChangeListener)), [setName](SimpleStyle.html#setName(java.lang.String))`
Methods inherited from class javax.swing.text.[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#clone()), [containsAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)), [containsAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)), [copyAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#copyAttributes()), [getAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttribute(java.lang.Object)), [getAttributeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeCount()), [getAttributeNames](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeNames()), [getResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getResolveParent()), [isDefined](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isDefined(java.lang.Object)), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEmpty()), [isEqual](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEqual(javax.swing.text.AttributeSet)), [setResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.text.[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)
`[containsAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)), [containsAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)), [copyAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#copyAttributes()), [getAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttribute(java.lang.Object)), [getAttributeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeCount()), [getAttributeNames](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeNames()), [getResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getResolveParent()), [isDefined](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isDefined(java.lang.Object)), [isEqual](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isEqual(javax.swing.text.AttributeSet))`
Methods inherited from interface javax.swing.text.[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)
`[setResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet))`

============ FIELD DETAIL =========== 
Field Details
ALIGN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ALIGN
Constants for align attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.ALIGN)
VALIGN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) VALIGN
Constants for valign attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.VALIGN)
COLOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLOR
Constants for color attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.COLOR)
ROWSPAN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROWSPAN
Constants for rowspan attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.ROWSPAN)
COLSPAN
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLSPAN
Constants for colspan attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.COLSPAN)
WIDTH
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) WIDTH
Constants for width attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.WIDTH)
MARGIN_LEFT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MARGIN_LEFT
Constants for marginLeft attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.MARGIN_LEFT)
MARGIN_RIGHT
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MARGIN_RIGHT
Constants for marginRight attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.MARGIN_RIGHT)
CELL_BORDER
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CELL_BORDER
Constants for cellborder attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.CELL_BORDER)
CELL_PADDING
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CELL_PADDING
Constants for cellpadding attribute.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.CELL_PADDING)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CellStyle
public CellStyle()
Creates a new style, with a null name and parent.
CellStyle
public CellStyle([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Creates a new style.
Parameters:
`name` - the style name, null for unnamed
 ============ METHOD DETAIL ========== 
Method Details
isHeader
public boolean isHeader()
Return a header.
Returns:
the header
setHeader
public void setHeader(boolean header)
Set a header.
Parameters:
`header` - the header to set
hashCode
public int hashCode()
Returns a hashcode for this set of attributes.
Overrides:
`[hashCode](SimpleStyle.html#hashCode())` in class `[SimpleStyle](SimpleStyle.html)`
Returns:
a hashcode value for this set of attributes.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Compares this object to the specified object. The result is `true` if the object is an equivalent
 set of attributes.
Overrides:
`[equals](SimpleStyle.html#equals(java.lang.Object))` in class `[SimpleStyle](SimpleStyle.html)`
Parameters:
`obj` - the object to compare this attribute set with
Returns:
`true` if the objects are equal; `false` otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class CellStyle">Class CellStyle</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">javax.swing.text.SimpleAttributeSet</a>
<div class="inheritance"><a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">com.nomagic.magicreport.format.html.SimpleStyle</a>
<div class="inheritance">com.nomagic.magicreport.format.html.CellStyle</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CellStyle</span>
<span class="extends-implements">extends <a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></span></div>
<div class="block">A collection of attributes, represent cell styles.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 1, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.format.html.CellStyle">Serialized Form</a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALIGN">ALIGN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for align attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CELL_BORDER">CELL_BORDER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for cellborder attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CELL_PADDING">CELL_PADDING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for cellpadding attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLOR">COLOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for color attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COLSPAN">COLSPAN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for colspan attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MARGIN_LEFT">MARGIN_LEFT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for marginLeft attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MARGIN_RIGHT">MARGIN_RIGHT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for marginRight attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROWSPAN">ROWSPAN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for rowspan attribute.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIGN">VALIGN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constants for valign attribute.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#WIDTH">WIDTH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Constants for width attribute.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.format.html.SimpleStyle">Fields inherited from class com.nomagic.magicreport.format.html.<a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></h3>
<code><a href="SimpleStyle.html#changeEvent">changeEvent</a>, <a href="SimpleStyle.html#listenerList">listenerList</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.text.SimpleAttributeSet">Fields inherited from class javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#EMPTY" title="class or interface in javax.swing.text">EMPTY</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-javax.swing.text.AttributeSet">Fields inherited from interface javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#NameAttribute" title="class or interface in javax.swing.text">NameAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#ResolveAttribute" title="class or interface in javax.swing.text">ResolveAttribute</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CellStyle</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new style, with a null name and parent.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">CellStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new style.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compares this object to the specified object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a hashcode for this set of attributes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHeader()">isHeader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a header.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeader(boolean)">setHeader</a><wbr/>(boolean header)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a header.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.format.html.SimpleStyle">Methods inherited from class com.nomagic.magicreport.format.html.<a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></h3>
<code><a href="SimpleStyle.html#addAttribute(java.lang.Object,java.lang.Object)">addAttribute</a>, <a href="SimpleStyle.html#addAttributes(javax.swing.text.AttributeSet)">addAttributes</a>, <a href="SimpleStyle.html#addChangeListener(javax.swing.event.ChangeListener)">addChangeListener</a>, <a href="SimpleStyle.html#fireStateChanged()">fireStateChanged</a>, <a href="SimpleStyle.html#getChangeListeners()">getChangeListeners</a>, <a href="SimpleStyle.html#getListeners(java.lang.Class)">getListeners</a>, <a href="SimpleStyle.html#getName()">getName</a>, <a href="SimpleStyle.html#removeAttribute(java.lang.Object)">removeAttribute</a>, <a href="SimpleStyle.html#removeAttributes(java.util.Enumeration)">removeAttributes</a>, <a href="SimpleStyle.html#removeAttributes(javax.swing.text.AttributeSet)">removeAttributes</a>, <a href="SimpleStyle.html#removeChangeListener(javax.swing.event.ChangeListener)">removeChangeListener</a>, <a href="SimpleStyle.html#setName(java.lang.String)">setName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.text.SimpleAttributeSet">Methods inherited from class javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">SimpleAttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#clone()" title="class or interface in javax.swing.text">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing.text">containsAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">containsAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#copyAttributes()" title="class or interface in javax.swing.text">copyAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttribute(java.lang.Object)" title="class or interface in javax.swing.text">getAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeCount()" title="class or interface in javax.swing.text">getAttributeCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeNames()" title="class or interface in javax.swing.text">getAttributeNames</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getResolveParent()" title="class or interface in javax.swing.text">getResolveParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isDefined(java.lang.Object)" title="class or interface in javax.swing.text">isDefined</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEmpty()" title="class or interface in javax.swing.text">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEqual(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">isEqual</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">setResolveParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#toString()" title="class or interface in javax.swing.text">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.text.AttributeSet">Methods inherited from interface javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)" title="class or interface in javax.swing.text">containsAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">containsAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#copyAttributes()" title="class or interface in javax.swing.text">copyAttributes</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttribute(java.lang.Object)" title="class or interface in javax.swing.text">getAttribute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeCount()" title="class or interface in javax.swing.text">getAttributeCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeNames()" title="class or interface in javax.swing.text">getAttributeNames</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getResolveParent()" title="class or interface in javax.swing.text">getResolveParent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isDefined(java.lang.Object)" title="class or interface in javax.swing.text">isDefined</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isEqual(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">isEqual</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.text.MutableAttributeSet">Methods inherited from interface javax.swing.text.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html" title="class or interface in javax.swing.text">MutableAttributeSet</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)" title="class or interface in javax.swing.text">setResolveParent</a></code></div>
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
<section class="detail" id="ALIGN">
<h3>ALIGN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ALIGN</span></div>
<div class="block">Constants for align attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.ALIGN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIGN">
<h3>VALIGN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIGN</span></div>
<div class="block">Constants for valign attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.VALIGN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLOR">
<h3>COLOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLOR</span></div>
<div class="block">Constants for color attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.COLOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROWSPAN">
<h3>ROWSPAN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROWSPAN</span></div>
<div class="block">Constants for rowspan attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.ROWSPAN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLSPAN">
<h3>COLSPAN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLSPAN</span></div>
<div class="block">Constants for colspan attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.COLSPAN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WIDTH">
<h3>WIDTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">WIDTH</span></div>
<div class="block">Constants for width attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.WIDTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MARGIN_LEFT">
<h3>MARGIN_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MARGIN_LEFT</span></div>
<div class="block">Constants for marginLeft attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.MARGIN_LEFT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MARGIN_RIGHT">
<h3>MARGIN_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MARGIN_RIGHT</span></div>
<div class="block">Constants for marginRight attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.MARGIN_RIGHT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CELL_BORDER">
<h3>CELL_BORDER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CELL_BORDER</span></div>
<div class="block">Constants for cellborder attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.CELL_BORDER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CELL_PADDING">
<h3>CELL_PADDING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CELL_PADDING</span></div>
<div class="block">Constants for cellpadding attribute.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.format.html.CellStyle.CELL_PADDING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<h3>CellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CellStyle</span>()</div>
<div class="block">Creates a new style, with a null name and parent.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>CellStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CellStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Creates a new style.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the style name, null for unnamed</dd>
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
<section class="detail" id="isHeader()">
<h3>isHeader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHeader</span>()</div>
<div class="block">Return a header.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the header</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeader(boolean)">
<h3>setHeader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHeader</span><wbr/><span class="parameters">(boolean header)</span></div>
<div class="block">Set a header.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>header</code> - the header to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Returns a hashcode for this set of attributes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SimpleStyle.html#hashCode()">hashCode</a></code> in class <code><a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></code></dd>
<dt>Returns:</dt>
<dd>a hashcode value for this set of attributes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Compares this object to the specified object. The result is <code>true</code> if the object is an equivalent
 set of attributes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="SimpleStyle.html#equals(java.lang.Object)">equals</a></code> in class <code><a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the object to compare this attribute set with</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the objects are equal; <code>false</code> otherwise</dd>
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
