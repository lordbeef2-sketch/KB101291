# JAVA OPENAPI: BasePresentationElementInheritanceVisitor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/BasePresentationElementInheritanceVisitor.html
- source_path: `com/nomagic/magicdraw/uml/symbols/BasePresentationElementInheritanceVisitor.html`
- source_sha256: `6e7c9f14807448bc7aeccf57e999690c738aa3d96f4873fe8b60dd2dabfb617d`
- captured_utc: `2026-07-14T16:46:05.867877+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Interface BasePresentationElementInheritanceVisitor

All Superinterfaces:
`[AbstractVisitor](../AbstractVisitor.html)`, `com.dassault_systemes.modeler.foundation.model.BaseElementVisitor`, `[BasePresentationElementVisitor](BasePresentationElementVisitor.html)`

All Known Subinterfaces:
`[PresentationElementInheritanceVisitor](../PresentationElementInheritanceVisitor.html)`

All Known Implementing Classes:
`[InheritanceVisitor](../InheritanceVisitor.html)`

@OpenApipublic interfaceBasePresentationElementInheritanceVisitorextends [BasePresentationElementVisitor](BasePresentationElementVisitor.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[visitPathConnector](#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector))([PathConnector](paths/PathConnector.html) o)`
Method visits given object.
`default void`
`[visitPathElement](#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](paths/PathElement.html) o)`
Method visits given object.
`default void`
`[visitShapeElement](#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](shapes/ShapeElement.html) o)`
Method visits given object.
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.BaseElementVisitor
`visitBaseElement`

============ METHOD DETAIL ========== 
Method Details
visitShapeElement
@OpenApidefault void visitShapeElement([ShapeElement](shapes/ShapeElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[BasePresentationElementVisitor](BasePresentationElementVisitor.html#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))`
Method visits given object.
Specified by:
`[visitShapeElement](BasePresentationElementVisitor.html#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))` in interface `[BasePresentationElementVisitor](BasePresentationElementVisitor.html)`
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visitPathConnector
@OpenApidefault void visitPathConnector([PathConnector](paths/PathConnector.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[BasePresentationElementVisitor](BasePresentationElementVisitor.html#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector))`
Method visits given object.
Specified by:
`[visitPathConnector](BasePresentationElementVisitor.html#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector))` in interface `[BasePresentationElementVisitor](BasePresentationElementVisitor.html)`
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
visitPathElement
@OpenApidefault void visitPathElement([PathElement](paths/PathElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Description copied from interface: `[BasePresentationElementVisitor](BasePresentationElementVisitor.html#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))`
Method visits given object.
Specified by:
`[visitPathElement](BasePresentationElementVisitor.html#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement))` in interface `[BasePresentationElementVisitor](BasePresentationElementVisitor.html)`
Parameters:
`o` - object to visit.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Interface BasePresentationElementInheritanceVisitor">Interface BasePresentationElementInheritanceVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code>, <code>com.dassault_systemes.modeler.foundation.model.BaseElementVisitor</code>, <code><a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../PresentationElementInheritanceVisitor.html" title="interface in com.nomagic.magicdraw.uml">PresentationElementInheritanceVisitor</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../InheritanceVisitor.html" title="class in com.nomagic.magicdraw.uml">InheritanceVisitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BasePresentationElementInheritanceVisitor</span><span class="extends-implements">
extends <a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></span></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">visitPathConnector</a><wbr/>(<a href="paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">visitPathElement</a><wbr/>(<a href="paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">visitShapeElement</a><wbr/>(<a href="shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.BaseElementVisitor">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.BaseElementVisitor</h3>
<code>visitBaseElement</code></div>
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
<section class="detail" id="visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>visitShapeElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitShapeElement</span><wbr/><span class="parameters">(<a href="shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> o)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="BasePresentationElementVisitor.html#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">BasePresentationElementVisitor</a></code></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BasePresentationElementVisitor.html#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">visitShapeElement</a></code> in interface <code><a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">
<h3>visitPathConnector</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathConnector</span><wbr/><span class="parameters">(<a href="paths/PathConnector.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathConnector</a> o)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="BasePresentationElementVisitor.html#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">BasePresentationElementVisitor</a></code></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BasePresentationElementVisitor.html#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">visitPathConnector</a></code> in interface <code><a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>visitPathElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">visitPathElement</span><wbr/><span class="parameters">(<a href="paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> o)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="BasePresentationElementVisitor.html#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">BasePresentationElementVisitor</a></code></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BasePresentationElementVisitor.html#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">visitPathElement</a></code> in interface <code><a href="BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - object to visit.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
