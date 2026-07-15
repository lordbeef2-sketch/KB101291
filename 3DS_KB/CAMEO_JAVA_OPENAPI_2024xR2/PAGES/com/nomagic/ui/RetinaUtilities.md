# JAVA OPENAPI: RetinaUtilities (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/ui/RetinaUtilities.html
- source_path: `com/nomagic/ui/RetinaUtilities.html`
- source_sha256: `b9b9664a9cfdd9d1a79f58759973d7227c821ad800b84e00e34671e537152bed`
- captured_utc: `2026-07-14T16:56:03.705549+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class RetinaUtilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.RetinaUtilities

@OpenApiAllpublic classRetinaUtilities
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Utilities to work with icons and images on Retina display on Mac.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RetinaUtilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[createCursor](#createCursor(javax.swing.Icon,java.awt.Point,java.lang.String))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)`
Creates a cursor from a given icon.
`static [ScalableImageIcon](ScalableImageIcon.html)`
`[createIcon](#createIcon(java.awt.Image))([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image)`
Create retina friendly image icon from a given image.
`static [BufferedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html)`
`[createImage](#createImage(int,int,int))(int width,
 int height,
 int type)`
Create retina friendly buffered image if retina is enabled.
`static [Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html)`
`[createMultiResolutionImage](#createMultiResolutionImage(byte%5B%5D,byte%5B%5D))(byte[] smallIconData,
 byte[] largeIconData)`
Create a multi resolution friendly image from a pair of given images - small (regular) and large one.
`static [Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html)`
`[createMultiResolutionImage](#createMultiResolutionImage(java.awt.image.RenderedImage,java.awt.image.RenderedImage))([RenderedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html) smallImage,
 [RenderedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html) largeImage)`
Create a multi resolution friendly image from a pair of given images - small (regular) and large one.
`static int`
`[getRetinaScaling](#getRetinaScaling())()`
Retrieve retina scaling factor from a default screen device.
`static boolean`
`[isMultiResolutionToolkitImage](#isMultiResolutionToolkitImage(java.awt.Image))([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image)`

`static boolean`
`[isRetinaScalingDefined](#isRetinaScalingDefined())()`

`static void`
`[paintRetinaImage](#paintRetinaImage(java.awt.Image,java.awt.image.ImageObserver,java.awt.Graphics,int,int))([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) img,
 [ImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html) observer,
 [Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y)`
Paint given retina image on the graphics.
`static double`
`[scaleDown](#scaleDown(double))(double size)`
Scale given size by retina factor.
`static double`
`[scaleUp](#scaleUp(double))(double size)`
Scale size
`static int`
`[scaleUp](#scaleUp(int))(int size)`
Scale given size by retina factor.
`static [Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html)`
`[toMultiResolutionImage](#toMultiResolutionImage(javax.swing.Icon,javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) smallIcon,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) largeIcon)`
Create a multi resolution friendly image from a pair of given icons - small (regular) and large one.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RetinaUtilities
public RetinaUtilities()
 ============ METHOD DETAIL ========== 
