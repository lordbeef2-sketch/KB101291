# JAVA OPENAPI: OrderedHierarchicDiagramLayouter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/orderedhier/OrderedHierarchicDiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/orderedhier/OrderedHierarchicDiagramLayouter.html`
- source_sha256: `bb7193f00468d3bb0b25a264cf795c48b212564ae6d0cc6922d4514e7e9d2241`
- captured_utc: `2026-07-14T16:55:58.962497+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout.orderedhier](package-summary.html)

## Class OrderedHierarchicDiagramLayouter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter](../AbstractDiagramLayouter.html)
[com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter](../AbstractHierarchicDiagramLayouter.html)
[com.nomagic.magicdraw.uml.symbols.layout.HierarchicDiagramLayouter](../HierarchicDiagramLayouter.html)
[com.nomagic.magicdraw.uml.symbols.layout.composite.CompositeStructureDiagramLayouter](../composite/CompositeStructureDiagramLayouter.html)
[com.nomagic.magicdraw.uml.symbols.layout.ClassDiagramLayouter](../ClassDiagramLayouter.html)
com.nomagic.magicdraw.uml.symbols.layout.orderedhier.OrderedHierarchicDiagramLayouter

All Implemented Interfaces:
`[DiagramLayouter](../DiagramLayouter.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public classOrderedHierarchicDiagramLayouter
extends [ClassDiagramLayouter](../ClassDiagramLayouter.html)

Deprecated.
diagram layouting should be done using [`Layouting`](../Layouting.html) class

A layouter with a default sequencing. It also automatically detects the orientation and changes alignment for shapes.
 Best fit for requirement diagrams.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractHierarchicDiagramLayouter](../AbstractHierarchicDiagramLayouter.html)
