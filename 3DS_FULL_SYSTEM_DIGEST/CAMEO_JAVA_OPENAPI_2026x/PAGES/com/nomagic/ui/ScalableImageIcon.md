# JAVA OPENAPI: ScalableImageIcon (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/ui/ScalableImageIcon.html
- source_path: `com/nomagic/ui/ScalableImageIcon.html`
- source_sha256: `c4b80b70911d2f18fc819ae4ee378961bbb23b214bcb6bda91b4c4dbdc013d83`
- captured_utc: `2026-07-14T16:58:41.881335+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class ScalableImageIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[javax.swing.ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
com.nomagic.ui.ScalableImageIcon

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.icons.LocatableIcon`, `[ResizableIcon](ResizableIcon.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html)`, `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`

Direct Known Subclasses:
`[DoubleSizeImageIcon](DoubleSizeImageIcon.html)`, `[ResizableIconImageIcon](ResizableIconImageIcon.html)`

@OpenApiAllpublic classScalableImageIcon
extends [ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
implements [ResizableIcon](ResizableIcon.html), com.dassault_systemes.modeler.foundation.icons.LocatableIcon

HiDPI(Retina) friendly ImageIcon implementation. 
 

This class dynamically chooses a right image by current screen dpi and/or scaling factor defined in the system (Retina and etc).
 If scaling is needed and svg icon with the same name is available at given location, svg icon will be used instead of a bitmap icon.
Dynamic choosing will work only if two icons are provided at the same location. For example:
 /com/product/icons/a.png
/com/product/icons/a.svg
ScalableImageIcon(Product.class, "/com/product/icons/a.png") will load a.png on a regular dpi monitor, but a.svg will be loaded on HiDPI monitor.
 Keep in mind that svg icon size can be any. Svg icon will be re-sized according to the size of a.png icon and scaling factor.
 For example if size of a.png is 16x16 and scaling factor is 2, loaded svg icon will be re-sized to 32x32 if needed.
Original icon will be loaded and scaled if svg icon is not provided, but HiDPI with scaling is used.
Icon image loading is lazy. Image will be loaded only if icon is painted, getImage() is called or icon width/height is retrieved.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.ui.ScalableImageIcon)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#component), [tracker](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ScalableImageIcon](#%3Cinit%3E(byte%5B%5D))(byte[] imageData)`
Load icon from given bytes.
`[ScalableImageIcon](#%3Cinit%3E(byte%5B%5D,java.net.URI))(byte[] imageData,
 [URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri)`
Load icon from given bytes.
`[ScalableImageIcon](#%3Cinit%3E(java.awt.Image))([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image)`
Wrap given image and use it for painting.
`[ScalableImageIcon](#%3Cinit%3E(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)`
Load icon from a resources of given class.
`[ScalableImageIcon](#%3Cinit%3E(java.lang.Class,java.lang.String,boolean))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location,
 boolean silent)`
