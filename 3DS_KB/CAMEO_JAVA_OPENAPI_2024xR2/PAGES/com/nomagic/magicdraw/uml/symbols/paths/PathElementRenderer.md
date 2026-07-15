# JAVA OPENAPI: PathElementRenderer (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/symbols/paths/PathElementRenderer.html
- source_path: `com/nomagic/magicdraw/uml/symbols/paths/PathElementRenderer.html`
- source_sha256: `19e8a616ebcac814b6afa4cbb94741c80187197988e77db1a500a89bfef65c53`
- captured_utc: `2026-07-14T16:55:55.780461+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.paths](package-summary.html)

## Class PathElementRenderer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer](../PresentationElementRenderer.html)
com.nomagic.magicdraw.uml.symbols.paths.PathElementRenderer

@OpenApiAllpublic abstract classPathElementRenderer
extends [PresentationElementRenderer](../PresentationElementRenderer.html)

Path element renderer allows to customize (change) the default
 view of [`PathElement`](PathElement.html).
 Path decoration methods are called even when the path is being drawn/created in a diagram, and supplier or client not yet connected, breakpoints are not yet set.

See Also:
[`PresentationElementRenderer`](../PresentationElementRenderer.html)
[`ShapeRenderer`](../shapes/ShapeRenderer.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PathElementRenderer](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[drawPathAdornment](#drawPathAdornment(java.awt.Graphics,com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.awt.Point,java.awt.Point,java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 [PathElement](PathElement.html) pathElement,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakPoints,
 [PresentationElement](../PresentationElement.html) supplier,
 [PresentationElement](../PresentationElement.html) client)`
Draws the path adornment.
`protected int`
`[getClientEndPreferredSize](#getClientEndPreferredSize(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PathElement](PathElement.html) pathElement,
 [PresentationElement](../PresentationElement.html) client)`
The path client end preferred size.
`protected [PathEndRenderer](PathEndRenderer.html)`
`[getClientEndRenderer](#getClientEndRenderer(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PathElement](PathElement.html) pathElement,
 [PresentationElement](../PresentationElement.html) client)`
Provides the path client end renderer.
`int`
`[getLineWidth](#getLineWidth(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) pathElement)`
Returns path line width
 Override to use the custom line width
`protected [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html)`
`[getPathStroke](#getPathStroke(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](PathElement.html) pathElement)`
Stroke used to draw path.
`protected int`
`[getSupplierEndPreferredSize](#getSupplierEndPreferredSize(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PathElement](PathElement.html) pathElement,
 [PresentationElement](../PresentationElement.html) supplier)`
The path supplier end preferred size.
`protected [PathEndRenderer](PathEndRenderer.html)`
`[getSupplierEndRenderer](#getSupplierEndRenderer(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PathElement](PathElement.html) pathElement,
 [PresentationElement](../PresentationElement.html) supplier)`
