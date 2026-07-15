# JAVA OPENAPI: UnmodifiableDimension (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/ui/UnmodifiableDimension.html
- source_path: `com/nomagic/ui/UnmodifiableDimension.html`
- source_sha256: `2fd664303610288fa65a6543c541a6cedcfc162921bca2cb13f034a97942f899`
- captured_utc: `2026-07-14T16:58:41.914335+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class UnmodifiableDimension

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.UnmodifiableDimension

@OpenApiAllpublic classUnmodifiableDimension
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Unmodifiable dimension. Values cannot be modified after creation.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [UnmodifiableDimension](UnmodifiableDimension.html)`
`[EMPTY](#EMPTY)`
Empty dimension holder.
`final int`
`[height](#height)`
Dimension's height
`final int`
`[width](#width)`
Dimension's width
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UnmodifiableDimension](UnmodifiableDimension.html)`
`[create](#create(int,int))(int width,
 int height)`
Factory method to create an instance of UnmodifiableDimension.
`static [UnmodifiableDimension](UnmodifiableDimension.html)`
`[create](#create(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html) dimension)`
Creates dimension from given [`Dimension`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html)
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`

`int`
`[getHeight](#getHeight())()`
Returns height
`int`
`[getWidth](#getWidth())()`
Returns width
`int`
`[hashCode](#hashCode())()`

`[UnmodifiableDimension](UnmodifiableDimension.html)`
`[set](#set(int,int))(int width,
 int height)`
Applies given width and height to self
`[UnmodifiableDimension](UnmodifiableDimension.html)`
`[set](#set(java.awt.Dimension))([Dimension](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html) dimension)`
Applies given dimension to self
`[UnmodifiableDimension](UnmodifiableDimension.html)`
`[setHeight](#setHeight(int))(int height)`
Applies given height to self
`[UnmodifiableDimension](UnmodifiableDimension.html)`
`[setWidth](#setWidth(int))(int width)`
Applies given width to self
`[Dimension](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html)`
`[toDimension](#toDimension())()`
Converts to [`Dimension`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html)
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns a string representation of this `UnmodifiableDimension` object.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
EMPTY
public static final [UnmodifiableDimension](UnmodifiableDimension.html) EMPTY
Empty dimension holder.
width
public final int width
Dimension's width
height
public final int height
Dimension's height
 ============ METHOD DETAIL ========== 
Method Details
create
public static [UnmodifiableDimension](UnmodifiableDimension.html) create(int width,
 int height)
Factory method to create an instance of UnmodifiableDimension.
Parameters:
`width` - width
`height` - height
Returns:
instance
create
public static [UnmodifiableDimension](UnmodifiableDimension.html) create([Dimension](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html) dimension)
Creates dimension from given [`Dimension`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html)
Parameters:
`dimension` - dimension
Returns:
created dimension
set
public [UnmodifiableDimension](UnmodifiableDimension.html) set(int width,
 int height)
Applies given width and height to self
Parameters:
`width` - width
`height` - height
Returns:
new dimension or self if width and height are not changed
set
public [UnmodifiableDimension](UnmodifiableDimension.html) set([Dimension](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html) dimension)
Applies given dimension to self
Parameters:
`dimension` - dimension
Returns:
new dimension or self if width and height are not changed
setWidth
public [UnmodifiableDimension](UnmodifiableDimension.html) setWidth(int width)
Applies given width to self
Parameters:
`width` - width
Returns:
new dimension or self if width is not changed
setHeight
public [UnmodifiableDimension](UnmodifiableDimension.html) setHeight(int height)
Applies given height to self
Parameters:
`height` - height
Returns:
new dimension or self if height is not changed
getWidth
public int getWidth()
Returns width
Returns:
width
getHeight
public int getHeight()
Returns height
Returns:
height
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Returns a string representation of this `UnmodifiableDimension` object.
 This method is intended to be used only for debugging purposes, and the content and format of the returned string may vary between implementations.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
a string representation of this `UnmodifiableDimension` object.
toDimension
public [Dimension](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html) toDimension()
Converts to [`Dimension`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html)
Returns:
[`Dimension`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class UnmodifiableDimension">Class UnmodifiableDimension</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.UnmodifiableDimension</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">UnmodifiableDimension</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Unmodifiable dimension. Values cannot be modified after creation.</div>
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
<div class="col-first even-row-color"><code>static final <a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMPTY">EMPTY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Empty dimension holder.</div>
</div>
<div class="col-first odd-row-color"><code>final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#height">height</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Dimension's height</div>
</div>
<div class="col-first even-row-color"><code>final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#width">width</a></code></div>
<div class="col-last even-row-color">
<div class="block">Dimension's width</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(int,int)">create</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Factory method to create an instance of UnmodifiableDimension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.awt.Dimension)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dimension)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates dimension from given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt"><code>Dimension</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHeight()">getHeight</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns height</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWidth()">getWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns width</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#set(int,int)">set</a><wbr/>(int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies given width and height to self</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#set(java.awt.Dimension)">set</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dimension)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies given dimension to self</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHeight(int)">setHeight</a><wbr/>(int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies given height to self</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWidth(int)">setWidth</a><wbr/>(int width)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies given width to self</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toDimension()">toDimension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts to <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt"><code>Dimension</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a string representation of this <code> UnmodifiableDimension</code> object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="EMPTY">
<h3>EMPTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">EMPTY</span></div>
<div class="block">Empty dimension holder.</div>
</section>
</li>
<li>
<section class="detail" id="width">
<h3>width</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">width</span></div>
<div class="block">Dimension's width</div>
</section>
</li>
<li>
<section class="detail" id="height">
<h3>height</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">int</span> <span class="element-name">height</span></div>
<div class="block">Dimension's height</div>
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
<section class="detail" id="create(int,int)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
<div class="block">Factory method to create an instance of UnmodifiableDimension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - width</dd>
<dd><code>height</code> - height</dd>
<dt>Returns:</dt>
<dd>instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.awt.Dimension)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dimension)</span></div>
<div class="block">Creates dimension from given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt"><code>Dimension</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dimension</code> - dimension</dd>
<dt>Returns:</dt>
<dd>created dimension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="set(int,int)">
<h3>set</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">set</span><wbr/><span class="parameters">(int width,
 int height)</span></div>
