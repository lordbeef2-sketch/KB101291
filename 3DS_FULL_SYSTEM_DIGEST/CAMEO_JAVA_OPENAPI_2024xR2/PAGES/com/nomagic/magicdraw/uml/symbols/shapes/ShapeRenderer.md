# JAVA OPENAPI: ShapeRenderer (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/symbols/shapes/ShapeRenderer.html
- source_path: `com/nomagic/magicdraw/uml/symbols/shapes/ShapeRenderer.html`
- source_sha256: `177ff94b996048a6151887d2bb6b99ab35bdcc337b6915d967cff6701a8d411d`
- captured_utc: `2026-07-14T16:55:57.356480+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.shapes](package-summary.html)

## Class ShapeRenderer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer](../PresentationElementRenderer.html)
com.nomagic.magicdraw.uml.symbols.shapes.ShapeRenderer

@OpenApiAllpublic classShapeRenderer
extends [PresentationElementRenderer](../PresentationElementRenderer.html)

Shape element renderer allows to customize (change) the default
 view of [`ShapeElement`](ShapeElement.html).

See Also:
[`PresentationElementRenderer`](../PresentationElementRenderer.html)
[`PathElementRenderer`](../paths/PathElementRenderer.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ShapeRenderer](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[calculateMinimumSize](#calculateMinimumSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Dimension))([ShapeElement](ShapeElement.html) presentationElement,
 [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) minimumSize)`
Calculate the minimum shape size of the given shape element.
`void`
`[calculatePreferredSize](#calculatePreferredSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Dimension))([ShapeElement](ShapeElement.html) shapeElement,
 [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) prefSize)`
Calculate the shape element preferred size.
`[ContainerShape](../../../../awt/ContainerShape.html)`
`[createBoundingShape](#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement))([ShapeElement](ShapeElement.html) shapeElement,
 [PathElement](../paths/PathElement.html) pathElement)`
Deprecated.
use [`createBoundingShape(ShapeElement, PathElement, BoundsTransformation)`](#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))
`[ContainerShape](../../../../awt/ContainerShape.html)`
`[createBoundingShape](#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))([ShapeElement](ShapeElement.html) shapeElement,
 [PathElement](../paths/PathElement.html) pathElement,
 [BoundsTransformation](../BoundsTransformation.html) data)`
Returns the shape element boundaries where the path will be connected.
`void`
`[draw](#draw(java.awt.Graphics,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 [PresentationElement](../PresentationElement.html) presentationElement)`
Draws the symbol using the predifined drawing pattern.
`[Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html)`
`[getDefaultSize](#getDefaultSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](ShapeElement.html) shapeElement)`
Return default shape element size used during symbol drawing.
`protected final void`
`[updateText](#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) presentationElement)`
Update shape text.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[PresentationElementRenderer](../PresentationElementRenderer.html)
`[afterUpdate](../PresentationElementRenderer.html#afterUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [beforeUpdate](../PresentationElementRenderer.html#beforeUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getCenterlinePoint](../PresentationElementRenderer.html#getCenterlinePoint(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getColor](../PresentationElementRenderer.html#getColor(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementColorEnum)), [getFontProvider](../PresentationElementRenderer.html#getFontProvider(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getText](../PresentationElementRenderer.html#getText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementTextEnum)), [propertiesChanged](../PresentationElementRenderer.html#propertiesChanged(com.nomagic.magicdraw.uml.symbols.PresentationElement))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ShapeRenderer
public ShapeRenderer()
 ============ METHOD DETAIL ========== 
Method Details
draw
public void draw([Graphics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html) g,
 [PresentationElement](../PresentationElement.html) presentationElement)
Draws the symbol using the predifined drawing pattern.
 Override the method to add the custom drawing.
Parameters:
`g` - graphics where shape is drawn.
`presentationElement` - presentation element to draw.
calculateMinimumSize
public void calculateMinimumSize([ShapeElement](ShapeElement.html) presentationElement,
 [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) minimumSize)
Calculate the minimum shape size of the given shape element.
 Override to change the shape element minimum size.
Parameters:
`presentationElement` - minimum size of.
`minimumSize` - calculated minimum size.
calculatePreferredSize
public void calculatePreferredSize([ShapeElement](ShapeElement.html) shapeElement,
 [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) prefSize)
Calculate the shape element preferred size.
 Override to change the shape element preferred size.
Parameters:
`shapeElement` - preferred size of.
`prefSize` - calculated preferred size.
getDefaultSize
@CheckForNullpublic [Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) getDefaultSize([ShapeElement](ShapeElement.html) shapeElement)
Return default shape element size used during symbol drawing.
 Override method to use custom default size.
Parameters:
`shapeElement` - shape
Returns:
custom default size, or null to use predefined default size.
createBoundingShape
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [ContainerShape](../../../../awt/ContainerShape.html) createBoundingShape([ShapeElement](ShapeElement.html) shapeElement,
 [PathElement](../paths/PathElement.html) pathElement)
Deprecated.
use [`createBoundingShape(ShapeElement, PathElement, BoundsTransformation)`](#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation))
Returns the shape element boundaries where the path will be connected.
 Override to add (calculate) the custom boundaries.
Parameters:
`shapeElement` - shape to calculate boundaries of.
`pathElement` - path connecting.
Returns:
bounding shape that defines the boundaries.
createBoundingShape
public [ContainerShape](../../../../awt/ContainerShape.html) createBoundingShape([ShapeElement](ShapeElement.html) shapeElement,
 [PathElement](../paths/PathElement.html) pathElement,
 [BoundsTransformation](../BoundsTransformation.html) data)
Returns the shape element boundaries where the path will be connected.
 Override to add (calculate) the custom boundaries.
Parameters:
`shapeElement` - shape to calculate boundaries of.
`pathElement` - path connecting.
`data` - bounds transformation data
Returns:
bounding shape that defines the boundaries.
updateText
protected final void updateText([PresentationElement](../PresentationElement.html) presentationElement)
Update shape text.
Specified by:
`[updateText](../PresentationElementRenderer.html#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[PresentationElementRenderer](../PresentationElementRenderer.html)`
Parameters:
`presentationElement` - element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.shapes</a></div>
<h1 class="title" title="Class ShapeRenderer">Class ShapeRenderer</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.shapes.ShapeRenderer</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ShapeRenderer</span>
<span class="extends-implements">extends <a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></span></div>
<div class="block">Shape element renderer allows to customize (change) the default
 view of <a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes"><code>ShapeElement</code></a>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementRenderer</code></a></li>
<li><a href="../paths/PathElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathElementRenderer</code></a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ShapeRenderer</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateMinimumSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Dimension)">calculateMinimumSize</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> presentationElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> minimumSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate the minimum shape size of the given shape element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#calculatePreferredSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Dimension)">calculatePreferredSize</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> prefSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate the shape element preferred size.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">createBoundingShape</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)"><code>createBoundingShape(ShapeElement, PathElement, BoundsTransformation)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">createBoundingShape</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the shape element boundaries where the path will be connected.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#draw(java.awt.Graphics,com.nomagic.magicdraw.uml.symbols.PresentationElement)">draw</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Draws the symbol using the predifined drawing pattern.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">getDefaultSize</a><wbr/>(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return default shape element size used during symbol drawing.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateText</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update shape text.</div>
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
<h3>ShapeRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ShapeRenderer</span>()</div>
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
<section class="detail" id="draw(java.awt.Graphics,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>draw</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">draw</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Graphics.html" title="class or interface in java.awt">Graphics</a> g,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Draws the symbol using the predifined drawing pattern.
 Override the method to add the custom drawing.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>g</code> - graphics where shape is drawn.</dd>
<dd><code>presentationElement</code> - presentation element to draw.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateMinimumSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Dimension)">
<h3>calculateMinimumSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculateMinimumSize</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> presentationElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> minimumSize)</span></div>
<div class="block">Calculate the minimum shape size of the given shape element.
 Override to change the shape element minimum size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - minimum size of.</dd>
