# JAVA OPENAPI: GraphicStyle (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/GraphicStyle.html
- source_path: `com/nomagic/magicreport/format/html/GraphicStyle.html`
- source_sha256: `991f6e164560e3b194a519192784803e0acc0883ab05651bf31d46ab1c6a7cd4`
- captured_utc: `2026-07-14T16:58:38.810299+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class GraphicStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.text.SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
[com.nomagic.magicreport.format.html.SimpleStyle](SimpleStyle.html)
com.nomagic.magicreport.format.html.GraphicStyle

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)`, `[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)`, `[Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html)`

@OpenApiAllpublic classGraphicStyle
extends [SimpleStyle](SimpleStyle.html)

A collection of attributes, represent graphic styles.

Since:
Mar 04, 2011
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.format.html.GraphicStyle)

=========== FIELD SUMMARY =========== 
Field Summary
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
`[GraphicStyle](#%3Cinit%3E())()`
Creates a new style, with a null name and parent.
`[GraphicStyle](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Creates a new style.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicreport.format.html.[SimpleStyle](SimpleStyle.html)
`[addAttribute](SimpleStyle.html#addAttribute(java.lang.Object,java.lang.Object)), [addAttributes](SimpleStyle.html#addAttributes(javax.swing.text.AttributeSet)), [addChangeListener](SimpleStyle.html#addChangeListener(javax.swing.event.ChangeListener)), [equals](SimpleStyle.html#equals(java.lang.Object)), [fireStateChanged](SimpleStyle.html#fireStateChanged()), [getChangeListeners](SimpleStyle.html#getChangeListeners()), [getListeners](SimpleStyle.html#getListeners(java.lang.Class)), [getName](SimpleStyle.html#getName()), [hashCode](SimpleStyle.html#hashCode()), [removeAttribute](SimpleStyle.html#removeAttribute(java.lang.Object)), [removeAttributes](SimpleStyle.html#removeAttributes(java.util.Enumeration)), [removeAttributes](SimpleStyle.html#removeAttributes(javax.swing.text.AttributeSet)), [removeChangeListener](SimpleStyle.html#removeChangeListener(javax.swing.event.ChangeListener)), [setName](SimpleStyle.html#setName(java.lang.String))`
Methods inherited from class javax.swing.text.[SimpleAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#clone()), [containsAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)), [containsAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)), [copyAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#copyAttributes()), [getAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttribute(java.lang.Object)), [getAttributeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeCount()), [getAttributeNames](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getAttributeNames()), [getResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#getResolveParent()), [isDefined](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isDefined(java.lang.Object)), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEmpty()), [isEqual](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#isEqual(javax.swing.text.AttributeSet)), [setResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.text.[AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html)
`[containsAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttribute(java.lang.Object,java.lang.Object)), [containsAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#containsAttributes(javax.swing.text.AttributeSet)), [copyAttributes](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#copyAttributes()), [getAttribute](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttribute(java.lang.Object)), [getAttributeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeCount()), [getAttributeNames](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getAttributeNames()), [getResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#getResolveParent()), [isDefined](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isDefined(java.lang.Object)), [isEqual](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html#isEqual(javax.swing.text.AttributeSet))`
Methods inherited from interface javax.swing.text.[MutableAttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html)
`[setResolveParent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/MutableAttributeSet.html#setResolveParent(javax.swing.text.AttributeSet))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
GraphicStyle
public GraphicStyle()
Creates a new style, with a null name and parent.
GraphicStyle
public GraphicStyle([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Creates a new style.
Parameters:
`name` - the style name, null for unnamed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class GraphicStyle">Class GraphicStyle</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/SimpleAttributeSet.html" title="class or interface in javax.swing.text">javax.swing.text.SimpleAttributeSet</a>
<div class="inheritance"><a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">com.nomagic.magicreport.format.html.SimpleStyle</a>
<div class="inheritance">com.nomagic.magicreport.format.html.GraphicStyle</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">GraphicStyle</span>
<span class="extends-implements">extends <a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></span></div>
<div class="block">A collection of attributes, represent graphic styles.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 04, 2011</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.format.html.GraphicStyle">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">GraphicStyle</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new style, with a null name and parent.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">GraphicStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.format.html.SimpleStyle">Methods inherited from class com.nomagic.magicreport.format.html.<a href="SimpleStyle.html" title="class in com.nomagic.magicreport.format.html">SimpleStyle</a></h3>
<code><a href="SimpleStyle.html#addAttribute(java.lang.Object,java.lang.Object)">addAttribute</a>, <a href="SimpleStyle.html#addAttributes(javax.swing.text.AttributeSet)">addAttributes</a>, <a href="SimpleStyle.html#addChangeListener(javax.swing.event.ChangeListener)">addChangeListener</a>, <a href="SimpleStyle.html#equals(java.lang.Object)">equals</a>, <a href="SimpleStyle.html#fireStateChanged()">fireStateChanged</a>, <a href="SimpleStyle.html#getChangeListeners()">getChangeListeners</a>, <a href="SimpleStyle.html#getListeners(java.lang.Class)">getListeners</a>, <a href="SimpleStyle.html#getName()">getName</a>, <a href="SimpleStyle.html#hashCode()">hashCode</a>, <a href="SimpleStyle.html#removeAttribute(java.lang.Object)">removeAttribute</a>, <a href="SimpleStyle.html#removeAttributes(java.util.Enumeration)">removeAttributes</a>, <a href="SimpleStyle.html#removeAttributes(javax.swing.text.AttributeSet)">removeAttributes</a>, <a href="SimpleStyle.html#removeChangeListener(javax.swing.event.ChangeListener)">removeChangeListener</a>, <a href="SimpleStyle.html#setName(java.lang.String)">setName</a></code></div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>GraphicStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GraphicStyle</span>()</div>
<div class="block">Creates a new style, with a null name and parent.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>GraphicStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GraphicStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
