# JAVA OPENAPI: AbstractLinkDiagramLayouter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/AbstractLinkDiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/AbstractLinkDiagramLayouter.html`
- source_sha256: `9f11bb22624f31a880abacbfa6d09654bff1e5c4f245e1cb37ea7a764dee667b`
- captured_utc: `2026-07-14T16:55:58.076490+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Class AbstractLinkDiagramLayouter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter](AbstractDiagramLayouter.html)
com.nomagic.magicdraw.uml.symbols.layout.AbstractLinkDiagramLayouter

All Implemented Interfaces:
`[DiagramLayouter](DiagramLayouter.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[OrganicLinkDiagramLayouter](OrganicLinkDiagramLayouter.html)`, `[OrthogonalLinkDiagramLayouter](OrthogonalLinkDiagramLayouter.html)`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public abstract classAbstractLinkDiagramLayouter
extends [AbstractDiagramLayouter](AbstractDiagramLayouter.html)

Deprecated.
diagram layouting should be done using [`Layouting`](Layouting.html) class

Layout the diagram symbols in diagram.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](AbstractDiagramLayouter.html)
`[layoutParameters](AbstractDiagramLayouter.html#layoutParameters)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractLinkDiagramLayouter](#%3Cinit%3E(java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths)`
Deprecated.
`[AbstractLinkDiagramLayouter](#%3Cinit%3E(java.lang.String,boolean,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)`
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected void`
`[clearOldRectangles](#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([BaseGraph](BaseGraph.html) graph)`
Deprecated.
Clears old rectangles for shapes.
`protected boolean`
`[containsSelectedFromTheSameParent](#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)`
Deprecated.
Checks if selected elements have the same parent.
`protected [BaseGraph](BaseGraph.html)`
`[createGraph](#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) optionsGroup)`
Deprecated.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[getConnectedPaths](#getConnectedPaths(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView)`
Deprecated.
Gets the selected paths and any paths that are connected to selected shapes.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[getSelected](#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView)`
Deprecated.
`protected void`
`[placeLegendAndInfo](#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [BaseGraph](BaseGraph.html) graph)`
Deprecated.
Places diagram legends and infos.
`protected void`
`[postprocessing](#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([BaseGraph](BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
Does some post-processing after layout.
`protected void`
`[resizeOuterBoundaryIfNecessary](#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
Resizes outer bondary according to graph
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](AbstractDiagramLayouter.html)
`[afterLayout](AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [afterLayout](AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [canLayout](AbstractDiagramLayouter.html#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [clone](AbstractDiagramLayouter.html#clone()), [createCommands](AbstractDiagramLayouter.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set)), [createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set,boolean)), [dispose](AbstractDiagramLayouter.html#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [drawLayoutResults](AbstractDiagramLayouter.html#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [getAnchoredPresentationElement](AbstractDiagramLayouter.html#getAnchoredPresentationElement()), [getDiagramLayouterAbortHandler](AbstractDiagramLayouter.html#getDiagramLayouterAbortHandler()), [getLayoutParameter](AbstractDiagramLayouter.html#getLayoutParameter(java.lang.String)), [getOptionsID](AbstractDiagramLayouter.html#getOptionsID()), [isTypeSupported](AbstractDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)), [layout](AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [layout](AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [layoutGraph](AbstractDiagramLayouter.html#layoutGraph(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [preProcessing](AbstractDiagramLayouter.html#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [setAnchoredPresentationElement](AbstractDiagramLayouter.html#setAnchoredPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)), [setDefaultLayoutParameters](AbstractDiagramLayouter.html#setDefaultLayoutParameters()), [setLabelConsiderationMode](AbstractDiagramLayouter.html#setLabelConsiderationMode(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [setLayoutParameter](AbstractDiagramLayouter.html#setLayoutParameter(java.lang.String,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractLinkDiagramLayouter
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public AbstractLinkDiagramLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths)
Deprecated.
Construct AbstractLinkDiagramLayouter with the given argument.
Parameters:
`optionId` - String.
`nodes` - boolean.
`paths` - boolean.
AbstractLinkDiagramLayouter
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public AbstractLinkDiagramLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
Construct AbstractLinkDiagramLayouter with the given argument.
Parameters:
`optionId` - String.
`nodes` - boolean.
`paths` - boolean.
`supportsSubgraph` - boolean.
 ============ METHOD DETAIL ========== 
Method Details
createGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")protected [BaseGraph](BaseGraph.html) createGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) optionsGroup)
Deprecated.
Constructs a graph for layout
Overrides:
`[createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`dpe` - shapes and edges are taken from this diagram
`optionsGroup` - layouter options
Returns:
a created UMLGraph
resizeOuterBoundaryIfNecessary
protected void resizeOuterBoundaryIfNecessary([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))`
Resizes outer bondary according to graph
Overrides:
`[resizeOuterBoundaryIfNecessary](AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`dpe` - diagram
`mc` - macro command
postprocessing
protected void postprocessing([BaseGraph](BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))`
Does some post-processing after layout. Moves the graph, layouts swimlanes.
Overrides:
`[postprocessing](AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`graph` - the graph data for post-processing
containsSelectedFromTheSameParent
protected boolean containsSelectedFromTheSameParent([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)
Deprecated.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))`
Checks if selected elements have the same parent. if nothing is selected return true
Overrides:
`[containsSelectedFromTheSameParent](AbstractDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
getSelected
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> getSelected([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView)
Deprecated.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))`
Collects a set of selected layoutable presentation elements in a diagram
Overrides:
`[getSelected](AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`diagramView` - the diagram that elements were selected in
Returns:
the selected paths and any paths that are connected to selected shapes. Paths connected
 by other shape element on shape edge are also included
getConnectedPaths
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> getConnectedPaths([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView)
Deprecated.
Gets the selected paths and any paths that are connected to selected shapes. Paths connected
 by other shape element on shape edge are also included
Parameters:
`diagramView` - diagram
Returns:
a set of path elements that should be processed
clearOldRectangles
protected void clearOldRectangles([BaseGraph](BaseGraph.html) graph)
Deprecated.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))`
Clears old rectangles for shapes. The old rectangle is used for link placement in movePath, MoveManager.
Overrides:
`[clearOldRectangles](AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`graph` - layouted graph
placeLegendAndInfo
protected void placeLegendAndInfo([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [BaseGraph](BaseGraph.html) graph)
Deprecated.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))`
Places diagram legends and infos.
Overrides:
`[placeLegendAndInfo](AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`diagram` - diagram

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Class AbstractLinkDiagramLayouter">Class AbstractLinkDiagramLayouter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.AbstractLinkDiagramLayouter</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="OrganicLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrganicLinkDiagramLayouter</a></code>, <code><a href="OrthogonalLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrthogonalLinkDiagramLayouter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractLinkDiagramLayouter</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">diagram layouting should be done using <a href="Layouting.html" title="class in com.nomagic.magicdraw.uml.symbols.layout"><code>Layouting</code></a> class</div>
</div>
<div class="block">Layout the diagram symbols in diagram.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="AbstractDiagramLayouter.html#layoutParameters">layoutParameters</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean,boolean)">AbstractLinkDiagramLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean,boolean,boolean)">AbstractLinkDiagramLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">clearOldRectangles</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Clears old rectangles for shapes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">containsSelectedFromTheSameParent</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if selected elements have the same parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">createGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> optionsGroup)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getConnectedPaths(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getConnectedPaths</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gets the selected paths and any paths that are connected to selected shapes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getSelected</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">placeLegendAndInfo</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Places diagram legends and infos.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">postprocessing</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Does some post-processing after layout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">resizeOuterBoundaryIfNecessary</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Resizes outer bondary according to graph</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">afterLayout</a>, <a href="AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">afterLayout</a>, <a href="AbstractDiagramLayouter.html#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">canLayout</a>, <a href="AbstractDiagramLayouter.html#clone()">clone</a>, <a href="AbstractDiagramLayouter.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">createCommands</a>, <a href="AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set)">createGraph</a>, <a href="AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set,boolean)">createGraph</a>, <a href="AbstractDiagramLayouter.html#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">dispose</a>, <a href="AbstractDiagramLayouter.html#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">drawLayoutResults</a>, <a href="AbstractDiagramLayouter.html#getAnchoredPresentationElement()">getAnchoredPresentationElement</a>, <a href="AbstractDiagramLayouter.html#getDiagramLayouterAbortHandler()">getDiagramLayouterAbortHandler</a>, <a href="AbstractDiagramLayouter.html#getLayoutParameter(java.lang.String)">getLayoutParameter</a>, <a href="AbstractDiagramLayouter.html#getOptionsID()">getOptionsID</a>, <a href="AbstractDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)">isTypeSupported</a>, <a href="AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">layout</a>, <a href="AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a>, <a href="AbstractDiagramLayouter.html#layoutGraph(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layoutGraph</a>, <a href="AbstractDiagramLayouter.html#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">preProcessing</a>, <a href="AbstractDiagramLayouter.html#setAnchoredPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">setAnchoredPresentationElement</a>, <a href="AbstractDiagramLayouter.html#setDefaultLayoutParameters()">setDefaultLayoutParameters</a>, <a href="AbstractDiagramLayouter.html#setLabelConsiderationMode(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">setLabelConsiderationMode</a>, <a href="AbstractDiagramLayouter.html#setLayoutParameter(java.lang.String,java.lang.Object)">setLayoutParameter</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,boolean,boolean)">
<h3>AbstractLinkDiagramLayouter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="element-name">AbstractLinkDiagramLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct AbstractLinkDiagramLayouter with the given argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionId</code> - String.</dd>
<dd><code>nodes</code> - boolean.</dd>
<dd><code>paths</code> - boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,boolean,boolean,boolean)">
<h3>AbstractLinkDiagramLayouter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="element-name">AbstractLinkDiagramLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
<div class="block">Construct AbstractLinkDiagramLayouter with the given argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionId</code> - String.</dd>
<dd><code>nodes</code> - boolean.</dd>
<dd><code>paths</code> - boolean.</dd>
<dd><code>supportsSubgraph</code> - boolean.</dd>
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
<section class="detail" id="createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">
<h3>createGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">protected</span> <span class="return-type"><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></span> <span class="element-name">createGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> optionsGroup)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a graph for layout</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">createGraph</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>dpe</code> - shapes and edges are taken from this diagram</dd>
<dd><code>optionsGroup</code> - layouter options</dd>
<dt>Returns:</dt>
<dd>a created UMLGraph</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>resizeOuterBoundaryIfNecessary</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resizeOuterBoundaryIfNecessary</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Resizes outer bondary according to graph</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">resizeOuterBoundaryIfNecessary</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>dpe</code> - diagram</dd>
<dd><code>mc</code> - macro command</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>postprocessing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">postprocessing</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Does some post-processing after layout. Moves the graph, layouts swimlanes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">postprocessing</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>graph</code> - the graph data for post-processing</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>containsSelectedFromTheSameParent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">containsSelectedFromTheSameParent</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Checks if selected elements have the same parent. if nothing is selected return true</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">containsSelectedFromTheSameParent</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSelected</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Collects a set of selected layoutable presentation elements in a diagram</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getSelected</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>diagramView</code> - the diagram that elements were selected in</dd>
<dt>Returns:</dt>
<dd>the selected paths and any paths that are connected to selected shapes. Paths connected
 by other shape element on shape edge are also included</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedPaths(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getConnectedPaths</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getConnectedPaths</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Gets the selected paths and any paths that are connected to selected shapes. Paths connected
 by other shape element on shape edge are also included</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramView</code> - diagram</dd>
<dt>Returns:</dt>
<dd>a set of path elements that should be processed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>clearOldRectangles</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clearOldRectangles</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Clears old rectangles for shapes. The old rectangle is used for link placement in movePath, MoveManager.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">clearOldRectangles</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>graph</code> - layouted graph</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>placeLegendAndInfo</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">placeLegendAndInfo</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Places diagram legends and infos.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">placeLegendAndInfo</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
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