Provides the path supplier end renderer.
`protected final void`
`[updateText](#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) presentationElement)`
Does nothing, should not be called
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElementRenderer](../PresentationElementRenderer.html)
`[afterUpdate](../PresentationElementRenderer.html#afterUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [beforeUpdate](../PresentationElementRenderer.html#beforeUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getCenterlinePoint](../PresentationElementRenderer.html#getCenterlinePoint(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getColor](../PresentationElementRenderer.html#getColor(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementColorEnum)), [getFontProvider](../PresentationElementRenderer.html#getFontProvider(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getText](../PresentationElementRenderer.html#getText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementTextEnum)), [propertiesChanged](../PresentationElementRenderer.html#propertiesChanged(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PathElementRenderer
public PathElementRenderer()
 ============ METHOD DETAIL ========== 
Method Details
getClientEndPreferredSize
protected int getClientEndPreferredSize([PathElement](PathElement.html) pathElement,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) client)
The path client end preferred size. End size is used when drawing adornment on path end (e.g. arrow on the end).
 Override to change the client end size.
Parameters:
`pathElement` - path element
`client` - client end of the path element. It might not be actually connected to the path. Should be used instead of [`PathElement.getClient()`](PathElement.html#getClient())
Returns:
end size, or 0 to use default end size
getSupplierEndPreferredSize
protected int getSupplierEndPreferredSize([PathElement](PathElement.html) pathElement,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) supplier)
The path supplier end preferred size. End size is used when drawing adornment on path end (e.g. arrow on the end).
 Override to change the supplier end size.
Parameters:
`pathElement` - path element
`supplier` - supplier end of the path. Might be null when the path is being newly created. Should be used instead of [`PathElement.getSupplier()`](PathElement.html#getSupplier())
Returns:
end size, or 0 to use default end size
getClientEndRenderer
@CheckForNullprotected [PathEndRenderer](PathEndRenderer.html) getClientEndRenderer([PathElement](PathElement.html) pathElement,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) client)
Provides the path client end renderer.
 Override the method to return the custom path end renderer.
Parameters:
`pathElement` - path element
`client` - client end of the path element. It might not be actually connected to the path. Should be used instead of [`PathElement.getClient()`](PathElement.html#getClient())
Returns:
custom renderer, or null to use default end renderer
See Also:
[`PathEndRenderer`](PathEndRenderer.html)
getSupplierEndRenderer
@CheckForNullprotected [PathEndRenderer](PathEndRenderer.html) getSupplierEndRenderer([PathElement](PathElement.html) pathElement,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) supplier)
Provides the path supplier end renderer.
 Override the method to return the custom path end renderer.
Parameters:
`pathElement` - path element
`supplier` - supplier end of the path. Might be null when the path is being newly created. Should be used instead of [`PathElement.getSupplier()`](PathElement.html#getSupplier())
Returns:
custom renderer, or null to use default end renderer
See Also:
[`PathEndRenderer`](PathEndRenderer.html)
getPathStroke
@CheckForNullprotected [BasicStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html) getPathStroke([PathElement](PathElement.html) pathElement)
Stroke used to draw path.
 Override to change the stroke for path drawing.
Parameters:
`pathElement` - drawing path
Returns:
custom stroke, or null to use the default stroke
See Also:
[`PresentationElement.getStroke(int)`](../PresentationElement.html#getStroke(int))
[`PresentationElement.getStroke(int, int)`](../PresentationElement.html#getStroke(int,int))
[`PresentationElement.getStroke(BasicStroke, int)`](../PresentationElement.html#getStroke(java.awt.BasicStroke,int))
[`PresentationElement.getStroke(int, int, int)`](../PresentationElement.html#getStroke(int,int,int))
[`PresentationElement.getStroke(float, int, int, float, float[], float)`](../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float))
getLineWidth
public int getLineWidth([PathElement](PathElement.html) pathElement)
Returns path line width
 Override to use the custom line width
Parameters:
`pathElement` - path to draw.
Returns:
line width, or 0 to use default line width.
drawPathAdornment
@OpenApiprotected void drawPathAdornment([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 [PathElement](PathElement.html) pathElement,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplierPoint,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) clientPoint,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> breakPoints,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) supplier,
 @CheckForNull
 [PresentationElement](../PresentationElement.html) client)
Draws the path adornment. By default draws no adornment.
 Override the method to add the custom adornment drawing.
Parameters:
`g` - graphics where path is drawn
`pathElement` - path to draw adornment for
`supplierPoint` - point where the supplier end should be painted. Should be used instead of [`PathElement.getSupplierDrawPoint()`](PathElement.html#getSupplierDrawPoint())
`clientPoint` - point where the client end should be painted. Should be used instead of [`PathElement.getClientDrawPoint()`](PathElement.html#getClientDrawPoint()) ()}
`breakPoints` - breakpoints between the supplier and client points, in that order. Should be used instead of [`PathElement.getBreakPoints()`](PathElement.html#getBreakPoints())
`supplier` - supplier end of the path. Might be null when the path is being newly created. Should be used instead of [`PathElement.getSupplier()`](PathElement.html#getSupplier())
`client` - client end of the path element. It might not be actually connected to the path. Should be used instead of [`PathElement.getClient()`](PathElement.html#getClient())
updateText
protected final void updateText([PresentationElement](../PresentationElement.html) presentationElement)
Does nothing, should not be called
Specified by:
`[updateText](../PresentationElementRenderer.html#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElementRenderer](../PresentationElementRenderer.html)`
Parameters:
`presentationElement` - presentation element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.paths</a></div>
<h1 class="title" title="Class PathElementRenderer">Class PathElementRenderer</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.paths.PathElementRenderer</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PathElementRenderer</span>
<span class="extends-implements">extends <a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></span></div>
<div class="block">Path element renderer allows to customize (change) the default
 view of <a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathElement</code></a>.
 Path decoration methods are called even when the path is being drawn/created in a diagram, and supplier or client not yet connected, breakpoints are not yet set.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementRenderer</code></a></li>
<li><a href="../shapes/ShapeRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes"><code>ShapeRenderer</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PathElementRenderer</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#drawPathAdornment(java.awt.Graphics,com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.awt.Point,java.awt.Point,java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">drawPathAdornment</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 <a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakPoints,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draws the path adornment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientEndPreferredSize(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">getClientEndPreferredSize</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The path client end preferred size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="PathEndRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndRenderer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClientEndRenderer(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">getClientEndRenderer</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides the path client end renderer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineWidth(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getLineWidth</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns path line width
 Override to use the custom line width</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathStroke(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getPathStroke</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stroke used to draw path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierEndPreferredSize(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSupplierEndPreferredSize</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The path supplier end preferred size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="PathEndRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndRenderer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupplierEndRenderer(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSupplierEndRenderer</a><wbr/>(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides the path supplier end renderer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateText</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does nothing, should not be called</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></h3>
<code><a href="../PresentationElementRenderer.html#afterUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">afterUpdate</a>, <a href="../PresentationElementRenderer.html#beforeUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">beforeUpdate</a>, <a href="../PresentationElementRenderer.html#getCenterlinePoint(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getCenterlinePoint</a>, <a href="../PresentationElementRenderer.html#getColor(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementColorEnum)">getColor</a>, <a href="../PresentationElementRenderer.html#getFontProvider(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getFontProvider</a>, <a href="../PresentationElementRenderer.html#getText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementTextEnum)">getText</a>, <a href="../PresentationElementRenderer.html#propertiesChanged(com.nomagic.magicdraw.uml.symbols.PresentationElement)">propertiesChanged</a></code></div>
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
<h3>PathElementRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathElementRenderer</span>()</div>
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
<section class="detail" id="getClientEndPreferredSize(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getClientEndPreferredSize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getClientEndPreferredSize</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</span></div>
<div class="block">The path client end preferred size. End size is used when drawing adornment on path end (e.g. arrow on the end).
 Override to change the client end size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathElement</code> - path element</dd>
<dd><code>client</code> - client end of the path element. It might not be actually connected to the path. Should be used instead of <a href="PathElement.html#getClient()"><code>PathElement.getClient()</code></a></dd>
<dt>Returns:</dt>
<dd>end size, or 0 to use default end size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierEndPreferredSize(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getSupplierEndPreferredSize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getSupplierEndPreferredSize</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier)</span></div>
<div class="block">The path supplier end preferred size. End size is used when drawing adornment on path end (e.g. arrow on the end).
 Override to change the supplier end size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathElement</code> - path element</dd>
<dd><code>supplier</code> - supplier end of the path. Might be null when the path is being newly created. Should be used instead of <a href="PathElement.html#getSupplier()"><code>PathElement.getSupplier()</code></a></dd>
<dt>Returns:</dt>
<dd>end size, or 0 to use default end size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClientEndRenderer(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getClientEndRenderer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="PathEndRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndRenderer</a></span> <span class="element-name">getClientEndRenderer</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</span></div>
<div class="block">Provides the path client end renderer.
 Override the method to return the custom path end renderer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathElement</code> - path element</dd>
<dd><code>client</code> - client end of the path element. It might not be actually connected to the path. Should be used instead of <a href="PathElement.html#getClient()"><code>PathElement.getClient()</code></a></dd>
<dt>Returns:</dt>
<dd>custom renderer, or null to use default end renderer</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PathEndRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathEndRenderer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSupplierEndRenderer(com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getSupplierEndRenderer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a href="PathEndRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathEndRenderer</a></span> <span class="element-name">getSupplierEndRenderer</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier)</span></div>
<div class="block">Provides the path supplier end renderer.
 Override the method to return the custom path end renderer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathElement</code> - path element</dd>
<dd><code>supplier</code> - supplier end of the path. Might be null when the path is being newly created. Should be used instead of <a href="PathElement.html#getSupplier()"><code>PathElement.getSupplier()</code></a></dd>
<dt>Returns:</dt>
<dd>custom renderer, or null to use default end renderer</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PathEndRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathEndRenderer</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPathStroke(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getPathStroke</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/BasicStroke.html" title="class or interface in java.awt">BasicStroke</a></span> <span class="element-name">getPathStroke</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</span></div>
<div class="block">Stroke used to draw path.
 Override to change the stroke for path drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathElement</code> - drawing path</dd>
<dt>Returns:</dt>
<dd>custom stroke, or null to use the default stroke</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../PresentationElement.html#getStroke(int)"><code>PresentationElement.getStroke(int)</code></a></li>
<li><a href="../PresentationElement.html#getStroke(int,int)"><code>PresentationElement.getStroke(int, int)</code></a></li>
<li><a href="../PresentationElement.html#getStroke(java.awt.BasicStroke,int)"><code>PresentationElement.getStroke(BasicStroke, int)</code></a></li>
<li><a href="../PresentationElement.html#getStroke(int,int,int)"><code>PresentationElement.getStroke(int, int, int)</code></a></li>
<li><a href="../PresentationElement.html#getStroke(float,int,int,float,float%5B%5D,float)"><code>PresentationElement.getStroke(float, int, int, float, float[], float)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLineWidth(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getLineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLineWidth</span><wbr/><span class="parameters">(<a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</span></div>
<div class="block">Returns path line width
 Override to use the custom line width</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathElement</code> - path to draw.</dd>
<dt>Returns:</dt>
<dd>line width, or 0 to use default line width.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawPathAdornment(java.awt.Graphics,com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.awt.Point,java.awt.Point,java.util.List,com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>drawPathAdornment</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">drawPathAdornment</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 <a href="PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplierPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> clientPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; breakPoints,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> supplier,
 @CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> client)</span></div>
<div class="block">Draws the path adornment. By default draws no adornment.
 Override the method to add the custom adornment drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics where path is drawn</dd>
<dd><code>pathElement</code> - path to draw adornment for</dd>
<dd><code>supplierPoint</code> - point where the supplier end should be painted. Should be used instead of <a href="PathElement.html#getSupplierDrawPoint()"><code>PathElement.getSupplierDrawPoint()</code></a></dd>
<dd><code>clientPoint</code> - point where the client end should be painted. Should be used instead of <a href="PathElement.html#getClientDrawPoint()"><code>PathElement.getClientDrawPoint()</code></a> ()}</dd>
<dd><code>breakPoints</code> - breakpoints between the supplier and client points, in that order. Should be used instead of <a href="PathElement.html#getBreakPoints()"><code>PathElement.getBreakPoints()</code></a></dd>
<dd><code>supplier</code> - supplier end of the path. Might be null when the path is being newly created. Should be used instead of <a href="PathElement.html#getSupplier()"><code>PathElement.getSupplier()</code></a></dd>
<dd><code>client</code> - client end of the path element. It might not be actually connected to the path. Should be used instead of <a href="PathElement.html#getClient()"><code>PathElement.getClient()</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>updateText</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">updateText</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Does nothing, should not be called</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElementRenderer.html#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateText</a></code> in class <code><a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - presentation element</dd>
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
