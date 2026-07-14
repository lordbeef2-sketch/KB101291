# JAVA OPENAPI: AbstractHierarchicDiagramLayouter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/AbstractHierarchicDiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/AbstractHierarchicDiagramLayouter.html`
- source_sha256: `61a67ce65355663bb227f73177078554b2755c34b0279fd8464bc792079c9b1a`
- captured_utc: `2026-07-14T16:55:58.048490+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Class AbstractHierarchicDiagramLayouter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter](AbstractDiagramLayouter.html)
com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter

All Implemented Interfaces:
`[DiagramLayouter](DiagramLayouter.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[HierarchicDiagramLayouter](HierarchicDiagramLayouter.html)`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public abstract classAbstractHierarchicDiagramLayouter
extends [AbstractDiagramLayouter](AbstractDiagramLayouter.html)

Deprecated.
use [`Layouting`](Layouting.html) class for layouting a diagram

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected com.dassault_systemes.modeler.magic.diagram.ylayout.candidates.AbstractCustomCandidates`
`[can](#can)`
Deprecated.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector>`
`[pathRerouteCollectors](#pathRerouteCollectors)`
Deprecated.
Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](AbstractDiagramLayouter.html)
`[layoutParameters](AbstractDiagramLayouter.html#layoutParameters)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractHierarchicDiagramLayouter](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId)`
Deprecated, for removal: This API element is subject to removal in a future version.
use no-arg constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected void`
`[addPathRerouteCollector](#addPathRerouteCollector(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector))(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector collector)`
Deprecated.
`protected void`
`[afterLayout](#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
`protected boolean`
`[canSetLocationForOnEdgeShape](#canSetLocationForOnEdgeShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../shapes/ShapeElement.html) shapeElement)`
Deprecated.
`[AbstractHierarchicDiagramLayouter](AbstractHierarchicDiagramLayouter.html)`
`[clone](#clone())()`
Deprecated.
`protected void`
`[collectOnEdgeElementsRecursively](#collectOnEdgeElementsRecursively(java.util.Collection,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ShapeElement](../shapes/ShapeElement.html)> collectTo,
 [ShapeElement](../shapes/ShapeElement.html) collectFrom)`
Deprecated.
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ShapeElement](../shapes/ShapeElement.html)>`
`[collectOnEdgeToResize](#collectOnEdgeToResize(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)`
Deprecated.
`protected boolean`
`[containsSelectedFromTheSameParent](#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)`
Deprecated.
Activity layouter should also consider when nodes in TableShapeViews are selected and layouted.
`protected y.layout.ComponentLayouter`
`[createComponentLayouter](#createComponentLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.grouping.RecursiveGroupLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup))([BaseGraph](BaseGraph.html) graph,
 y.layout.grouping.RecursiveGroupLayouter coreLayouter,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) opt)`
Deprecated.
Creates a component layouter if possible.
`protected void`
`[createPathRerouteCollectors](#createPathRerouteCollectors())()`
Deprecated.
`protected void`
`[dispose](#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([BaseGraph](BaseGraph.html) graph)`
Deprecated.
`protected void`
`[fixOnFrameElements](#fixOnFrameElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup))([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) o)`
Deprecated.
Fixes, moves, sorts overlapping shapes on diagram frame.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector>`
`[getPathRerouteCollectors](#getPathRerouteCollectors())()`
Deprecated.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView>`
`[getTableShapeViewsInFirstLevel](#getTableShapeViewsInFirstLevel(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)`
Deprecated.
`protected y.layout.hierarchic.IncrementalHierarchicLayouter`
`[initDefaultHierarchicSettings](#initDefaultHierarchicSettings(com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) opt,
 [BaseGraph](BaseGraph.html) graph)`
Deprecated.
Initializes hierarchic layouter settings: - Enables backlooping - Sets group compaction
 enabled - Aligns groups in center - Sets routing style to orthogonal - Adds group node insets
 - Enables label layout - Sets the node sequence within layer.
`protected static boolean`
`[isLayoutAsGrid](#isLayoutAsGrid(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([BaseGraph](BaseGraph.html) graph)`
Deprecated.
Checks if the graph should be layouted as grid
`protected boolean`
`[layout](#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) opt,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](BaseGraph.html) graph)`
Deprecated, for removal: This API element is subject to removal in a future version.
`protected void`
`[moveOutOfFrameHeader](#moveOutOfFrameHeader(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) o)`
Deprecated.
Moves elements of the diagram frame header view, so that they would not overlap
`protected void`
`[preProcessing](#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
`protected void`
`[resizeOnEdgeElements](#resizeOnEdgeElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)`
Deprecated.
Resizes elements on edge to the minimal size.
`protected void`
`[resizeOnEdgeShapes](#resizeOnEdgeShapes(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Collection))([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ShapeElement](../shapes/ShapeElement.html)> shapesToResize)`
Deprecated.
`protected void`
`[routeNonRoutedPaths](#routeNonRoutedPaths(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection))([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector> rerouteCollectors)`
Deprecated.
`protected void`
`[runIHLLayoutSeries](#runIHLLayoutSeries(y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup))(y.layout.hierarchic.IncrementalHierarchicLayouter ihl,
 [BaseGraph](BaseGraph.html) graph,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) options)`
Deprecated.
`protected y.layout.Layouter`
`[wrapToAccordingGroupLayouter](#wrapToAccordingGroupLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,boolean))([BaseGraph](BaseGraph.html) graph,
 y.layout.hierarchic.IncrementalHierarchicLayouter layouter,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) opt,
 boolean fromSketch)`
Deprecated.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](AbstractDiagramLayouter.html)
`[afterLayout](AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [canLayout](AbstractDiagramLayouter.html#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [clearOldRectangles](AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [createCommands](AbstractDiagramLayouter.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set)), [createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set,boolean)), [drawLayoutResults](AbstractDiagramLayouter.html#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [getAnchoredPresentationElement](AbstractDiagramLayouter.html#getAnchoredPresentationElement()), [getDiagramLayouterAbortHandler](AbstractDiagramLayouter.html#getDiagramLayouterAbortHandler()), [getLayoutParameter](AbstractDiagramLayouter.html#getLayoutParameter(java.lang.String)), [getOptionsID](AbstractDiagramLayouter.html#getOptionsID()), [getSelected](AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)), [isTypeSupported](AbstractDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)), [layout](AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [layoutGraph](AbstractDiagramLayouter.html#layoutGraph(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [placeLegendAndInfo](AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [postprocessing](AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [resizeOuterBoundaryIfNecessary](AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [setAnchoredPresentationElement](AbstractDiagramLayouter.html#setAnchoredPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)), [setDefaultLayoutParameters](AbstractDiagramLayouter.html#setDefaultLayoutParameters()), [setLabelConsiderationMode](AbstractDiagramLayouter.html#setLabelConsiderationMode(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)), [setLayoutParameter](AbstractDiagramLayouter.html#setLayoutParameter(java.lang.String,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
can
@CheckForNullprotected com.dassault_systemes.modeler.magic.diagram.ylayout.candidates.AbstractCustomCandidates can
Deprecated.
pathRerouteCollectors
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector> pathRerouteCollectors
Deprecated.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractHierarchicDiagramLayouter
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public AbstractHierarchicDiagramLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId)
Deprecated, for removal: This API element is subject to removal in a future version.
use no-arg constructor
 ============ METHOD DETAIL ========== 
Method Details
initDefaultHierarchicSettings
protected y.layout.hierarchic.IncrementalHierarchicLayouter initDefaultHierarchicSettings([HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) opt,
 [BaseGraph](BaseGraph.html) graph)
Deprecated.
Initializes hierarchic layouter settings: - Enables backlooping - Sets group compaction
 enabled - Aligns groups in center - Sets routing style to orthogonal - Adds group node insets
 - Enables label layout - Sets the node sequence within layer.
Parameters:
`opt` - options
`graph` - current graph that should be layouted
runIHLLayoutSeries
protected void runIHLLayoutSeries(y.layout.hierarchic.IncrementalHierarchicLayouter ihl,
 [BaseGraph](BaseGraph.html) graph,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) options)
Deprecated.
wrapToAccordingGroupLayouter
protected y.layout.Layouter wrapToAccordingGroupLayouter([BaseGraph](BaseGraph.html) graph,
 y.layout.hierarchic.IncrementalHierarchicLayouter layouter,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) opt,
 boolean fromSketch)
Deprecated.
createComponentLayouter
@CheckForNullprotected y.layout.ComponentLayouter createComponentLayouter([BaseGraph](BaseGraph.html) graph,
 y.layout.grouping.RecursiveGroupLayouter coreLayouter,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) opt)
Deprecated.
Creates a component layouter if possible. Sub-graphs that can be identified as separate components will be processed and placed to a more convenient location.
 It may not be possible to create component layouter if sequencing, tableShape partitions etc. are used
Parameters:
`graph` - layouted graph
`coreLayouter` - the core layouter for component layouter
`opt` - hierarchic options
Returns:
a component layouter if possible.
isLayoutAsGrid
protected static boolean isLayoutAsGrid([BaseGraph](BaseGraph.html) graph)
Deprecated.
Checks if the graph should be layouted as grid
Parameters:
`graph` - graph to check
Returns:
true if should layout the graph as grid, false otherwise
layout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)protected boolean layout([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) opt,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](BaseGraph.html) graph)
Deprecated, for removal: This API element is subject to removal in a future version.
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))`
Layouts a diagram
Specified by:
`[layout](AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`opt` - layouter options
`dpe` - diagram to layout
`graph` - a constructed graph from the diagram
Returns:
true if it was layouted successfully , false otherwise.
resizeOnEdgeElements
protected void resizeOnEdgeElements([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)
Deprecated.
Resizes elements on edge to the minimal size.
Parameters:
`graph` - layouted graph
`options` - options that may be regarded while adjusting
collectOnEdgeToResize
protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ShapeElement](../shapes/ShapeElement.html)> collectOnEdgeToResize([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options)
Deprecated.
resizeOnEdgeShapes
protected void resizeOnEdgeShapes([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ShapeElement](../shapes/ShapeElement.html)> shapesToResize)
Deprecated.
canSetLocationForOnEdgeShape
protected boolean canSetLocationForOnEdgeShape([ShapeElement](../shapes/ShapeElement.html) shapeElement)
Deprecated.
collectOnEdgeElementsRecursively
protected void collectOnEdgeElementsRecursively([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ShapeElement](../shapes/ShapeElement.html)> collectTo,
 [ShapeElement](../shapes/ShapeElement.html) collectFrom)
Deprecated.
preProcessing
protected void preProcessing([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Overrides:
`[preProcessing](AbstractDiagramLayouter.html#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
afterLayout
protected void afterLayout([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](BaseGraph.html) graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Overrides:
`[afterLayout](AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
routeNonRoutedPaths
protected void routeNonRoutedPaths([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 @CheckForNull
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector> rerouteCollectors)
Deprecated.
fixOnFrameElements
protected void fixOnFrameElements([BaseGraph](BaseGraph.html) graph,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) o)
Deprecated.
Fixes, moves, sorts overlapping shapes on diagram frame.
Parameters:
`graph` - the graph that is layouted
`dpe` - diagram
`o` - options group
moveOutOfFrameHeader
protected void moveOutOfFrameHeader([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [HierarchicLayouterOptionsGroup](../../../core/options/HierarchicLayouterOptionsGroup.html) o)
Deprecated.
Moves elements of the diagram frame header view, so that they would not overlap
Parameters:
`diagram` - the diagram
createPathRerouteCollectors
protected void createPathRerouteCollectors()
Deprecated.
addPathRerouteCollector
protected void addPathRerouteCollector(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector collector)
Deprecated.
getPathRerouteCollectors
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector> getPathRerouteCollectors()
Deprecated.
dispose
protected void dispose([BaseGraph](BaseGraph.html) graph)
Deprecated.
Overrides:
`[dispose](AbstractDiagramLayouter.html#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
clone
public [AbstractHierarchicDiagramLayouter](AbstractHierarchicDiagramLayouter.html) clone()
Deprecated.
Overrides:
`[clone](AbstractDiagramLayouter.html#clone())` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
getTableShapeViewsInFirstLevel
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView> getTableShapeViewsInFirstLevel([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)
Deprecated.
containsSelectedFromTheSameParent
protected boolean containsSelectedFromTheSameParent([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)
Deprecated.
Activity layouter should also consider when nodes in TableShapeViews are selected and layouted.
Overrides:
`[containsSelectedFromTheSameParent](AbstractDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`dpe` - diagram
Returns:
true if selected in same cell(can also have elements that are owned by whole tableShape)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Class AbstractHierarchicDiagramLayouter">Class AbstractHierarchicDiagramLayouter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">HierarchicDiagramLayouter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractHierarchicDiagramLayouter</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="Layouting.html" title="class in com.nomagic.magicdraw.uml.symbols.layout"><code>Layouting</code></a> class for layouting a diagram</div>
</div>
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
<div class="col-first even-row-color"><code>protected com.dassault_systemes.modeler.magic.diagram.ylayout.candidates.AbstractCustomCandidates</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#can">can</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#pathRerouteCollectors">pathRerouteCollectors</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">AbstractHierarchicDiagramLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use no-arg constructor</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addPathRerouteCollector(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector)">addPathRerouteCollector</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector collector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">afterLayout</a><wbr/>(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#canSetLocationForOnEdgeShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">canSetLocationForOnEdgeShape</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#collectOnEdgeElementsRecursively(java.util.Collection,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">collectOnEdgeElementsRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt; collectTo,
 <a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> collectFrom)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#collectOnEdgeToResize(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">collectOnEdgeToResize</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">containsSelectedFromTheSameParent</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Activity layouter should also consider when nodes in TableShapeViews are selected and layouted.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.layout.ComponentLayouter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createComponentLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.grouping.RecursiveGroupLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">createComponentLayouter</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 y.layout.grouping.RecursiveGroupLayouter coreLayouter,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> opt)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates a component layouter if possible.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createPathRerouteCollectors()">createPathRerouteCollectors</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">dispose</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#fixOnFrameElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">fixOnFrameElements</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Fixes, moves, sorts overlapping shapes on diagram frame.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPathRerouteCollectors()">getPathRerouteCollectors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getTableShapeViewsInFirstLevel(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getTableShapeViewsInFirstLevel</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.layout.hierarchic.IncrementalHierarchicLayouter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#initDefaultHierarchicSettings(com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">initDefaultHierarchicSettings</a><wbr/>(<a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> opt,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Initializes hierarchic layouter settings: - Enables backlooping - Sets group compaction
 enabled - Aligns groups in center - Sets routing style to orthogonal - Adds group node insets
 - Enables label layout - Sets the node sequence within layer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>protected static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isLayoutAsGrid(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">isLayoutAsGrid</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if the graph should be layouted as grid</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a><wbr/>(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> opt,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#moveOutOfFrameHeader(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">moveOutOfFrameHeader</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Moves elements of the diagram frame header view, so that they would not overlap</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">preProcessing</a><wbr/>(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resizeOnEdgeElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">resizeOnEdgeElements</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Resizes elements on edge to the minimal size.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resizeOnEdgeShapes(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Collection)">resizeOnEdgeShapes</a><wbr/>(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt; shapesToResize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#routeNonRoutedPaths(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">routeNonRoutedPaths</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector&gt; rerouteCollectors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#runIHLLayoutSeries(y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">runIHLLayoutSeries</a><wbr/>(y.layout.hierarchic.IncrementalHierarchicLayouter ihl,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.layout.Layouter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#wrapToAccordingGroupLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,boolean)">wrapToAccordingGroupLayouter</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 y.layout.hierarchic.IncrementalHierarchicLayouter layouter,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> opt,
 boolean fromSketch)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">afterLayout</a>, <a href="AbstractDiagramLayouter.html#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">canLayout</a>, <a href="AbstractDiagramLayouter.html#clearOldRectangles(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">clearOldRectangles</a>, <a href="AbstractDiagramLayouter.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">createCommands</a>, <a href="AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">createGraph</a>, <a href="AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set)">createGraph</a>, <a href="AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Set,boolean)">createGraph</a>, <a href="AbstractDiagramLayouter.html#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">drawLayoutResults</a>, <a href="AbstractDiagramLayouter.html#getAnchoredPresentationElement()">getAnchoredPresentationElement</a>, <a href="AbstractDiagramLayouter.html#getDiagramLayouterAbortHandler()">getDiagramLayouterAbortHandler</a>, <a href="AbstractDiagramLayouter.html#getLayoutParameter(java.lang.String)">getLayoutParameter</a>, <a href="AbstractDiagramLayouter.html#getOptionsID()">getOptionsID</a>, <a href="AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getSelected</a>, <a href="AbstractDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)">isTypeSupported</a>, <a href="AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">layout</a>, <a href="AbstractDiagramLayouter.html#layoutGraph(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layoutGraph</a>, <a href="AbstractDiagramLayouter.html#placeLegendAndInfo(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">placeLegendAndInfo</a>, <a href="AbstractDiagramLayouter.html#postprocessing(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">postprocessing</a>, <a href="AbstractDiagramLayouter.html#resizeOuterBoundaryIfNecessary(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">resizeOuterBoundaryIfNecessary</a>, <a href="AbstractDiagramLayouter.html#setAnchoredPresentationElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean)">setAnchoredPresentationElement</a>, <a href="AbstractDiagramLayouter.html#setDefaultLayoutParameters()">setDefaultLayoutParameters</a>, <a href="AbstractDiagramLayouter.html#setLabelConsiderationMode(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">setLabelConsiderationMode</a>, <a href="AbstractDiagramLayouter.html#setLayoutParameter(java.lang.String,java.lang.Object)">setLayoutParameter</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="can">
<h3>can</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.magic.diagram.ylayout.candidates.AbstractCustomCandidates</span> <span class="element-name">can</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="pathRerouteCollectors">
<h3>pathRerouteCollectors</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector&gt;</span> <span class="element-name">pathRerouteCollectors</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>AbstractHierarchicDiagramLayouter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="element-name">AbstractHierarchicDiagramLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">use no-arg constructor</div>
</div>
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
<section class="detail" id="initDefaultHierarchicSettings(com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>initDefaultHierarchicSettings</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.layout.hierarchic.IncrementalHierarchicLayouter</span> <span class="element-name">initDefaultHierarchicSettings</span><wbr/><span class="parameters">(<a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> opt,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Initializes hierarchic layouter settings: - Enables backlooping - Sets group compaction
 enabled - Aligns groups in center - Sets routing style to orthogonal - Adds group node insets
 - Enables label layout - Sets the node sequence within layer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>opt</code> - options</dd>
<dd><code>graph</code> - current graph that should be layouted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runIHLLayoutSeries(y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">
<h3>runIHLLayoutSeries</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">runIHLLayoutSeries</span><wbr/><span class="parameters">(y.layout.hierarchic.IncrementalHierarchicLayouter ihl,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> options)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="wrapToAccordingGroupLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.hierarchic.IncrementalHierarchicLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup,boolean)">
<h3>wrapToAccordingGroupLayouter</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.layout.Layouter</span> <span class="element-name">wrapToAccordingGroupLayouter</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 y.layout.hierarchic.IncrementalHierarchicLayouter layouter,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> opt,
 boolean fromSketch)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="createComponentLayouter(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,y.layout.grouping.RecursiveGroupLayouter,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">
<h3>createComponentLayouter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">y.layout.ComponentLayouter</span> <span class="element-name">createComponentLayouter</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 y.layout.grouping.RecursiveGroupLayouter coreLayouter,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> opt)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates a component layouter if possible. Sub-graphs that can be identified as separate components will be processed and placed to a more convenient location.
 It may not be possible to create component layouter if sequencing, tableShape partitions etc. are used</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>graph</code> - layouted graph</dd>
<dd><code>coreLayouter</code> - the core layouter for component layouter</dd>
<dd><code>opt</code> - hierarchic options</dd>
<dt>Returns:</dt>
<dd>a component layouter if possible.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLayoutAsGrid(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>isLayoutAsGrid</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">boolean</span> <span class="element-name">isLayoutAsGrid</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if the graph should be layouted as grid</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>graph</code> - graph to check</dd>
<dt>Returns:</dt>
<dd>true if should layout the graph as grid, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> opt,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Layouts a diagram</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
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
<section class="detail" id="resizeOnEdgeElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">
<h3>resizeOnEdgeElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resizeOnEdgeElements</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Resizes elements on edge to the minimal size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>graph</code> - layouted graph</dd>
<dd><code>options</code> - options that may be regarded while adjusting</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectOnEdgeToResize(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">
<h3>collectOnEdgeToResize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt;</span> <span class="element-name">collectOnEdgeToResize</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="resizeOnEdgeShapes(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,java.util.Collection)">
<h3>resizeOnEdgeShapes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resizeOnEdgeShapes</span><wbr/><span class="parameters">(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt; shapesToResize)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="canSetLocationForOnEdgeShape(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>canSetLocationForOnEdgeShape</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">canSetLocationForOnEdgeShape</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shapeElement)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="collectOnEdgeElementsRecursively(java.util.Collection,com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>collectOnEdgeElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">collectOnEdgeElementsRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a>&gt; collectTo,
 <a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> collectFrom)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>preProcessing</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preProcessing</span><wbr/><span class="parameters">(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#preProcessing(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">preProcessing</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>afterLayout</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterLayout</span><wbr/><span class="parameters">(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#afterLayout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">afterLayout</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="routeNonRoutedPaths(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.dassault_systemes.modeler.foundation.editing.CompositeCommand,java.util.Collection)">
<h3>routeNonRoutedPaths</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">routeNonRoutedPaths</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 @CheckForNull
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector&gt; rerouteCollectors)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="fixOnFrameElements(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">
<h3>fixOnFrameElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">fixOnFrameElements</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> o)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Fixes, moves, sorts overlapping shapes on diagram frame.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>graph</code> - the graph that is layouted</dd>
<dd><code>dpe</code> - diagram</dd>
<dd><code>o</code> - options group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="moveOutOfFrameHeader(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.HierarchicLayouterOptionsGroup)">
<h3>moveOutOfFrameHeader</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">moveOutOfFrameHeader</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a> o)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Moves elements of the diagram frame header view, so that they would not overlap</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPathRerouteCollectors()">
<h3>createPathRerouteCollectors</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createPathRerouteCollectors</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="addPathRerouteCollector(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector)">
<h3>addPathRerouteCollector</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addPathRerouteCollector</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector collector)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getPathRerouteCollectors()">
<h3>getPathRerouteCollectors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.PathRerouteCollector&gt;</span> <span class="element-name">getPathRerouteCollectors</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">dispose</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#dispose(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">dispose</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></span> <span class="element-name">clone</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#clone()">clone</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTableShapeViewsInFirstLevel(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getTableShapeViewsInFirstLevel</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&gt;</span> <span class="element-name">getTableShapeViewsInFirstLevel</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>containsSelectedFromTheSameParent</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">containsSelectedFromTheSameParent</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Activity layouter should also consider when nodes in TableShapeViews are selected and layouted.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractDiagramLayouter.html#containsSelectedFromTheSameParent(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">containsSelectedFromTheSameParent</a></code> in class <code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>dpe</code> - diagram</dd>
<dt>Returns:</dt>
<dd>true if selected in same cell(can also have elements that are owned by whole tableShape)</dd>
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
