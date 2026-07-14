# JAVA OPENAPI: ZoomHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/zoom/ZoomHelper.html
- source_path: `com/nomagic/magicdraw/ui/zoom/ZoomHelper.html`
- source_sha256: `c0b18767d2bcf6728b31162af89169b5337170b9dac7e8ea8a2ce31a0f60de5f`
- captured_utc: `2026-07-14T16:55:53.408435+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.zoom](package-summary.html)

## Class ZoomHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.zoom.ZoomHelper

@OpenApipublic classZoomHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Helper functions to display zoomed GUI components

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final float`
`[MAX_ZOOM](#MAX_ZOOM)`

`static final float`
`[MIN_TABLE_ZOOM](#MIN_TABLE_ZOOM)`
min scale factor for diagrams, that display table components
`static final float`
`[MIN_ZOOM](#MIN_ZOOM)`
Common scale factor range
`static final int[]`
`[TABLE_ZOOM_CHOICES](#TABLE_ZOOM_CHOICES)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ZoomHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static float`
`[calculateZoom](#calculateZoom(float,int,float))(float currentZoomFactor,
 int mouseWheelRotation,
 float zoomStep)`

`static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[calculateZoomedScrollPosition](#calculateZoomedScrollPosition(java.awt.Point,java.awt.Point,float))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) zoomAtPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) currentScrollPosition,
 float zoomChange)`

`static float`
`[calculateZoomFactorToFit](#calculateZoomFactorToFit(java.awt.Dimension,java.awt.Dimension,boolean))([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) componentSize,
 [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) windowSize,
 boolean max1)`

`static [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html)`
`[getOriginalFont](#getOriginalFont(javax.swing.JLabel))([JLabel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html) label)`

`static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getOriginalIcon](#getOriginalIcon(javax.swing.JLabel))([JLabel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html) label)`

`static int`
`[getOriginalSize](#getOriginalSize(int,float))(int scaledSize,
 float zoomFactor)`
Opposite method to [`getScaledSize(int, float)`](#getScaledSize(int,float)).
`static [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html)`
`[getScaledFont](#getScaledFont(java.awt.Font,float))([Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) font,
 float zoomFactor)`
Takes the provided font and scales it's size by the given zoomFactor.
`static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getScaledIcon](#getScaledIcon(javax.swing.Icon,float))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 float zoomFactor)`
Takes the provided icon and scales it's size by the given zoomFactor.
`static int`
`[getScaledSize](#getScaledSize(int,float))(int size,
 float zoomFactor)`
Takes the provided integer and scales (multiplies) it by the given zoomFactor.
`static int`
`[getScaledSizeRounded](#getScaledSizeRounded(int,float))(int size,
 float zoomFactor)`

`static [Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html)`
`[increaseSmallFontReadability](#increaseSmallFontReadability(java.awt.Graphics))([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g)`
Modify graphics to provide increased readability of very small fonts
`static boolean`
`[isScalingRequired](#isScalingRequired(float))(float zoomFactor)`
Checks if zoomFactor is positive and not equal to one
`static float`
`[roundZoom](#roundZoom(double))(double zoomFactor)`
Fix float precision problems by rounding zoomFactor to 4 decimal places
`static float`
`[validateZoom](#validateZoom(float))(float zoomFactor)`
Validates given zoom value by the default min max values
`static float`
`[validateZoom](#validateZoom(float,float,float))(float zoomFactor,
 float minZoom,
 float maxZoom)`

`static boolean`
`[zoomComponent](#zoomComponent(java.awt.Component,float))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 float zoomFactor)`
If component implements [`Zoomable`](Zoomable.html) interface, zooms the component by the given factor.
`static boolean`
`[zoomComponents](#zoomComponents(java.awt.Container,float))([Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html) container,
 float zoomFactor)`
Iterates through inner components recursively and zooms all components that implement [`Zoomable`](Zoomable.html) interface.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
MIN_ZOOM
public static final float MIN_ZOOM
Common scale factor range
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.zoom.ZoomHelper.MIN_ZOOM)
MAX_ZOOM
public static final float MAX_ZOOM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.zoom.ZoomHelper.MAX_ZOOM)
MIN_TABLE_ZOOM
public static final float MIN_TABLE_ZOOM
min scale factor for diagrams, that display table components
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.ui.zoom.ZoomHelper.MIN_TABLE_ZOOM)
TABLE_ZOOM_CHOICES
public static final int[] TABLE_ZOOM_CHOICES
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ZoomHelper
public ZoomHelper()
 ============ METHOD DETAIL ========== 
