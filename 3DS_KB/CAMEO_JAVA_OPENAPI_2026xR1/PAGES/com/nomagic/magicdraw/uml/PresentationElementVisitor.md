# JAVA OPENAPI: PresentationElementVisitor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/PresentationElementVisitor.html
- source_path: `com/nomagic/magicdraw/uml/PresentationElementVisitor.html`
- source_sha256: `d5974136b83382c7f5223b8725ddfc56c361fb9f5f41b0229771dfba77d09a95`
- captured_utc: `2026-07-14T16:46:05.240870+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Interface PresentationElementVisitor

All Superinterfaces:
`[AbstractVisitor](AbstractVisitor.html)`, `com.dassault_systemes.modeler.foundation.model.BaseElementVisitor`, `[BasePresentationElementVisitor](symbols/BasePresentationElementVisitor.html)`

All Known Subinterfaces:
`[PresentationElementInheritanceVisitor](PresentationElementInheritanceVisitor.html)`

All Known Implementing Classes:
`[InheritanceVisitor](InheritanceVisitor.html)`, `[Visitor](Visitor.html)`

@OpenApipublic interfacePresentationElementVisitorextends [BasePresentationElementVisitor](symbols/BasePresentationElementVisitor.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[visitDiagramPresentationElement](#visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](symbols/DiagramPresentationElement.html) o)`
Method visits given object.
Methods inherited from interface com.dassault_systemes.modeler.foundation.model.BaseElementVisitor
`visitBaseElement`
Methods inherited from interface com.nomagic.magicdraw.uml.symbols.[BasePresentationElementVisitor](symbols/BasePresentationElementVisitor.html)
`[visitAbstractDiagramPresentationElement](symbols/BasePresentationElementVisitor.html#visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [visitPathConnector](symbols/BasePresentationElementVisitor.html#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)), [visitPathElement](symbols/BasePresentationElementVisitor.html#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [visitPresentationElement](symbols/BasePresentationElementVisitor.html#visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [visitShapeElement](symbols/BasePresentationElementVisitor.html#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))`

============ METHOD DETAIL ========== 
Method Details
visitDiagramPresentationElement
@OpenApidefault void visitDiagramPresentationElement([DiagramPresentationElement](symbols/DiagramPresentationElement.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Method visits given object.
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Interface PresentationElementVisitor">Interface PresentationElementVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="AbstractVisitor.html" title="interface in com.nomagic.magicdraw.uml">AbstractVisitor</a></code>, <code>com.dassault_systemes.modeler.foundation.model.BaseElementVisitor</code>, <code><a href="symbols/BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="PresentationElementInheritanceVisitor.html" title="interface in com.nomagic.magicdraw.uml">PresentationElementInheritanceVisitor</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="InheritanceVisitor.html" title="class in com.nomagic.magicdraw.uml">InheritanceVisitor</a></code>, <code><a href="Visitor.html" title="class in com.nomagic.magicdraw.uml">Visitor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PresentationElementVisitor</span><span class="extends-implements">
extends <a href="symbols/BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></span></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#visitDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">visitDiagramPresentationElement</a><wbr/>(<a href="symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method visits given object.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.model.BaseElementVisitor">Methods inherited from interface com.dassault_systemes.modeler.foundation.model.BaseElementVisitor</h3>
<code>visitBaseElement</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.BasePresentationElementVisitor">Methods inherited from interface com.nomagic.magicdraw.uml.symbols.<a href="symbols/BasePresentationElementVisitor.html" title="interface in com.nomagic.magicdraw.uml.symbols">BasePresentationElementVisitor</a></h3>
<code><a href="symbols/BasePresentationElementVisitor.html#visitAbstractDiagramPresentationElement(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">visitAbstractDiagramPresentationElement</a>, <a href="symbols/BasePresentationElementVisitor.html#visitPathConnector(com.nomagic.magicdraw.uml.symbols.paths.PathConnector)">visitPathConnector</a>, <a href="symbols/BasePresentationElementVisitor.html#visitPathElement(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">visitPathElement</a>, <a href="symbols/BasePresentationElementVisitor.html#visitPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement)">visitPresentationElement</a>, <a href="symbols/BasePresentationElementVisitor.html#visitShapeElement(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">visitShapeElement</a></code></div>
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
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Method visits given object.</div>
<dl class="notes">
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
