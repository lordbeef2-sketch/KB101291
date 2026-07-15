# JAVA OPENAPI: RetinaImageIcon (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/ui/RetinaImageIcon.html
- source_path: `com/nomagic/ui/RetinaImageIcon.html`
- source_sha256: `61d4b8ae94d509c1b2dbe6c90a6dbaaba98da8838ba7d98d7c0be9927d6b4b95`
- captured_utc: `2026-07-14T16:58:41.834333+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class RetinaImageIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
[com.nomagic.ui.ScalableImageIcon](ScalableImageIcon.html)
[com.nomagic.ui.ResizableIconImageIcon](ResizableIconImageIcon.html)
com.nomagic.ui.RetinaImageIcon

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.icons.LocatableIcon`, `[ResizableIcon](ResizableIcon.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html)`, `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`

@OpenApiAllpublic classRetinaImageIcon
extends [ResizableIconImageIcon](ResizableIconImageIcon.html)

Retina friendly image icon implementation. Icon(and image returned by this icon) is twice smaller then the wrapped icon itself.

 Wrapped icon is used for painting. On paint Graphics is scaled down by retina scale factor and wrapped icon is painted.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.ui.RetinaImageIcon)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#component), [tracker](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RetinaImageIcon](#%3Cinit%3E(com.nomagic.ui.ResizableIcon))([ResizableIcon](ResizableIcon.html) icon)`
Constructor.
`[RetinaImageIcon](#%3Cinit%3E(com.nomagic.ui.ResizableIcon,int,int))([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)`
Constructor.
`[RetinaImageIcon](#%3Cinit%3E(java.awt.Image))([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image)`
Constructor.
`[RetinaImageIcon](#%3Cinit%3E(java.awt.Image,int,int))([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image,
 int width,
 int height)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getIconHeight](#getIconHeight())()`

`int`
`[getIconWidth](#getIconWidth())()`

`void`
`[paintIcon](#paintIcon(java.awt.Component,java.awt.Graphics,int,int))([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y)`

`void`
`[paintIcon](#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int))([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y,
 int w,
 int h)`