Load icon from a resources of given class.
`[ScalableImageIcon](#%3Cinit%3E(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)`
Load icon from a given url.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`
Returns cloned instance of this icon.
`static [ScalableImageIcon](ScalableImageIcon.html)`
`[create](#create(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName)`
Load icon from a file.
`void`
`[doNotScale](#doNotScale())()`
Do not scale this icon by screen dpi.
`int`
`[getIconHeight](#getIconHeight())()`

`int`
`[getIconWidth](#getIconWidth())()`

`[Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html)`
`[getImage](#getImage())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getLocation](#getLocation())()`

`[URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)`
`[getURL](#getURL())()`

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
`void`
`[setImage](#setImage(java.awt.Image))([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image)`

`static [ScalableImageIcon](ScalableImageIcon.html)`
`[toImageIcon](#toImageIcon(com.nomagic.ui.ResizableIcon))([ResizableIcon](ResizableIcon.html) icon)`
Convert given icon to a ImageIcon.
`static [ScalableImageIcon](ScalableImageIcon.html)`
`[toImageIcon](#toImageIcon(com.nomagic.ui.ResizableIcon,int,int))([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)`
Convert given icon to a ImageIcon of given width and height.
`static [ScalableImageIcon](ScalableImageIcon.html)`
`[toImageIcon](#toImageIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Convert given icon to a ImageIcon.
Methods inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[getAccessibleContext](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()), [getDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()), [getImageLoadStatus](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()), [getImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()), [loadImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)), [setDescription](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)), [setImageObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ScalableImageIcon
public ScalableImageIcon([Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image)
Wrap given image and use it for painting.
Parameters:
`image` - image
ScalableImageIcon
public ScalableImageIcon(byte[] imageData)
Load icon from given bytes.
Parameters:
`imageData` - image bytes
ScalableImageIcon
public ScalableImageIcon(byte[] imageData,
 [URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri)
Load icon from given bytes.
Parameters:
`imageData` - image bytes
`uri` - uri describing the bytes (format etc.)
ScalableImageIcon
public ScalableImageIcon([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url)
Load icon from a given url.
Parameters:
`url` - url
ScalableImageIcon
public ScalableImageIcon([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location)
Load icon from a resources of given class.
Parameters:
`clazz` - class
`location` - resources location relative to a given class
ScalableImageIcon
public ScalableImageIcon([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) location,
 boolean silent)
Load icon from a resources of given class.
Parameters:
`clazz` - class
`location` - resources location relative to a given class
`silent` - if true, does not report to log file about missing icon at given location
 ============ METHOD DETAIL ========== 
Method Details
create
@CheckForNullpublic static [ScalableImageIcon](ScalableImageIcon.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName)
Load icon from a file.
Parameters:
`fileName` - file name
paintIcon
public void paintIcon(@CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y)
Specified by:
`[paintIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int))` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
Overrides:
`[paintIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int))` in class `[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)`
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
Parameters:
`c` - the given component.
`g` - the graphics to paint on.
`x` - x coordinate.
`y` - y coordinate.
`w` - width to paint.
`h` - height to paint.
getIconHeight
public int getIconHeight()
Specified by:
`[getIconHeight](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight())` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
Overrides:
`[getIconHeight](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconHeight())` in class `[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)`
getIconWidth
public int getIconWidth()
Specified by:
`[getIconWidth](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth())` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
Overrides:
`[getIconWidth](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconWidth())` in class `[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)`
setImage
public void setImage(@CheckForNull
 [Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) image)
Overrides:
`[setImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImage(java.awt.Image))` in class `[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)`
getImage
public [Image](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html) getImage()
Overrides:
`[getImage](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImage())` in class `[ImageIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html)`
getLocation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getLocation()
Specified by:
`getLocation` in interface `com.dassault_systemes.modeler.foundation.icons.LocatableIcon`
Returns:
location of resource if icon is loaded from resources of some class. Null otherwise
getURL
public [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) getURL()
Returns:
url if icon is loaded from url. Null otherwise
clone
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) clone()
Description copied from interface: `[ResizableIcon](ResizableIcon.html#clone())`
Returns cloned instance of this icon.
Specified by:
`[clone](ResizableIcon.html#clone())` in interface `[ResizableIcon](ResizableIcon.html)`
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
cloned instance.
doNotScale
public void doNotScale()
Do not scale this icon by screen dpi. This method has effect only if ScalableImageIcon was just created and image was not loaded yet.
toImageIcon
@CheckForNullpublic static [ScalableImageIcon](ScalableImageIcon.html) toImageIcon(@CheckForNull
 [ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)
Convert given icon to a ImageIcon of given width and height. Same icon is returned if it is already ImageIcon and has same size.
Parameters:
`icon` - icon to convert
`width` - icon width
`height` - icon height
Returns:
converted icon or same icon if it is already suitable
toImageIcon
@CheckForNullpublic static [ScalableImageIcon](ScalableImageIcon.html) toImageIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon)
Convert given icon to a ImageIcon. Same icon is returned if it is already ImageIcon.
Parameters:
`icon` - icon to convert
Returns:
converted icon or same icon if it is already suitable
toImageIcon
@CheckForNullpublic static [ScalableImageIcon](ScalableImageIcon.html) toImageIcon(@CheckForNull
 [ResizableIcon](ResizableIcon.html) icon)
Convert given icon to a ImageIcon. Same icon is returned if it is already ImageIcon.
Parameters:
`icon` - icon to convert
Returns:
converted icon or same icon if it is already suitable

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class ScalableImageIcon">Class ScalableImageIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">javax.swing.ImageIcon</a>
<div class="inheritance">com.nomagic.ui.ScalableImageIcon</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.icons.LocatableIcon</code>, <code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DoubleSizeImageIcon.html" title="class in com.nomagic.ui">DoubleSizeImageIcon</a></code>, <code><a href="ResizableIconImageIcon.html" title="class in com.nomagic.ui">ResizableIconImageIcon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ScalableImageIcon</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a>
implements <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a>, com.dassault_systemes.modeler.foundation.icons.LocatableIcon</span></div>
<div class="block">HiDPI(Retina) friendly ImageIcon implementation.<br/> <br/>
<p>
 This class dynamically chooses a right image by current screen dpi and/or scaling factor defined in the system (Retina and etc).
 If scaling is needed and svg icon with the same name is available at given location, svg icon will be used instead of a bitmap icon.
 </p>
<p>
 Dynamic choosing will work only if two icons are provided at the same location. For example:
 <li>/com/product/icons/a.png</li>
<li>/com/product/icons/a.svg</li>
</p>
<p>
 ScalableImageIcon(Product.class, "/com/product/icons/a.png") will load a.png on a regular dpi monitor, but a.svg will be loaded on HiDPI monitor.
 Keep in mind that svg icon size can be any. Svg icon will be re-sized according to the size of a.png icon and scaling factor.
 For example if size of a.png is 16x16 and scaling factor is 2, loaded svg icon will be re-sized to 32x32 if needed.
 </p>
<p>
 Original icon will be loaded and scaled if svg icon is not provided, but HiDPI with scaling is used.
 </p>
<p>
 Icon image loading is lazy. Image will be loaded only if icon is painted, getImage() is called or icon width/height is retrieved.
 </p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.ui.ScalableImageIcon">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(byte%5B%5D)">ScalableImageIcon</a><wbr/>(byte[] imageData)</code></div>
<div class="col-last even-row-color">
<div class="block">Load icon from given bytes.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(byte%5B%5D,java.net.URI)">ScalableImageIcon</a><wbr/>(byte[] imageData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</code></div>
<div class="col-last odd-row-color">
<div class="block">Load icon from given bytes.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.awt.Image)">ScalableImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</code></div>
<div class="col-last even-row-color">
<div class="block">Wrap given image and use it for painting.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.String)">ScalableImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last odd-row-color">
<div class="block">Load icon from a resources of given class.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.String,boolean)">ScalableImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location,
 boolean silent)</code></div>
