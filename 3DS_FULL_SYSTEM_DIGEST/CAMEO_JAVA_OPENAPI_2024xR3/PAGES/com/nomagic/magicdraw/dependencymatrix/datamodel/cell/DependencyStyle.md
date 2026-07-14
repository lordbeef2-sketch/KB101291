# JAVA OPENAPI: DependencyStyle (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/dependencymatrix/datamodel/cell/DependencyStyle.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/cell/DependencyStyle.html`
- source_sha256: `f7f640f4693f6b18a0e4d1e6e6026ab9f2a4c9158937ffa9f4492622f2a8c9cd`
- captured_utc: `2026-07-14T16:55:13.741991+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.cell](package-summary.html)

## Class DependencyStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.datamodel.cell.DependencyStyle

@OpenApiAllpublic classDependencyStyle
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Visual style of a DependencyEntry

See Also:
[`Connection`](../../../ui/pathicon/Connection.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [DependencyStyle](DependencyStyle.html)`
`[DEFAULT_STYLE](#DEFAULT_STYLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DependencyStyle](#%3Cinit%3E())()`

`[DependencyStyle](#%3Cinit%3E(com.nomagic.ui.ResizableIcon))([ResizableIcon](../../../../ui/ResizableIcon.html) icon)`

`[DependencyStyle](#%3Cinit%3E(java.awt.Color,java.awt.BasicStroke,int,com.nomagic.ui.ResizableIcon,int,com.nomagic.ui.ResizableIcon))([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color,
 [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke,
 int connectionTypeA,
 [ResizableIcon](../../../../ui/ResizableIcon.html) connectionIconA,
 int connectionTypeB,
 [ResizableIcon](../../../../ui/ResizableIcon.html) connectionIconB)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getColor](#getColor())()`

`[ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getConnectionIconA](#getConnectionIconA())()`

`[ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getConnectionIconB](#getConnectionIconB())()`

`int`
`[getConnectionTypeA](#getConnectionTypeA())()`

`int`
`[getConnectionTypeB](#getConnectionTypeB())()`

`[ResizableIcon](../../../../ui/ResizableIcon.html)`
`[getIcon](#getIcon())()`

`[BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getStroke](#getStroke())()`

`int`
`[hashCode](#hashCode())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
DEFAULT_STYLE
public static final [DependencyStyle](DependencyStyle.html) DEFAULT_STYLE
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DependencyStyle
public DependencyStyle()
DependencyStyle
public DependencyStyle([Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color,
 [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) stroke,
 int connectionTypeA,
 @CheckForNull
 [ResizableIcon](../../../../ui/ResizableIcon.html) connectionIconA,
 int connectionTypeB,
 @CheckForNull
 [ResizableIcon](../../../../ui/ResizableIcon.html) connectionIconB)
Constructor
Parameters:
`color` - line color
`stroke` - line stroke
`connectionTypeB` - line connection type
See Also:
[`Connection`](../../../ui/pathicon/Connection.html)
DependencyStyle
public DependencyStyle([ResizableIcon](../../../../ui/ResizableIcon.html) icon)
 ============ METHOD DETAIL ========== 
Method Details
getConnectionTypeB
public int getConnectionTypeB()
getColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getColor()
getStroke
public [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getStroke()
getConnectionIconB
public [ResizableIcon](../../../../ui/ResizableIcon.html) getConnectionIconB()
getIcon
public [ResizableIcon](../../../../ui/ResizableIcon.html) getIcon()
getConnectionTypeA
public int getConnectionTypeA()
getConnectionIconA
public [ResizableIcon](../../../../ui/ResizableIcon.html) getConnectionIconA()
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.cell</a></div>
<h1 class="title" title="Class DependencyStyle">Class DependencyStyle</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.datamodel.cell.DependencyStyle</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DependencyStyle</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Visual style of a DependencyEntry</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../ui/pathicon/Connection.html" title="class in com.nomagic.magicdraw.ui.pathicon"><code>Connection</code></a></li>
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
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a href="DependencyStyle.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyStyle</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_STYLE">DEFAULT_STYLE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DependencyStyle</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.ui.ResizableIcon)">DependencyStyle</a><wbr/>(<a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.awt.Color,java.awt.BasicStroke,int,com.nomagic.ui.ResizableIcon,int,com.nomagic.ui.ResizableIcon)">DependencyStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke,
 int connectionTypeA,
 <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> connectionIconA,
 int connectionTypeB,
 <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> connectionIconB)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColor()">getColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectionIconA()">getConnectionIconA</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectionIconB()">getConnectionIconB</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectionTypeA()">getConnectionTypeA</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectionTypeB()">getConnectionTypeB</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStroke()">getStroke</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="DEFAULT_STYLE">
<h3>DEFAULT_STYLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="DependencyStyle.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyStyle</a></span> <span class="element-name">DEFAULT_STYLE</span></div>
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
<h3>DependencyStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DependencyStyle</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.awt.Color,java.awt.BasicStroke,int,com.nomagic.ui.ResizableIcon,int,com.nomagic.ui.ResizableIcon)">
<h3>DependencyStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DependencyStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a> stroke,
 int connectionTypeA,
 @CheckForNull
 <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> connectionIconA,
 int connectionTypeB,
 @CheckForNull
 <a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> connectionIconB)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - line color</dd>
<dd><code>stroke</code> - line stroke</dd>
<dd><code>connectionTypeB</code> - line connection type</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../ui/pathicon/Connection.html" title="class in com.nomagic.magicdraw.ui.pathicon"><code>Connection</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.ui.ResizableIcon)">
<h3>DependencyStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DependencyStyle</span><wbr/><span class="parameters">(<a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a> icon)</span></div>
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
<section class="detail" id="getConnectionTypeB()">
<h3>getConnectionTypeB</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getConnectionTypeB</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getColor()">
<h3>getColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getColor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getStroke()">
<h3>getStroke</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getStroke</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getConnectionIconB()">
<h3>getConnectionIconB</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getConnectionIconB</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getConnectionTypeA()">
<h3>getConnectionTypeA</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getConnectionTypeA</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getConnectionIconA()">
<h3>getConnectionIconA</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getConnectionIconA</span>()</div>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