Method Details
getScaledSize
@OpenApipublic static int getScaledSize(int size,
 float zoomFactor)
Takes the provided integer and scales (multiplies) it by the given zoomFactor.
 Trims the floating part of the result down.
Returns:
scaled size
getOriginalSize
@OpenApipublic static int getOriginalSize(int scaledSize,
 float zoomFactor)
Opposite method to [`getScaledSize(int, float)`](#getScaledSize(int,float)).
 Takes the provided scaledSize, which is already scaled by the given zoomFactor and returns the original not scaled size,
 by dividing the scaledSize from zoomFactor.
Returns:
not scaled size
getScaledFont
@OpenApi
@CheckForNullpublic static [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) getScaledFont(@CheckForNull
 [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) font,
 float zoomFactor)
Takes the provided font and scales it's size by the given zoomFactor.
Returns:
scaled font
getScaledIcon
@OpenApi
@CheckForNullpublic static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getScaledIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 float zoomFactor)
Takes the provided icon and scales it's size by the given zoomFactor.
 Icon caching is used to prevent repeated scaling of the same icon and zoomFactor.
Returns:
scaled icon
zoomComponent
@OpenApipublic static boolean zoomComponent([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 float zoomFactor)
If component implements [`Zoomable`](Zoomable.html) interface, zooms the component by the given factor.
 If component does not implement Zoomable, but it is a Container, then looks for Zoomable inner components recursively and zooms each of them.
Returns:
true if component or at least one of it's sub components was zoomed
See Also:
[`zoomComponents(java.awt.Container, float)`](#zoomComponents(java.awt.Container,float))
zoomComponents
@OpenApipublic static boolean zoomComponents([Container](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html) container,
 float zoomFactor)
Iterates through inner components recursively and zooms all components that implement [`Zoomable`](Zoomable.html) interface.
Returns:
true if at least one of Container's inner components is Zoomable
isScalingRequired
public static boolean isScalingRequired(float zoomFactor)
Checks if zoomFactor is positive and not equal to one
Returns:
false if original size should be used
roundZoom
public static float roundZoom(double zoomFactor)
Fix float precision problems by rounding zoomFactor to 4 decimal places
Returns:
zoomFactor rounded with 0.001 precision
validateZoom
public static float validateZoom(float zoomFactor)
Validates given zoom value by the default min max values
Parameters:
`zoomFactor` - given zoom value
Returns:
valid zoom value
validateZoom
public static float validateZoom(float zoomFactor,
 float minZoom,
 float maxZoom)
getScaledSizeRounded
public static int getScaledSizeRounded(int size,
 float zoomFactor)
calculateZoomedScrollPosition
public static [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) calculateZoomedScrollPosition(@CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) zoomAtPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) currentScrollPosition,
 float zoomChange)
Parameters:
`zoomAtPoint` - mouse point at which zooming action occurred
`currentScrollPosition` - current view position of the scroll pane
`zoomChange` - new zoom factor divided from the old (current) zoom factor
Returns:
new point to set as view position of the scroll pane
calculateZoomFactorToFit
public static float calculateZoomFactorToFit([Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) componentSize,
 [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) windowSize,
 boolean max1)
