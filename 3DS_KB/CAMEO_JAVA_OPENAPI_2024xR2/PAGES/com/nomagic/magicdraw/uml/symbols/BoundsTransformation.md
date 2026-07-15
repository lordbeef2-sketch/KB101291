# JAVA OPENAPI: BoundsTransformation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/symbols/BoundsTransformation.html
- source_path: `com/nomagic/magicdraw/uml/symbols/BoundsTransformation.html`
- source_sha256: `cdc3657ecf68cf7b7a807dc44f076e8fed98f832a0b658e7e980c54f381a62f0`
- captured_utc: `2026-07-14T16:55:54.433446+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class BoundsTransformation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.BoundsTransformation

@OpenApiAllpublic classBoundsTransformation
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Symbol bounds transformation.
 It provides only one transformation - bounds growing by some factor. Same as [`Rectangle.grow(int, int)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html#grow(int,int))

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BoundsTransformation](#%3Cinit%3E())()`
Constructor with 0 bounds growing factor
`[BoundsTransformation](#%3Cinit%3E(int))(int grow)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getGrow](#getGrow())()`

`double`
`[grow](#grow(double))(double vector)`
Grow length of given vector
`int`
`[grow](#grow(int))(int vector)`
Grow length of given vector
`[RoundRectangle2D.Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html)`
`[grow](#grow(java.awt.geom.RoundRectangle2D.Double))([RoundRectangle2D.Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html) r)`
Grow give rectangle
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[grow](#grow(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Grow give rectangle
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BoundsTransformation
public BoundsTransformation()
Constructor with 0 bounds growing factor
BoundsTransformation
public BoundsTransformation(int grow)
Constructor
Parameters:
`grow` - bounds growing factor
 ============ METHOD DETAIL ========== 
Method Details
getGrow
public int getGrow()
Returns:
bounds growing factor
grow
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) grow([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
Grow give rectangle
Parameters:
`r` - rectangle
Returns:
result rectangle
grow
public [RoundRectangle2D.Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html) grow([RoundRectangle2D.Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html) r)
Grow give rectangle
Parameters:
`r` - rectangle
Returns:
result rectangle
grow
public int grow(int vector)
Grow length of given vector
Parameters:
`vector` - vector
Returns:
vector vector
grow
public double grow(double vector)
Grow length of given vector
Parameters:
`vector` - vector
Returns:
vector vector

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class BoundsTransformation">Class BoundsTransformation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.BoundsTransformation</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BoundsTransformation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Symbol bounds transformation.
 It provides only one transformation - bounds growing by some factor. Same as <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html#grow(int,int)" title="class or interface in java.awt"><code>Rectangle.grow(int, int)</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">BoundsTransformation</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor with 0 bounds growing factor</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int)">BoundsTransformation</a><wbr/>(int grow)</code></div>
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
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGrow()">getGrow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#grow(double)">grow</a><wbr/>(double vector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Grow length of given vector</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#grow(int)">grow</a><wbr/>(int vector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Grow length of given vector</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html" title="class or interface in java.awt.geom">RoundRectangle2D.Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#grow(java.awt.geom.RoundRectangle2D.Double)">grow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html" title="class or interface in java.awt.geom">RoundRectangle2D.Double</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Grow give rectangle</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#grow(java.awt.Rectangle)">grow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Grow give rectangle</div>
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
<h3>BoundsTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BoundsTransformation</span>()</div>
<div class="block">Constructor with 0 bounds growing factor</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(int)">
<h3>BoundsTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BoundsTransformation</span><wbr/><span class="parameters">(int grow)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>grow</code> - bounds growing factor</dd>
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
<section class="detail" id="getGrow()">
<h3>getGrow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getGrow</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>bounds growing factor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="grow(java.awt.Rectangle)">
<h3>grow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">grow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
<div class="block">Grow give rectangle</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - rectangle</dd>
<dt>Returns:</dt>
<dd>result rectangle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="grow(java.awt.geom.RoundRectangle2D.Double)">
<h3>grow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html" title="class or interface in java.awt.geom">RoundRectangle2D.Double</a></span> <span class="element-name">grow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.Double.html" title="class or interface in java.awt.geom">RoundRectangle2D.Double</a> r)</span></div>
<div class="block">Grow give rectangle</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - rectangle</dd>
<dt>Returns:</dt>
<dd>result rectangle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="grow(int)">
<h3>grow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">grow</span><wbr/><span class="parameters">(int vector)</span></div>
<div class="block">Grow length of given vector</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector</code> - vector</dd>
<dt>Returns:</dt>
<dd>vector vector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="grow(double)">
<h3>grow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">grow</span><wbr/><span class="parameters">(double vector)</span></div>
<div class="block">Grow length of given vector</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vector</code> - vector</dd>
<dt>Returns:</dt>
<dd>vector vector</dd>
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
