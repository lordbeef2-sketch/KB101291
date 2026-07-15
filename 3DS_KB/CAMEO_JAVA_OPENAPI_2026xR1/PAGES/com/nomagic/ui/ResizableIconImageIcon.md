# JAVA OPENAPI: ResizableIconImageIcon (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/ui/ResizableIconImageIcon.html
- source_path: `com/nomagic/ui/ResizableIconImageIcon.html`
- source_sha256: `48eab518d1f0c0cbdbbfd9a5d8302614b150b8592e7140393ec27b5f11a72e1c`
- captured_utc: `2026-07-14T16:46:17.249030+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class ResizableIconImageIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
[com.nomagic.ui.ScalableImageIcon](ScalableImageIcon.html)
com.nomagic.ui.ResizableIconImageIcon

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.icons.LocatableIcon`, `[ResizableIcon](ResizableIcon.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html)`, `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`

Direct Known Subclasses:
`[RetinaImageIcon](RetinaImageIcon.html)`, `[SquareIcon](SquareIcon.html)`

@OpenApiAllpublic classResizableIconImageIcon
extends [ScalableImageIcon](ScalableImageIcon.html)

Image icon which wraps other icon and provides an image for a wrapped icon.
 Provided image is HiDPI/Retina friendly. On Mac special instance of java.awt.Image (sun.awt.image.MultiResolutionToolkitImage) is returned which supports multi-resolution.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.ui.ResizableIconImageIcon)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#component), [tracker](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ResizableIconImageIcon](#%3Cinit%3E(com.nomagic.ui.ResizableIcon))([ResizableIcon](ResizableIcon.html) icon)`
Constructor
`[ResizableIconImageIcon](#%3Cinit%3E(com.nomagic.ui.ResizableIcon,int,int))([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.ui.[ScalableImageIcon](ScalableImageIcon.html)
`[clone](ScalableImageIcon.html#clone()), [create](ScalableImageIcon.html#create(java.lang.String)), [doNotScale](ScalableImageIcon.html#doNotScale()), [getIconHeight](ScalableImageIcon.html#getIconHeight()), [getIconWidth](ScalableImageIcon.html#getIconWidth()), [getImage](ScalableImageIcon.html#getImage()), [getLocation](ScalableImageIcon.html#getLocation()), [getURL](ScalableImageIcon.html#getURL()), [paintIcon](ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)), [paintIcon](ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)), [setImage](ScalableImageIcon.html#setImage(java.awt.Image)), [toImageIcon](ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon)), [toImageIcon](ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon,int,int)), [toImageIcon](ScalableImageIcon.html#toImageIcon(javax.swing.Icon))`
Methods inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[getAccessibleContext](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()), [getDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()), [getImageLoadStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()), [getImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()), [loadImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)), [setDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)), [setImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ResizableIconImageIcon
public ResizableIconImageIcon([ResizableIcon](ResizableIcon.html) icon)
Constructor
Parameters:
`icon` - wrapped icon
ResizableIconImageIcon
public ResizableIconImageIcon([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)
Constructor
Parameters:
`icon` - wrapped icon
`width` - icon width
`height` - icon height

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class ResizableIconImageIcon">Class ResizableIconImageIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">javax.swing.ImageIcon</a>
<div class="inheritance"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">com.nomagic.ui.ScalableImageIcon</a>
<div class="inheritance">com.nomagic.ui.ResizableIconImageIcon</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.icons.LocatableIcon</code>, <code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="RetinaImageIcon.html" title="class in com.nomagic.ui">RetinaImageIcon</a></code>, <code><a href="SquareIcon.html" title="class in com.nomagic.ui">SquareIcon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ResizableIconImageIcon</span>
<span class="extends-implements">extends <a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></span></div>
<div class="block">Image icon which wraps other icon and provides an image for a wrapped icon.
 <p>
 Provided image is HiDPI/Retina friendly. On Mac special instance of java.awt.Image (sun.awt.image.MultiResolutionToolkitImage) is returned which supports multi-resolution.
 </p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.ui.ResizableIconImageIcon">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-javax.swing.ImageIcon">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#component" title="class or interface in javax.swing">component</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker" title="class or interface in javax.swing">tracker</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ui.ResizableIcon)">ResizableIconImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ui.ResizableIcon,int,int)">ResizableIconImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.ui.ScalableImageIcon">Methods inherited from class com.nomagic.ui.<a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></h3>
<code><a href="ScalableImageIcon.html#clone()">clone</a>, <a href="ScalableImageIcon.html#create(java.lang.String)">create</a>, <a href="ScalableImageIcon.html#doNotScale()">doNotScale</a>, <a href="ScalableImageIcon.html#getIconHeight()">getIconHeight</a>, <a href="ScalableImageIcon.html#getIconWidth()">getIconWidth</a>, <a href="ScalableImageIcon.html#getImage()">getImage</a>, <a href="ScalableImageIcon.html#getLocation()">getLocation</a>, <a href="ScalableImageIcon.html#getURL()">getURL</a>, <a href="ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)">paintIcon</a>, <a href="ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">paintIcon</a>, <a href="ScalableImageIcon.html#setImage(java.awt.Image)">setImage</a>, <a href="ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon)">toImageIcon</a>, <a href="ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon,int,int)">toImageIcon</a>, <a href="ScalableImageIcon.html#toImageIcon(javax.swing.Icon)">toImageIcon</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.ImageIcon">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()" title="class or interface in javax.swing">getAccessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()" title="class or interface in javax.swing">getDescription</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()" title="class or interface in javax.swing">getImageLoadStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()" title="class or interface in javax.swing">getImageObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)" title="class or interface in javax.swing">loadImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)" title="class or interface in javax.swing">setDescription</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)" title="class or interface in javax.swing">setImageObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#toString()" title="class or interface in javax.swing">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.ui.ResizableIcon)">
<h3>ResizableIconImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ResizableIconImageIcon</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - wrapped icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.ui.ResizableIcon,int,int)">
<h3>ResizableIconImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ResizableIconImageIcon</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - wrapped icon</dd>
<dd><code>width</code> - icon width</dd>
<dd><code>height</code> - icon height</dd>
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
