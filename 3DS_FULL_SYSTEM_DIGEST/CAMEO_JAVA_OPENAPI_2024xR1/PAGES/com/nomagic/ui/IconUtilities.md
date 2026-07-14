# JAVA OPENAPI: IconUtilities (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/ui/IconUtilities.html
- source_path: `com/nomagic/ui/IconUtilities.html`
- source_sha256: `53c82b1aceaebc462815f34c32bd324cf2c1f0a6eb9f902cabac11f63a02df3f`
- captured_utc: `2026-07-14T16:52:24.787049+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class IconUtilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.IconUtilities

@OpenApiAllpublic classIconUtilities
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Utility class to work wih Icons

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[IMAGE_SHAPE_IMAGE_TYPES](#IMAGE_SHAPE_IMAGE_TYPES)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[IconUtilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ResizableIcon](ResizableIcon.html)`
`[getGrayIcon](#getGrayIcon(javax.swing.Icon,java.awt.Component))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)`
Returns gray(disabled) icon for a given one.
`static boolean`
`[isExistingIconImage](#isExistingIconImage(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Used to check if icon really contains a valid image
`static boolean`
`[isImageFile](#isImageFile(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`

`static [BufferedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[toImage](#toImage(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Create an image from a given icon
`static byte[]`
`[toPng](#toPng(java.awt.image.RenderedImage))([RenderedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html) img)`
Export given image to PNG.
`static byte[]`
`[toPng](#toPng(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Export given icon to PNG.
`static byte[]`
`[toSvg](#toSvg(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Export given icon to SVG.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
IMAGE_SHAPE_IMAGE_TYPES
public static final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> IMAGE_SHAPE_IMAGE_TYPES
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
IconUtilities
public IconUtilities()
 ============ METHOD DETAIL ========== 
Method Details
toSvg
public static byte[] toSvg([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Export given icon to SVG.
Parameters:
`icon` - icon
Returns:
svg bytes
toPng
public static byte[] toPng([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Export given icon to PNG.
Parameters:
`icon` - icon
Returns:
png bytes
toPng
public static byte[] toPng([RenderedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html) img)
Export given image to PNG.
Parameters:
`img` - image
Returns:
png bytes
getGrayIcon
@CheckForNullpublic static [ResizableIcon](ResizableIcon.html) getGrayIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)
Returns gray(disabled) icon for a given one.
Parameters:
`icon` - the given icon
`component` - component
Returns:
gray(disabled) icon
toImage
public static [BufferedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html) toImage([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Create an image from a given icon
Parameters:
`icon` - icon
Returns:
image
isImageFile
public static boolean isImageFile([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
isExistingIconImage
public static boolean isExistingIconImage([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Used to check if icon really contains a valid image
Parameters:
`icon` - icon
Returns:
if icon image is valid

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class IconUtilities">Class IconUtilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.IconUtilities</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">IconUtilities</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work wih Icons</div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IMAGE_SHAPE_IMAGE_TYPES">IMAGE_SHAPE_IMAGE_TYPES</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">IconUtilities</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getGrayIcon(javax.swing.Icon,java.awt.Component)">getGrayIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns gray(disabled) icon for a given one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExistingIconImage(javax.swing.Icon)">isExistingIconImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Used to check if icon really contains a valid image</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isImageFile(java.io.File)">isImageFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toImage(javax.swing.Icon)">toImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an image from a given icon</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toPng(java.awt.image.RenderedImage)">toPng</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html" title="class or interface in java.awt.image">RenderedImage</a> img)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Export given image to PNG.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toPng(javax.swing.Icon)">toPng</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Export given icon to PNG.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toSvg(javax.swing.Icon)">toSvg</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Export given icon to SVG.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="IMAGE_SHAPE_IMAGE_TYPES">
<h3>IMAGE_SHAPE_IMAGE_TYPES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">IMAGE_SHAPE_IMAGE_TYPES</span></div>
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
<h3>IconUtilities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IconUtilities</span>()</div>
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
<section class="detail" id="toSvg(javax.swing.Icon)">
<h3>toSvg</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toSvg</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Export given icon to SVG.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>svg bytes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toPng(javax.swing.Icon)">
<h3>toPng</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toPng</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Export given icon to PNG.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>png bytes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toPng(java.awt.image.RenderedImage)">
<h3>toPng</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toPng</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html" title="class or interface in java.awt.image">RenderedImage</a> img)</span></div>
<div class="block">Export given image to PNG.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>img</code> - image</dd>
<dt>Returns:</dt>
<dd>png bytes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGrayIcon(javax.swing.Icon,java.awt.Component)">
<h3>getGrayIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getGrayIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</span></div>
<div class="block">Returns gray(disabled) icon for a given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the given icon</dd>
<dd><code>component</code> - component</dd>
<dt>Returns:</dt>
<dd>gray(disabled) icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toImage(javax.swing.Icon)">
<h3>toImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">toImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Create an image from a given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isImageFile(java.io.File)">
<h3>isImageFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isImageFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
</section>
</li>
<li>
<section class="detail" id="isExistingIconImage(javax.swing.Icon)">
<h3>isExistingIconImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExistingIconImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Used to check if icon really contains a valid image</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>if icon image is valid</dd>
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