increaseSmallFontReadability
public static [Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) increaseSmallFontReadability([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g)
Modify graphics to provide increased readability of very small fonts
getOriginalIcon
@CheckForNullpublic static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getOriginalIcon([JLabel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html) label)
getOriginalFont
@CheckForNullpublic static [Font](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html) getOriginalFont([JLabel](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html) label)
calculateZoom
public static float calculateZoom(float currentZoomFactor,
 int mouseWheelRotation,
 float zoomStep)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.zoom</a></div>
<h1 class="title" title="Class ZoomHelper">Class ZoomHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.zoom.ZoomHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ZoomHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helper functions to display zoomed GUI components</div>
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
<div class="col-first even-row-color"><code>static final float</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MAX_ZOOM">MAX_ZOOM</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final float</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MIN_TABLE_ZOOM">MIN_TABLE_ZOOM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">min scale factor for diagrams, that display table components</div>
</div>
<div class="col-first even-row-color"><code>static final float</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MIN_ZOOM">MIN_ZOOM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Common scale factor range</div>
</div>
<div class="col-first odd-row-color"><code>static final int[]</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TABLE_ZOOM_CHOICES">TABLE_ZOOM_CHOICES</a></code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ZoomHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateZoom(float,int,float)">calculateZoom</a><wbr/>(float currentZoomFactor,
 int mouseWheelRotation,
 float zoomStep)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateZoomedScrollPosition(java.awt.Point,java.awt.Point,float)">calculateZoomedScrollPosition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> zoomAtPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> currentScrollPosition,
 float zoomChange)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateZoomFactorToFit(java.awt.Dimension,java.awt.Dimension,boolean)">calculateZoomFactorToFit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> componentSize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> windowSize,
 boolean max1)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalFont(javax.swing.JLabel)">getOriginalFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html" title="class or interface in javax.swing">JLabel</a> label)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalIcon(javax.swing.JLabel)">getOriginalIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html" title="class or interface in javax.swing">JLabel</a> label)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalSize(int,float)">getOriginalSize</a><wbr/>(int scaledSize,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opposite method to <a href="#getScaledSize(int,float)"><code>getScaledSize(int, float)</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledFont(java.awt.Font,float)">getScaledFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Takes the provided font and scales it's size by the given zoomFactor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledIcon(javax.swing.Icon,float)">getScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Takes the provided icon and scales it's size by the given zoomFactor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledSize(int,float)">getScaledSize</a><wbr/>(int size,
 float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Takes the provided integer and scales (multiplies) it by the given zoomFactor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledSizeRounded(int,float)">getScaledSizeRounded</a><wbr/>(int size,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#increaseSmallFontReadability(java.awt.Graphics)">increaseSmallFontReadability</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Modify graphics to provide increased readability of very small fonts</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isScalingRequired(float)">isScalingRequired</a><wbr/>(float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if zoomFactor is positive and not equal to one</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#roundZoom(double)">roundZoom</a><wbr/>(double zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Fix float precision problems by rounding zoomFactor to 4 decimal places</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#validateZoom(float)">validateZoom</a><wbr/>(float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Validates given zoom value by the default min max values</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#validateZoom(float,float,float)">validateZoom</a><wbr/>(float zoomFactor,
 float minZoom,
 float maxZoom)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zoomComponent(java.awt.Component,float)">zoomComponent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If component implements <a href="Zoomable.html" title="interface in com.nomagic.magicdraw.ui.zoom"><code>Zoomable</code></a> interface, zooms the component by the given factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zoomComponents(java.awt.Container,float)">zoomComponents</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Iterates through inner components recursively and zooms all components that implement <a href="Zoomable.html" title="interface in com.nomagic.magicdraw.ui.zoom"><code>Zoomable</code></a> interface.</div>
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
<section class="detail" id="MIN_ZOOM">
<h3>MIN_ZOOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">float</span> <span class="element-name">MIN_ZOOM</span></div>
<div class="block">Common scale factor range</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.zoom.ZoomHelper.MIN_ZOOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MAX_ZOOM">
<h3>MAX_ZOOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">float</span> <span class="element-name">MAX_ZOOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.zoom.ZoomHelper.MAX_ZOOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MIN_TABLE_ZOOM">
<h3>MIN_TABLE_ZOOM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">float</span> <span class="element-name">MIN_TABLE_ZOOM</span></div>
<div class="block">min scale factor for diagrams, that display table components</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.ui.zoom.ZoomHelper.MIN_TABLE_ZOOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TABLE_ZOOM_CHOICES">
<h3>TABLE_ZOOM_CHOICES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int[]</span> <span class="element-name">TABLE_ZOOM_CHOICES</span></div>
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
<h3>ZoomHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ZoomHelper</span>()</div>
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
<section class="detail" id="getScaledSize(int,float)">
<h3>getScaledSize</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getScaledSize</span><wbr/><span class="parameters">(int size,
 float zoomFactor)</span></div>
<div class="block">Takes the provided integer and scales (multiplies) it by the given zoomFactor.
 Trims the floating part of the result down.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scaled size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOriginalSize(int,float)">
<h3>getOriginalSize</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getOriginalSize</span><wbr/><span class="parameters">(int scaledSize,
 float zoomFactor)</span></div>
<div class="block">Opposite method to <a href="#getScaledSize(int,float)"><code>getScaledSize(int, float)</code></a>.
 Takes the provided scaledSize, which is already scaled by the given zoomFactor and returns the original not scaled size,
 by dividing the scaledSize from zoomFactor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>not scaled size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScaledFont(java.awt.Font,float)">
