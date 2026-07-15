# JAVA OPENAPI: Line (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/awt/Line.html
- source_path: `com/nomagic/awt/Line.html`
- source_sha256: `53cec9f3fdbc69206b6356f59bc4ad030d92fa894243e84026d072e88e9c23fb`
- captured_utc: `2026-07-14T16:55:01.305852+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.awt](package-summary.html)

## Class Line

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.awt.Line

@OpenApiAllpublic classLine
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The Line represents a line segment in (x, y) coordinate space.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[A](#A)`
The first point of the line.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[B](#B)`
The second point of the line.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Line](#%3Cinit%3E())()`
Constructs a new line whose first point is at (0,0) in the
 coordinate space, and whose second point is at (0, 0) in the
 coordinate space.
`[Line](#%3Cinit%3E(int,int,int,int))(int x1,
 int y1,
 int x2,
 int y2)`
Constructs a new line whose first point is specified as
 (`x`, `y`) and whose second point
 is specified as (`x`, `y`).
`[Line](#%3Cinit%3E(com.nomagic.awt.Line))([Line](Line.html) l)`
Constructs a new line, initialized to match the values of
 the specified line.
`[Line](#%3Cinit%3E(java.awt.Point,java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p1,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p2)`
Constructs a new line whose first point is specified as
 `p1` and whose second point is specified as
 `p2`.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[belongs](#belongs(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)`
Checks whether specified point belongs to this line.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`
Checks whether two lines are equal.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds())()`
Gets the bounding rectangle of this line.
`int`
`[hashCode](#hashCode())()`

`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[intersection](#intersection(com.nomagic.awt.Line))([Line](Line.html) l)`
Computes the intersection of this line with the
 specified line.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[intersection](#intersection(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)`
Computes the intersection of this line with the
 line perpendicular to this line.
`boolean`
`[intersects](#intersects(com.nomagic.awt.Line))([Line](Line.html) l)`
Determines whether this line and the specified line
 intersect.
`boolean`
`[isVertical](#isVertical())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Returns a string representation of this line
 and its values.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
A
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) A
The first point of the line.
B
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) B
The second point of the line.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Line
public Line()
Constructs a new line whose first point is at (0,0) in the
 coordinate space, and whose second point is at (0, 0) in the
 coordinate space.
Line
public Line([Line](Line.html) l)
Constructs a new line, initialized to match the values of
 the specified line.
Parameters:
`l` - a line from which to copy initial values.
Line
public Line([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p1,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p2)
Constructs a new line whose first point is specified as
 `p1` and whose second point is specified as
 `p2`.
Parameters:
`p1` - the first point.
`p2` - the second point.
Line
public Line(int x1,
 int y1,
 int x2,
 int y2)
Constructs a new line whose first point is specified as
 (`x`, `y`) and whose second point
 is specified as (`x`, `y`).
Parameters:
`x1` - the first point *x* coordinate.
`y1` - the first point *y* coordinate.
`x2` - the second point *x* coordinate.
`y2` - the second point *y* coordinate.
 ============ METHOD DETAIL ========== 
Method Details
intersects
public boolean intersects([Line](Line.html) l)
Determines whether this line and the specified line
 intersect.
Parameters:
`l` - a line.
Returns:
`true` if the specified line
 and this line insersect;
 `false` otherwise.
intersection
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) intersection([Line](Line.html) l)
Computes the intersection of this line with the
 specified line. Returns a new point that
 represents the intersection of the two lines.
Parameters:
`l` - a line.
Returns:
the lines intersection point
intersection
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) intersection([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)
Computes the intersection of this line with the
 line perpendicular to this line. Perpendicular line go throught
 specified point. Returns a new point that
 represents the intersection of the two lines.
Parameters:
`p` - a point.
Returns:
the lines intersection point
belongs
public boolean belongs([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) p)
Checks whether specified point belongs to this line.
 The result is `true` if and only if the argument is not
 `null` and belongs to this line.
Parameters:
`p` - a point.
Returns:
`true` if specified point belongs to this line;
 `false` otherwise.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Checks whether two lines are equal.
 The result is `true` if and only if the argument is not
 `null` and is a `Line` object that has the
 same first point and second point as this line.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Parameters:
`obj` - the object to compare with.
Returns:
`true` if the objects are equal;
 `false` otherwise.
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
toString
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Returns a string representation of this line
 and its values.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
a string representation of this line.
getBounds
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds()
Gets the bounding rectangle of this line.
 This method is included for completeness, to parallel the
 `getBounds` method of `Component`.
Returns:
a new rectangle, equal to the bounding rectangle
 for this line.
See Also:
[`Component.getBounds()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds())
isVertical
public boolean isVertical()
Returns:
true if line is more vertical than horizontal.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.awt</a></div>
<h1 class="title" title="Class Line">Class Line</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.awt.Line</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Line</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The Line represents a line segment in (x, y) coordinate space.</div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#A">A</a></code></div>
<div class="col-last even-row-color">
<div class="block">The first point of the line.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#B">B</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The second point of the line.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Line</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new line whose first point is at (0,0) in the
 coordinate space, and whose second point is at (0, 0) in the
 coordinate space.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int,int,int,int)">Line</a><wbr/>(int x1,
 int y1,
 int x2,
 int y2)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new line whose first point is specified as
 (<code>x</code>, <code>y</code>) and whose second point
 is specified as (<code>x</code>, <code>y</code>).</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.awt.Line)">Line</a><wbr/>(<a href="Line.html" title="class in com.nomagic.awt">Line</a> l)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new line, initialized to match the values of
 the specified line.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.awt.Point,java.awt.Point)">Line</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p2)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new line whose first point is specified as
 <code>p1</code> and whose second point is specified as
 <code>p2</code>.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#belongs(java.awt.Point)">belongs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks whether specified point belongs to this line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks whether two lines are equal.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBounds()">getBounds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the bounding rectangle of this line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersection(com.nomagic.awt.Line)">intersection</a><wbr/>(<a href="Line.html" title="class in com.nomagic.awt">Line</a> l)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Computes the intersection of this line with the
 specified line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersection(java.awt.Point)">intersection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Computes the intersection of this line with the
 line perpendicular to this line.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intersects(com.nomagic.awt.Line)">intersects</a><wbr/>(<a href="Line.html" title="class in com.nomagic.awt">Line</a> l)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether this line and the specified line
 intersect.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVertical()">isVertical</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a string representation of this line
 and its values.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="A">
