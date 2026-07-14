# JAVA OPENAPI: SwingImageIcon (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/ui/SwingImageIcon.html
- source_path: `com/nomagic/ui/SwingImageIcon.html`
- source_sha256: `f63cd10853eefc4b66e515e7b32dc6a1e35e929ce055cc583462b46d9d7ca61e`
- captured_utc: `2026-07-14T16:56:03.764550+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class SwingImageIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[javax.swing.ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)
com.nomagic.ui.SwingImageIcon

All Implemented Interfaces:
`[ResizableIcon](ResizableIcon.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Accessible](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/accessibility/Accessible.html)`, `[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`

@OpenApiAll
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public classSwingImageIcon
extends [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)
implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [ResizableIcon](ResizableIcon.html)

Deprecated.
use [`ScalableImageIcon`](ScalableImageIcon.html)

Extended version of javax.swing.ImageIcon with some utility methods.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.ui.SwingImageIcon)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#component), [tracker](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SwingImageIcon](#%3Cinit%3E(byte%5B%5D,java.lang.String))(byte[] imageData,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)`
Deprecated.
Construct icon from image data
`[SwingImageIcon](#%3Cinit%3E(java.awt.Image))([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image)`
Deprecated.
Constructs a new ImageIcon instance.
`[SwingImageIcon](#%3Cinit%3E(java.lang.Class,java.lang.String))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) location)`
Deprecated.
Construct image from resources available to class loader of given class at given location
`[SwingImageIcon](#%3Cinit%3E(java.lang.Class,java.lang.String,boolean))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) location,
 boolean silent)`
Deprecated.
Construct image from resources available to class loader of given class at given location
`[SwingImageIcon](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) file)`
Deprecated.
Construct image from file
`[SwingImageIcon](#%3Cinit%3E(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) url)`
Deprecated.
Construct image from url
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[clone](#clone())()`
Deprecated.
Returns cloned instance of this icon.
`static [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)`
`[createImageIcon](#createImageIcon(com.nomagic.ui.ResizableIcon,int,int))([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)`
Deprecated.
Create image icon of given size from given icon
`static [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)`
`[createImageIcon](#createImageIcon(java.awt.Component,javax.swing.Icon))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Deprecated.
Utility method to create an image icon from given icon
`static [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)`
`[createImageIcon](#createImageIcon(javax.swing.Icon,int,int))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int width,
 int height)`
Deprecated.
Create image icon of given size from given icon
`static [ResizableIcon](ResizableIcon.html)`
`[createScaledInstance](#createScaledInstance(com.nomagic.ui.ResizableIcon,int))([ResizableIcon](ResizableIcon.html) icon,
 int size)`
Deprecated.
Utility method to create a scaled instance of given icon
`static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[createScaledInstance](#createScaledInstance(javax.swing.Icon,int))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int size)`
Deprecated.
Utility method to create a scaled instance of given icon
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLocation](#getLocation())()`
Deprecated.
`[URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html)`
`[getURL](#getURL())()`
Deprecated.
`void`
`[paintIcon](#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y,
 int w,
 int h)`
Deprecated.
Draw the icon in the given bounds.
Methods inherited from class javax.swing.[ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html)
`[getAccessibleContext](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()), [getDescription](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()), [getIconHeight](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconHeight()), [getIconWidth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconWidth()), [getImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getImage()), [getImageLoadStatus](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()), [getImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()), [loadImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)), [paintIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)), [setDescription](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)), [setImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#setImage(java.awt.Image)), [setImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface javax.swing.[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)
`[getIconHeight](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight()), [getIconWidth](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth()), [paintIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SwingImageIcon
public SwingImageIcon([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image)
Deprecated.
Constructs a new ImageIcon instance.
SwingImageIcon
public SwingImageIcon(byte[] imageData,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description)
Deprecated.
Construct icon from image data
Parameters:
`imageData` - image data
`description` - description
SwingImageIcon
public SwingImageIcon([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) file)
Deprecated.
Construct image from file
Parameters:
`file` - file
SwingImageIcon
public SwingImageIcon([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) url)
Deprecated.
Construct image from url
Parameters:
`url` - url
SwingImageIcon
public SwingImageIcon([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) location)
Deprecated.
Construct image from resources available to class loader of given class at given location
Parameters:
`clazz` - class
`location` - location
SwingImageIcon
public SwingImageIcon([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) location,
 boolean silent)
Deprecated.
Construct image from resources available to class loader of given class at given location
Parameters:
`clazz` - class
`location` - location
`silent` - if true, does not report to log file about missing icon at given location
 ============ METHOD DETAIL ========== 
Method Details
paintIcon
public void paintIcon([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y,
 int w,
 int h)
Deprecated.
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
getLocation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLocation()
Deprecated.
Returns:
location
getURL
public [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) getURL()
Deprecated.
Returns:
url
clone
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) clone()
Deprecated.
Description copied from interface: `[ResizableIcon](ResizableIcon.html#clone())`
Returns cloned instance of this icon.
Specified by:
`[clone](ResizableIcon.html#clone())` in interface `[ResizableIcon](ResizableIcon.html)`
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
cloned instance.
createScaledInstance
public static [ResizableIcon](ResizableIcon.html) createScaledInstance([ResizableIcon](ResizableIcon.html) icon,
 int size)
Deprecated.
Utility method to create a scaled instance of given icon
Parameters:
`icon` - icon
`size` - size
Returns:
scaled icon
createScaledInstance
public static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) createScaledInstance([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int size)
Deprecated.
Utility method to create a scaled instance of given icon
Parameters:
`icon` - icon
`size` - size
Returns:
scaled icon
createImageIcon
public static [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html) createImageIcon(@CheckForNull
 [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 @Nonnull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Deprecated.
Utility method to create an image icon from given icon
Parameters:
`component` - owner of icon
`icon` - icon
Returns:
scaled icon
createImageIcon
public static [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html) createImageIcon([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 int width,
 int height)
Deprecated.
Create image icon of given size from given icon
Parameters:
`icon` - icon
`width` - width
`height` - height
Returns:
image icon
createImageIcon
public static [ImageIcon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html) createImageIcon([ResizableIcon](ResizableIcon.html) icon,
 int width,
 int height)
Deprecated.
Create image icon of given size from given icon
Parameters:
`icon` - icon
`width` - width
`height` - height
Returns:
image icon

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class SwingImageIcon">Class SwingImageIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">javax.swing.ImageIcon</a>
<div class="inheritance">com.nomagic.ui.SwingImageIcon</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/accessibility/Accessible.html" title="class or interface in javax.accessibility">Accessible</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SwingImageIcon</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a>, <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="ScalableImageIcon.html" title="class in com.nomagic.ui"><code>ScalableImageIcon</code></a></div>
</div>
<div class="block">Extended version of javax.swing.ImageIcon with some utility methods.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../serialized-form.html#com.nomagic.ui.SwingImageIcon">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-javax.swing.ImageIcon">Fields inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#component" title="class or interface in javax.swing">component</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#tracker" title="class or interface in javax.swing">tracker</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(byte%5B%5D,java.lang.String)">SwingImageIcon</a><wbr/>(byte[] imageData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct icon from image data</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.awt.Image)">SwingImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a new ImageIcon instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.String)">SwingImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from resources available to class loader of given class at given location</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,java.lang.String,boolean)">SwingImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location,
 boolean silent)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from resources available to class loader of given class at given location</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">SwingImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from file</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.net.URL)">SwingImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from url</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns cloned instance of this icon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createImageIcon(com.nomagic.ui.ResizableIcon,int,int)">createImageIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create image icon of given size from given icon</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createImageIcon(java.awt.Component,javax.swing.Icon)">createImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Utility method to create an image icon from given icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createImageIcon(javax.swing.Icon,int,int)">createImageIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create image icon of given size from given icon</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createScaledInstance(com.nomagic.ui.ResizableIcon,int)">createScaledInstance</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Utility method to create a scaled instance of given icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createScaledInstance(javax.swing.Icon,int)">createScaledInstance</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Utility method to create a scaled instance of given icon</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLocation()">getLocation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getURL()">getURL</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">paintIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y,
 int w,
 int h)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Draw the icon in the given bounds.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.ImageIcon">Methods inherited from class javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getAccessibleContext()" title="class or interface in javax.swing">getAccessibleContext</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getDescription()" title="class or interface in javax.swing">getDescription</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconHeight()" title="class or interface in javax.swing">getIconHeight</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getIconWidth()" title="class or interface in javax.swing">getIconWidth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getImage()" title="class or interface in javax.swing">getImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageLoadStatus()" title="class or interface in javax.swing">getImageLoadStatus</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#getImageObserver()" title="class or interface in javax.swing">getImageObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#loadImage(java.awt.Image)" title="class or interface in javax.swing">loadImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)" title="class or interface in javax.swing">paintIcon</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#setDescription(java.lang.String)" title="class or interface in javax.swing">setDescription</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#setImage(java.awt.Image)" title="class or interface in javax.swing">setImage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver)" title="class or interface in javax.swing">setImageObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html#toString()" title="class or interface in javax.swing">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-javax.swing.Icon">Methods inherited from interface javax.swing.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight()" title="class or interface in javax.swing">getIconHeight</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth()" title="class or interface in javax.swing">getIconWidth</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)" title="class or interface in javax.swing">paintIcon</a></code></div>
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
<h3>SwingImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SwingImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a new ImageIcon instance.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(byte[],java.lang.String)">
<h3>SwingImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SwingImageIcon</span><wbr/><span class="parameters">(byte[] imageData,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct icon from image data</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageData</code> - image data</dd>
<dd><code>description</code> - description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>SwingImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SwingImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from file</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.net.URL)">
<h3>SwingImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SwingImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from url</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.String)">
<h3>SwingImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SwingImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from resources available to class loader of given class at given location</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - class</dd>
<dd><code>location</code> - location</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,java.lang.String,boolean)">
<h3>SwingImageIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SwingImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> location,
 boolean silent)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct image from resources available to class loader of given class at given location</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - class</dd>
<dd><code>location</code> - location</dd>
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
<section class="detail" id="paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">
<h3>paintIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y,
 int w,
 int h)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ResizableIcon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">ResizableIcon</a></code></span></div>
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
<section class="detail" id="getLocation()">
<h3>getLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLocation</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>location</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getURL()">
<h3>getURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a></span> <span class="element-name">getURL</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>url</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">clone</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ResizableIcon.html#clone()">ResizableIcon</a></code></span></div>
<div class="block">Returns cloned instance of this icon.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ResizableIcon.html#clone()">clone</a></code> in interface <code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>cloned instance.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createScaledInstance(com.nomagic.ui.ResizableIcon,int)">
<h3>createScaledInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">createScaledInstance</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int size)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Utility method to create a scaled instance of given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createScaledInstance(javax.swing.Icon,int)">
<h3>createScaledInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">createScaledInstance</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int size)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Utility method to create a scaled instance of given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageIcon(java.awt.Component,javax.swing.Icon)">
<h3>createImageIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></span> <span class="element-name">createImageIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 @Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Utility method to create an image icon from given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>component</code> - owner of icon</dd>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageIcon(javax.swing.Icon,int,int)">
<h3>createImageIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></span> <span class="element-name">createImageIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 int width,
 int height)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create image icon of given size from given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dd><code>width</code> - width</dd>
<dd><code>height</code> - height</dd>
<dt>Returns:</dt>
<dd>image icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageIcon(com.nomagic.ui.ResizableIcon,int,int)">
<h3>createImageIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/ImageIcon.html" title="class or interface in javax.swing">ImageIcon</a></span> <span class="element-name">createImageIcon</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int width,
 int height)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create image icon of given size from given icon</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dd><code>width</code> - width</dd>
<dd><code>height</code> - height</dd>
<dt>Returns:</dt>
<dd>image icon</dd>
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