`[can](../AbstractHierarchicDiagramLayouter.html#can), [pathRerouteCollectors](../AbstractHierarchicDiagramLayouter.html#pathRerouteCollectors)`
Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](../AbstractDiagramLayouter.html)
`[layoutParameters](../AbstractDiagramLayouter.html#layoutParameters)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OrderedHierarchicDiagramLayouter](#%3Cinit%3E())()`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected void`
`[afterLayout](#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([AbstractDiagramLayouterOptionsGroup](../../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](../BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
`protected boolean`
`[layout](#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([AbstractDiagramLayouterOptionsGroup](../../../../core/options/AbstractDiagramLayouterOptionsGroup.html) opt,
 [AbstractDiagramPresentationElement](../../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](../BaseGraph.html) graph)`
Deprecated, for removal: This API element is subject to removal in a future version.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.composite.[CompositeStructureDiagramLayouter](../composite/CompositeStructureDiagramLayouter.html)
`[createPathRerouteCollectors](../composite/CompositeStructureDiagramLayouter.html#createPathRerouteCollectors()), [preProcessing](../composite/CompositeStructureDiagramLayouter.html#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[HierarchicDiagramLayouter](../HierarchicDiagramLayouter.html)
`[canSetLocationForOnEdgeShape](../HierarchicDiagramLayouter.html#canSetLocationForOnEdgeShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [collectOnEdgeToResize](../HierarchicDiagramLayouter.html#collectOnEdgeToResize(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [isTypeSupported](../HierarchicDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractHierarchicDiagramLayouter](../AbstractHierarchicDiagramLayouter.html)
`[addPathRerouteCollector](../AbstractHierarchicDiagramLayouter.html#addPathRerouteCollector(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector)), [clone](../AbstractHierarchicDiagramLayouter.html#clone()), [collectOnEdgeElementsRecursively](../AbstractHierarchicDiagramLayouter.html#collectOnEdgeElementsRecursively(java.util.Collection,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [containsSelectedFromTheSameParent](../AbstractHierarchicDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [createComponentLayouter](../AbstractHierarchicDiagramLayouter.html#createComponentLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.grouping.RecursiveGroupLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)), [dispose](../AbstractHierarchicDiagramLayouter.html#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [fixOnFrameElements](../AbstractHierarchicDiagramLayouter.html#fixOnFrameElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)), [getPathRerouteCollectors](../AbstractHierarchicDiagramLayouter.html#getPathRerouteCollectors()), [getTableShapeViewsInFirstLevel](../AbstractHierarchicDiagramLayouter.html#getTableShapeViewsInFirstLevel(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [initDefaultHierarchicSettings](../AbstractHierarchicDiagramLayouter.html#initDefaultHierarchicSettings(com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [isLayoutAsGrid](../AbstractHierarchicDiagramLayouter.html#isLayoutAsGrid(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [moveOutOfFrameHeader](../AbstractHierarchicDiagramLayouter.html#moveOutOfFrameHeader(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)), [resizeOnEdgeElements](../AbstractHierarchicDiagramLayouter.html#resizeOnEdgeElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [resizeOnEdgeShapes](../AbstractHierarchicDiagramLayouter.html#resizeOnEdgeShapes(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Collection)), [routeNonRoutedPaths](../AbstractHierarchicDiagramLayouter.html#routeNonRoutedPaths(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)), [runIHLLayoutSeries](../AbstractHierarchicDiagramLayouter.html#runIHLLayoutSeries(y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)), [wrapToAccordingGroupLayouter](../AbstractHierarchicDiagramLayouter.html#wrapToAccordingGroupLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,boolean))`
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](../AbstractDiagramLayouter.html)
`[afterLayout](../AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [canLayout](../AbstractDiagramLayouter.html#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [clearOldRectangles](../AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [createCommands](../AbstractDiagramLayouter.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [createGraph](../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [createGraph](../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set)), [createGraph](../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set,boolean)), [drawLayoutResults](../AbstractDiagramLayouter.html#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [getAnchoredPresentationElement](../AbstractDiagramLayouter.html#getAnchoredPresentationElement()), [getDiagramLayouterAbortHandler](../AbstractDiagramLayouter.html#getDiagramLayouterAbortHandler()), [getLayoutParameter](../AbstractDiagramLayouter.html#getLayoutParameter(java.lang.String)), [getOptionsID](../AbstractDiagramLayouter.html#getOptionsID()), [getSelected](../AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [layout](../AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [layoutGraph](../AbstractDiagramLayouter.html#layoutGraph(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [placeLegendAndInfo](../AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [postprocessing](../AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [resizeOuterBoundaryIfNecessary](../AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [setAnchoredPresentationElement](../AbstractDiagramLayouter.html#setAnchoredPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)), [setDefaultLayoutParameters](../AbstractDiagramLayouter.html#setDefaultLayoutParameters()), [setLabelConsiderationMode](../AbstractDiagramLayouter.html#setLabelConsiderationMode(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [setLayoutParameter](../AbstractDiagramLayouter.html#setLayoutParameter(java.lang.String,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OrderedHierarchicDiagramLayouter
@OpenApipublic OrderedHierarchicDiagramLayouter()
Deprecated.
 ============ METHOD DETAIL ========== 
Method Details
layout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)protected boolean layout([AbstractDiagramLayouterOptionsGroup](../../../../core/options/AbstractDiagramLayouterOptionsGroup.html) opt,
 [AbstractDiagramPresentationElement](../../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](../BaseGraph.html) graph)
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `[AbstractDiagramLayouter](../AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))`
Layouts a diagram
Overrides:
`[layout](../ClassDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))` in class `[ClassDiagramLayouter](../ClassDiagramLayouter.html)`
Parameters:
`opt` - layouter options
`dpe` - diagram to layout
`graph` - a constructed graph from the diagram
Returns:
true if it was layouted successfully , false otherwise.
afterLayout
protected void afterLayout([AbstractDiagramLayouterOptionsGroup](../../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](../BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Overrides:
`[afterLayout](../AbstractHierarchicDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))` in class `[AbstractHierarchicDiagramLayouter](../AbstractHierarchicDiagramLayouter.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout.orderedhier</a></div>
<h1 class="title" title="Class OrderedHierarchicDiagramLayouter">Class OrderedHierarchicDiagramLayouter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter</a>
<div class="inheritance"><a href="../AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter</a>
<div class="inheritance"><a href="../HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.HierarchicDiagramLayouter</a>
<div class="inheritance"><a href="../composite/CompositeStructureDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.composite">com.nomagic.magicdraw.uml.symbols.layout.composite.CompositeStructureDiagramLayouter</a>
<div class="inheritance"><a href="../ClassDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.ClassDiagramLayouter</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.orderedhier.OrderedHierarchicDiagramLayouter</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OrderedHierarchicDiagramLayouter</span>
<span class="extends-implements">extends <a href="../ClassDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">ClassDiagramLayouter</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">diagram layouting should be done using <a href="../Layouting.html" title="class in com.nomagic.magicdraw.uml.symbols.layout"><code>Layouting</code></a> class</div>
</div>
<div class="block">A layouter with a default sequencing. It also automatically detects the orientation and changes alignment for shapes.
 Best fit for requirement diagrams.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter">Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="../AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></h3>
<code><a href="../AbstractHierarchicDiagramLayouter.html#can">can</a>, <a href="../AbstractHierarchicDiagramLayouter.html#pathRerouteCollectors">pathRerouteCollectors</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="../AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="../AbstractDiagramLayouter.html#layoutParameters">layoutParameters</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">OrderedHierarchicDiagramLayouter</a>()</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">afterLayout</a><wbr/>(<a href="../../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a><wbr/>(<a href="../../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> opt,
 <a href="../../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.composite.CompositeStructureDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.composite.<a href="../composite/CompositeStructureDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.composite">CompositeStructureDiagramLayouter</a></h3>
<code><a href="../composite/CompositeStructureDiagramLayouter.html#createPathRerouteCollectors()">createPathRerouteCollectors</a>, <a href="../composite/CompositeStructureDiagramLayouter.html#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">preProcessing</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.HierarchicDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="../HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">HierarchicDiagramLayouter</a></h3>
<code><a href="../HierarchicDiagramLayouter.html#canSetLocationForOnEdgeShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">canSetLocationForOnEdgeShape</a>, <a href="../HierarchicDiagramLayouter.html#collectOnEdgeToResize(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">collectOnEdgeToResize</a>, <a href="../HierarchicDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)">isTypeSupported</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="../AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></h3>
<code><a href="../AbstractHierarchicDiagramLayouter.html#addPathRerouteCollector(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector)">addPathRerouteCollector</a>, <a href="../AbstractHierarchicDiagramLayouter.html#clone()">clone</a>, <a href="../AbstractHierarchicDiagramLayouter.html#collectOnEdgeElementsRecursively(java.util.Collection,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">collectOnEdgeElementsRecursively</a>, <a href="../AbstractHierarchicDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">containsSelectedFromTheSameParent</a>, <a href="../AbstractHierarchicDiagramLayouter.html#createComponentLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.grouping.RecursiveGroupLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">createComponentLayouter</a>, <a href="../AbstractHierarchicDiagramLayouter.html#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">dispose</a>, <a href="../AbstractHierarchicDiagramLayouter.html#fixOnFrameElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">fixOnFrameElements</a>, <a href="../AbstractHierarchicDiagramLayouter.html#getPathRerouteCollectors()">getPathRerouteCollectors</a>, <a href="../AbstractHierarchicDiagramLayouter.html#getTableShapeViewsInFirstLevel(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getTableShapeViewsInFirstLevel</a>, <a href="../AbstractHierarchicDiagramLayouter.html#initDefaultHierarchicSettings(com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">initDefaultHierarchicSettings</a>, <a href="../AbstractHierarchicDiagramLayouter.html#isLayoutAsGrid(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">isLayoutAsGrid</a>, <a href="../AbstractHierarchicDiagramLayouter.html#moveOutOfFrameHeader(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">moveOutOfFrameHeader</a>, <a href="../AbstractHierarchicDiagramLayouter.html#resizeOnEdgeElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">resizeOnEdgeElements</a>, <a href="../AbstractHierarchicDiagramLayouter.html#resizeOnEdgeShapes(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Collection)">resizeOnEdgeShapes</a>, <a href="../AbstractHierarchicDiagramLayouter.html#routeNonRoutedPaths(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">routeNonRoutedPaths</a>, <a href="../AbstractHierarchicDiagramLayouter.html#runIHLLayoutSeries(y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">runIHLLayoutSeries</a>, <a href="../AbstractHierarchicDiagramLayouter.html#wrapToAccordingGroupLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,boolean)">wrapToAccordingGroupLayouter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="../AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="../AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">afterLayout</a>, <a href="../AbstractDiagramLayouter.html#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">canLayout</a>, <a href="../AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">clearOldRectangles</a>, <a href="../AbstractDiagramLayouter.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">createCommands</a>, <a href="../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">createGraph</a>, <a href="../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set)">createGraph</a>, <a href="../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set,boolean)">createGraph</a>, <a href="../AbstractDiagramLayouter.html#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">drawLayoutResults</a>, <a href="../AbstractDiagramLayouter.html#getAnchoredPresentationElement()">getAnchoredPresentationElement</a>, <a href="../AbstractDiagramLayouter.html#getDiagramLayouterAbortHandler()">getDiagramLayouterAbortHandler</a>, <a href="../AbstractDiagramLayouter.html#getLayoutParameter(java.lang.String)">getLayoutParameter</a>, <a href="../AbstractDiagramLayouter.html#getOptionsID()">getOptionsID</a>, <a href="../AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getSelected</a>, <a href="../AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">layout</a>, <a href="../AbstractDiagramLayouter.html#layoutGraph(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layoutGraph</a>, <a href="../AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">placeLegendAndInfo</a>, <a href="../AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">postprocessing</a>, <a href="../AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">resizeOuterBoundaryIfNecessary</a>, <a href="../AbstractDiagramLayouter.html#setAnchoredPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">setAnchoredPresentationElement</a>, <a href="../AbstractDiagramLayouter.html#setDefaultLayoutParameters()">setDefaultLayoutParameters</a>, <a href="../AbstractDiagramLayouter.html#setLabelConsiderationMode(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">setLabelConsiderationMode</a>, <a href="../AbstractDiagramLayouter.html#setLayoutParameter(java.lang.String,java.lang.Object)">setLayoutParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>OrderedHierarchicDiagramLayouter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">OrderedHierarchicDiagramLayouter</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
<section class="detail" id="layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> opt,
 <a href="../../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Layouts a diagram</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../ClassDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a></code> in class <code><a href="../ClassDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">ClassDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>opt</code> - layouter options</dd>
<dd><code>dpe</code> - diagram to layout</dd>
<dd><code>graph</code> - a constructed graph from the diagram</dd>
<dt>Returns:</dt>
<dd>true if it was layouted successfully , false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>afterLayout</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterLayout</span><wbr/><span class="parameters">(<a href="../../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../AbstractHierarchicDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">afterLayout</a></code> in class <code><a href="../AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></code></dd>
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
