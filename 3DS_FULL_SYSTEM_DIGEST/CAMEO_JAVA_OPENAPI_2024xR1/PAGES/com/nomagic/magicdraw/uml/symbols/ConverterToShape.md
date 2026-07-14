# JAVA OPENAPI: ConverterToShape (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/symbols/ConverterToShape.html
- source_path: `com/nomagic/magicdraw/uml/symbols/ConverterToShape.html`
- source_sha256: `bae6136e95eb76b4763e57636e475542d99c2ebcefd67143d9cc4c0a36eeaf50`
- captured_utc: `2026-07-14T16:52:08.883838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class ConverterToShape

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.ConverterToShape

@OpenApiAllpublic classConverterToShape
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convert shape bounds to [`Shape`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html). Optionally can use [`BoundsTransformation`](BoundsTransformation.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ConverterToShape](#%3Cinit%3E())()`
Constructor
`[ConverterToShape](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.BoundsTransformation))([BoundsTransformation](BoundsTransformation.html) transformation)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(com.nomagic.awt.ContainerShape,com.nomagic.magicdraw.uml.symbols.PresentationElement))([ContainerShape](../../../awt/ContainerShape.html) shape,
 [PresentationElement](PresentationElement.html) element)`
Convert container to shape
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(java.awt.geom.Arc2D,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Arc2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html) arc,
 [PresentationElement](PresentationElement.html) element)`
Convert arc to shape
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(java.awt.geom.GeneralPath,com.nomagic.magicdraw.uml.symbols.PresentationElement))([GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html) path,
 [PresentationElement](PresentationElement.html) element)`
Convert path to shape
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(java.awt.geom.Rectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Rectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html) rectangle,
 [PresentationElement](PresentationElement.html) element)`
Convert rectangle to shape
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(java.awt.geom.RoundRectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement))([RoundRectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html) rectangle,
 [PresentationElement](PresentationElement.html) element)`
Convert rounded rectangle to shape
`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(java.awt.Polygon,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Polygon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html) polygon,
 [PresentationElement](PresentationElement.html) element)`
Convert polygon to shape
`final [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convert](#convert(java.awt.Shape,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) shape,
 [PresentationElement](PresentationElement.html) element)`

`[Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html)`
`[convertToEllipse](#convertToEllipse(java.awt.geom.Rectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Rectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html) ellipse,
 [PresentationElement](PresentationElement.html) element)`
Convert ellipse to shape
`[BoundsTransformation](BoundsTransformation.html)`
`[getTransformation](#getTransformation())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ConverterToShape
public ConverterToShape()
Constructor
ConverterToShape
public ConverterToShape([BoundsTransformation](BoundsTransformation.html) transformation)
Constructor
Parameters:
`transformation` - converting transformation
 ============ METHOD DETAIL ========== 
Method Details
getTransformation
public [BoundsTransformation](BoundsTransformation.html) getTransformation()
Returns:
transformation
convert
public final [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) shape,
 [PresentationElement](PresentationElement.html) element)
convert
public [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([Rectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html) rectangle,
 [PresentationElement](PresentationElement.html) element)
Convert rectangle to shape
Parameters:
`rectangle` - rectangle
`element` - symbol
Returns:
shape
convert
public [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([RoundRectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html) rectangle,
 [PresentationElement](PresentationElement.html) element)
Convert rounded rectangle to shape
Parameters:
`rectangle` - rectangle
`element` - symbol
Returns:
shape
convert
public [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([Arc2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html) arc,
 [PresentationElement](PresentationElement.html) element)
Convert arc to shape
Parameters:
`arc` - arc
`element` - symbol
Returns:
shape
convert
@CheckForNullpublic [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([ContainerShape](../../../awt/ContainerShape.html) shape,
 [PresentationElement](PresentationElement.html) element)
Convert container to shape
Parameters:
`shape` - container shape
`element` - symbol
Returns:
shape
convertToEllipse
public [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convertToEllipse([Rectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html) ellipse,
 [PresentationElement](PresentationElement.html) element)
Convert ellipse to shape
Parameters:
`ellipse` - ellipse
`element` - symbol
Returns:
shape
convert
public [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([GeneralPath](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html) path,
 [PresentationElement](PresentationElement.html) element)
Convert path to shape
Parameters:
`path` - path
`element` - symbol
Returns:
shape
convert
public [Shape](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html) convert([Polygon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html) polygon,
 [PresentationElement](PresentationElement.html) element)
Convert polygon to shape
Parameters:
`polygon` - polygon
`element` - symbol
Returns:
shape

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class ConverterToShape">Class ConverterToShape</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.ConverterToShape</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ConverterToShape</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convert shape bounds to <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt"><code>Shape</code></a>. Optionally can use <a href="BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>BoundsTransformation</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ConverterToShape</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">ConverterToShape</a><wbr/>(<a href="BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(com.nomagic.awt.ContainerShape,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a href="../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a> shape,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert container to shape</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.awt.geom.Arc2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html" title="class or interface in java.awt.geom">Arc2D</a> arc,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert arc to shape</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.awt.geom.GeneralPath,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a> path,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert path to shape</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.awt.geom.Rectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html" title="class or interface in java.awt.geom">Rectangle2D</a> rectangle,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert rectangle to shape</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.awt.geom.RoundRectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html" title="class or interface in java.awt.geom">RoundRectangle2D</a> rectangle,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert rounded rectangle to shape</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.awt.Polygon,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html" title="class or interface in java.awt">Polygon</a> polygon,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert polygon to shape</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convert(java.awt.Shape,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a> shape,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#convertToEllipse(java.awt.geom.Rectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">convertToEllipse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html" title="class or interface in java.awt.geom">Rectangle2D</a> ellipse,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Convert ellipse to shape</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformation()">getTransformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<h3>ConverterToShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConverterToShape</span>()</div>
<div class="block">Constructor</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">
<h3>ConverterToShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConverterToShape</span><wbr/><span class="parameters">(<a href="BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> transformation)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformation</code> - converting transformation</dd>
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
<section class="detail" id="getTransformation()">
<h3>getTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a></span> <span class="element-name">getTransformation</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(java.awt.Shape,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a> shape,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="convert(java.awt.geom.Rectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html" title="class or interface in java.awt.geom">Rectangle2D</a> rectangle,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert rectangle to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rectangle</code> - rectangle</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(java.awt.geom.RoundRectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html" title="class or interface in java.awt.geom">RoundRectangle2D</a> rectangle,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert rounded rectangle to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rectangle</code> - rectangle</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(java.awt.geom.Arc2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Arc2D.html" title="class or interface in java.awt.geom">Arc2D</a> arc,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert arc to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>arc</code> - arc</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(com.nomagic.awt.ContainerShape,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a href="../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a> shape,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert container to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - container shape</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertToEllipse(java.awt.geom.Rectangle2D,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convertToEllipse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convertToEllipse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/Rectangle2D.html" title="class or interface in java.awt.geom">Rectangle2D</a> ellipse,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert ellipse to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ellipse</code> - ellipse</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(java.awt.geom.GeneralPath,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/GeneralPath.html" title="class or interface in java.awt.geom">GeneralPath</a> path,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert path to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - path</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convert(java.awt.Polygon,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>convert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Shape.html" title="class or interface in java.awt">Shape</a></span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html" title="class or interface in java.awt">Polygon</a> polygon,
 <a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Convert polygon to shape</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>polygon</code> - polygon</dd>
<dd><code>element</code> - symbol</dd>
<dt>Returns:</dt>
<dd>shape</dd>
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
