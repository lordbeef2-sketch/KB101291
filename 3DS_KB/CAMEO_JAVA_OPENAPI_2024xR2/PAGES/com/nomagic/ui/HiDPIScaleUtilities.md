# JAVA OPENAPI: HiDPIScaleUtilities (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/ui/HiDPIScaleUtilities.html
- source_path: `com/nomagic/ui/HiDPIScaleUtilities.html`
- source_sha256: `894667b89c0dd9823b62cd1d429fda358932348e0e25fadca3bfa03f6df1ed65`
- captured_utc: `2026-07-14T16:56:03.503548+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class HiDPIScaleUtilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.HiDPIScaleUtilitiesInternal
com.nomagic.ui.HiDPIScaleUtilities

@OpenApiAllpublic classHiDPIScaleUtilities
extends com.nomagic.ui.HiDPIScaleUtilitiesInternal
Utilities to work with various scaling aspects on HiDPI screens.
 These utilities do not have any affect on Mac Retina screens. On Retina screens [`RetinaUtilities`](RetinaUtilities.html) should be used.
 There are two types of scaling factors: system and user.
 System scaling factor is managed by JVM. If it is enabled - graphics is scaled automatically.
 System Scaling factor is calculated using [`Toolkit.getScreenResolution()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Toolkit.html#getScreenResolution()) value.
 User scaling factor is defined by user supplying jvm argument magicdraw.resolution.scale. For example -Dmagicdraw.resolution.scale=2 means scale ui two times.
 Both scaling factors has multiplicative relation, ui is scaled by both scaling factors.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HI_DPI_SCALED](#HI_DPI_SCALED)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[HiDPIScaleUtilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[addHiDPIScaledProperty](#addHiDPIScaledProperty(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)`
Mark this component as HiDPI scaled
`static void`
`[adjustFontByLookAndFeelDefaults](#adjustFontByLookAndFeelDefaults(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)`
Apply L&F default font group if this is Windows L&F
`static float`
`[calculateSystemScaleFactor](#calculateSystemScaleFactor())()`
Calculates system scaling factor.
`static void`
`[fixWindowsFonts](#fixWindowsFonts())()`

`static [ResizableIcon](ResizableIcon.html)`
`[getNonScaledIcon](#getNonScaledIcon(com.nomagic.ui.ResizableIcon,int,double))([ResizableIcon](ResizableIcon.html) icon,
 int size,
 double maxScale)`
Return icon scaled down to a given size.
`static double`
`[getReducedScalingFactor](#getReducedScalingFactor())()`
Deprecated.
use getReducedUserScalingFactor()
`static double`
`[getReducedUserScalingFactor](#getReducedUserScalingFactor())()`
In some cased real scaling scales UI too much.
`static [ResizableIcon](ResizableIcon.html)`
`[getScaled16x16Icon](#getScaled16x16Icon(com.nomagic.ui.ResizableIcon))([ResizableIcon](ResizableIcon.html) icon)`
Return scaled to 16x16 icon for a given icon.
`static float`
`[getScaleFactorByScreenResolution](#getScaleFactorByScreenResolution())()`
Deprecated.
use calculateSystemScaleFactor()
`static double`
`[getScalingFactor](#getScalingFactor())()`
Deprecated.
use getUserScalingFactor()
`static [ResizableIcon](ResizableIcon.html)`
`[getSystemScaled16x16Icon](#getSystemScaled16x16Icon(com.nomagic.ui.ResizableIcon))([ResizableIcon](ResizableIcon.html) icon)`

`static [ResizableIcon](ResizableIcon.html)`
`[getSystemScaledIcon](#getSystemScaledIcon(com.nomagic.ui.ResizableIcon))([ResizableIcon](ResizableIcon.html) icon)`
Return resizable icon scaled by system scale factor.
`static double`
`[getSystemScaleFactor](#getSystemScaleFactor())()`
System scale factor.
`static double`
`[getUserScalingFactor](#getUserScalingFactor())()`
User scale factor.
`static boolean`
`[isScalingFactorDefined](#isScalingFactorDefined())()`
Checks if system or user scaling factor is defined.
`static boolean`
`[isScalingFactorFromProperty](#isScalingFactorFromProperty())()`
Deprecated.
isUserScalingFactorDefined()
`static boolean`
`[isSystemScalingEnabled](#isSystemScalingEnabled())()`
Checks if system scaling is enabled.
`static boolean`
`[isUserScalingFactorDefined](#isUserScalingFactorDefined())()`
Checks if user scaling factor is defined by jvm argument magicdraw.resolution.scale.
`static boolean`
`[isWindowsLookAndFeel](#isWindowsLookAndFeel())()`
Check if Windows Look and Feel is active.
`static double`
`[scaleByComponent](#scaleByComponent(java.awt.Component,double))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 double value)`

`static int`
`[scaleByComponent](#scaleByComponent(java.awt.Component,int))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 int value)`

`static void`
`[scaleComponent](#scaleComponent(com.nomagic.ui.HiDPIScalableComponent))([HiDPIScalableComponent](HiDPIScalableComponent.html) component)`
Scale components and its children preferred size and similar.
`static float`
`[scaleDownFont](#scaleDownFont(float))(float size)`
Scale font size down.
`static float`
`[scaleFont](#scaleFont(float))(float size)`
Scale font size.
`static int`
`[scaleIcon](#scaleIcon(int))(int size)`
Scale Icon size.
`static void`
`[scaleLookAndFeel](#scaleLookAndFeel())()`
Scale various java Look&Feel settings like fonts, icons sizes, insets and etc.
`static double`
`[scaleUI](#scaleUI(double))(double size)`
Scale User Interface item size.
`static int`
`[scaleUI](#scaleUI(int))(int size)`
Scale User Interface item size.
`static void`
`[scaleUIRecursively](#scaleUIRecursively(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)`
Scale components and its children preferred size and similar.
`static int`
`[systemScaleValueUp](#systemScaleValueUp(int))(int value)`
Scales given value by system scale factor.
Methods inherited from class com.nomagic.ui.HiDPIScaleUtilitiesInternal
`adjustDimensionForFractionalScale, isScalingFractional`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
HI_DPI_SCALED
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HI_DPI_SCALED
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.ui.HiDPIScaleUtilities.HI_DPI_SCALED)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
HiDPIScaleUtilities
public HiDPIScaleUtilities()
 ============ METHOD DETAIL ========== 