<h3>A</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">A</span></div>
<div class="block">The first point of the line.</div>
</section>
</li>
<li>
<section class="detail" id="B">
<h3>B</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">B</span></div>
<div class="block">The second point of the line.</div>
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
<h3>Line</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Line</span>()</div>
<div class="block">Constructs a new line whose first point is at (0,0) in the
 coordinate space, and whose second point is at (0, 0) in the
 coordinate space.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.awt.Line)">
<h3>Line</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Line</span><wbr/><span class="parameters">(<a href="Line.html" title="class in com.nomagic.awt">Line</a> l)</span></div>
<div class="block">Constructs a new line, initialized to match the values of
 the specified line.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>l</code> - a line from which to copy initial values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.awt.Point,java.awt.Point)">
<h3>Line</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Line</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p2)</span></div>
<div class="block">Constructs a new line whose first point is specified as
 <code>p1</code> and whose second point is specified as
 <code>p2</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p1</code> - the first point.</dd>
<dd><code>p2</code> - the second point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(int,int,int,int)">
<h3>Line</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Line</span><wbr/><span class="parameters">(int x1,
 int y1,
 int x2,
 int y2)</span></div>
<div class="block">Constructs a new line whose first point is specified as
 (<code>x</code>, <code>y</code>) and whose second point
 is specified as (<code>x</code>, <code>y</code>).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>x1</code> - the first point <i>x</i> coordinate.</dd>
<dd><code>y1</code> - the first point <i>y</i> coordinate.</dd>
<dd><code>x2</code> - the second point <i>x</i> coordinate.</dd>
<dd><code>y2</code> - the second point <i>y</i> coordinate.</dd>
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
<section class="detail" id="intersects(com.nomagic.awt.Line)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(<a href="Line.html" title="class in com.nomagic.awt">Line</a> l)</span></div>
<div class="block">Determines whether this line and the specified line
 intersect.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>l</code> - a line.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the specified line
 and this line insersect;
 <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersection(com.nomagic.awt.Line)">
<h3>intersection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">intersection</span><wbr/><span class="parameters">(<a href="Line.html" title="class in com.nomagic.awt">Line</a> l)</span></div>
<div class="block">Computes the intersection of this line with the
 specified line. Returns a new point that
 represents the intersection of the two lines.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>l</code> - a line.</dd>
<dt>Returns:</dt>
<dd>the lines intersection point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersection(java.awt.Point)">
<h3>intersection</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">intersection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</span></div>
<div class="block">Computes the intersection of this line with the
 line perpendicular to this line. Perpendicular line go throught
 specified point. Returns a new point that
 represents the intersection of the two lines.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - a point.</dd>
<dt>Returns:</dt>
<dd>the lines intersection point</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="belongs(java.awt.Point)">
<h3>belongs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">belongs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> p)</span></div>
<div class="block">Checks whether specified point belongs to this line.
 <p>
 The result is <kbd>true</kbd> if  and only if the argument is not
 <kbd>null</kbd> and belongs to this line.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p</code> - a point.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if specified point belongs to this line;
 <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Checks whether two lines are equal.
 <p>
 The result is <kbd>true</kbd> if and only if the argument is not
 <kbd>null</kbd> and is a <kbd>Line</kbd> object that has the
 same first point and second point as this line.</p></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the object to compare with.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the objects are equal;
 <code>false</code> otherwise.</dd>
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
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Returns a string representation of this line
 and its values.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this line.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds()">
<h3>getBounds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span>()</div>
<div class="block">Gets the bounding rectangle of this line.
 <p>
 This method is included for completeness, to parallel the
 <code>getBounds</code> method of <code>Component</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a new rectangle, equal to the bounding rectangle
 for this line.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html#getBounds()" title="class or interface in java.awt"><code>Component.getBounds()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVertical()">
<h3>isVertical</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVertical</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if line is more vertical than horizontal.</dd>
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
