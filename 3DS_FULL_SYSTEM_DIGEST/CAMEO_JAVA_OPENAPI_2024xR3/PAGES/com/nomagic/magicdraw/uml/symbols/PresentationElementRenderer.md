# JAVA OPENAPI: PresentationElementRenderer (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/PresentationElementRenderer.html
- source_path: `com/nomagic/magicdraw/uml/symbols/PresentationElementRenderer.html`
- source_sha256: `70d959dea37354213bf9cc411f7fe2fd4dfe566d6299fd29fa72ad208d0203ac`
- captured_utc: `2026-07-14T16:55:56.169469+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class PresentationElementRenderer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer

Direct Known Subclasses:
`[PathElementRenderer](paths/PathElementRenderer.html)`, `[PathRenderer](paths/PathRenderer.html)`, `[ShapeRenderer](shapes/ShapeRenderer.html)`

@OpenApiAllpublic abstract classPresentationElementRenderer
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Base class for presentation element renderer.
 Presentation element renderer allows to customize (change) the default view of element.
 E.g. change the displayed text, font, color.
 
 There two types of renderers - [`ShapeRenderer`](shapes/ShapeRenderer.html), and
 [`PathElementRenderer`](paths/PathElementRenderer.html).
 Renderers are registered by [`PresentationElementRendererManager`](PresentationElementRendererManager.html).

See Also:
[`ShapeRenderer`](shapes/ShapeRenderer.html)
[`PathElementRenderer`](paths/PathElementRenderer.html)
[`PresentationElementRendererManager`](PresentationElementRendererManager.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PresentationElementRenderer](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[afterUpdate](#afterUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Invoked right after presentation element update.
`void`
`[beforeUpdate](#beforeUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Invoked right before presentation element update.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getCenterlinePoint](#getCenterlinePoint(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Returns a point for centerline drawing.
`[Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html)`
`[getColor](#getColor(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementColorEnum))([PresentationElement](PresentationElement.html) presentationElement,
 [PresentationElementColorEnum](PresentationElementColorEnum.html) colorEnum)`
Provides the color used to draw presentation element.
`[FontProvider](FontProvider.html)`
`[getFontProvider](#getFontProvider(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Returns the font provider.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementTextEnum))([PresentationElement](PresentationElement.html) presentationElement,
 [PresentationElementTextEnum](PresentationElementTextEnum.html) textEnum)`
Provides the displayable text for the given presentation element.
`void`
`[propertiesChanged](#propertiesChanged(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Invoked when presentation element properties were changed.
`protected abstract void`
`[updateText](#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Update the given presentation element text.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PresentationElementRenderer
public PresentationElementRenderer()
 ============ METHOD DETAIL ========== 
Method Details
beforeUpdate
public void beforeUpdate([PresentationElement](PresentationElement.html) presentationElement)
Invoked right before presentation element update.
Parameters:
`presentationElement` - updating element.
afterUpdate
public void afterUpdate([PresentationElement](PresentationElement.html) presentationElement)
Invoked right after presentation element update.
Parameters:
`presentationElement` - updating element.
propertiesChanged
public void propertiesChanged([PresentationElement](PresentationElement.html) presentationElement)
Invoked when presentation element properties were changed.
Parameters:
`presentationElement` - properties of this element were updated.
getText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText([PresentationElement](PresentationElement.html) presentationElement,
 [PresentationElementTextEnum](PresentationElementTextEnum.html) textEnum)
Provides the displayable text for the given presentation element.
 Override the method to display the custom text.
Parameters:
`presentationElement` - element to display text for.
`textEnum` - describes the displayable text purpose (text is displayed as name, stereotypes, tags, or constraints).
Returns:
displayble text, or null to use the predefined text.
See Also:
[`PresentationElementTextEnum`](PresentationElementTextEnum.html)
getColor
public [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) getColor([PresentationElement](PresentationElement.html) presentationElement,
 [PresentationElementColorEnum](PresentationElementColorEnum.html) colorEnum)
Provides the color used to draw presentation element.
 Override the method to use the custom color.
Parameters:
`presentationElement` - element to draw.
`colorEnum` - describes the color purpose (color is used to draw lines, text, or fill shape).
Returns:
color, or null to use the predefined color.
See Also:
[`PresentationElementColorEnum`](PresentationElementColorEnum.html)
getFontProvider
public [FontProvider](FontProvider.html) getFontProvider([PresentationElement](PresentationElement.html) presentationElement)
Returns the font provider. Provided font is used to display text.
 Override the method to use custom font.
Parameters:
`presentationElement` - presentation element to use font for.
Returns:
custom font provider, or null to use predefined font.
See Also:
[`FontProvider`](FontProvider.html)
getCenterlinePoint
public [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getCenterlinePoint([PresentationElement](PresentationElement.html) presentationElement)
Returns a point for centerline drawing.
 Override the method to use custom centerline point.
Parameters:
`presentationElement` - - element for which centerline point has to be retrieved.
Returns:
centerline point, or null to use predefined point.
updateText
protected abstract void updateText([PresentationElement](PresentationElement.html) presentationElement)
Update the given presentation element text.
Parameters:
`presentationElement` -

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class PresentationElementRenderer">Class PresentationElementRenderer</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.PresentationElementRenderer</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="paths/PathElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElementRenderer</a></code>, <code><a href="paths/PathRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathRenderer</a></code>, <code><a href="shapes/ShapeRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeRenderer</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">PresentationElementRenderer</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Base class for presentation element renderer.
 Presentation element renderer allows to customize (change) the default view of element.
 E.g. change the displayed text, font, color.
 <p></p>
 There two types of renderers - <a href="shapes/ShapeRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes"><code>ShapeRenderer</code></a>, and
 <a href="paths/PathElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathElementRenderer</code></a>.
 Renderers are registered by <a href="PresentationElementRendererManager.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementRendererManager</code></a>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="shapes/ShapeRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes"><code>ShapeRenderer</code></a></li>
<li><a href="paths/PathElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols.paths"><code>PathElementRenderer</code></a></li>
<li><a href="PresentationElementRendererManager.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementRendererManager</code></a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PresentationElementRenderer</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">afterUpdate</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoked right after presentation element update.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">beforeUpdate</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoked right before presentation element update.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenterlinePoint(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getCenterlinePoint</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a point for centerline drawing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColor(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementColorEnum)">getColor</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement,
 <a href="PresentationElementColorEnum.html" title="enum class in com.nomagic.magicdraw.uml.symbols">PresentationElementColorEnum</a> colorEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides the color used to draw presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FontProvider.html" title="class in com.nomagic.magicdraw.uml.symbols">FontProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFontProvider(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getFontProvider</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the font provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementTextEnum)">getText</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement,
 <a href="PresentationElementTextEnum.html" title="enum class in com.nomagic.magicdraw.uml.symbols">PresentationElementTextEnum</a> textEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides the displayable text for the given presentation element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertiesChanged(com.nomagic.magicdraw.uml.symbols.PresentationElement)">propertiesChanged</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoked when presentation element properties were changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">updateText</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Update the given presentation element text.</div>
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
<h3>PresentationElementRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PresentationElementRenderer</span>()</div>
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
<section class="detail" id="beforeUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>beforeUpdate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">beforeUpdate</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Invoked right before presentation element update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - updating element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterUpdate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>afterUpdate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">afterUpdate</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Invoked right after presentation element update.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - updating element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertiesChanged(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>propertiesChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertiesChanged</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Invoked when presentation element properties were changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - properties of this element were updated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementTextEnum)">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement,
 <a href="PresentationElementTextEnum.html" title="enum class in com.nomagic.magicdraw.uml.symbols">PresentationElementTextEnum</a> textEnum)</span></div>
<div class="block">Provides the displayable text for the given presentation element.
 Override the method to display the custom text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - element to display text for.</dd>
<dd><code>textEnum</code> - describes the displayable text purpose (text is displayed as name, stereotypes, tags, or constraints).</dd>
<dt>Returns:</dt>
<dd>displayble text, or null to use the predefined text.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PresentationElementTextEnum.html" title="enum class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementTextEnum</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColor(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElementColorEnum)">
<h3>getColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a></span> <span class="element-name">getColor</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement,
 <a href="PresentationElementColorEnum.html" title="enum class in com.nomagic.magicdraw.uml.symbols">PresentationElementColorEnum</a> colorEnum)</span></div>
<div class="block">Provides the color used to draw presentation element.
 Override the method to use the custom color.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - element to draw.</dd>
<dd><code>colorEnum</code> - describes the color purpose (color is used to draw lines, text, or fill shape).</dd>
<dt>Returns:</dt>
<dd>color, or null to use the predefined color.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PresentationElementColorEnum.html" title="enum class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementColorEnum</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFontProvider(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getFontProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="FontProvider.html" title="class in com.nomagic.magicdraw.uml.symbols">FontProvider</a></span> <span class="element-name">getFontProvider</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Returns the font provider. Provided font is used to display text.
 Override the method to use custom font.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - presentation element to use font for.</dd>
<dt>Returns:</dt>
<dd>custom font provider, or null to use predefined font.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="FontProvider.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>FontProvider</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenterlinePoint(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getCenterlinePoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getCenterlinePoint</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Returns a point for centerline drawing.
 Override the method to use custom centerline point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - - element for which centerline point has to be retrieved.</dd>
<dt>Returns:</dt>
<dd>centerline point, or null to use predefined point.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateText(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>updateText</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">updateText</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Update the given presentation element text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - </dd>
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