Method Details
isSystemScalingEnabled
public static boolean isSystemScalingEnabled()
Checks if system scaling is enabled.
Returns:
true if system scaling is enabled
getSystemScaleFactor
public static double getSystemScaleFactor()
System scale factor. Scaling factor is calculated using [`Toolkit.getScreenResolution()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Toolkit.html#getScreenResolution()) value.
Returns:
system scaling factor.
systemScaleValueUp
public static int systemScaleValueUp(int value)
Scales given value by system scale factor.
Parameters:
`value` - value to scale
Returns:
scaled value
isWindowsLookAndFeel
public static boolean isWindowsLookAndFeel()
Check if Windows Look and Feel is active.
Returns:
true if Windows Look and Feel is active
getSystemScaled16x16Icon
@CheckForNullpublic static [ResizableIcon](ResizableIcon.html) getSystemScaled16x16Icon(@CheckForNull
 [ResizableIcon](ResizableIcon.html) icon)
getSystemScaledIcon
public static [ResizableIcon](ResizableIcon.html) getSystemScaledIcon([ResizableIcon](ResizableIcon.html) icon)
Return resizable icon scaled by system scale factor.
Parameters:
`icon` - icon to scale
Returns:
scaled icon
getScaled16x16Icon
@CheckForNullpublic static [ResizableIcon](ResizableIcon.html) getScaled16x16Icon(@CheckForNull
 [ResizableIcon](ResizableIcon.html) icon)
Return scaled to 16x16 icon for a given icon. Scaling factor is taken into account, so in scaled environment icon size will be scaled by a scale factor.
 Scaled icons are cached using WeakReferences.
Parameters:
`icon` - icon
Returns:
scaled icon
getNonScaledIcon
@CheckForNullpublic static [ResizableIcon](ResizableIcon.html) getNonScaledIcon(@CheckForNull
 [ResizableIcon](ResizableIcon.html) icon,
 int size,
 double maxScale)
Return icon scaled down to a given size. Scaled icons are cached using WeakReferences.
Parameters:
`icon` - icon
Returns:
icon of given size
See Also:
`SquareIcon.create(ResizableIcon, int, double)`
scaleIcon
public static int scaleIcon(int size)
Scale Icon size.
Parameters:
`size` - size
Returns:
Scaled size or the same value as provided.
scaleUI
public static double scaleUI(double size)
Scale User Interface item size.
Parameters:
`size` - size
Returns:
Scaled size or the same value as provided.
scaleUI
public static int scaleUI(int size)
Scale User Interface item size.
Parameters:
`size` - size
Returns:
Scaled size or the same value as provided.
scaleFont
public static float scaleFont(float size)
Scale font size.
Parameters:
`size` - size
Returns:
Scaled size or the same value as provided.
scaleDownFont
public static float scaleDownFont(float size)
Scale font size down.
Parameters:
`size` - size
Returns:
Scaled size or the same value as provided.
getUserScalingFactor
public static double getUserScalingFactor()
User scale factor. It is defined by jvm argument magicdraw.resolution.scale
Returns:
user scaling factor.
getScalingFactor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static double getScalingFactor()
Deprecated.
use getUserScalingFactor()
User scale factor. It is defined by jvm argument magicdraw.resolution.scale
Returns:
user scaling factor.
getReducedUserScalingFactor
public static double getReducedUserScalingFactor()
In some cased real scaling scales UI too much. This methods returns reduced scaling factor for cases then real scaling scales UI too much.
Returns:
reduced scaling factor
getReducedScalingFactor
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static double getReducedScalingFactor()
Deprecated.
use getReducedUserScalingFactor()
In some cased real scaling scales UI too much. This methods returns reduced scaling factor for cases then real scaling scales UI too much.
Returns:
reduced scaling factor
isScalingFactorDefined
public static boolean isScalingFactorDefined()
Checks if system or user scaling factor is defined.
Returns:
true if system or user scaling factor is defined
isUserScalingFactorDefined
public static boolean isUserScalingFactorDefined()
Checks if user scaling factor is defined by jvm argument magicdraw.resolution.scale.
Returns:
true if user scaling factor is defined
addHiDPIScaledProperty
public static void addHiDPIScaledProperty([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)
Mark this component as HiDPI scaled
Parameters:
`component` - component
scaleComponent
public static void scaleComponent([HiDPIScalableComponent](HiDPIScalableComponent.html) component)
Scale components and its children preferred size and similar.
Parameters:
`component` - component
scaleUIRecursively
public static void scaleUIRecursively([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)
Scale components and its children preferred size and similar.
Parameters:
`component` - component
scaleLookAndFeel
public static void scaleLookAndFeel()
Scale various java Look&Feel settings like fonts, icons sizes, insets and etc.
fixWindowsFonts
public static void fixWindowsFonts()
adjustFontByLookAndFeelDefaults
public static void adjustFontByLookAndFeelDefaults([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)
Apply L&F default font group if this is Windows L&F
isScalingFactorFromProperty
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isScalingFactorFromProperty()
Deprecated.
isUserScalingFactorDefined()
Checks if scaling factor is defined from system property.
Returns:
true if scaling factor is from resolution scale property.
calculateSystemScaleFactor
public static float calculateSystemScaleFactor()
Calculates system scaling factor.
Returns:
scaling factor.
getScaleFactorByScreenResolution
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static float getScaleFactorByScreenResolution()
Deprecated.
use calculateSystemScaleFactor()
Calculates system scaling factor from screen resolution.
Returns:
scaling factor.
scaleByComponent
public static int scaleByComponent([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 int value)
scaleByComponent
public static double scaleByComponent([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component,
 double value)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class HiDPIScaleUtilities">Class HiDPIScaleUtilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.HiDPIScaleUtilitiesInternal
<div class="inheritance">com.nomagic.ui.HiDPIScaleUtilities</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">HiDPIScaleUtilities</span>
<span class="extends-implements">extends com.nomagic.ui.HiDPIScaleUtilitiesInternal</span></div>
<div class="block">Utilities to work with various scaling aspects on HiDPI screens.
 <p>
 These utilities do not have any affect on Mac Retina screens. On Retina screens <a href="RetinaUtilities.html" title="class in com.nomagic.ui"><code>RetinaUtilities</code></a> should be used.
 <p>
<p>
 There are two types of scaling factors: system and user.
 System scaling factor is managed by JVM. If it is enabled - graphics is scaled automatically.
 System Scaling factor is calculated using <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Toolkit.html#getScreenResolution()" title="class or interface in java.awt"><code>Toolkit.getScreenResolution()</code></a> value.
 User scaling factor is defined by user supplying jvm argument magicdraw.resolution.scale. For example -Dmagicdraw.resolution.scale=2 means scale ui two times.
 Both scaling factors has multiplicative relation, ui is scaled by both scaling factors.
 </p></p></p></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HI_DPI_SCALED">HI_DPI_SCALED</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">HiDPIScaleUtilities</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addHiDPIScaledProperty(java.awt.Component)">addHiDPIScaledProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Mark this component as HiDPI scaled</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustFontByLookAndFeelDefaults(java.awt.Component)">adjustFontByLookAndFeelDefaults</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Apply L&amp;F default font group if this is Windows L&amp;F</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateSystemScaleFactor()">calculateSystemScaleFactor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates system scaling factor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fixWindowsFonts()">fixWindowsFonts</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getNonScaledIcon(com.nomagic.ui.ResizableIcon,int,double)">getNonScaledIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int size,
 double maxScale)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return icon scaled down to a given size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getReducedScalingFactor()">getReducedScalingFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getReducedUserScalingFactor()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReducedUserScalingFactor()">getReducedUserScalingFactor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">In some cased real scaling scales UI too much.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaled16x16Icon(com.nomagic.ui.ResizableIcon)">getScaled16x16Icon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return scaled to 16x16 icon for a given icon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getScaleFactorByScreenResolution()">getScaleFactorByScreenResolution</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use calculateSystemScaleFactor()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getScalingFactor()">getScalingFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getUserScalingFactor()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSystemScaled16x16Icon(com.nomagic.ui.ResizableIcon)">getSystemScaled16x16Icon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSystemScaledIcon(com.nomagic.ui.ResizableIcon)">getSystemScaledIcon</a><wbr/>(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return resizable icon scaled by system scale factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSystemScaleFactor()">getSystemScaleFactor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">System scale factor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserScalingFactor()">getUserScalingFactor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">User scale factor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isScalingFactorDefined()">isScalingFactorDefined</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if system or user scaling factor is defined.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isScalingFactorFromProperty()">isScalingFactorFromProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">isUserScalingFactorDefined()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSystemScalingEnabled()">isSystemScalingEnabled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if system scaling is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUserScalingFactorDefined()">isUserScalingFactorDefined</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if user scaling factor is defined by jvm argument magicdraw.resolution.scale.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isWindowsLookAndFeel()">isWindowsLookAndFeel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if Windows Look and Feel is active.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleByComponent(java.awt.Component,double)">scaleByComponent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleByComponent(java.awt.Component,int)">scaleByComponent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleComponent(com.nomagic.ui.HiDPIScalableComponent)">scaleComponent</a><wbr/>(<a href="HiDPIScalableComponent.html" title="interface in com.nomagic.ui">HiDPIScalableComponent</a> component)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale components and its children preferred size and similar.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleDownFont(float)">scaleDownFont</a><wbr/>(float size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale font size down.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static float</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleFont(float)">scaleFont</a><wbr/>(float size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale font size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleIcon(int)">scaleIcon</a><wbr/>(int size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale Icon size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleLookAndFeel()">scaleLookAndFeel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale various java Look&amp;Feel settings like fonts, icons sizes, insets and etc.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleUI(double)">scaleUI</a><wbr/>(double size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale User Interface item size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleUI(int)">scaleUI</a><wbr/>(int size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale User Interface item size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#scaleUIRecursively(java.awt.Component)">scaleUIRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scale components and its children preferred size and similar.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#systemScaleValueUp(int)">systemScaleValueUp</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Scales given value by system scale factor.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.ui.HiDPIScaleUtilitiesInternal">Methods inherited from class com.nomagic.ui.HiDPIScaleUtilitiesInternal</h3>
<code>adjustDimensionForFractionalScale, isScalingFractional</code></div>
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
<section class="detail" id="HI_DPI_SCALED">
<h3>HI_DPI_SCALED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HI_DPI_SCALED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.ui.HiDPIScaleUtilities.HI_DPI_SCALED">Constant Field Values</a></li>
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
<h3>HiDPIScaleUtilities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">HiDPIScaleUtilities</span>()</div>
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
<section class="detail" id="isSystemScalingEnabled()">
<h3>isSystemScalingEnabled</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSystemScalingEnabled</span>()</div>
<div class="block">Checks if system scaling is enabled.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if system scaling is enabled</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSystemScaleFactor()">
<h3>getSystemScaleFactor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">getSystemScaleFactor</span>()</div>
<div class="block">System scale factor. Scaling factor is calculated using <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Toolkit.html#getScreenResolution()" title="class or interface in java.awt"><code>Toolkit.getScreenResolution()</code></a> value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>system scaling factor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="systemScaleValueUp(int)">
<h3>systemScaleValueUp</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">systemScaleValueUp</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block">Scales given value by system scale factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value to scale</dd>
<dt>Returns:</dt>
<dd>scaled value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isWindowsLookAndFeel()">
<h3>isWindowsLookAndFeel</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isWindowsLookAndFeel</span>()</div>
<div class="block">Check if Windows Look and Feel is active.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if Windows Look and Feel is active</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSystemScaled16x16Icon(com.nomagic.ui.ResizableIcon)">
<h3>getSystemScaled16x16Icon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSystemScaled16x16Icon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSystemScaledIcon(com.nomagic.ui.ResizableIcon)">
<h3>getSystemScaledIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getSystemScaledIcon</span><wbr/><span class="parameters">(<a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Return resizable icon scaled by system scale factor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon to scale</dd>
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScaled16x16Icon(com.nomagic.ui.ResizableIcon)">
<h3>getScaled16x16Icon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getScaled16x16Icon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
<div class="block">Return scaled to 16x16 icon for a given icon. Scaling factor is taken into account, so in scaled environment icon size will be scaled by a scale factor.
 Scaled icons are cached using WeakReferences.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>scaled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNonScaledIcon(com.nomagic.ui.ResizableIcon,int,double)">
<h3>getNonScaledIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getNonScaledIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon,
 int size,
 double maxScale)</span></div>
<div class="block">Return icon scaled down to a given size. Scaled icons are cached using WeakReferences.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - icon</dd>
<dt>Returns:</dt>
<dd>icon of given size</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>SquareIcon.create(ResizableIcon, int, double)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleIcon(int)">
<h3>scaleIcon</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">scaleIcon</span><wbr/><span class="parameters">(int size)</span></div>
<div class="block">Scale Icon size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>Scaled size or the same value as provided.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleUI(double)">
<h3>scaleUI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">scaleUI</span><wbr/><span class="parameters">(double size)</span></div>
<div class="block">Scale User Interface item size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>Scaled size or the same value as provided.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleUI(int)">
<h3>scaleUI</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">scaleUI</span><wbr/><span class="parameters">(int size)</span></div>
<div class="block">Scale User Interface item size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>Scaled size or the same value as provided.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleFont(float)">
<h3>scaleFont</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">scaleFont</span><wbr/><span class="parameters">(float size)</span></div>
<div class="block">Scale font size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>Scaled size or the same value as provided.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleDownFont(float)">
<h3>scaleDownFont</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">scaleDownFont</span><wbr/><span class="parameters">(float size)</span></div>
<div class="block">Scale font size down.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>size</code> - size</dd>
<dt>Returns:</dt>
<dd>Scaled size or the same value as provided.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserScalingFactor()">
<h3>getUserScalingFactor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">getUserScalingFactor</span>()</div>
<div class="block">User scale factor. It is defined by jvm argument magicdraw.resolution.scale</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user scaling factor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScalingFactor()">
<h3>getScalingFactor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">getScalingFactor</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getUserScalingFactor()</div>
</div>
<div class="block">User scale factor. It is defined by jvm argument magicdraw.resolution.scale</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user scaling factor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReducedUserScalingFactor()">
<h3>getReducedUserScalingFactor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">getReducedUserScalingFactor</span>()</div>
<div class="block">In some cased real scaling scales UI too much. This methods returns reduced scaling factor for cases then real scaling scales UI too much.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>reduced scaling factor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReducedScalingFactor()">
<h3>getReducedScalingFactor</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">getReducedScalingFactor</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getReducedUserScalingFactor()</div>
</div>
<div class="block">In some cased real scaling scales UI too much. This methods returns reduced scaling factor for cases then real scaling scales UI too much.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>reduced scaling factor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isScalingFactorDefined()">
<h3>isScalingFactorDefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isScalingFactorDefined</span>()</div>
<div class="block">Checks if system or user scaling factor is defined.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if system or user scaling factor is defined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUserScalingFactorDefined()">
<h3>isUserScalingFactorDefined</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUserScalingFactorDefined</span>()</div>
<div class="block">Checks if user scaling factor is defined by jvm argument magicdraw.resolution.scale.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if user scaling factor is defined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addHiDPIScaledProperty(java.awt.Component)">
<h3>addHiDPIScaledProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addHiDPIScaledProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</span></div>
<div class="block">Mark this component as HiDPI scaled</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>component</code> - component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleComponent(com.nomagic.ui.HiDPIScalableComponent)">
<h3>scaleComponent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">scaleComponent</span><wbr/><span class="parameters">(<a href="HiDPIScalableComponent.html" title="interface in com.nomagic.ui">HiDPIScalableComponent</a> component)</span></div>
<div class="block">Scale components and its children preferred size and similar.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>component</code> - component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleUIRecursively(java.awt.Component)">
<h3>scaleUIRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">scaleUIRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</span></div>
<div class="block">Scale components and its children preferred size and similar.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>component</code> - component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleLookAndFeel()">
<h3>scaleLookAndFeel</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">scaleLookAndFeel</span>()</div>
<div class="block">Scale various java Look&amp;Feel settings like fonts, icons sizes, insets and etc.</div>
</section>
</li>
<li>
<section class="detail" id="fixWindowsFonts()">
<h3>fixWindowsFonts</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fixWindowsFonts</span>()</div>
</section>
</li>
<li>
<section class="detail" id="adjustFontByLookAndFeelDefaults(java.awt.Component)">
<h3>adjustFontByLookAndFeelDefaults</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">adjustFontByLookAndFeelDefaults</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</span></div>
<div class="block">Apply L&amp;F default font group if this is Windows L&amp;F</div>
</section>
</li>
<li>
<section class="detail" id="isScalingFactorFromProperty()">
<h3>isScalingFactorFromProperty</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isScalingFactorFromProperty</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">isUserScalingFactorDefined()</div>
</div>
<div class="block">Checks if scaling factor is defined from system property.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if scaling factor is from resolution scale property.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateSystemScaleFactor()">
<h3>calculateSystemScaleFactor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">calculateSystemScaleFactor</span>()</div>
<div class="block">Calculates system scaling factor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scaling factor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScaleFactorByScreenResolution()">
<h3>getScaleFactorByScreenResolution</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">float</span> <span class="element-name">getScaleFactorByScreenResolution</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use calculateSystemScaleFactor()</div>
</div>
<div class="block">Calculates system scaling factor from screen resolution.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scaling factor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="scaleByComponent(java.awt.Component,int)">
<h3>scaleByComponent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">scaleByComponent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 int value)</span></div>
</section>
</li>
<li>
<section class="detail" id="scaleByComponent(java.awt.Component,double)">
<h3>scaleByComponent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">scaleByComponent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 double value)</span></div>
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
