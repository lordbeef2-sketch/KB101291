# JAVA OPENAPI: ZoomHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/zoom/ZoomHelper.html
- source_path: `com/nomagic/magicdraw/ui/zoom/ZoomHelper.html`
- source_sha256: `ef12d4b136ce3e81dd5e7c58e216409fa4c06af4625d91e736fa5fd5a7d96055`
- captured_utc: `2026-07-14T16:52:06.354803+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.zoom](package-summary.html)

## Class ZoomHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.zoom.ZoomHelper

@OpenApipublic classZoomHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Helper functions to display zoomed GUI components

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOriginalSize(int,float)">getOriginalSize</a><wbr/>(int scaledSize,
 float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opposite method to <a href="#getScaledSize(int,float)"><code>getScaledSize(int, float)</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledFont(java.awt.Font,float)">getScaledFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Takes the provided font and scales it's size by the given zoomFactor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledIcon(javax.swing.Icon,float)">getScaledIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Takes the provided icon and scales it's size by the given zoomFactor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getScaledSize(int,float)">getScaledSize</a><wbr/>(int size,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Takes the provided integer and scales (multiplies) it by the given zoomFactor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zoomComponent(java.awt.Component,float)">zoomComponent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component,
 float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If component implements <a href="Zoomable.html" title="interface in com.nomagic.magicdraw.ui.zoom"><code>Zoomable</code></a> interface, zooms the component by the given factor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zoomComponents(java.awt.Container,float)">zoomComponents</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Container.html" title="class or interface in java.awt">Container</a> container,
 float zoomFactor)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