<h3>getScaledFont</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></span> <span class="element-name">getScaledFont</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 float zoomFactor)</span></div>
<div class="block">Takes the provided font and scales it's size by the given zoomFactor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scaled font</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScaledIcon(javax.swing.Icon,float)">
<h3>getScaledIcon</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getScaledIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 float zoomFactor)</span></div>
<div class="block">Takes the provided icon and scales it's size by the given zoomFactor.
 Icon caching is used to prevent repeated scaling of the same icon and zoomFactor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="zoomComponent(java.awt.Component,float)">
<h3>zoomComponent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">zoomComponent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 float zoomFactor)</span></div>
<div class="block">If component implements <a href="Zoomable.html" title="interface in com.nomagic.magicdraw.ui.zoom"><code>Zoomable</code></a> interface, zooms the component by the given factor.
 If component does not implement Zoomable, but it is a Container, then looks for Zoomable inner components recursively and zooms each of them.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if component or at least one of it's sub components was zoomed</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#zoomComponents(java.awt.Container,float)"><code>zoomComponents(java.awt.Container, float)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="zoomComponents(java.awt.Container,float)">
<h3>zoomComponents</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">zoomComponents</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 float zoomFactor)</span></div>
<div class="block">Iterates through inner components recursively and zooms all components that implement <a href="Zoomable.html" title="interface in com.nomagic.magicdraw.ui.zoom"><code>Zoomable</code></a> interface.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if at least one of Container's inner components is Zoomable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isScalingRequired(float)">
<h3>isScalingRequired</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isScalingRequired</span><wbr/><span class="parameters">(float zoomFactor)</span></div>
<div class="block">Checks if zoomFactor is positive and not equal to one</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>false if original size should be used</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="roundZoom(double)">
<h3>roundZoom</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">roundZoom</span><wbr/><span class="parameters">(double zoomFactor)</span></div>
<div class="block">Fix float precision problems by rounding zoomFactor to 4 decimal places</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>zoomFactor rounded with 0.001 precision</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="validateZoom(float)">
<h3>validateZoom</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">validateZoom</span><wbr/><span class="parameters">(float zoomFactor)</span></div>
<div class="block">Validates given zoom value by the default min max values</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zoomFactor</code> - given zoom value</dd>
<dt>Returns:</dt>
<dd>valid zoom value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="validateZoom(float,float,float)">
<h3>validateZoom</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">validateZoom</span><wbr/><span class="parameters">(float zoomFactor,
 float minZoom,
 float maxZoom)</span></div>
</section>
</li>
<li>
<section class="detail" id="getScaledSizeRounded(int,float)">
<h3>getScaledSizeRounded</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">getScaledSizeRounded</span><wbr/><span class="parameters">(int size,
 float zoomFactor)</span></div>
</section>
</li>
<li>
<section class="detail" id="calculateZoomedScrollPosition(java.awt.Point,java.awt.Point,float)">
<h3>calculateZoomedScrollPosition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">calculateZoomedScrollPosition</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> zoomAtPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> currentScrollPosition,
 float zoomChange)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zoomAtPoint</code> - mouse point at which zooming action occurred</dd>
<dd><code>currentScrollPosition</code> - current view position of the scroll pane</dd>
<dd><code>zoomChange</code> - new zoom factor divided from the old (current) zoom factor</dd>
<dt>Returns:</dt>
<dd>new point to set as view position of the scroll pane</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateZoomFactorToFit(java.awt.Dimension,java.awt.Dimension,boolean)">
<h3>calculateZoomFactorToFit</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">calculateZoomFactorToFit</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> componentSize,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> windowSize,
 boolean max1)</span></div>
</section>
</li>
<li>
<section class="detail" id="increaseSmallFontReadability(java.awt.Graphics)">
<h3>increaseSmallFontReadability</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a></span> <span class="element-name">increaseSmallFontReadability</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g)</span></div>
<div class="block">Modify graphics to provide increased readability of very small fonts</div>
</section>
</li>
<li>
<section class="detail" id="getOriginalIcon(javax.swing.JLabel)">
<h3>getOriginalIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getOriginalIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html" title="class or interface in javax.swing">JLabel</a> label)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOriginalFont(javax.swing.JLabel)">
<h3>getOriginalFont</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></span> <span class="element-name">getOriginalFont</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JLabel.html" title="class or interface in javax.swing">JLabel</a> label)</span></div>
</section>
</li>
<li>
<section class="detail" id="calculateZoom(float,int,float)">
<h3>calculateZoom</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">calculateZoom</span><wbr/><span class="parameters">(float currentZoomFactor,
 int mouseWheelRotation,
 float zoomStep)</span></div>
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