<div class="block">Applies given width and height to self</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - width</dd>
<dd><code>height</code> - height</dd>
<dt>Returns:</dt>
<dd>new dimension or self if width and height are not changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="set(java.awt.Dimension)">
<h3>set</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">set</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> dimension)</span></div>
<div class="block">Applies given dimension to self</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dimension</code> - dimension</dd>
<dt>Returns:</dt>
<dd>new dimension or self if width and height are not changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWidth(int)">
<h3>setWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">setWidth</span><wbr/><span class="parameters">(int width)</span></div>
<div class="block">Applies given width to self</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - width</dd>
<dt>Returns:</dt>
<dd>new dimension or self if width is not changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHeight(int)">
<h3>setHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="UnmodifiableDimension.html" title="class in com.nomagic.ui">UnmodifiableDimension</a></span> <span class="element-name">setHeight</span><wbr/><span class="parameters">(int height)</span></div>
<div class="block">Applies given height to self</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>height</code> - height</dd>
<dt>Returns:</dt>
<dd>new dimension or self if height is not changed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWidth()">
<h3>getWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getWidth</span>()</div>
<div class="block">Returns width</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>width</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHeight()">
<h3>getHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getHeight</span>()</div>
<div class="block">Returns height</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>height</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns a string representation of this <code> UnmodifiableDimension</code> object.
 This method is intended to be used only for debugging purposes, and the content and format of the returned string may vary between implementations.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this <code> UnmodifiableDimension</code> object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toDimension()">
<h3>toDimension</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></span> <span class="element-name">toDimension</span>()</div>
<div class="block">Converts to <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt"><code>Dimension</code></a></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt"><code>Dimension</code></a></dd>
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
