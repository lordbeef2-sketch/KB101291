# JAVA OPENAPI: AlphaCompositeIcon (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/ui/AlphaCompositeIcon.html
- source_path: `com/nomagic/ui/AlphaCompositeIcon.html`
- source_sha256: `5378fbd38bd752b581d46151aa439962770743d8ec43f0e215bc7db043bd0277`
- captured_utc: `2026-07-14T16:46:16.949024+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Class AlphaCompositeIcon

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.ui.AlphaCompositeIcon

All Implemented Interfaces:
`[ResizableIcon](ResizableIcon.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`

@OpenApiAllpublic classAlphaCompositeIcon
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [ResizableIcon](ResizableIcon.html)

Paints wrapped icon with alpha composite.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AlphaCompositeIcon](#%3Cinit%3E(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon)`

`[AlphaCompositeIcon](#%3Cinit%3E(javax.swing.Icon,java.awt.Composite))([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Composite](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Composite.html) composite)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[AlphaCompositeIcon](AlphaCompositeIcon.html)`
`[clone](#clone())()`
Returns cloned instance of this icon.
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
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AlphaCompositeIcon
public AlphaCompositeIcon([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon)
AlphaCompositeIcon
public AlphaCompositeIcon([Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Composite](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Composite.html) composite)
 ============ METHOD DETAIL ========== 
Method Details
paintIcon
public void paintIcon([Component](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html) c,
 [Graphics](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html) g,
 int x,
 int y)
Specified by:
`[paintIcon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int))` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
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
clone
public [AlphaCompositeIcon](AlphaCompositeIcon.html) clone()
Description copied from interface: `[ResizableIcon](ResizableIcon.html#clone())`
Returns cloned instance of this icon.
Specified by:
`[clone](ResizableIcon.html#clone())` in interface `[ResizableIcon](ResizableIcon.html)`
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
cloned instance.
getIconWidth
public int getIconWidth()
Specified by:
`[getIconWidth](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth())` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`
getIconHeight
public int getIconHeight()
Specified by:
`[getIconHeight](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconHeight())` in interface `[Icon](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Class AlphaCompositeIcon">Class AlphaCompositeIcon</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.ui.AlphaCompositeIcon</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AlphaCompositeIcon</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span></div>
<div class="block">Paints wrapped icon with alpha composite.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(javax.swing.Icon)">AlphaCompositeIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(javax.swing.Icon,java.awt.Composite)">AlphaCompositeIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Composite.html" title="class or interface in java.awt">Composite</a> composite)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="AlphaCompositeIcon.html" title="class in com.nomagic.ui">AlphaCompositeIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns cloned instance of this icon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconHeight()">getIconHeight</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIconWidth()">getIconWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintIcon(java.awt.Component,java.awt.Graphics,int,int)">paintIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#paintIcon(java.awt.Component,java.awt.Graphics,int,int,int,int)">paintIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y,
 int w,
 int h)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draw the icon in the given bounds.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(javax.swing.Icon)">
<h3>AlphaCompositeIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AlphaCompositeIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(javax.swing.Icon,java.awt.Composite)">
<h3>AlphaCompositeIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AlphaCompositeIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Composite.html" title="class or interface in java.awt">Composite</a> composite)</span></div>
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
<section class="detail" id="paintIcon(java.awt.Component,java.awt.Graphics,int,int)">
<h3>paintIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">paintIcon</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> c,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 int x,
 int y)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#paintIcon(java.awt.Component,java.awt.Graphics,int,int)" title="class or interface in javax.swing">paintIcon</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
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
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AlphaCompositeIcon.html" title="class in com.nomagic.ui">AlphaCompositeIcon</a></span> <span class="element-name">clone</span>()</div>
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
<section class="detail" id="getIconWidth()">
<h3>getIconWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getIconWidth</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html#getIconWidth()" title="class or interface in javax.swing">getIconWidth</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></dd>
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