<dd><code>minimumSize</code> - calculated minimum size.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculatePreferredSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Dimension)">
<h3>calculatePreferredSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculatePreferredSize</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a> prefSize)</span></div>
<div class="block">Calculate the shape element preferred size.
 Override to change the shape element preferred size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shapeElement</code> - preferred size of.</dd>
<dd><code>prefSize</code> - calculated preferred size.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultSize(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>getDefaultSize</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></span> <span class="element-name">getDefaultSize</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement)</span></div>
<div class="block">Return default shape element size used during symbol drawing.
 Override method to use custom default size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shapeElement</code> - shape</dd>
<dt>Returns:</dt>
<dd>custom default size, or null to use predefined default size.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>createBoundingShape</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createBoundingShape</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)"><code>createBoundingShape(ShapeElement, PathElement, BoundsTransformation)</code></a></div>
</div>
<div class="block">Returns the shape element boundaries where the path will be connected.
 Override to add (calculate) the custom boundaries.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shapeElement</code> - shape to calculate boundaries of.</dd>
<dd><code>pathElement</code> - path connecting.</dd>
<dt>Returns:</dt>
<dd>bounding shape that defines the boundaries.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createBoundingShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,com.nomagic.magicdraw.uml.symbols.paths.PathElement,com.nomagic.magicdraw.uml.symbols.BoundsTransformation)">
<h3>createBoundingShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../awt/ContainerShape.html" title="class in com.nomagic.awt">ContainerShape</a></span> <span class="element-name">createBoundingShape</span><wbr/><span class="parameters">(<a href="ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement,
 <a href="../BoundsTransformation.html" title="class in com.nomagic.magicdraw.uml.symbols">BoundsTransformation</a> data)</span></div>
<div class="block">Returns the shape element boundaries where the path will be connected.
 Override to add (calculate) the custom boundaries.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shapeElement</code> - shape to calculate boundaries of.</dd>
<dd><code>pathElement</code> - path connecting.</dd>
<dd><code>data</code> - bounds transformation data</dd>
<dt>Returns:</dt>
<dd>bounding shape that defines the boundaries.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>updateText</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">updateText</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Update shape text.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../PresentationElementRenderer.html#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateText</a></code> in class <code><a href="../PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - element</dd>
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