Draw the icon in the given bounds.
Methods inherited from class com.nomagic.ui.[ScalableImageIcon](ScalableImageIcon.html)
`[clone](ScalableImageIcon.html#clone()), [create](ScalableImageIcon.html#create(java.lang.String)), [doNotScale](ScalableImageIcon.html#doNotScale()), [getImage](ScalableImageIcon.html#getImage()), [getLocation](ScalableImageIcon.html#getLocation()), [getURL](ScalableImageIcon.html#getURL()), [setImage](ScalableImageIcon.html#setImage(java.awt.Image)), [toImageIcon](ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon)), [toImageIcon](ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon,int,int)), [toImageIcon](ScalableImageIcon.html#toImageIcon(javax.swing.Icon))`
Methods inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[getAccessibleContext](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()), [getDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()), [getImageLoadStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()), [getImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()), [loadImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)), [setDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)), [setImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RetinaImageIcon
public RetinaImageIcon([ResizableIcon](ResizableIcon.html) icon)
Constructor. Scales down given icon by retina factor.
Parameters:
`icon` - given icon
RetinaImageIcon
public RetinaImageIcon([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)
Constructor. Scales down given icon to the given width and height.
Parameters:
`icon` - given icon
RetinaImageIcon
public RetinaImageIcon([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image,
 int width,
 int height)
Constructor. Scales down given icon to the given width and height.
Parameters:
`image` - given image
RetinaImageIcon
public RetinaImageIcon([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image)
Constructor. Scales down given image by retina factor.
Parameters:
`image` - given image
 ============ METHOD DETAIL ========== 
Method Details
paintIcon
public void paintIcon(@CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y,
 int w,
 int h)
Description copied from interface: `[ResizableIcon](ResizableIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int))`
Draw the icon in the given bounds. Icon implementations may use the Component argument
 to get properties useful for painting, e.g. the foreground or background color.
Specified by:
`[paintIcon](ResizableIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int))` in interface `[ResizableIcon](ResizableIcon.html)`
Overrides:
`[paintIcon](ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int))` in class `[ScalableImageIcon](ScalableImageIcon.html)`
Parameters:
`c` - the given component.
`g` - the graphics to paint on.
`x` - x coordinate.
`y` - y coordinate.
`w` - width to paint.
`h` - height to paint.
paintIcon
public void paintIcon([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y)
Specified by:
`[paintIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int))` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
Overrides:
`[paintIcon](ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int))` in class `[ScalableImageIcon](ScalableImageIcon.html)`
getIconWidth
public int getIconWidth()
Specified by:
`[getIconWidth](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth())` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
Overrides:
`[getIconWidth](ScalableImageIcon.html#getIconWidth())` in class `[ScalableImageIcon](ScalableImageIcon.html)`
getIconHeight
public int getIconHeight()
Specified by:
`[getIconHeight](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight())` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
Overrides:
`[getIconHeight](ScalableImageIcon.html#getIconHeight())` in class `[ScalableImageIcon](ScalableImageIcon.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class RetinaImageIcon">Class RetinaImageIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">javax.swing.ImageIcon</a>
<div class="inheritance"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">com.nomagic.ui.ScalableImageIcon</a>
<div class="inheritance"><a href="ResizableIconImageIcon.html" title="class in com.nomagic.ui">com.nomagic.ui.ResizableIconImageIcon</a>
<div class="inheritance">com.nomagic.ui.RetinaImageIcon</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.icons.LocatableIcon</code>, <code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RetinaImageIcon</span>
<span class="extends-implements">extends <a href="ResizableIconImageIcon.html" title="class in com.nomagic.ui">ResizableIconImageIcon</a></span></div>
<div class="block">Retina friendly image icon implementation. Icon(and image returned by this icon) is twice smaller then the wrapped icon itself.

 Wrapped icon is used for painting. On paint Graphics is scaled down by retina scale factor and wrapped icon is painted.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.ui.RetinaImageIcon">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ui.ResizableIcon)">RetinaImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ui.ResizableIcon,int,int)">RetinaImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.awt.Image)">RetinaImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.awt.Image,int,int)">RetinaImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconHeight()">getIconHeight</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconWidth()">getIconWidth</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintIcon(java.awt.Component,java.awt.Graphics,int,int)">paintIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">paintIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y,
 int w,
 int h)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draw the icon in the given bounds.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.ui.ScalableImageIcon">Methods inherited from class com.nomagic.ui.<a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></h3>
<code><a href="ScalableImageIcon.html#clone()">clone</a>, <a href="ScalableImageIcon.html#create(java.lang.String)">create</a>, <a href="ScalableImageIcon.html#doNotScale()">doNotScale</a>, <a href="ScalableImageIcon.html#getImage()">getImage</a>, <a href="ScalableImageIcon.html#getLocation()">getLocation</a>, <a href="ScalableImageIcon.html#getURL()">getURL</a>, <a href="ScalableImageIcon.html#setImage(java.awt.Image)">setImage</a>, <a href="ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon)">toImageIcon</a>, <a href="ScalableImageIcon.html#toImageIcon(com.nomagic.ui.ResizableIcon,int,int)">toImageIcon</a>, <a href="ScalableImageIcon.html#toImageIcon(javax.swing.Icon)">toImageIcon</a></code></div>
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
<h3>RetinaImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RetinaImageIcon</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Constructor. Scales down given icon by retina factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - given icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.ui.ResizableIcon,int,int)">
<h3>RetinaImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RetinaImageIcon</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</span></div>
<div class="block">Constructor. Scales down given icon to the given width and height.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - given icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.awt.Image,int,int)">
<h3>RetinaImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RetinaImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image,
 int width,
 int height)</span></div>
<div class="block">Constructor. Scales down given icon to the given width and height.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - given image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.awt.Image)">
<h3>RetinaImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RetinaImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</span></div>
<div class="block">Constructor. Scales down given image by retina factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - given image</dd>
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
<section class="detail" id="paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">
<h3>paintIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y,
 int w,
 int h)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ResizableIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">ResizableIcon</a></code></span></div>
<div class="block">Draw the icon in the given bounds.  Icon implementations may use the Component argument
 to get properties useful for painting, e.g. the foreground or background color.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ResizableIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">paintIcon</a></code> in interface <code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">paintIcon</a></code> in class <code><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></dd>
<dt>Parameters:</dt>
<dd><code>c</code> - the given component.</dd>
<dd><code>g</code> - the graphics to paint on.</dd>
<dd><code>x</code> - x coordinate.</dd>
<dd><code>y</code> - y coordinate.</dd>
<dd><code>w</code> - width to paint.</dd>
<dd><code>h</code> - height to paint.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintIcon(java.awt.Component,java.awt.Graphics,int,int)">
<h3>paintIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)" title="class or interface in javax.swing">paintIcon</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ScalableImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)">paintIcon</a></code> in class <code><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconWidth()">
<h3>getIconWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIconWidth</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth()" title="class or interface in javax.swing">getIconWidth</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ScalableImageIcon.html#getIconWidth()">getIconWidth</a></code> in class <code><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIconHeight()">
<h3>getIconHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIconHeight</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight()" title="class or interface in javax.swing">getIconHeight</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ScalableImageIcon.html#getIconHeight()">getIconHeight</a></code> in class <code><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></dd>
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
