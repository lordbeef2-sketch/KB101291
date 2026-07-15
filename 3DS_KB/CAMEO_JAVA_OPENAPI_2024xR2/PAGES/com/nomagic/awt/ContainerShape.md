# JAVA OPENAPI: ContainerShape (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/awt/ContainerShape.html
- source_path: `com/nomagic/awt/ContainerShape.html`
- source_sha256: `d71f511e44412699909973ccf102ce2c853c447f0de7dd5380c360b20ae8d3af`
- captured_utc: `2026-07-14T16:55:01.320851+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.awt](package-summary.html)

## Class ContainerShape

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.awt.ContainerShape

@OpenApiAllpublic classContainerShape
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This shape can have rectangles, ellipses and lines.
 The shape form is the union of all contained shapes.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ContainerShape](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addEllipse](#addEllipse(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) el)`
Add ellipse.
`void`
`[addShape](#addShape(com.nomagic.awt.Line))([Line](Line.html) line)`
Add line.
`void`
`[addShape](#addShape(java.awt.geom.RoundRectangle2D))([RoundRectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html) rect)`
Add rectangle shape.
`void`
`[addShape](#addShape(java.awt.Polygon))([Polygon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html) polygon)`
Add Polygon.
`void`
`[addShape](#addShape(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
Add rectangle shape.
`static [ContainerShape](ContainerShape.html)`
`[createPolygonContainerShape](#createPolygonContainerShape(int%5B%5D,int%5B%5D))(int[] x,
 int[] y)`
Creates container shape from polygon points.
`static [ContainerShape](ContainerShape.html)`
`[createPolygonContainerShape](#createPolygonContainerShape(com.nomagic.awt.ContainerShape,int%5B%5D,int%5B%5D))([ContainerShape](ContainerShape.html) shape,
 int[] x,
 int[] y)`
Creates container shape from polygon points.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)>`
`[getEllipses](#getEllipses())()`
Returns contained ellipses
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Line](Line.html)>`
`[getLines](#getLines())()`
Returns contained lines.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Polygon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html)>`
`[getPolygons](#getPolygons())()`
Returns polygons
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)>`
`[getRectangles](#getRectangles())()`
Returns contained rectangles.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[RoundRectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html)>`
`[getRoundRectangles](#getRoundRectangles())()`
Returns round rectangles
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[intersection](#intersection(int,int,int,int))(int ax,
 int ay,
 int bx,
 int by)`
Computes the intersection of this shape (intersection with any of contained shapes) with the specified line.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[intersection](#intersection(java.awt.Point,java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) a,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) b)`

`boolean`
`[intersects](#intersects(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Indicates if container shape intersects with specified bounds.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ContainerShape
public ContainerShape()
 ============ METHOD DETAIL ========== 
Method Details
intersection
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) intersection([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) a,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) b)
intersection
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) intersection(int ax,
 int ay,
 int bx,
 int by)
Computes the intersection of this shape (intersection with any of contained shapes) with the specified line.
 Returns a new point that represents the intersection of two shapes.
Parameters:
`ax` - first point of line
`ay` - first point of line
`bx` - second point of line
`by` - second point of line
Returns:
the shapes intersection point
addShape
public void addShape([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
Add rectangle shape.
addShape
public void addShape([RoundRectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html) rect)
Add rectangle shape.
addShape
public void addShape([Line](Line.html) line)
Add line.
addEllipse
public void addEllipse([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) el)
Add ellipse.
addShape
public void addShape([Polygon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html) polygon)
Add Polygon.
getEllipses
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)> getEllipses()
Returns contained ellipses
Returns:
ellipses
getRectangles
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)> getRectangles()
Returns contained rectangles.
Returns:
rectangle
getLines
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Line](Line.html)> getLines()
Returns contained lines.
Returns:
lines
getRoundRectangles
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[RoundRectangle2D](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html)> getRoundRectangles()
Returns round rectangles
Returns:
round rectangles
getPolygons
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Polygon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html)> getPolygons()
Returns polygons
Returns:
polygons
createPolygonContainerShape
public static [ContainerShape](ContainerShape.html) createPolygonContainerShape(int[] x,
 int[] y)
Creates container shape from polygon points.
Parameters:
`x` - array of x coordinates.
`y` - array of y coordinates.
Returns:
created container shape.
createPolygonContainerShape
public static [ContainerShape](ContainerShape.html) createPolygonContainerShape([ContainerShape](ContainerShape.html) shape,
 int[] x,
 int[] y)
Creates container shape from polygon points.
Parameters:
`shape` - container shape to modify.
`x` - array of x coordinates.
`y` - array of y coordinates.
Returns:
created container shape.
intersects
public boolean intersects([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Indicates if container shape intersects with specified bounds.
Parameters:
`bounds` - bounds to check.
Returns:
true if container shape intersects with specified bounds, false otherwise.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.awt</a></div>
<h1 class="title" title="Class ContainerShape">Class ContainerShape</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.awt.ContainerShape</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ContainerShape</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This shape can have rectangles, ellipses and lines.
 The shape form is the union of all contained shapes.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ContainerShape</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEllipse(java.awt.Rectangle)">addEllipse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> el)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add ellipse.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addShape(com.nomagic.awt.Line)">addShape</a><wbr/>(<a href="Line.html" title="class in com.nomagic.awt">Line</a> line)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add line.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addShape(java.awt.geom.RoundRectangle2D)">addShape</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html" title="class or interface in java.awt.geom">RoundRectangle2D</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add rectangle shape.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addShape(java.awt.Polygon)">addShape</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html" title="class or interface in java.awt">Polygon</a> polygon)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add Polygon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addShape(java.awt.Rectangle)">addShape</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add rectangle shape.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createPolygonContainerShape(int%5B%5D,int%5B%5D)">createPolygonContainerShape</a><wbr/>(int[] x,
 int[] y)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates container shape from polygon points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createPolygonContainerShape(com.nomagic.awt.ContainerShape,int%5B%5D,int%5B%5D)">createPolygonContainerShape</a><wbr/>(<a href="ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a> shape,
 int[] x,
 int[] y)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates container shape from polygon points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEllipses()">getEllipses</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns contained ellipses</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Line.html" title="class in com.nomagic.awt">Line</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLines()">getLines</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns contained lines.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html" title="class or interface in java.awt">Polygon</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPolygons()">getPolygons</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns polygons</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRectangles()">getRectangles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns contained rectangles.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html" title="class or interface in java.awt.geom">RoundRectangle2D</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRoundRectangles()">getRoundRectangles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns round rectangles</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersection(int,int,int,int)">intersection</a><wbr/>(int ax,
 int ay,
 int bx,
 int by)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Computes the intersection of this shape (intersection with any of contained shapes) with the specified line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersection(java.awt.Point,java.awt.Point)">intersection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> a,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(java.awt.Rectangle)">intersects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if container shape intersects with specified bounds.</div>
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
<h3>ContainerShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ContainerShape</span>()</div>
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
<section class="detail" id="intersection(java.awt.Point,java.awt.Point)">
<h3>intersection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">intersection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> a,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> b)</span></div>
</section>
</li>
<li>
<section class="detail" id="intersection(int,int,int,int)">
<h3>intersection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">intersection</span><wbr/><span class="parameters">(int ax,
 int ay,
 int bx,
 int by)</span></div>
<div class="block">Computes the intersection of this shape (intersection with any of contained shapes) with the specified line.
 Returns a new point that represents the intersection of two shapes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ax</code> - first point of line</dd>
<dd><code>ay</code> - first point of line</dd>
<dd><code>bx</code> - second point of line</dd>
<dd><code>by</code> - second point of line</dd>
<dt>Returns:</dt>
<dd>the shapes intersection point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addShape(java.awt.Rectangle)">
<h3>addShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addShape</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block">Add rectangle shape.</div>
</section>
</li>
<li>
<section class="detail" id="addShape(java.awt.geom.RoundRectangle2D)">
<h3>addShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addShape</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html" title="class or interface in java.awt.geom">RoundRectangle2D</a> rect)</span></div>
<div class="block">Add rectangle shape.</div>
</section>
</li>
<li>
<section class="detail" id="addShape(com.nomagic.awt.Line)">
<h3>addShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addShape</span><wbr/><span class="parameters">(<a href="Line.html" title="class in com.nomagic.awt">Line</a> line)</span></div>
<div class="block">Add line.</div>
</section>
</li>
<li>
<section class="detail" id="addEllipse(java.awt.Rectangle)">
<h3>addEllipse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEllipse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> el)</span></div>
<div class="block">Add ellipse.</div>
</section>
</li>
<li>
<section class="detail" id="addShape(java.awt.Polygon)">
<h3>addShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addShape</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html" title="class or interface in java.awt">Polygon</a> polygon)</span></div>
<div class="block">Add Polygon.</div>
</section>
</li>
<li>
<section class="detail" id="getEllipses()">
<h3>getEllipses</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a>&gt;</span> <span class="element-name">getEllipses</span>()</div>
<div class="block">Returns contained ellipses</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ellipses</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRectangles()">
<h3>getRectangles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a>&gt;</span> <span class="element-name">getRectangles</span>()</div>
<div class="block">Returns contained rectangles.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rectangle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLines()">
<h3>getLines</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Line.html" title="class in com.nomagic.awt">Line</a>&gt;</span> <span class="element-name">getLines</span>()</div>
<div class="block">Returns contained lines.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>lines</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoundRectangles()">
<h3>getRoundRectangles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/RoundRectangle2D.html" title="class or interface in java.awt.geom">RoundRectangle2D</a>&gt;</span> <span class="element-name">getRoundRectangles</span>()</div>
<div class="block">Returns round rectangles</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>round rectangles</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPolygons()">
<h3>getPolygons</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Polygon.html" title="class or interface in java.awt">Polygon</a>&gt;</span> <span class="element-name">getPolygons</span>()</div>
<div class="block">Returns polygons</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>polygons</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPolygonContainerShape(int[],int[])">
<h3>createPolygonContainerShape</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createPolygonContainerShape</span><wbr/><span class="parameters">(int[] x,
 int[] y)</span></div>
<div class="block">Creates container shape from polygon points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x</code> - array of x coordinates.</dd>
<dd><code>y</code> - array of y coordinates.</dd>
<dt>Returns:</dt>
<dd>created container shape.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPolygonContainerShape(com.nomagic.awt.ContainerShape,int[],int[])">
<h3>createPolygonContainerShape</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createPolygonContainerShape</span><wbr/><span class="parameters">(<a href="ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a> shape,
 int[] x,
 int[] y)</span></div>
<div class="block">Creates container shape from polygon points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - container shape to modify.</dd>
<dd><code>x</code> - array of x coordinates.</dd>
<dd><code>y</code> - array of y coordinates.</dd>
<dt>Returns:</dt>
<dd>created container shape.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersects(java.awt.Rectangle)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Indicates if container shape intersects with specified bounds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - bounds to check.</dd>
<dt>Returns:</dt>
<dd>true if container shape intersects with specified bounds, false otherwise.</dd>
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
