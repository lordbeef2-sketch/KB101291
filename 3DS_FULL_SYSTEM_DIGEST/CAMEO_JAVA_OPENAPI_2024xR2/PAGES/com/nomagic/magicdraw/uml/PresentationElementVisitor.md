# JAVA OPENAPI: PresentationElementVisitor (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/PresentationElementVisitor.html
- source_path: `com/nomagic/magicdraw/uml/PresentationElementVisitor.html`
- source_sha256: `da7c947a3778d68e251ffb2650eb002ac3045514bdee608170d1d7093bf59991`
- captured_utc: `2026-07-14T16:55:53.929441+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Interface PresentationElementVisitor

All Known Implementing Classes:
`[InheritanceVisitor](InheritanceVisitor.html)`, `[Visitor](Visitor.html)`

@OpenApipublic interfacePresentationElementVisitor

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[visitAbstractDiagramPresentationElement](#visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](symbols/AbstractDiagramPresentationElement.html) o)`
Method visits given object.
`default void`
`[visitDiagramPresentationElement](#visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](symbols/DiagramPresentationElement.html) o)`
Method visits given object.
`default void`
`[visitPathConnector](#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathConnector](symbols/paths/PathConnector.html) o)`
Method visits given object.
`default void`
`[visitPathElement](#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](symbols/paths/PathElement.html) o)`
Method visits given object.
`default void`
`[visitPresentationElement](#visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](symbols/PresentationElement.html) o)`
Method visits given object.
`default void`
`[visitShapeElement](#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](symbols/shapes/ShapeElement.html) o)`
Method visits given object.

============ METHOD DETAIL ========== 
Method Details
visitDiagramPresentationElement
@OpenApidefault void visitDiagramPresentationElement([DiagramPresentationElement](symbols/DiagramPresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitAbstractDiagramPresentationElement
@OpenApidefault void visitAbstractDiagramPresentationElement([AbstractDiagramPresentationElement](symbols/AbstractDiagramPresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPresentationElement
@OpenApidefault void visitPresentationElement([PresentationElement](symbols/PresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPathConnector
@OpenApidefault void visitPathConnector([PathConnector](symbols/paths/PathConnector.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitPathElement
@OpenApidefault void visitPathElement([PathElement](symbols/paths/PathElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visitShapeElement
@OpenApidefault void visitShapeElement([ShapeElement](symbols/shapes/ShapeElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Interface PresentationElementVisitor">Interface PresentationElementVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="InheritanceVisitor.html" title="class in com.nomagic.magicdraw.uml">InheritanceVisitor</a></code>, <code><a href="Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PresentationElementVisitor</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">visitAbstractDiagramPresentationElement</a><wbr/>(<a href="symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">visitDiagramPresentationElement</a><wbr/>(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">visitPathConnector</a><wbr/>(<a href="symbols/paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">visitPathElement</a><wbr/>(<a href="symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">visitPresentationElement</a><wbr/>(<a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">visitShapeElement</a><wbr/>(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>visitDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitDiagramPresentationElement</span><wbr/><span class="parameters">(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> o)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>visitAbstractDiagramPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitAbstractDiagramPresentationElement</span><wbr/><span class="parameters">(<a href="symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> o)</span>
                                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>visitPresentationElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPresentationElement</span><wbr/><span class="parameters">(<a href="symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> o)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>visitPathConnector</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathConnector</span><wbr/><span class="parameters">(<a href="symbols/paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>visitPathElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathElement</span><wbr/><span class="parameters">(<a href="symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>visitShapeElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitShapeElement</span><wbr/><span class="parameters">(<a href="symbols/shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