<div class="col-last even-row-color">
<div class="block">Load icon from a resources of given class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.net.URL)">ScalableImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last odd-row-color">
<div class="block">Load icon from a given url.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns cloned instance of this icon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load icon from a file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#doNotScale()">doNotScale</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Do not scale this icon by screen dpi.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconHeight()">getIconHeight</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconWidth()">getIconWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImage()">getImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLocation()">getLocation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getURL()">getURL</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImage(java.awt.Image)">setImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toImageIcon(com.nomagic.ui.ResizableIcon)">toImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert given icon to a ImageIcon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toImageIcon(com.nomagic.ui.ResizableIcon,int,int)">toImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert given icon to a ImageIcon of given width and height.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toImageIcon(javax.swing.Icon)">toImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert given icon to a ImageIcon.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="&lt;init&gt;(java.awt.Image)">
<h3>ScalableImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalableImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</span></div>
<div class="block">Wrap given image and use it for painting.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(byte[])">
<h3>ScalableImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalableImageIcon</span><wbr/><span class="parameters">(byte[] imageData)</span></div>
<div class="block">Load icon from given bytes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageData</code> - image bytes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(byte[],java.net.URI)">
<h3>ScalableImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalableImageIcon</span><wbr/><span class="parameters">(byte[] imageData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri)</span></div>
<div class="block">Load icon from given bytes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageData</code> - image bytes</dd>
<dd><code>uri</code> - uri describing the bytes (format etc.)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.net.URL)">
<h3>ScalableImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalableImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Load icon from a given url.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.String)">
<h3>ScalableImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalableImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span></div>
<div class="block">Load icon from a resources of given class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - class</dd>
<dd><code>location</code> - resources location relative to a given class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.String,boolean)">
<h3>ScalableImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScalableImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location,
 boolean silent)</span></div>