Method Details
isRetinaScalingDefined
public static boolean isRetinaScalingDefined()
Returns:
true if retina is used on the primary display
getRetinaScaling
public static int getRetinaScaling()
Retrieve retina scaling factor from a default screen device.
Returns:
retina scaling factor. 1 if retina is not available, 2 if retina is available.
See Also:
[`GraphicsEnvironment.getDefaultScreenDevice()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/GraphicsEnvironment.html#getDefaultScreenDevice())
scaleUp
public static int scaleUp(int size)
Scale given size by retina factor.
Parameters:
`size` - size
Returns:
scaled size
scaleUp
public static double scaleUp(double size)
Scale size
Parameters:
`size` - size
Returns:
scaled size
scaleDown
public static double scaleDown(double size)
Scale given size by retina factor.
Parameters:
`size` - size
Returns:
scaled size
createImage
public static [BufferedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html) createImage(int width,
 int height,
 int type)
Create retina friendly buffered image if retina is enabled.
 Actual size of returned image is scaled up by retina scale factor (twice bigger).
 Image will
Parameters:
`width` - width
`height` - height
`type` - image type
Returns:
image
createIcon
public static [ScalableImageIcon](ScalableImageIcon.html) createIcon([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image)
Create retina friendly image icon from a given image.
Parameters:
`image` - image
Returns:
retina icon or simple icon if retina is not available
See Also:
[`RetinaImageIcon`](RetinaImageIcon.html)
createCursor
public static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) createCursor([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)
Creates a cursor from a given icon. Multi-resolution image is created from a given icon and that image is used for a cursor.
Parameters:
`icon` - the given icon
`pt` - the hot point
`cursorName` - the cursor name
Returns:
cursor
See Also:
[`toMultiResolutionImage(javax.swing.Icon, javax.swing.Icon)`](#toMultiResolutionImage(javax.swing.Icon,javax.swing.Icon))
paintRetinaImage
public static void paintRetinaImage([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) img,
 @CheckForNull
 [ImageObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html) observer,
 [Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y)
Paint given retina image on the graphics. Retina image is twice bigger than normal, so painting will apply 0.5 scale on the graphics.
Parameters:
`img` - image
`observer` - component
`g` - graphics
`x` - x
`y` - y
createMultiResolutionImage
public static [Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) createMultiResolutionImage([RenderedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html) smallImage,
 [RenderedImage](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html) largeImage)
Create a multi resolution friendly image from a pair of given images - small (regular) and large one.
Parameters:
`smallImage` - small image
`largeImage` - large icon
Returns:
multi-resolution friendly image
See Also:
[`isMultiResolutionToolkitImage(java.awt.Image)`](#isMultiResolutionToolkitImage(java.awt.Image))
createMultiResolutionImage
public static [Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) createMultiResolutionImage(byte[] smallIconData,
 byte[] largeIconData)
Create a multi resolution friendly image from a pair of given images - small (regular) and large one.
Parameters:
`smallIconData` - small image data
`largeIconData` - large image data
Returns:
multi-resolution friendly image
See Also:
[`isMultiResolutionToolkitImage(java.awt.Image)`](#isMultiResolutionToolkitImage(java.awt.Image))
toMultiResolutionImage
public static [Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) toMultiResolutionImage([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) smallIcon,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) largeIcon)
Create a multi resolution friendly image from a pair of given icons - small (regular) and large one.
 If small icon is an ImageIcon, and it's image is multi-resolution friendly, that image is returned.
Parameters:
`smallIcon` - small icon
`largeIcon` - large icon
Returns:
multi-resolution friendly image
See Also:
[`isMultiResolutionToolkitImage(java.awt.Image)`](#isMultiResolutionToolkitImage(java.awt.Image))
isMultiResolutionToolkitImage
public static boolean isMultiResolutionToolkitImage([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image)
Parameters:
`image` - image
Returns:
true if given image is instance of sun.awt.image.MultiResolutionToolkitImage

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class RetinaUtilities">Class RetinaUtilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.RetinaUtilities</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RetinaUtilities</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utilities to work with icons and images on Retina display on Mac.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RetinaUtilities</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCursor(javax.swing.Icon,java.awt.Point,java.lang.String)">createCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a cursor from a given icon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createIcon(java.awt.Image)">createIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create retina friendly image icon from a given image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createImage(int,int,int)">createImage</a><wbr/>(int width,
 int height,
 int type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create retina friendly buffered image if retina is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiResolutionImage(byte%5B%5D,byte%5B%5D)">createMultiResolutionImage</a><wbr/>(byte[] smallIconData,
 byte[] largeIconData)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a multi resolution friendly image from a pair of given images - small (regular) and large one.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiResolutionImage(java.awt.image.RenderedImage,java.awt.image.RenderedImage)">createMultiResolutionImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html" title="class or interface in java.awt.image">RenderedImage</a> smallImage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html" title="class or interface in java.awt.image">RenderedImage</a> largeImage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a multi resolution friendly image from a pair of given images - small (regular) and large one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRetinaScaling()">getRetinaScaling</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieve retina scaling factor from a default screen device.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMultiResolutionToolkitImage(java.awt.Image)">isMultiResolutionToolkitImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRetinaScalingDefined()">isRetinaScalingDefined</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#paintRetinaImage(java.awt.Image,java.awt.image.ImageObserver,java.awt.Graphics,int,int)">paintRetinaImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> img,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html" title="class or interface in java.awt.image">ImageObserver</a> observer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Paint given retina image on the graphics.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleDown(double)">scaleDown</a><wbr/>(double size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale given size by retina factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleUp(double)">scaleUp</a><wbr/>(double size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale size</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleUp(int)">scaleUp</a><wbr/>(int size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale given size by retina factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toMultiResolutionImage(javax.swing.Icon,javax.swing.Icon)">toMultiResolutionImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> smallIcon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> largeIcon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a multi resolution friendly image from a pair of given icons - small (regular) and large one.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>RetinaUtilities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RetinaUtilities</span>()</div>
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
<section class="detail" id="isRetinaScalingDefined()">
<h3>isRetinaScalingDefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRetinaScalingDefined</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if retina is used on the primary display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRetinaScaling()">
<h3>getRetinaScaling</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getRetinaScaling</span>()</div>
<div class="block">Retrieve retina scaling factor from a default screen device.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>retina scaling factor. 1 if retina is not available, 2 if retina is available.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/GraphicsEnvironment.html#getDefaultScreenDevice()" title="class or interface in java.awt"><code>GraphicsEnvironment.getDefaultScreenDevice()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleUp(int)">
<h3>scaleUp</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">scaleUp</span><wbr/><span class="parameters">(int size)</span></div>
<div class="block">Scale given size by retina factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>scaled size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleUp(double)">
<h3>scaleUp</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">scaleUp</span><wbr/><span class="parameters">(double size)</span></div>
<div class="block">Scale size</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>scaled size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleDown(double)">
<h3>scaleDown</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">scaleDown</span><wbr/><span class="parameters">(double size)</span></div>
<div class="block">Scale given size by retina factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>scaled size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImage(int,int,int)">
<h3>createImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/BufferedImage.html" title="class or interface in java.awt.image">BufferedImage</a></span> <span class="element-name">createImage</span><wbr/><span class="parameters">(int width,
 int height,
 int type)</span></div>
<div class="block">Create retina friendly buffered image if retina is enabled.
 Actual size of returned image is scaled up by retina scale factor (twice bigger).
 Image will</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - width</dd>
<dd><code>height</code> - height</dd>
<dd><code>type</code> - image type</dd>
<dt>Returns:</dt>
<dd>image</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createIcon(java.awt.Image)">
<h3>createIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ScalableImageIcon.html" title="class in com.nomagic.ui">ScalableImageIcon</a></span> <span class="element-name">createIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</span></div>
<div class="block">Create retina friendly image icon from a given image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - image</dd>
<dt>Returns:</dt>
<dd>retina icon or simple icon if retina is not available</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="RetinaImageIcon.html" title="class in com.nomagic.ui"><code>RetinaImageIcon</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCursor(javax.swing.Icon,java.awt.Point,java.lang.String)">
<h3>createCursor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">createCursor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</span></div>
<div class="block">Creates a cursor from a given icon. Multi-resolution image is created from a given icon and that image is used for a cursor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the given icon</dd>
<dd><code>pt</code> - the hot point</dd>
<dd><code>cursorName</code> - the cursor name</dd>
<dt>Returns:</dt>
<dd>cursor</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#toMultiResolutionImage(javax.swing.Icon,javax.swing.Icon)"><code>toMultiResolutionImage(javax.swing.Icon, javax.swing.Icon)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="paintRetinaImage(java.awt.Image,java.awt.image.ImageObserver,java.awt.Graphics,int,int)">
<h3>paintRetinaImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">paintRetinaImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> img,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/ImageObserver.html" title="class or interface in java.awt.image">ImageObserver</a> observer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</span></div>
<div class="block">Paint given retina image on the graphics. Retina image is twice bigger than normal, so painting will apply 0.5 scale on the graphics.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>img</code> - image</dd>
<dd><code>observer</code> - component</dd>
<dd><code>g</code> - graphics</dd>
<dd><code>x</code> - x</dd>
<dd><code>y</code> - y</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiResolutionImage(java.awt.image.RenderedImage,java.awt.image.RenderedImage)">
<h3>createMultiResolutionImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></span> <span class="element-name">createMultiResolutionImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html" title="class or interface in java.awt.image">RenderedImage</a> smallImage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/image/RenderedImage.html" title="class or interface in java.awt.image">RenderedImage</a> largeImage)</span></div>
<div class="block">Create a multi resolution friendly image from a pair of given images - small (regular) and large one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>smallImage</code> - small image</dd>
<dd><code>largeImage</code> - large icon</dd>
<dt>Returns:</dt>
<dd>multi-resolution friendly image</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#isMultiResolutionToolkitImage(java.awt.Image)"><code>isMultiResolutionToolkitImage(java.awt.Image)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiResolutionImage(byte[],byte[])">
<h3>createMultiResolutionImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></span> <span class="element-name">createMultiResolutionImage</span><wbr/><span class="parameters">(byte[] smallIconData,
 byte[] largeIconData)</span></div>
<div class="block">Create a multi resolution friendly image from a pair of given images - small (regular) and large one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>smallIconData</code> - small image data</dd>
<dd><code>largeIconData</code> - large image data</dd>
<dt>Returns:</dt>
<dd>multi-resolution friendly image</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#isMultiResolutionToolkitImage(java.awt.Image)"><code>isMultiResolutionToolkitImage(java.awt.Image)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toMultiResolutionImage(javax.swing.Icon,javax.swing.Icon)">
<h3>toMultiResolutionImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a></span> <span class="element-name">toMultiResolutionImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> smallIcon,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> largeIcon)</span></div>
<div class="block">Create a multi resolution friendly image from a pair of given icons - small (regular) and large one.
 If small icon is an ImageIcon, and it's image is multi-resolution friendly, that image is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>smallIcon</code> - small icon</dd>
<dd><code>largeIcon</code> - large icon</dd>
<dt>Returns:</dt>
<dd>multi-resolution friendly image</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#isMultiResolutionToolkitImage(java.awt.Image)"><code>isMultiResolutionToolkitImage(java.awt.Image)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiResolutionToolkitImage(java.awt.Image)">
<h3>isMultiResolutionToolkitImage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMultiResolutionToolkitImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - image</dd>
<dt>Returns:</dt>
<dd>true if given image is instance of sun.awt.image.MultiResolutionToolkitImage</dd>
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