<div class="block">Load icon from a resources of given class.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - class</dd>
<dd><code>location</code> - resources location relative to a given class</dd>
<dd><code>silent</code> - if true, does not report to log file about missing icon at given location</dd>
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
<section class="detail" id="create(java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Load icon from a file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - file name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintIcon(java.awt.Component,java.awt.Graphics,int,int)">
<h3>paintIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)" title="class or interface in javax.swing">paintIcon</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)" title="class or interface in javax.swing">paintIcon</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></dd>
</dl>
</section>
</li>
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
<section class="detail" id="getIconHeight()">
<h3>getIconHeight</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIconHeight</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight()" title="class or interface in javax.swing">getIconHeight</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconHeight()" title="class or interface in javax.swing">getIconHeight</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></dd>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconWidth()" title="class or interface in javax.swing">getIconWidth</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImage(java.awt.Image)">
<h3>setImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImage</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#setImage(java.awt.Image)" title="class or interface in javax.swing">setImage</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImage()">
<h3>getImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></span> <span class="element-name">getImage</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html#getImage()" title="class or interface in javax.swing">getImage</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocation()">
<h3>getLocation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocation</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getLocation</code> in interface <code>com.dassault_systemes.modeler.foundation.icons.LocatableIcon</code></dd>
<dt>Returns:</dt>
<dd>location of resource if icon is loaded from resources of some class. Null otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURL()">
<h3>getURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></span> <span class="element-name">getURL</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>url if icon is loaded from url. Null otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="ResizableIcon.html#clone()">ResizableIcon</a></code></span></div>
<div class="block">Returns cloned instance of this icon.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ResizableIcon.html#clone()">clone</a></code> in interface <code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>cloned instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doNotScale()">
<h3>doNotScale</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">doNotScale</span>()</div>
<div class="block">Do not scale this icon by screen dpi. This method has effect only if ScalableImageIcon was just created and image was not loaded yet.</div>
</section>
</li>
<li>
<section class="detail" id="toImageIcon(com.nomagic.ui.ResizableIcon,int,int)">
<h3>toImageIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></span> <span class="element-name">toImageIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</span></div>
<div class="block">Convert given icon to a ImageIcon of given width and height. Same icon is returned if it is already ImageIcon and has same size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon to convert</dd>
<dd><code>width</code> - icon width</dd>
<dd><code>height</code> - icon height</dd>
<dt>Returns:</dt>
<dd>converted icon or same icon if it is already suitable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toImageIcon(javax.swing.Icon)">
<h3>toImageIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></span> <span class="element-name">toImageIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="block">Convert given icon to a ImageIcon. Same icon is returned if it is already ImageIcon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon to convert</dd>
<dt>Returns:</dt>
<dd>converted icon or same icon if it is already suitable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toImageIcon(com.nomagic.ui.ResizableIcon)">
<h3>toImageIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></span> <span class="element-name">toImageIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Convert given icon to a ImageIcon. Same icon is returned if it is already ImageIcon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon to convert</dd>
<dt>Returns:</dt>
<dd>converted icon or same icon if it is already suitable</dd>
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
