# JAVA OPENAPI: BaseGraph (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/BaseGraph.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/BaseGraph.html`
- source_sha256: `9a3c97c8d724fa3987906cf1b829a6820fab453e992407d2276806ee7f846203`
- captured_utc: `2026-07-14T16:55:58.914497+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Class BaseGraph

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
y.base.Graph
y.layout.LayoutGraph
y.layout.DefaultLayoutGraph
com.nomagic.magicdraw.uml.symbols.layout.BaseGraph

All Implemented Interfaces:
`y.base.GraphInterface`, `y.layout.GraphLayout`

Direct Known Subclasses:
`[UMLGraph](UMLGraph.html)`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public classBaseGraph
extends y.layout.DefaultLayoutGraph

Deprecated.

UML graph data.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[currentTableCellView](#currentTableCellView)`
Deprecated.
`protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[currentTableShapeView](#currentTableShapeView)`
Deprecated.
`protected final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PathElement](../paths/PathElement.html)>`
`[doNotRepaint](#doNotRepaint)`
Deprecated.
`static final int`
`[EDGE_LABEL_ALL](#EDGE_LABEL_ALL)`
Deprecated.
`static final int`
`[EDGE_LABEL_AT_ENDS](#EDGE_LABEL_AT_ENDS)`
Deprecated.
`static final int`
`[EDGE_LABEL_NON_ENDS](#EDGE_LABEL_NON_ENDS)`
Deprecated.
`static final int`
`[EDGE_LABEL_NONE](#EDGE_LABEL_NONE)`
Deprecated.
`protected final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<y.layout.EdgeLabelLayout>>`
`[edgeLabelDataMap](#edgeLabelDataMap)`
Deprecated.
`protected com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory`
`[edgeLabelFactory](#edgeLabelFactory)`
Deprecated.
`protected y.layout.grid.PartitionGrid`
`[grid](#grid)`
Deprecated.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[LAYOUTABLE_NODE_FEATURE_ID](#LAYOUTABLE_NODE_FEATURE_ID)`
Deprecated.
`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[mDataMap](#mDataMap)`
Deprecated.
PresentationElement (path or shape) bind to yFiles edge or node.
`protected [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html)`
`[mDiagramView](#mDiagramView)`
Deprecated.
`protected y.base.EdgeMap`
`[mEdgeMap](#mEdgeMap)`
Deprecated.
`protected final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),y.base.Edge>`
`[mFakeElementsMap](#mFakeElementsMap)`
Deprecated.
`protected y.base.NodeMap`
`[mGroupKey](#mGroupKey)`
Deprecated.
`protected y.base.NodeMap`
`[mNodeId](#mNodeId)`
Deprecated.
`protected y.base.NodeMap`
`[mNodeMap](#mNodeMap)`
Deprecated.
`protected final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[mNotSupported](#mNotSupported)`
Deprecated.
`protected [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[mPaths](#mPaths)`
Deprecated.
`protected [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[mSelected](#mSelected)`
Deprecated.
`protected com.dassault_systemes.modeler.magic.diagram.ylayout.labels.NodeLabelFactory`
`[nodeLabelFactory](#nodeLabelFactory)`
Deprecated.
`protected final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Node,com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure>`
`[nodeToTableShapeViewPlacement](#nodeToTableShapeViewPlacement)`
Deprecated.
`protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[partitionInfo](#partitionInfo)`
Deprecated.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SHRINKABLE_SHAPE_INSET_DP](#SHRINKABLE_SHAPE_INSET_DP)`
Deprecated.
`protected [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView>`
`[tableShapeViews](#tableShapeViews)`
Deprecated.
The table shape views that were visited and should be considered one way or another.
Fields inherited from class y.layout.DefaultLayoutGraph
`edgeLabelFeatureMap, edgeLabelMap, nodeLabelFeatureMap, nodeLabelMap`
Fields inherited from class y.layout.LayoutGraph
`z`
Fields inherited from class y.base.Graph
`AFTER, BEFORE`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Deprecated.
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`y.base.EdgeMap`
`[addEdgeSelectionProvider](#addEdgeSelectionProvider(java.lang.Object,java.util.Collection))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) provider,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<y.base.Edge> c)`
Deprecated.
Add Edge Selection Provider.
`y.base.EdgeMap`
`[addEdgeSelectionProvider](#addEdgeSelectionProvider(java.lang.Object,y.base.Edge))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) provider,
 y.base.Edge edge)`
Deprecated.
Add Edge Selection Provider.
`void`
`[addGroupNodeInsetsProvider](#addGroupNodeInsetsProvider())()`
Deprecated.
Add Group node inset provider.
`protected void`
`[addPaths](#addPaths(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) pe)`
Deprecated.
`protected void`
`[addToPathList](#addToPathList(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) path)`
Deprecated.
`protected void`
`[addToPathList](#addToPathList(java.lang.Iterable))([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<[PathElement](../paths/PathElement.html)> paths)`
Deprecated.
`void`
`[addToReversedList](#addToReversedList(y.base.Edge))(y.base.Edge edge)`
Deprecated.
`protected void`
`[adjustFakeAtEndShapeLabelOrientation](#adjustFakeAtEndShapeLabelOrientation(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) symbol)`
Deprecated.
`boolean`
`[areParentToChildConnected](#areParentToChildConnected(java.lang.Iterable))([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<[PathElement](../paths/PathElement.html)> connectedPathElements)`
Deprecated.
`boolean`
`[belongsToHierarchy](#belongsToHierarchy(y.base.Edge))(y.base.Edge edge)`
Deprecated.
Check The given Edge belongs to hierarchy.
`boolean`
`[belongsToHierarchy](#belongsToHierarchy(y.base.Node))(y.base.Node node)`
Deprecated.
Checks the given node belongs to Hierarchy.
`protected void`
`[collectPathsRecursively](#collectPathsRecursively(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node))([ShapeElement](../shapes/ShapeElement.html) element,
 y.base.Node node)`
Deprecated.
`boolean`
`[containsHierarchy](#containsHierarchy())()`
Deprecated.
Check If contains hierarchy.
`protected void`
`[createAllNodeLabels](#createAllNodeLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node))([ShapeElement](../shapes/ShapeElement.html) shape,
 y.base.Node node)`
Deprecated.
`protected void`
`[createAllPathLabels](#createAllPathLabels(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory,y.base.Edge,com.nomagic.magicdraw.uml.symbols.paths.PathElement))(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory factory,
 y.base.Edge edge,
 [PathElement](../paths/PathElement.html) pathElement)`
Deprecated.
`void`
`[createCommands](#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand))(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
Create command with given parameter.
`void`
`[createEdge](#createEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) path)`
Deprecated.
Creates an edge in a graph by provided path element.
`protected void`
`[createEdgesToNotLayoutableOnEdge](#createEdgesToNotLayoutableOnEdge(y.base.Node,java.util.Collection))(y.base.Node node,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> manipulatedElements)`
Deprecated.
`y.layout.grouping.GroupBoundsCalculator`
`[createGroupBoundsCalculator](#createGroupBoundsCalculator())()`
Deprecated.
Creates bounds calculator for group nodes
`void`
`[createHierarchicInfo](#createHierarchicInfo(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?>> classTypes)`
Deprecated.
Create Hierarchy Information of path element.
`protected y.base.Node`
`[createNode](#createNode(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../shapes/ShapeElement.html) shape)`
Deprecated.
`y.base.Node`
`[createNode](#createNode(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) id)`
Deprecated.
Create new Node and set the given id to it.
`protected void`
`[createNodeData](#createNodeData(java.lang.Object,com.nomagic.magicdraw.uml.symbols.PresentationElement))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentId,
 [PresentationElement](../PresentationElement.html) view)`
Deprecated.
`protected void`
`[createNodesData](#createNodesData(java.lang.Object,java.util.Collection))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentId,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> presentationElements)`
Deprecated.
`void`
`[dispose](#dispose())()`
Deprecated.
Dispose the graph and graph related data.
`protected boolean`
`[doesNotHaveConnectedLayoutableEdges](#doesNotHaveConnectedLayoutableEdges(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../shapes/ShapeElement.html) e)`
Deprecated.
`void`
`[drawResults](#drawResults())()`
Deprecated.
Draw a result.
`[PresentationElement](../PresentationElement.html)`
`[getAnchoredShape](#getAnchoredShape())()`
Deprecated.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundingBox](#getBoundingBox())()`
Deprecated.
`int`
`[getCreateEdgeLabels](#getCreateEdgeLabels())()`
Deprecated.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getDataMap](#getDataMap())()`
Deprecated.
`[AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html)`
`[getDiagram](#getDiagram())()`
Deprecated.
Get Presentation Diagram.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PathElement](../paths/PathElement.html)>`
`[getDoNotRepaintPaths](#getDoNotRepaintPaths())()`
Deprecated.
`y.base.Edge`
`[getEdge](#getEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement))([PathElement](../paths/PathElement.html) path)`
Deprecated.
Get Edge of given path element.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getEdgeLabelBoundingBox](#getEdgeLabelBoundingBox(y.base.Edge,y.layout.EdgeLabelLayout))(y.base.Edge e,
 y.layout.EdgeLabelLayout ell)`
Deprecated.
Get bounding box of the given edge label.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<y.layout.EdgeLabelLayout>>`
`[getEdgeLabelDataMap](#getEdgeLabelDataMap())()`
Deprecated.
`y.base.EdgeMap`
`[getEdgeMap](#getEdgeMap())()`
Deprecated.
`y.layout.NodeHalo`
`[getEnclosingShapeHalo](#getEnclosingShapeHalo(y.base.Node))(y.base.Node forNode)`
Deprecated.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),y.base.Edge>`
`[getFakeElementsMap](#getFakeElementsMap())()`
Deprecated.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getID](#getID(y.base.Node))(y.base.Node node)`
Deprecated.
Get The given node ID.
`y.base.NodeMap`
`[getInsetMap](#getInsetMap())()`
Deprecated.
`protected y.geom.YInsets`
`[getInsets](#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../shapes/ShapeElement.html) shape)`
Deprecated.
`protected y.geom.YInsets`
`[getInsets](#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Insets))([ShapeElement](../shapes/ShapeElement.html) shape,
 [Insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html) addAdditional)`
Deprecated.
`protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor>>`
`[getLabelByCondition](#getLabelByCondition(java.util.function.Predicate))([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<y.layout.EdgeLabelLayout> condition)`
Deprecated.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor>>`
`[getLabelDescriptorsNotAtEnd](#getLabelDescriptorsNotAtEnd())()`
Deprecated.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getLayouterParameters](#getLayouterParameters())()`
Deprecated.
`y.base.Node`
`[getNode](#getNode(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) se)`
Deprecated.
Get Node from the Presentation element recursively.
`y.base.Node`
`[getNodeDirectly](#getNodeDirectly(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) se)`
Deprecated.
`y.geom.YPoint`
`[getNodeHaloAdjustedSourcePointAbs](#getNodeHaloAdjustedSourcePointAbs(y.base.Edge))(y.base.Edge edge)`
Deprecated.
Get absolute location of edge source point on halo, not on the source node itself.
`y.geom.YPoint`
`[getNodeHaloAdjustedTargetPointAbs](#getNodeHaloAdjustedTargetPointAbs(y.base.Edge))(y.base.Edge edge)`
Deprecated.
Get absolute location of edge target point on halo, not on the target node itself.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Node,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<y.layout.NodeLabelLayout>>`
`[getNodeLabelDataMap](#getNodeLabelDataMap())()`
Deprecated.
`y.base.NodeMap`
`[getNodeMap](#getNodeMap())()`
Deprecated.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Node,com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure>`
`[getNodeToTableShapeAndCellStructure](#getNodeToTableShapeAndCellStructure())()`
Deprecated.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[getNonSupportedSymbols](#getNonSupportedSymbols())()`
Deprecated.
`[PresentationElement](../PresentationElement.html)`
`[getOuterBoundaryShape](#getOuterBoundaryShape())()`
Deprecated.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getParentId](#getParentId(y.base.Node))(y.base.Node node)`
Deprecated.
Get Node 's parent id.
`y.layout.grid.PartitionGrid`
`[getPartitionGrid](#getPartitionGrid())()`
Deprecated.
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getPartitionInfo](#getPartitionInfo())()`
Deprecated.
`[PathElement](../paths/PathElement.html)`
`[getPathElement](#getPathElement(y.base.Edge))(y.base.Edge edge)`
Deprecated.
Get Path Element of the given edge.
`int`
`[getPlaceEdgeLabelsPositions](#getPlaceEdgeLabelsPositions())()`
Deprecated.
`[ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>`
`[getPointsFromEdge](#getPointsFromEdge(y.base.Edge))(y.base.Edge edge)`
Deprecated.
Returns the points from an edge
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<y.base.Edge>`
`[getReversedList](#getReversedList())()`
Deprecated.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[getSelected](#getSelected())()`
Deprecated.
Get Set of the selected PresentationElement.
`[ShapeElement](../shapes/ShapeElement.html)`
`[getShapeElement](#getShapeElement(y.base.Node))(y.base.Node node)`
Deprecated.
Get The given node 's Shape Element.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)>`
`[getSpecialInnerManipulatedPresentationElements](#getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) view)`
Deprecated.
`[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)`
`[getSphereCenterPoint](#getSphereCenterPoint())()`
Deprecated.
`int`
`[getSphereRadius](#getSphereRadius())()`
Deprecated.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getStyle](#getStyle())()`
Deprecated.
Get String representation of Style.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView>`
`[getTableShapeViews](#getTableShapeViews())()`
Deprecated.
The tableShapeViews that are considered in this graph.
`protected void`
`[ignoreCenterlines](#ignoreCenterlines(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) shape)`
Deprecated.
Ignores centerlines on shape bound changes for centerlineable shape.
`void`
`[initializeData](#initializeData())()`
Deprecated.
`boolean`
`[isConsideredAsOuterBoundary](#isConsideredAsOuterBoundary(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) presentationElement)`
Deprecated.
`protected boolean`
`[isCreatableNode](#isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) view)`
Deprecated.
`boolean`
`[isGroupNode](#isGroupNode(y.base.Node))(y.base.Node node)`
Deprecated.
Checks if a given node is a group node or not.
`protected boolean`
`[isInSphereRadius](#isInSphereRadius(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../shapes/ShapeElement.html) element)`
Deprecated.
`static boolean`
`[isLayoutableByProviders](#isLayoutableByProviders(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) el)`
Deprecated.
Checks if symbol is layoutable by providers.
`boolean`
`[isLayoutAnchoredShapeOwnerAsLabel](#isLayoutAnchoredShapeOwnerAsLabel(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner))(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner view)`
Deprecated.
`protected boolean`
`[isNotLayoutedChild](#isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) view)`
Deprecated.
`static boolean`
`[isTreeOverlapping](#isTreeOverlapping(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape,int,java.lang.Iterable))(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape tree,
 int y,
 [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape> trees)`
Deprecated.
Check Is tree overlapping.
`void`
`[makeSubTree](#makeSubTree(y.base.Node,java.lang.Class,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))(y.base.Node node,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> classType,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
Make subtree.
`void`
`[makeSubTrees](#makeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand))(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
Make sub trees with the given Macrocommand.
`protected boolean`
`[needToCreate](#needToCreate(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) pe)`
Deprecated.
`protected void`
`[placeLayoutedPathLabel](#placeLayoutedPathLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement,y.base.Edge,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([PresentationElement](../PresentationElement.html) pe,
 y.base.Edge edge,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
`protected void`
`[placePath](#placePath(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.paths.PathElement,y.base.Edge))(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 [PathElement](../paths/PathElement.html) path,
 y.base.Edge edge)`
Deprecated.
`protected void`
`[placePaths](#placePaths(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,boolean,com.dassault_systemes.modeler.magic.diagram.command.MoveManager))(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 boolean bpaths,
 com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager)`
Deprecated.
`void`
`[removeGroupNodeInsetsProvider](#removeGroupNodeInsetsProvider())()`
Deprecated.
Remove The group node in sets of provider.
`static void`
`[removeSubTrees](#removeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set))(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selection)`
Deprecated.
Remove Sub Trees from the given presentation element.
`void`
`[resetLabel](#resetLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) pe)`
Deprecated.
Resets label to their default position.
`protected void`
`[resetUnhandledPath](#resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement))(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 [PresentationElement](../PresentationElement.html) prEl)`
Deprecated.
`void`
`[reverseAndAddToNoReverseList](#reverseAndAddToNoReverseList(y.base.Edge))(y.base.Edge edg)`
Deprecated.
Reverses an edge in graph, does not reverse if path is already reversed.
`void`
`[reverseEdge](#reverseEdge(y.base.Edge))(y.base.Edge edge)`
Deprecated.
Reverses an edge.
`void`
`[reverseEdgeAndLabels](#reverseEdgeAndLabels(y.base.Edge))(y.base.Edge edg)`
Deprecated.
Reverses the edge along with labels, but does not add them to no reverse list.
`void`
`[setAnchoredShape](#setAnchoredShape(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) anchoredShape)`
Deprecated.
`void`
`[setCreateEdgeLabels](#setCreateEdgeLabels(int))(int createEdgeLabels)`
Deprecated.
`void`
`[setCreateNodeLabels](#setCreateNodeLabels(boolean))(boolean shouldCreateNodeLabels)`
Deprecated.
`void`
`[setEdgeLabelFactory](#setEdgeLabelFactory(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory))(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory edgeLabelFactory)`
Deprecated.
`void`
`[setGroupNode](#setGroupNode(y.base.Node,boolean))(y.base.Node node,
 boolean isGroup)`
Deprecated.
`void`
`[setLayouterParameters](#setLayouterParameters(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> layouterParameters)`
Deprecated.
`void`
`[setMinimalGroupNodeSize](#setMinimalGroupNodeSize(y.base.Node,y.geom.YDimension))(y.base.Node node,
 y.geom.YDimension dim)`
Deprecated.
Sets the minimal group node size that is obeyed by layouter.
`protected void`
`[setNodeSizeEnsureNotZero](#setNodeSizeEnsureNotZero(java.awt.Rectangle,y.base.Node))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 y.base.Node node)`
Deprecated.
Sets graph node size, ensures the node height or width is not 0
`void`
`[setOuterBoundaryShape](#setOuterBoundaryShape(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) outerBoundaryShape)`
Deprecated.
`void`
`[setParent](#setParent(y.base.Node,java.lang.Object))(y.base.Node node,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentId)`
Deprecated.
Set node 's parent.
`void`
`[setPartitionGrid](#setPartitionGrid(y.layout.grid.PartitionGrid))(y.layout.grid.PartitionGrid partitionGrid)`
Deprecated.
`void`
`[setPartitionInfo](#setPartitionInfo(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) info)`
Deprecated.
`protected void`
`[setPathBreakPoints](#setPathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List,java.awt.Point,java.awt.Point,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([PathElement](../paths/PathElement.html) path,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> points,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) client,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplier,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated.
Set Path break point.
`void`
`[setPathStyle](#setPathStyle(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)`
Deprecated.
Set path style
`void`
`[setPlaceEdgeLabelsTo](#setPlaceEdgeLabelsTo(int))(int placeEdgeLabelsTo)`
Deprecated.
`void`
`[setPlaceNodeLabels](#setPlaceNodeLabels(boolean))(boolean shouldPlaceNodeLabelsToCalculatedPositions)`
Deprecated.
`final void`
`[setResetLabelsAtInit](#setResetLabelsAtInit(boolean))(boolean resetLabelsAtInit)`
Deprecated.
`void`
`[setSphereCenterPoint](#setSphereCenterPoint(java.awt.Point))([Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)`
Deprecated.
Sets the center of the sphere that is used for node creation
`void`
`[setSphereRadius](#setSphereRadius(int))(int radius)`
Deprecated.
Sets the sphere from the defined point.
`boolean`
`[shouldCreateNodeLabels](#shouldCreateNodeLabels())()`
Deprecated.
`boolean`
`[shouldPlaceNodeLabels](#shouldPlaceNodeLabels())()`
Deprecated.
`boolean`
`[shouldResetLabelsAtInit](#shouldResetLabelsAtInit())()`
Deprecated.
Methods inherited from class y.layout.DefaultLayoutGraph
`createEdgeLayout, createGraphCopyFactory, createLabelFactory, createNodeLayout, getFeature, getFeature, getLabelLayout, getLabelLayout, getLayout, getLayout, setLabelLayout, setLabelLayout, setLabelLayout, setLayout, setLayout`
Methods inherited from class y.layout.LayoutGraph
`getCenter, getCenterX, getCenterY, getEdgeLabelLayout, getEdgeLayout, getEdgeList, getHeight, getLocation, getNodeLabelLayout, getNodeLayout, getPath, getPathList, getPointList, getPoints, getRectangle, getSize, getSourcePointAbs, getSourcePointRel, getTargetPointAbs, getTargetPointRel, getWidth, getX, getY, moveBy, setCenter, setCenter, setEndPointsAbs, setLocation, setLocation, setPath, setPath, setPoints, setPoints, setSize, setSize, setSourcePointAbs, setSourcePointRel, setTargetPointAbs, setTargetPointRel`
Methods inherited from class y.base.Graph
`addDataProvider, addGraphListener, changeEdge, changeEdge, changeEdge, clear, contains, contains, containsEdge, createCopy, createEdge, createEdge, createEdgeMap, createGraph, createNode, createNodeMap, disposeEdgeMap, disposeNodeMap, E, edgeCount, edgeObjects, edges, fireGraphEvent, firePostEvent, firePostEvent, firePreEvent, firePreEvent, firstEdge, firstNode, firstOutEdge, getDataProvider, getDataProviderKeys, getEdgeArray, getGraphCopyFactory, getGraphListeners, getNodeArray, getRegisteredEdgeMaps, getRegisteredNodeMaps, getSource, getTarget, hasListeners, hide, hide, isEmpty, lastEdge, lastNode, moveSubGraph, moveToFirst, moveToFirst, moveToLast, moveToLast, N, nodeCount, nodeObjects, nodes, printNodeSlotSize, reInsertEdge, reInsertNode, removeDataProvider, removeEdge, removeGraphListener, removeNode, setGraphCopyFactory, sortEdges, sortEdges, sortNodes, toString, unhide, unhide`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
LAYOUTABLE_NODE_FEATURE_ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LAYOUTABLE_NODE_FEATURE_ID
Deprecated.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.LAYOUTABLE_NODE_FEATURE_ID)
SHRINKABLE_SHAPE_INSET_DP
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHRINKABLE_SHAPE_INSET_DP
Deprecated.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.SHRINKABLE_SHAPE_INSET_DP)
EDGE_LABEL_NONE
public static final int EDGE_LABEL_NONE
Deprecated.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_NONE)
EDGE_LABEL_AT_ENDS
public static final int EDGE_LABEL_AT_ENDS
Deprecated.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_AT_ENDS)
EDGE_LABEL_NON_ENDS
public static final int EDGE_LABEL_NON_ENDS
Deprecated.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_NON_ENDS)
EDGE_LABEL_ALL
public static final int EDGE_LABEL_ALL
Deprecated.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_ALL)
mFakeElementsMap
protected final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),y.base.Edge> mFakeElementsMap
Deprecated.
doNotRepaint
protected final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PathElement](../paths/PathElement.html)> doNotRepaint
Deprecated.
mNotSupported
protected final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> mNotSupported
Deprecated.
mDataMap
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> mDataMap
Deprecated.
PresentationElement (path or shape) bind to yFiles edge or node.
mNodeMap
protected y.base.NodeMap mNodeMap
Deprecated.
mEdgeMap
protected y.base.EdgeMap mEdgeMap
Deprecated.
mNodeId
protected y.base.NodeMap mNodeId
Deprecated.
mGroupKey
protected y.base.NodeMap mGroupKey
Deprecated.
mPaths
protected [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> mPaths
Deprecated.
mDiagramView
protected [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) mDiagramView
Deprecated.
mSelected
protected [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> mSelected
Deprecated.
edgeLabelDataMap
protected final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<y.layout.EdgeLabelLayout>> edgeLabelDataMap
Deprecated.
partitionInfo
protected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) partitionInfo
Deprecated.
nodeToTableShapeViewPlacement
protected final [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Node,com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure> nodeToTableShapeViewPlacement
Deprecated.
tableShapeViews
protected [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView> tableShapeViews
Deprecated.
The table shape views that were visited and should be considered one way or another.
currentTableShapeView
@CheckForNullprotected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) currentTableShapeView
Deprecated.
currentTableCellView
@CheckForNullprotected [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) currentTableCellView
Deprecated.
grid
protected y.layout.grid.PartitionGrid grid
Deprecated.
edgeLabelFactory
@CheckForNullprotected com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory edgeLabelFactory
Deprecated.
nodeLabelFactory
@CheckForNullprotected com.dassault_systemes.modeler.magic.diagram.ylayout.labels.NodeLabelFactory nodeLabelFactory
Deprecated.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Deprecated.
Construct a graph with given parameter
Parameters:
`diagramView` - diagram for which to construct graph.
`selected` - selected elements
BaseGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
BaseGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
Deprecated.
BaseGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
 ============ METHOD DETAIL ========== 
Method Details
initializeData
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public void initializeData()
Deprecated.
Collects all data provided by diagram to nodes and edges.
getInsets
protected y.geom.YInsets getInsets([ShapeElement](../shapes/ShapeElement.html) shape)
Deprecated.
getInsets
protected y.geom.YInsets getInsets([ShapeElement](../shapes/ShapeElement.html) shape,
 [Insets](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html) addAdditional)
Deprecated.
createNode
protected y.base.Node createNode([ShapeElement](../shapes/ShapeElement.html) shape)
Deprecated.
setNodeSizeEnsureNotZero
protected void setNodeSizeEnsureNotZero([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds,
 y.base.Node node)
Deprecated.
Sets graph node size, ensures the node height or width is not 0
Parameters:
`bounds` - the bounds to set
`node` - the node that should have the minimal size
createAllNodeLabels
protected void createAllNodeLabels([ShapeElement](../shapes/ShapeElement.html) shape,
 y.base.Node node)
Deprecated.
getBoundingBox
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundingBox()
Deprecated.
Specified by:
`getBoundingBox` in interface `y.layout.GraphLayout`
Overrides:
`getBoundingBox` in class `y.layout.LayoutGraph`
createNode
public y.base.Node createNode([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) id)
Deprecated.
Create new Node and set the given id to it.
Parameters:
`id` - The given id.
Returns:
Create node.
getID
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getID(y.base.Node node)
Deprecated.
Get The given node ID.
Parameters:
`node` - The given node.
Returns:
Object.
createEdge
public void createEdge([PathElement](../paths/PathElement.html) path)
Deprecated.
Creates an edge in a graph by provided path element.
Parameters:
`path` - the path that will correspond an edge
createAllPathLabels
protected void createAllPathLabels(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory factory,
 y.base.Edge edge,
 [PathElement](../paths/PathElement.html) pathElement)
Deprecated.
getPathElement
public [PathElement](../paths/PathElement.html) getPathElement(y.base.Edge edge)
Deprecated.
Get Path Element of the given edge.
Parameters:
`edge` - The given edge.
Returns:
PathElement.
getShapeElement
public [ShapeElement](../shapes/ShapeElement.html) getShapeElement(y.base.Node node)
Deprecated.
Get The given node 's Shape Element.
Parameters:
`node` - The given node.
Returns:
ShapeElement.
setParent
public void setParent(y.base.Node node,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentId)
Deprecated.
Set node 's parent.
Parameters:
`node` - The given node.
`parentId` - The parent 's id.
getParentId
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getParentId(y.base.Node node)
Deprecated.
Get Node 's parent id.
Parameters:
`node` - The given node.
Returns:
Object
getDiagram
public [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) getDiagram()
Deprecated.
Get Presentation Diagram.
Returns:
Presentation Diagram.
needToCreate
protected boolean needToCreate([PresentationElement](../PresentationElement.html) pe)
Deprecated.
createNodesData
protected void createNodesData(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentId,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> presentationElements)
Deprecated.
isLayoutAnchoredShapeOwnerAsLabel
public boolean isLayoutAnchoredShapeOwnerAsLabel(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner view)
Deprecated.
createNodeData
protected void createNodeData(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) parentId,
 [PresentationElement](../PresentationElement.html) view)
Deprecated.
createEdgesToNotLayoutableOnEdge
protected void createEdgesToNotLayoutableOnEdge(y.base.Node node,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> manipulatedElements)
Deprecated.
getSpecialInnerManipulatedPresentationElements
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> getSpecialInnerManipulatedPresentationElements([PresentationElement](../PresentationElement.html) view)
Deprecated.
isCreatableNode
protected boolean isCreatableNode([PresentationElement](../PresentationElement.html) view)
Deprecated.
adjustFakeAtEndShapeLabelOrientation
protected void adjustFakeAtEndShapeLabelOrientation([PresentationElement](../PresentationElement.html) symbol)
Deprecated.
addToPathList
protected void addToPathList([PathElement](../paths/PathElement.html) path)
Deprecated.
addToPathList
protected void addToPathList([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<[PathElement](../paths/PathElement.html)> paths)
Deprecated.
doesNotHaveConnectedLayoutableEdges
protected boolean doesNotHaveConnectedLayoutableEdges([ShapeElement](../shapes/ShapeElement.html) e)
Deprecated.
areParentToChildConnected
public boolean areParentToChildConnected([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<[PathElement](../paths/PathElement.html)> connectedPathElements)
Deprecated.
collectPathsRecursively
protected void collectPathsRecursively([ShapeElement](../shapes/ShapeElement.html) element,
 y.base.Node node)
Deprecated.
addPaths
protected void addPaths([PresentationElement](../PresentationElement.html) pe)
Deprecated.
getNode
@CheckForNullpublic y.base.Node getNode([PresentationElement](../PresentationElement.html) se)
Deprecated.
Get Node from the Presentation element recursively.
Parameters:
`se` - PresentationElement.
Returns:
a node for presentation element, or null if not found
getNodeDirectly
@CheckForNullpublic y.base.Node getNodeDirectly(@CheckForNull
 [PresentationElement](../PresentationElement.html) se)
Deprecated.
getEdge
public y.base.Edge getEdge([PathElement](../paths/PathElement.html) path)
Deprecated.
Get Edge of given path element.
Parameters:
`path` - The given path element.
Returns:
Edge.
isNotLayoutedChild
protected boolean isNotLayoutedChild([PresentationElement](../PresentationElement.html) view)
Deprecated.
isLayoutableByProviders
public static boolean isLayoutableByProviders([PresentationElement](../PresentationElement.html) el)
Deprecated.
Checks if symbol is layoutable by providers.
Parameters:
`el` - checked element
Returns:
true if all providers say that the symbol is layoutable, false if at least one says it is not layoutable
createCommands
public void createCommands(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Create command with given parameter.
Parameters:
`mc` - MacroCommand.
getEnclosingShapeHalo
@CheckForNullpublic y.layout.NodeHalo getEnclosingShapeHalo(@CheckForNull
 y.base.Node forNode)
Deprecated.
ignoreCenterlines
protected void ignoreCenterlines([PresentationElement](../PresentationElement.html) shape)
Deprecated.
Ignores centerlines on shape bound changes for centerlineable shape.
Parameters:
`shape` - the shape to ignore centerlines on shape bound changes
placePaths
protected void placePaths(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 boolean bpaths,
 com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager)
Deprecated.
placePath
protected void placePath(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 [PathElement](../paths/PathElement.html) path,
 y.base.Edge edge)
Deprecated.
resetUnhandledPath
protected void resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 [PresentationElement](../PresentationElement.html) prEl)
Deprecated.
getPointsFromEdge
public [ArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> getPointsFromEdge(y.base.Edge edge)
Deprecated.
Returns the points from an edge
Parameters:
`edge` - edge's point to return
Returns:
edge points excluding source and target
setPathBreakPoints
protected void setPathBreakPoints([PathElement](../paths/PathElement.html) path,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> points,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) client,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) supplier,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Set Path break point.
Parameters:
`path` - Path Element.
`points` - List of break point.
`client` - Client point.
`supplier` - Supplier point.
`mc` - Macro command.
placeLayoutedPathLabel
protected void placeLayoutedPathLabel([PresentationElement](../PresentationElement.html) pe,
 y.base.Edge edge,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
getLabelDescriptorsNotAtEnd
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor>> getLabelDescriptorsNotAtEnd()
Deprecated.
getLabelByCondition
protected [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor>> getLabelByCondition([Predicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html)<y.layout.EdgeLabelLayout> condition)
Deprecated.
resetLabel
public void resetLabel([PresentationElement](../PresentationElement.html) pe)
Deprecated.
Resets label to their default position. This is done when collecting labels while creating
 graph.
Parameters:
`pe` - the element that labels will be reset
shouldResetLabelsAtInit
public boolean shouldResetLabelsAtInit()
Deprecated.
Returns:
if label positions should be reset before creating the graph
setResetLabelsAtInit
public final void setResetLabelsAtInit(boolean resetLabelsAtInit)
Deprecated.
Parameters:
`resetLabelsAtInit` - true for label reset when creating the graph, false otherwise. Use true for layouting, false when graph is used as a
 reference for routing.
getEdgeLabelBoundingBox
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getEdgeLabelBoundingBox(y.base.Edge e,
 y.layout.EdgeLabelLayout ell)
Deprecated.
Get bounding box of the given edge label.
Parameters:
`e` - Edge
`ell` - Edge Label Layout.
Returns:
the bounding box rectangle
dispose
public void dispose()
Deprecated.
Dispose the graph and graph related data.
setMinimalGroupNodeSize
public void setMinimalGroupNodeSize(y.base.Node node,
 y.geom.YDimension dim)
Deprecated.
Sets the minimal group node size that is obeyed by layouter.
Parameters:
`node` - the node that should have the minimal size
`dim` - the size of node
isGroupNode
public boolean isGroupNode(y.base.Node node)
Deprecated.
Checks if a given node is a group node or not.
Parameters:
`node` - the node to check
Returns:
true if node is a group node, false otherwise.
setGroupNode
public void setGroupNode(y.base.Node node,
 boolean isGroup)
Deprecated.
getStyle
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStyle()
Deprecated.
Get String representation of Style.
Returns:
String.
setPathStyle
public void setPathStyle([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) style)
Deprecated.
Set path style
Parameters:
`style` - path style to set
makeSubTrees
public void makeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Make sub trees with the given Macrocommand.
Parameters:
`mc` - macro
makeSubTree
public void makeSubTree(y.base.Node node,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> classType,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated.
Make subtree.
Parameters:
`node` - The given node.
`classType` - The given class type.
`mc` - Macro Command.
isTreeOverlapping
public static boolean isTreeOverlapping(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape tree,
 int y,
 [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape> trees)
Deprecated.
Check Is tree overlapping.
Parameters:
`tree` - The given tree view.
`y` - y coordinate of the horizontal bar of the tree view.
`trees` - Collection of trees.
Returns:
boolean.
removeSubTrees
public static void removeSubTrees(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selection)
Deprecated.
Remove Sub Trees from the given presentation element.
Parameters:
`mc` - MacroCommand
`dpe` - DiagramPresentation.
`selection` - if not null or empty removes only trees that groups all selected paths or
 all path connectors.
belongsToHierarchy
public boolean belongsToHierarchy(y.base.Node node)
Deprecated.
Checks the given node belongs to Hierarchy.
Parameters:
`node` - The given node.
Returns:
true, if the node belongs to some hierarchy
belongsToHierarchy
public boolean belongsToHierarchy(y.base.Edge edge)
Deprecated.
Check The given Edge belongs to hierarchy.
Parameters:
`edge` - The given edge.
Returns:
boolean
containsHierarchy
public boolean containsHierarchy()
Deprecated.
Check If contains hierarchy.
Returns:
boolean
createHierarchicInfo
public void createHierarchicInfo(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?>> classTypes)
Deprecated.
Create Hierarchy Information of path element.
Parameters:
`classTypes` - List of class type.
drawResults
public void drawResults()
Deprecated.
Draw a result. You need to comment the graph.dispose() call in AbstractDiagramLayouter in order to see the results.
getSelected
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> getSelected()
Deprecated.
Get Set of the selected PresentationElement.
Returns:
Set of selected presentation elements
addEdgeSelectionProvider
public y.base.EdgeMap addEdgeSelectionProvider([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) provider,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<y.base.Edge> c)
Deprecated.
Add Edge Selection Provider.
Parameters:
`provider` - The given provider.
`c` - Collection of Edge.
Returns:
EdgeMap.
addEdgeSelectionProvider
public y.base.EdgeMap addEdgeSelectionProvider([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) provider,
 y.base.Edge edge)
Deprecated.
Add Edge Selection Provider.
Parameters:
`provider` - The given provider.
`edge` - single edge
Returns:
EdgeMap.
addGroupNodeInsetsProvider
public void addGroupNodeInsetsProvider()
Deprecated.
Add Group node inset provider.
removeGroupNodeInsetsProvider
public void removeGroupNodeInsetsProvider()
Deprecated.
Remove The group node in sets of provider.
createGroupBoundsCalculator
public y.layout.grouping.GroupBoundsCalculator createGroupBoundsCalculator()
Deprecated.
Creates bounds calculator for group nodes
Returns:
calculator
getNodeMap
public y.base.NodeMap getNodeMap()
Deprecated.
Returns:
a node map associated with a data provider
getEdgeMap
public y.base.EdgeMap getEdgeMap()
Deprecated.
Returns:
an edge map associated with a data provider
getDataMap
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getDataMap()
Deprecated.
Returns:
an edge map associated with a data provider
reverseAndAddToNoReverseList
public void reverseAndAddToNoReverseList(y.base.Edge edg)
Deprecated.
Reverses an edge in graph, does not reverse if path is already reversed. This method handles label sides also, but only if they are described by
 PreferredPlacementDescriptor.
 PreferredPlacementDescriptor.PLACE_AT_TARGET is changed to PreferredPlacementDescriptor.PLACE_AT_SOURCE
Parameters:
`edg` - the edge to reverse
reverseEdgeAndLabels
public void reverseEdgeAndLabels(y.base.Edge edg)
Deprecated.
Reverses the edge along with labels, but does not add them to no reverse list.
Parameters:
`edg` - edge to reverse
reverseEdge
public void reverseEdge(y.base.Edge edge)
Deprecated.
Reverses an edge. Note: does not reverse the labels if they are placed on edge ends. Check
 the [`reverseAndAddToNoReverseList`](#reverseAndAddToNoReverseList(y.base.Edge)) method.
Overrides:
`reverseEdge` in class `y.base.Graph`
Parameters:
`edge` - edge to reverse
addToReversedList
public void addToReversedList(y.base.Edge edge)
Deprecated.
Parameters:
`edge` - edge to add
getReversedList
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<y.base.Edge> getReversedList()
Deprecated.
Returns:
a set of reversed edges
setPlaceEdgeLabelsTo
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public void setPlaceEdgeLabelsTo(int placeEdgeLabelsTo)
Deprecated.
Sets the calculated label placement for labels. Labels can be created for consideration only, but not placed at the calculated location.
 One of EDGE_LABEL_NONE, EDGE_LABEL_AT_ENDS, EDGE_LABEL_NON_ENDS , EDGE_LABEL_ALL.
 EDGE_LABEL_ALL by default.
Parameters:
`placeEdgeLabelsTo` - the edge placement mode
getPlaceEdgeLabelsPositions
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public int getPlaceEdgeLabelsPositions()
Deprecated.
Returns:
the edge placement mode
setCreateEdgeLabels
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public void setCreateEdgeLabels(int createEdgeLabels)
Deprecated.
Sets the label creation mode. One of EDGE_LABEL_NONE, EDGE_LABEL_AT_ENDS, EDGE_LABEL_NON_ENDS , EDGE_LABEL_ALL.
 EDGE_LABEL_ALL by default.
Parameters:
`createEdgeLabels` - edge placement mode
getCreateEdgeLabels
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public int getCreateEdgeLabels()
Deprecated.
Returns:
the edge creation mode
setPlaceNodeLabels
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public void setPlaceNodeLabels(boolean shouldPlaceNodeLabelsToCalculatedPositions)
Deprecated.
Parameters:
`shouldPlaceNodeLabelsToCalculatedPositions` - determines if node labels should be placed at the calculated graph position
shouldPlaceNodeLabels
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public boolean shouldPlaceNodeLabels()
Deprecated.
Returns:
true if node labels should be set at the calculated position, false for the default position
setCreateNodeLabels
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public void setCreateNodeLabels(boolean shouldCreateNodeLabels)
Deprecated.
Parameters:
`shouldCreateNodeLabels` - determines if node labels should be created and considered by the graph
shouldCreateNodeLabels
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public boolean shouldCreateNodeLabels()
Deprecated.
Returns:
the node label creation mode
getPartitionGrid
public y.layout.grid.PartitionGrid getPartitionGrid()
Deprecated.
Returns:
instance of partition grid
setPartitionGrid
public void setPartitionGrid(y.layout.grid.PartitionGrid partitionGrid)
Deprecated.
Parameters:
`partitionGrid` - sets to use this partition grid as grid
getNodeToTableShapeAndCellStructure
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Node,com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure> getNodeToTableShapeAndCellStructure()
Deprecated.
Returns:
the node belonging to a tableShape structure
getPartitionInfo
public [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getPartitionInfo()
Deprecated.
Returns:
the constructed partition info.
setPartitionInfo
public void setPartitionInfo([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) info)
Deprecated.
Parameters:
`info` - the information of partitions
setSphereRadius
public void setSphereRadius(int radius)
Deprecated.
Sets the sphere from the defined point. All element within this sphere will be collected and
 initiated. Shapes outside the sphere will be ignored.
Parameters:
`radius` - the radius that shapes are collected
getSphereRadius
public int getSphereRadius()
Deprecated.
Returns:
the sphere size for data initialization
setSphereCenterPoint
public void setSphereCenterPoint(@CheckForNull
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) point)
Deprecated.
Sets the center of the sphere that is used for node creation
Parameters:
`point` - new point of center, default is 0,0
getSphereCenterPoint
@CheckForNullpublic [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) getSphereCenterPoint()
Deprecated.
Returns:
the center of the sphere for node creation
isInSphereRadius
protected boolean isInSphereRadius([ShapeElement](../shapes/ShapeElement.html) element)
Deprecated.
Returns:
true, if shape is in sphere radius, or sphere radius is the default, false otherwise.
getNodeHaloAdjustedSourcePointAbs
public y.geom.YPoint getNodeHaloAdjustedSourcePointAbs(y.base.Edge edge)
Deprecated.
Get absolute location of edge source point on halo, not on the source node itself. As symbols themselves are adjusted by the halos, this is necessary for on edge shape
 placement to calculate a correct position. Currently only UMLGraphKeys.ENCLOSING_SHAPE_HALO_DP_KEY is considered.
Parameters:
`edge` - edge
Returns:
the source point on halo, rather than node
getNodeHaloAdjustedTargetPointAbs
public y.geom.YPoint getNodeHaloAdjustedTargetPointAbs(y.base.Edge edge)
Deprecated.
Get absolute location of edge target point on halo, not on the target node itself. As symbols themselves are adjusted by the halos, this is necessary for on edge shape
 placement to calculate a correct position. Currently only UMLGraphKeys.ENCLOSING_SHAPE_HALO_DP_KEY is considered.
Parameters:
`edge` - edge
Returns:
the target point on halo, rather than node
setEdgeLabelFactory
public void setEdgeLabelFactory(@CheckForNull
 com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory edgeLabelFactory)
Deprecated.
getNonSupportedSymbols
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> getNonSupportedSymbols()
Deprecated.
Returns:
set of symbols(shapes or paths) that are not supported by the graph and will not be included into layout and/or will be treated not as a part
 of the graph
getDoNotRepaintPaths
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PathElement](../paths/PathElement.html)> getDoNotRepaintPaths()
Deprecated.
Returns:
set of collected paths that are included in the layout, but not repainted according to the graph result
getFakeElementsMap
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../PresentationElement.html),y.base.Edge> getFakeElementsMap()
Deprecated.
getInsetMap
public y.base.NodeMap getInsetMap()
Deprecated.
getEdgeLabelDataMap
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Edge,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<y.layout.EdgeLabelLayout>> getEdgeLabelDataMap()
Deprecated.
getNodeLabelDataMap
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<y.base.Node,[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<y.layout.NodeLabelLayout>> getNodeLabelDataMap()
Deprecated.
getAnchoredShape
@CheckForNullpublic [PresentationElement](../PresentationElement.html) getAnchoredShape()
Deprecated.
setAnchoredShape
public void setAnchoredShape(@CheckForNull
 [PresentationElement](../PresentationElement.html) anchoredShape)
Deprecated.
getLayouterParameters
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getLayouterParameters()
Deprecated.
setLayouterParameters
public void setLayouterParameters([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> layouterParameters)
Deprecated.
isConsideredAsOuterBoundary
public boolean isConsideredAsOuterBoundary([PresentationElement](../PresentationElement.html) presentationElement)
Deprecated.
getOuterBoundaryShape
@CheckForNullpublic [PresentationElement](../PresentationElement.html) getOuterBoundaryShape()
Deprecated.
setOuterBoundaryShape
public void setOuterBoundaryShape(@CheckForNull
 [PresentationElement](../PresentationElement.html) outerBoundaryShape)
Deprecated.
getTableShapeViews
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView> getTableShapeViews()
Deprecated.
The tableShapeViews that are considered in this graph.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Class BaseGraph">Class BaseGraph</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">y.base.Graph
<div class="inheritance">y.layout.LayoutGraph
<div class="inheritance">y.layout.DefaultLayoutGraph
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.BaseGraph</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>y.base.GraphInterface</code>, <code>y.layout.GraphLayout</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="UMLGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">UMLGraph</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BaseGraph</span>
<span class="extends-implements">extends y.layout.DefaultLayoutGraph</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">UML graph data.</div>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#currentTableCellView">currentTableCellView</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#currentTableShapeView">currentTableShapeView</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#doNotRepaint">doNotRepaint</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EDGE_LABEL_ALL">EDGE_LABEL_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EDGE_LABEL_AT_ENDS">EDGE_LABEL_AT_ENDS</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EDGE_LABEL_NON_ENDS">EDGE_LABEL_NON_ENDS</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EDGE_LABEL_NONE">EDGE_LABEL_NONE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;y.layout.EdgeLabelLayout&gt;&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#edgeLabelDataMap">edgeLabelDataMap</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#edgeLabelFactory">edgeLabelFactory</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected y.layout.grid.PartitionGrid</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#grid">grid</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LAYOUTABLE_NODE_FEATURE_ID">LAYOUTABLE_NODE_FEATURE_ID</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#mDataMap">mDataMap</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">PresentationElement (path or shape) bind to yFiles edge or node.</div>
</div>
<div class="col-first even-row-color"><code>protected <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mDiagramView">mDiagramView</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected y.base.EdgeMap</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#mEdgeMap">mEdgeMap</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/>y.base.Edge&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mFakeElementsMap">mFakeElementsMap</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected y.base.NodeMap</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#mGroupKey">mGroupKey</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected y.base.NodeMap</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mNodeId">mNodeId</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected y.base.NodeMap</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#mNodeMap">mNodeMap</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mNotSupported">mNotSupported</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#mPaths">mPaths</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#mSelected">mSelected</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected com.dassault_systemes.modeler.magic.diagram.ylayout.labels.NodeLabelFactory</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#nodeLabelFactory">nodeLabelFactory</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Node,<wbr/>com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#nodeToTableShapeViewPlacement">nodeToTableShapeViewPlacement</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#partitionInfo">partitionInfo</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SHRINKABLE_SHAPE_INSET_DP">SHRINKABLE_SHAPE_INSET_DP</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#tableShapeViews">tableShapeViews</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The table shape views that were visited and should be considered one way or another.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-y.layout.DefaultLayoutGraph">Fields inherited from class y.layout.DefaultLayoutGraph</h3>
<code>edgeLabelFeatureMap, edgeLabelMap, nodeLabelFeatureMap, nodeLabelMap</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-y.layout.LayoutGraph">Fields inherited from class y.layout.LayoutGraph</h3>
<code>z</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-y.base.Graph">Fields inherited from class y.base.Graph</h3>
<code>AFTER, BEFORE</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</code></div>
<div class="col-last odd-row-color">
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.EdgeMap</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addEdgeSelectionProvider(java.lang.Object,java.util.Collection)">addEdgeSelectionProvider</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> provider,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;y.base.Edge&gt; c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Add Edge Selection Provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.EdgeMap</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addEdgeSelectionProvider(java.lang.Object,y.base.Edge)">addEdgeSelectionProvider</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> provider,
 y.base.Edge edge)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Add Edge Selection Provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addGroupNodeInsetsProvider()">addGroupNodeInsetsProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Add Group node inset provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addPaths(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPaths</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addToPathList(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addToPathList</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addToPathList(java.lang.Iterable)">addToPathList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt; paths)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#addToReversedList(y.base.Edge)">addToReversedList</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#adjustFakeAtEndShapeLabelOrientation(com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustFakeAtEndShapeLabelOrientation</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#areParentToChildConnected(java.lang.Iterable)">areParentToChildConnected</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt; connectedPathElements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#belongsToHierarchy(y.base.Edge)">belongsToHierarchy</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check The given Edge belongs to hierarchy.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#belongsToHierarchy(y.base.Node)">belongsToHierarchy</a><wbr/>(y.base.Node node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks the given node belongs to Hierarchy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#collectPathsRecursively(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)">collectPathsRecursively</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> element,
 y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#containsHierarchy()">containsHierarchy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check If contains hierarchy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAllNodeLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)">createAllNodeLabels</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createAllPathLabels(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory,y.base.Edge,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">createAllPathLabels</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory factory,
 y.base.Edge edge,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">createCommands</a><wbr/>(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create command with given parameter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">createEdge</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates an edge in a graph by provided path element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createEdgesToNotLayoutableOnEdge(y.base.Node,java.util.Collection)">createEdgesToNotLayoutableOnEdge</a><wbr/>(y.base.Node node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; manipulatedElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.layout.grouping.GroupBoundsCalculator</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createGroupBoundsCalculator()">createGroupBoundsCalculator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates bounds calculator for group nodes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createHierarchicInfo(java.util.Collection)">createHierarchicInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;&gt; classTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create Hierarchy Information of path element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.base.Node</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createNode(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">createNode</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.Node</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createNode(java.lang.Object)">createNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create new Node and set the given id to it.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createNodeData(java.lang.Object,com.nomagic.magicdraw.uml.symbols.PresentationElement)">createNodeData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentId,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createNodesData(java.lang.Object,java.util.Collection)">createNodesData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; presentationElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Dispose the graph and graph related data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#doesNotHaveConnectedLayoutableEdges(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">doesNotHaveConnectedLayoutableEdges</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#drawResults()">drawResults</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Draw a result.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getAnchoredShape()">getAnchoredShape</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getCreateEdgeLabels()">getCreateEdgeLabels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDataMap()">getDataMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDiagram()">getDiagram</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Presentation Diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDoNotRepaintPaths()">getDoNotRepaintPaths</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.Edge</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getEdge</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Edge of given path element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEdgeLabelBoundingBox(y.base.Edge,y.layout.EdgeLabelLayout)">getEdgeLabelBoundingBox</a><wbr/>(y.base.Edge e,
 y.layout.EdgeLabelLayout ell)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get bounding box of the given edge label.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;y.layout.EdgeLabelLayout&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEdgeLabelDataMap()">getEdgeLabelDataMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.EdgeMap</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEdgeMap()">getEdgeMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.layout.NodeHalo</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getEnclosingShapeHalo(y.base.Node)">getEnclosingShapeHalo</a><wbr/>(y.base.Node forNode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/>y.base.Edge&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFakeElementsMap()">getFakeElementsMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getID(y.base.Node)">getID</a><wbr/>(y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get The given node ID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.NodeMap</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInsetMap()">getInsetMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.geom.YInsets</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">getInsets</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.geom.YInsets</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Insets)">getInsets</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html" title="class or interface in java.awt">Insets</a> addAdditional)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLabelByCondition(java.util.function.Predicate)">getLabelByCondition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;y.layout.EdgeLabelLayout&gt; condition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLabelDescriptorsNotAtEnd()">getLabelDescriptorsNotAtEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getLayouterParameters()">getLayouterParameters</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.Node</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getNode</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> se)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Node from the Presentation element recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.Node</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNodeDirectly(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getNodeDirectly</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> se)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.geom.YPoint</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNodeHaloAdjustedSourcePointAbs(y.base.Edge)">getNodeHaloAdjustedSourcePointAbs</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get absolute location of edge source point on halo, not on the source node itself.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.geom.YPoint</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNodeHaloAdjustedTargetPointAbs(y.base.Edge)">getNodeHaloAdjustedTargetPointAbs</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get absolute location of edge target point on halo, not on the target node itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Node,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;y.layout.NodeLabelLayout&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNodeLabelDataMap()">getNodeLabelDataMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.base.NodeMap</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNodeMap()">getNodeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Node,<wbr/>com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNodeToTableShapeAndCellStructure()">getNodeToTableShapeAndCellStructure</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNonSupportedSymbols()">getNonSupportedSymbols</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getOuterBoundaryShape()">getOuterBoundaryShape</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getParentId(y.base.Node)">getParentId</a><wbr/>(y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Node 's parent id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>y.layout.grid.PartitionGrid</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPartitionGrid()">getPartitionGrid</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPartitionInfo()">getPartitionInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPathElement(y.base.Edge)">getPathElement</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Path Element of the given edge.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPlaceEdgeLabelsPositions()">getPlaceEdgeLabelsPositions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getPointsFromEdge(y.base.Edge)">getPointsFromEdge</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns the points from an edge</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;y.base.Edge&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getReversedList()">getReversedList</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSelected()">getSelected</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Set of the selected PresentationElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getShapeElement(y.base.Node)">getShapeElement</a><wbr/>(y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get The given node 's Shape Element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSpecialInnerManipulatedPresentationElements</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSphereCenterPoint()">getSphereCenterPoint</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSphereRadius()">getSphereRadius</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getStyle()">getStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get String representation of Style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getTableShapeViews()">getTableShapeViews</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The tableShapeViews that are considered in this graph.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#ignoreCenterlines(com.nomagic.magicdraw.uml.symbols.PresentationElement)">ignoreCenterlines</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> shape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Ignores centerlines on shape bound changes for centerlineable shape.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#initializeData()">initializeData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isConsideredAsOuterBoundary(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isConsideredAsOuterBoundary</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isCreatableNode</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isGroupNode(y.base.Node)">isGroupNode</a><wbr/>(y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if a given node is a group node or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isInSphereRadius(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">isInSphereRadius</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isLayoutableByProviders(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isLayoutableByProviders</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> el)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if symbol is layoutable by providers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isLayoutAnchoredShapeOwnerAsLabel(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner)">isLayoutAnchoredShapeOwnerAsLabel</a><wbr/>(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isNotLayoutedChild</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isTreeOverlapping(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape,int,java.lang.Iterable)">isTreeOverlapping</a><wbr/>(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape tree,
 int y,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape&gt; trees)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check Is tree overlapping.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#makeSubTree(y.base.Node,java.lang.Class,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">makeSubTree</a><wbr/>(y.base.Node node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; classType,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Make subtree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#makeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">makeSubTrees</a><wbr/>(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Make sub trees with the given Macrocommand.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#needToCreate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">needToCreate</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#placeLayoutedPathLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement,y.base.Edge,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">placeLayoutedPathLabel</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe,
 y.base.Edge edge,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#placePath(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.paths.PathElement,y.base.Edge)">placePath</a><wbr/>(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 y.base.Edge edge)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#placePaths(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,boolean,com.dassault_systemes.modeler.magic.diagram.command.MoveManager)">placePaths</a><wbr/>(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 boolean bpaths,
 com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#removeGroupNodeInsetsProvider()">removeGroupNodeInsetsProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Remove The group node in sets of provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#removeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">removeSubTrees</a><wbr/>(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Remove Sub Trees from the given presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resetLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement)">resetLabel</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Resets label to their default position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">resetUnhandledPath</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> prEl)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#reverseAndAddToNoReverseList(y.base.Edge)">reverseAndAddToNoReverseList</a><wbr/>(y.base.Edge edg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Reverses an edge in graph, does not reverse if path is already reversed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#reverseEdge(y.base.Edge)">reverseEdge</a><wbr/>(y.base.Edge edge)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Reverses an edge.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#reverseEdgeAndLabels(y.base.Edge)">reverseEdgeAndLabels</a><wbr/>(y.base.Edge edg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Reverses the edge along with labels, but does not add them to no reverse list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setAnchoredShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setAnchoredShape</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> anchoredShape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setCreateEdgeLabels(int)">setCreateEdgeLabels</a><wbr/>(int createEdgeLabels)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setCreateNodeLabels(boolean)">setCreateNodeLabels</a><wbr/>(boolean shouldCreateNodeLabels)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setEdgeLabelFactory(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory)">setEdgeLabelFactory</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory edgeLabelFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setGroupNode(y.base.Node,boolean)">setGroupNode</a><wbr/>(y.base.Node node,
 boolean isGroup)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setLayouterParameters(java.util.Map)">setLayouterParameters</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; layouterParameters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setMinimalGroupNodeSize(y.base.Node,y.geom.YDimension)">setMinimalGroupNodeSize</a><wbr/>(y.base.Node node,
 y.geom.YDimension dim)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the minimal group node size that is obeyed by layouter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setNodeSizeEnsureNotZero(java.awt.Rectangle,y.base.Node)">setNodeSizeEnsureNotZero</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 y.base.Node node)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets graph node size, ensures the node height or width is not 0</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setOuterBoundaryShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setOuterBoundaryShape</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> outerBoundaryShape)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setParent(y.base.Node,java.lang.Object)">setParent</a><wbr/>(y.base.Node node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set node 's parent.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPartitionGrid(y.layout.grid.PartitionGrid)">setPartitionGrid</a><wbr/>(y.layout.grid.PartitionGrid partitionGrid)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPartitionInfo(java.lang.Object)">setPartitionInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> info)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List,java.awt.Point,java.awt.Point,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">setPathBreakPoints</a><wbr/>(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; points,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> client,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplier,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set Path break point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPathStyle(java.lang.String)">setPathStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set path style</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPlaceEdgeLabelsTo(int)">setPlaceEdgeLabelsTo</a><wbr/>(int placeEdgeLabelsTo)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setPlaceNodeLabels(boolean)">setPlaceNodeLabels</a><wbr/>(boolean shouldPlaceNodeLabelsToCalculatedPositions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setResetLabelsAtInit(boolean)">setResetLabelsAtInit</a><wbr/>(boolean resetLabelsAtInit)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setSphereCenterPoint(java.awt.Point)">setSphereCenterPoint</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the center of the sphere that is used for node creation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setSphereRadius(int)">setSphereRadius</a><wbr/>(int radius)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the sphere from the defined point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#shouldCreateNodeLabels()">shouldCreateNodeLabels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#shouldPlaceNodeLabels()">shouldPlaceNodeLabels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#shouldResetLabelsAtInit()">shouldResetLabelsAtInit</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-y.layout.DefaultLayoutGraph">Methods inherited from class y.layout.DefaultLayoutGraph</h3>
<code>createEdgeLayout, createGraphCopyFactory, createLabelFactory, createNodeLayout, getFeature, getFeature, getLabelLayout, getLabelLayout, getLayout, getLayout, setLabelLayout, setLabelLayout, setLabelLayout, setLayout, setLayout</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-y.layout.LayoutGraph">Methods inherited from class y.layout.LayoutGraph</h3>
<code>getCenter, getCenterX, getCenterY, getEdgeLabelLayout, getEdgeLayout, getEdgeList, getHeight, getLocation, getNodeLabelLayout, getNodeLayout, getPath, getPathList, getPointList, getPoints, getRectangle, getSize, getSourcePointAbs, getSourcePointRel, getTargetPointAbs, getTargetPointRel, getWidth, getX, getY, moveBy, setCenter, setCenter, setEndPointsAbs, setLocation, setLocation, setPath, setPath, setPoints, setPoints, setSize, setSize, setSourcePointAbs, setSourcePointRel, setTargetPointAbs, setTargetPointRel</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-y.base.Graph">Methods inherited from class y.base.Graph</h3>
<code>addDataProvider, addGraphListener, changeEdge, changeEdge, changeEdge, clear, contains, contains, containsEdge, createCopy, createEdge, createEdge, createEdgeMap, createGraph, createNode, createNodeMap, disposeEdgeMap, disposeNodeMap, E, edgeCount, edgeObjects, edges, fireGraphEvent, firePostEvent, firePostEvent, firePreEvent, firePreEvent, firstEdge, firstNode, firstOutEdge, getDataProvider, getDataProviderKeys, getEdgeArray, getGraphCopyFactory, getGraphListeners, getNodeArray, getRegisteredEdgeMaps, getRegisteredNodeMaps, getSource, getTarget, hasListeners, hide, hide, isEmpty, lastEdge, lastNode, moveSubGraph, moveToFirst, moveToFirst, moveToLast, moveToLast, N, nodeCount, nodeObjects, nodes, printNodeSlotSize, reInsertEdge, reInsertNode, removeDataProvider, removeEdge, removeGraphListener, removeNode, setGraphCopyFactory, sortEdges, sortEdges, sortNodes, toString, unhide, unhide</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="LAYOUTABLE_NODE_FEATURE_ID">
<h3>LAYOUTABLE_NODE_FEATURE_ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LAYOUTABLE_NODE_FEATURE_ID</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.LAYOUTABLE_NODE_FEATURE_ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHRINKABLE_SHAPE_INSET_DP">
<h3>SHRINKABLE_SHAPE_INSET_DP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHRINKABLE_SHAPE_INSET_DP</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.SHRINKABLE_SHAPE_INSET_DP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDGE_LABEL_NONE">
<h3>EDGE_LABEL_NONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EDGE_LABEL_NONE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_NONE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDGE_LABEL_AT_ENDS">
<h3>EDGE_LABEL_AT_ENDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EDGE_LABEL_AT_ENDS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_AT_ENDS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDGE_LABEL_NON_ENDS">
<h3>EDGE_LABEL_NON_ENDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EDGE_LABEL_NON_ENDS</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_NON_ENDS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EDGE_LABEL_ALL">
<h3>EDGE_LABEL_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">EDGE_LABEL_ALL</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.BaseGraph.EDGE_LABEL_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mFakeElementsMap">
<h3>mFakeElementsMap</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/>y.base.Edge&gt;</span> <span class="element-name">mFakeElementsMap</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="doNotRepaint">
<h3>doNotRepaint</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">doNotRepaint</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mNotSupported">
<h3>mNotSupported</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">mNotSupported</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mDataMap">
<h3>mDataMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">mDataMap</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">PresentationElement (path or shape) bind to yFiles edge or node.</div>
</section>
</li>
<li>
<section class="detail" id="mNodeMap">
<h3>mNodeMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.base.NodeMap</span> <span class="element-name">mNodeMap</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mEdgeMap">
<h3>mEdgeMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.base.EdgeMap</span> <span class="element-name">mEdgeMap</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mNodeId">
<h3>mNodeId</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.base.NodeMap</span> <span class="element-name">mNodeId</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mGroupKey">
<h3>mGroupKey</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.base.NodeMap</span> <span class="element-name">mGroupKey</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mPaths">
<h3>mPaths</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">mPaths</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mDiagramView">
<h3>mDiagramView</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">mDiagramView</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="mSelected">
<h3>mSelected</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">mSelected</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="edgeLabelDataMap">
<h3>edgeLabelDataMap</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;y.layout.EdgeLabelLayout&gt;&gt;</span> <span class="element-name">edgeLabelDataMap</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="partitionInfo">
<h3>partitionInfo</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">partitionInfo</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="nodeToTableShapeViewPlacement">
<h3>nodeToTableShapeViewPlacement</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Node,<wbr/>com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure&gt;</span> <span class="element-name">nodeToTableShapeViewPlacement</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="tableShapeViews">
<h3>tableShapeViews</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&gt;</span> <span class="element-name">tableShapeViews</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The table shape views that were visited and should be considered one way or another.</div>
</section>
</li>
<li>
<section class="detail" id="currentTableShapeView">
<h3>currentTableShapeView</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">currentTableShapeView</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="currentTableCellView">
<h3>currentTableCellView</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">currentTableCellView</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="grid">
<h3>grid</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.layout.grid.PartitionGrid</span> <span class="element-name">grid</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="edgeLabelFactory">
<h3>edgeLabelFactory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory</span> <span class="element-name">edgeLabelFactory</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="nodeLabelFactory">
<h3>nodeLabelFactory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.magic.diagram.ylayout.labels.NodeLabelFactory</span> <span class="element-name">nodeLabelFactory</span></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct a graph with given parameter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramView</code> - diagram for which to construct graph.</dd>
<dd><code>selected</code> - selected elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
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
<section class="detail" id="initializeData()">
<h3>initializeData</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initializeData</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Collects all data provided by diagram to nodes and edges.</div>
</section>
</li>
<li>
<section class="detail" id="getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>getInsets</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.geom.YInsets</span> <span class="element-name">getInsets</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Insets)">
<h3>getInsets</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.geom.YInsets</span> <span class="element-name">getInsets</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Insets.html" title="class or interface in java.awt">Insets</a> addAdditional)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="createNode(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>createNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.base.Node</span> <span class="element-name">createNode</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="setNodeSizeEnsureNotZero(java.awt.Rectangle,y.base.Node)">
<h3>setNodeSizeEnsureNotZero</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setNodeSizeEnsureNotZero</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds,
 y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets graph node size, ensures the node height or width is not 0</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bounds</code> - the bounds to set</dd>
<dd><code>node</code> - the node that should have the minimal size</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAllNodeLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)">
<h3>createAllNodeLabels</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createAllNodeLabels</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape,
 y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBoundingBox</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getBoundingBox</code> in interface <code>y.layout.GraphLayout</code></dd>
<dt>Overrides:</dt>
<dd><code>getBoundingBox</code> in class <code>y.layout.LayoutGraph</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNode(java.lang.Object)">
<h3>createNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.Node</span> <span class="element-name">createNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> id)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create new Node and set the given id to it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - The given id.</dd>
<dt>Returns:</dt>
<dd>Create node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID(y.base.Node)">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getID</span><wbr/><span class="parameters">(y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get The given node ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - The given node.</dd>
<dt>Returns:</dt>
<dd>Object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>createEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createEdge</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates an edge in a graph by provided path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - the path that will correspond an edge</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAllPathLabels(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory,y.base.Edge,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>createAllPathLabels</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createAllPathLabels</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory factory,
 y.base.Edge edge,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> pathElement)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getPathElement(y.base.Edge)">
<h3>getPathElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a></span> <span class="element-name">getPathElement</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Path Element of the given edge.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - The given edge.</dd>
<dt>Returns:</dt>
<dd>PathElement.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShapeElement(y.base.Node)">
<h3>getShapeElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a></span> <span class="element-name">getShapeElement</span><wbr/><span class="parameters">(y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get The given node 's Shape Element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - The given node.</dd>
<dt>Returns:</dt>
<dd>ShapeElement.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParent(y.base.Node,java.lang.Object)">
<h3>setParent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParent</span><wbr/><span class="parameters">(y.base.Node node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentId)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set node 's parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - The given node.</dd>
<dd><code>parentId</code> - The parent 's id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentId(y.base.Node)">
<h3>getParentId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getParentId</span><wbr/><span class="parameters">(y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Node 's parent id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - The given node.</dd>
<dt>Returns:</dt>
<dd>Object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagram()">
<h3>getDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a></span> <span class="element-name">getDiagram</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Presentation Diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Presentation Diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="needToCreate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>needToCreate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">needToCreate</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="createNodesData(java.lang.Object,java.util.Collection)">
<h3>createNodesData</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createNodesData</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; presentationElements)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="isLayoutAnchoredShapeOwnerAsLabel(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner)">
<h3>isLayoutAnchoredShapeOwnerAsLabel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLayoutAnchoredShapeOwnerAsLabel</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="createNodeData(java.lang.Object,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>createNodeData</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createNodeData</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> parentId,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="createEdgesToNotLayoutableOnEdge(y.base.Node,java.util.Collection)">
<h3>createEdgesToNotLayoutableOnEdge</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createEdgesToNotLayoutableOnEdge</span><wbr/><span class="parameters">(y.base.Node node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; manipulatedElements)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getSpecialInnerManipulatedPresentationElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSpecialInnerManipulatedPresentationElements</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isCreatableNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isCreatableNode</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="adjustFakeAtEndShapeLabelOrientation(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>adjustFakeAtEndShapeLabelOrientation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">adjustFakeAtEndShapeLabelOrientation</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="addToPathList(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>addToPathList</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addToPathList</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="addToPathList(java.lang.Iterable)">
<h3>addToPathList</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addToPathList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt; paths)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="doesNotHaveConnectedLayoutableEdges(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>doesNotHaveConnectedLayoutableEdges</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">doesNotHaveConnectedLayoutableEdges</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> e)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="areParentToChildConnected(java.lang.Iterable)">
<h3>areParentToChildConnected</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">areParentToChildConnected</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt; connectedPathElements)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="collectPathsRecursively(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)">
<h3>collectPathsRecursively</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">collectPathsRecursively</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> element,
 y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="addPaths(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>addPaths</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addPaths</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getNode</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">y.base.Node</span> <span class="element-name">getNode</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> se)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Node from the Presentation element recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>se</code> - PresentationElement.</dd>
<dt>Returns:</dt>
<dd>a node for presentation element, or null if not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeDirectly(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getNodeDirectly</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">y.base.Node</span> <span class="element-name">getNodeDirectly</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> se)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">
<h3>getEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.Edge</span> <span class="element-name">getEdge</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Edge of given path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - The given path element.</dd>
<dt>Returns:</dt>
<dd>Edge.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isNotLayoutedChild</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNotLayoutedChild</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="isLayoutableByProviders(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isLayoutableByProviders</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isLayoutableByProviders</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> el)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if symbol is layoutable by providers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>el</code> - checked element</dd>
<dt>Returns:</dt>
<dd>true if all providers say that the symbol is layoutable, false if at least one says it is not layoutable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>createCommands</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createCommands</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create command with given parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mc</code> - MacroCommand.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnclosingShapeHalo(y.base.Node)">
<h3>getEnclosingShapeHalo</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">y.layout.NodeHalo</span> <span class="element-name">getEnclosingShapeHalo</span><wbr/><span class="parameters">(@CheckForNull
 y.base.Node forNode)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="ignoreCenterlines(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>ignoreCenterlines</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">ignoreCenterlines</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> shape)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Ignores centerlines on shape bound changes for centerlineable shape.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shape</code> - the shape to ignore centerlines on shape bound changes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="placePaths(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,boolean,com.dassault_systemes.modeler.magic.diagram.command.MoveManager)">
<h3>placePaths</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">placePaths</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 boolean bpaths,
 com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="placePath(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.paths.PathElement,y.base.Edge)">
<h3>placePath</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">placePath</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 <a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>resetUnhandledPath</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resetUnhandledPath</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> prEl)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getPointsFromEdge(y.base.Edge)">
<h3>getPointsFromEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html" title="class or interface in java.util">ArrayList</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">getPointsFromEdge</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Returns the points from an edge</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - edge's point to return</dd>
<dt>Returns:</dt>
<dd>edge points excluding source and target</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List,java.awt.Point,java.awt.Point,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>setPathBreakPoints</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setPathBreakPoints</span><wbr/><span class="parameters">(<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; points,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> client,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> supplier,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set Path break point.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - Path Element.</dd>
<dd><code>points</code> - List of break point.</dd>
<dd><code>client</code> - Client point.</dd>
<dd><code>supplier</code> - Supplier point.</dd>
<dd><code>mc</code> - Macro command.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="placeLayoutedPathLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement,y.base.Edge,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>placeLayoutedPathLabel</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">placeLayoutedPathLabel</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe,
 y.base.Edge edge,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getLabelDescriptorsNotAtEnd()">
<h3>getLabelDescriptorsNotAtEnd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor&gt;&gt;</span> <span class="element-name">getLabelDescriptorsNotAtEnd</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getLabelByCondition(java.util.function.Predicate)">
<h3>getLabelByCondition</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.dassault_systemes.modeler.magic.diagram.ylayout.labels.AbstractCompositeEdgeLabelDescriptor&gt;&gt;</span> <span class="element-name">getLabelByCondition</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;y.layout.EdgeLabelLayout&gt; condition)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="resetLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>resetLabel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resetLabel</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Resets label to their default position. This is done when collecting labels while creating
 graph.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pe</code> - the element that labels will be reset</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shouldResetLabelsAtInit()">
<h3>shouldResetLabelsAtInit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">shouldResetLabelsAtInit</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>if label positions should be reset before creating the graph</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResetLabelsAtInit(boolean)">
<h3>setResetLabelsAtInit</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">setResetLabelsAtInit</span><wbr/><span class="parameters">(boolean resetLabelsAtInit)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resetLabelsAtInit</code> - true for label reset when creating the graph, false otherwise. Use true for layouting, false when graph is used as a
                          reference for routing.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEdgeLabelBoundingBox(y.base.Edge,y.layout.EdgeLabelLayout)">
<h3>getEdgeLabelBoundingBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getEdgeLabelBoundingBox</span><wbr/><span class="parameters">(y.base.Edge e,
 y.layout.EdgeLabelLayout ell)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get bounding box of the given edge label.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - Edge</dd>
<dd><code>ell</code> - Edge Label Layout.</dd>
<dt>Returns:</dt>
<dd>the bounding box rectangle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Dispose the graph and graph related data.</div>
</section>
</li>
<li>
<section class="detail" id="setMinimalGroupNodeSize(y.base.Node,y.geom.YDimension)">
<h3>setMinimalGroupNodeSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMinimalGroupNodeSize</span><wbr/><span class="parameters">(y.base.Node node,
 y.geom.YDimension dim)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the minimal group node size that is obeyed by layouter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - the node that should have the minimal size</dd>
<dd><code>dim</code> - the size of node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isGroupNode(y.base.Node)">
<h3>isGroupNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isGroupNode</span><wbr/><span class="parameters">(y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks if a given node is a group node or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - the node to check</dd>
<dt>Returns:</dt>
<dd>true if node is a group node, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGroupNode(y.base.Node,boolean)">
<h3>setGroupNode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGroupNode</span><wbr/><span class="parameters">(y.base.Node node,
 boolean isGroup)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getStyle()">
<h3>getStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStyle</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get String representation of Style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPathStyle(java.lang.String)">
<h3>setPathStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPathStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> style)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Set path style</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - path style to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>makeSubTrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeSubTrees</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Make sub trees with the given Macrocommand.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mc</code> - macro</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeSubTree(y.base.Node,java.lang.Class,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>makeSubTree</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeSubTree</span><wbr/><span class="parameters">(y.base.Node node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; classType,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Make subtree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - The given node.</dd>
<dd><code>classType</code> - The given class type.</dd>
<dd><code>mc</code> - Macro Command.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTreeOverlapping(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape,int,java.lang.Iterable)">
<h3>isTreeOverlapping</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isTreeOverlapping</span><wbr/><span class="parameters">(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape tree,
 int y,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape&gt; trees)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check Is tree overlapping.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - The given tree view.</dd>
<dd><code>y</code> - y coordinate of the horizontal bar of the tree view.</dd>
<dd><code>trees</code> - Collection of trees.</dd>
<dt>Returns:</dt>
<dd>boolean.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">
<h3>removeSubTrees</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeSubTrees</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selection)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Remove Sub Trees from the given presentation element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mc</code> - MacroCommand</dd>
<dd><code>dpe</code> - DiagramPresentation.</dd>
<dd><code>selection</code> - if not null or empty removes only trees that groups all selected paths or
                  all path connectors.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="belongsToHierarchy(y.base.Node)">
<h3>belongsToHierarchy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">belongsToHierarchy</span><wbr/><span class="parameters">(y.base.Node node)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks the given node belongs to Hierarchy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - The given node.</dd>
<dt>Returns:</dt>
<dd>true, if the node belongs to some hierarchy</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="belongsToHierarchy(y.base.Edge)">
<h3>belongsToHierarchy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">belongsToHierarchy</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check The given Edge belongs to hierarchy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - The given edge.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsHierarchy()">
<h3>containsHierarchy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">containsHierarchy</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Check If contains hierarchy.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createHierarchicInfo(java.util.Collection)">
<h3>createHierarchicInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createHierarchicInfo</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;&gt; classTypes)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Create Hierarchy Information of path element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classTypes</code> - List of class type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawResults()">
<h3>drawResults</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">drawResults</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Draw a result. You need to comment the graph.dispose() call in AbstractDiagramLayouter in order to see the results.</div>
</section>
</li>
<li>
<section class="detail" id="getSelected()">
<h3>getSelected</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSelected</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get Set of the selected PresentationElement.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Set of selected presentation elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addEdgeSelectionProvider(java.lang.Object,java.util.Collection)">
<h3>addEdgeSelectionProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.EdgeMap</span> <span class="element-name">addEdgeSelectionProvider</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> provider,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;y.base.Edge&gt; c)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Add Edge Selection Provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The given provider.</dd>
<dd><code>c</code> - Collection of Edge.</dd>
<dt>Returns:</dt>
<dd>EdgeMap.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addEdgeSelectionProvider(java.lang.Object,y.base.Edge)">
<h3>addEdgeSelectionProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.EdgeMap</span> <span class="element-name">addEdgeSelectionProvider</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> provider,
 y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Add Edge Selection Provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The given provider.</dd>
<dd><code>edge</code> - single edge</dd>
<dt>Returns:</dt>
<dd>EdgeMap.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addGroupNodeInsetsProvider()">
<h3>addGroupNodeInsetsProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addGroupNodeInsetsProvider</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Add Group node inset provider.</div>
</section>
</li>
<li>
<section class="detail" id="removeGroupNodeInsetsProvider()">
<h3>removeGroupNodeInsetsProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeGroupNodeInsetsProvider</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Remove The group node in sets of provider.</div>
</section>
</li>
<li>
<section class="detail" id="createGroupBoundsCalculator()">
<h3>createGroupBoundsCalculator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.layout.grouping.GroupBoundsCalculator</span> <span class="element-name">createGroupBoundsCalculator</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates bounds calculator for group nodes</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>calculator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeMap()">
<h3>getNodeMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.NodeMap</span> <span class="element-name">getNodeMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a node map associated with a data provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEdgeMap()">
<h3>getEdgeMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.EdgeMap</span> <span class="element-name">getEdgeMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an edge map associated with a data provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDataMap()">
<h3>getDataMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getDataMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an edge map associated with a data provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reverseAndAddToNoReverseList(y.base.Edge)">
<h3>reverseAndAddToNoReverseList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reverseAndAddToNoReverseList</span><wbr/><span class="parameters">(y.base.Edge edg)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Reverses an edge in graph, does not reverse if path is already reversed. This method handles label sides also, but only if they are described by
 PreferredPlacementDescriptor.
 PreferredPlacementDescriptor.PLACE_AT_TARGET is changed to PreferredPlacementDescriptor.PLACE_AT_SOURCE</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edg</code> - the edge to reverse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reverseEdgeAndLabels(y.base.Edge)">
<h3>reverseEdgeAndLabels</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reverseEdgeAndLabels</span><wbr/><span class="parameters">(y.base.Edge edg)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Reverses the edge along with labels, but does not add them to no reverse list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edg</code> - edge to reverse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reverseEdge(y.base.Edge)">
<h3>reverseEdge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reverseEdge</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Reverses an edge. Note: does not reverse the labels if they are placed on edge ends. Check
 the <a href="#reverseAndAddToNoReverseList(y.base.Edge)"><code>reverseAndAddToNoReverseList</code></a> method.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>reverseEdge</code> in class <code>y.base.Graph</code></dd>
<dt>Parameters:</dt>
<dd><code>edge</code> - edge to reverse</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addToReversedList(y.base.Edge)">
<h3>addToReversedList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addToReversedList</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - edge to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReversedList()">
<h3>getReversedList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;y.base.Edge&gt;</span> <span class="element-name">getReversedList</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a set of reversed edges</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPlaceEdgeLabelsTo(int)">
<h3>setPlaceEdgeLabelsTo</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPlaceEdgeLabelsTo</span><wbr/><span class="parameters">(int placeEdgeLabelsTo)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the calculated label placement for labels. Labels can be created for consideration only, but not placed at the calculated location.
 One of EDGE_LABEL_NONE, EDGE_LABEL_AT_ENDS, EDGE_LABEL_NON_ENDS , EDGE_LABEL_ALL.
 EDGE_LABEL_ALL by default.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>placeEdgeLabelsTo</code> - the edge placement mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPlaceEdgeLabelsPositions()">
<h3>getPlaceEdgeLabelsPositions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPlaceEdgeLabelsPositions</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the edge placement mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateEdgeLabels(int)">
<h3>setCreateEdgeLabels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateEdgeLabels</span><wbr/><span class="parameters">(int createEdgeLabels)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the label creation mode. One of EDGE_LABEL_NONE, EDGE_LABEL_AT_ENDS, EDGE_LABEL_NON_ENDS , EDGE_LABEL_ALL.
 EDGE_LABEL_ALL by default.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>createEdgeLabels</code> - edge placement mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreateEdgeLabels()">
<h3>getCreateEdgeLabels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getCreateEdgeLabels</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the edge creation mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPlaceNodeLabels(boolean)">
<h3>setPlaceNodeLabels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPlaceNodeLabels</span><wbr/><span class="parameters">(boolean shouldPlaceNodeLabelsToCalculatedPositions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shouldPlaceNodeLabelsToCalculatedPositions</code> - determines if node labels should be placed at the calculated graph position</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shouldPlaceNodeLabels()">
<h3>shouldPlaceNodeLabels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">shouldPlaceNodeLabels</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if node labels should be set at the calculated position, false for the default position</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCreateNodeLabels(boolean)">
<h3>setCreateNodeLabels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateNodeLabels</span><wbr/><span class="parameters">(boolean shouldCreateNodeLabels)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shouldCreateNodeLabels</code> - determines if node labels should be created and considered by the graph</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="shouldCreateNodeLabels()">
<h3>shouldCreateNodeLabels</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">shouldCreateNodeLabels</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the node label creation mode</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPartitionGrid()">
<h3>getPartitionGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.layout.grid.PartitionGrid</span> <span class="element-name">getPartitionGrid</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of partition grid</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPartitionGrid(y.layout.grid.PartitionGrid)">
<h3>setPartitionGrid</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPartitionGrid</span><wbr/><span class="parameters">(y.layout.grid.PartitionGrid partitionGrid)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>partitionGrid</code> - sets to use this partition grid as grid</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeToTableShapeAndCellStructure()">
<h3>getNodeToTableShapeAndCellStructure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Node,<wbr/>com.dassault_systemes.modeler.magic.diagram.ylayout.partition.TableShapeAndCellStructure&gt;</span> <span class="element-name">getNodeToTableShapeAndCellStructure</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the node belonging to a tableShape structure</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPartitionInfo()">
<h3>getPartitionInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getPartitionInfo</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the constructed partition info.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPartitionInfo(java.lang.Object)">
<h3>setPartitionInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPartitionInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> info)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>info</code> - the information of partitions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSphereRadius(int)">
<h3>setSphereRadius</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSphereRadius</span><wbr/><span class="parameters">(int radius)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the sphere from the defined point. All element within this sphere will be collected and
 initiated. Shapes outside the sphere will be ignored.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>radius</code> - the radius that shapes are collected</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSphereRadius()">
<h3>getSphereRadius</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSphereRadius</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the sphere size for data initialization</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSphereCenterPoint(java.awt.Point)">
<h3>setSphereCenterPoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSphereCenterPoint</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> point)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Sets the center of the sphere that is used for node creation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - new point of center, default is 0,0</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSphereCenterPoint()">
<h3>getSphereCenterPoint</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a></span> <span class="element-name">getSphereCenterPoint</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the center of the sphere for node creation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isInSphereRadius(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>isInSphereRadius</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isInSphereRadius</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if shape is in sphere radius, or sphere radius is the default, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeHaloAdjustedSourcePointAbs(y.base.Edge)">
<h3>getNodeHaloAdjustedSourcePointAbs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.geom.YPoint</span> <span class="element-name">getNodeHaloAdjustedSourcePointAbs</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get absolute location of edge source point on halo, not on the source node itself. As symbols themselves are adjusted by the halos, this is necessary for on edge shape
 placement to calculate a correct position. Currently only UMLGraphKeys.ENCLOSING_SHAPE_HALO_DP_KEY is considered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - edge</dd>
<dt>Returns:</dt>
<dd>the source point on halo, rather than node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNodeHaloAdjustedTargetPointAbs(y.base.Edge)">
<h3>getNodeHaloAdjustedTargetPointAbs</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.geom.YPoint</span> <span class="element-name">getNodeHaloAdjustedTargetPointAbs</span><wbr/><span class="parameters">(y.base.Edge edge)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Get absolute location of edge target point on halo, not on the target node itself. As symbols themselves are adjusted by the halos, this is necessary for on edge shape
 placement to calculate a correct position. Currently only UMLGraphKeys.ENCLOSING_SHAPE_HALO_DP_KEY is considered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>edge</code> - edge</dd>
<dt>Returns:</dt>
<dd>the target point on halo, rather than node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEdgeLabelFactory(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory)">
<h3>setEdgeLabelFactory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEdgeLabelFactory</span><wbr/><span class="parameters">(@CheckForNull
 com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory edgeLabelFactory)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getNonSupportedSymbols()">
<h3>getNonSupportedSymbols</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getNonSupportedSymbols</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>set of symbols(shapes or paths) that are not supported by the graph and will not be included into layout and/or will be treated not as a part
 of the graph</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDoNotRepaintPaths()">
<h3>getDoNotRepaintPaths</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a>&gt;</span> <span class="element-name">getDoNotRepaintPaths</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>set of collected paths that are included in the layout, but not repainted according to the graph result</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFakeElementsMap()">
<h3>getFakeElementsMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/>y.base.Edge&gt;</span> <span class="element-name">getFakeElementsMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getInsetMap()">
<h3>getInsetMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">y.base.NodeMap</span> <span class="element-name">getInsetMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getEdgeLabelDataMap()">
<h3>getEdgeLabelDataMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Edge,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;y.layout.EdgeLabelLayout&gt;&gt;</span> <span class="element-name">getEdgeLabelDataMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getNodeLabelDataMap()">
<h3>getNodeLabelDataMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;y.base.Node,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;y.layout.NodeLabelLayout&gt;&gt;</span> <span class="element-name">getNodeLabelDataMap</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getAnchoredShape()">
<h3>getAnchoredShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getAnchoredShape</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="setAnchoredShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setAnchoredShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnchoredShape</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> anchoredShape)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getLayouterParameters()">
<h3>getLayouterParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getLayouterParameters</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="setLayouterParameters(java.util.Map)">
<h3>setLayouterParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLayouterParameters</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; layouterParameters)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="isConsideredAsOuterBoundary(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isConsideredAsOuterBoundary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isConsideredAsOuterBoundary</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getOuterBoundaryShape()">
<h3>getOuterBoundaryShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a></span> <span class="element-name">getOuterBoundaryShape</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="setOuterBoundaryShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>setOuterBoundaryShape</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOuterBoundaryShape</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> outerBoundaryShape)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="getTableShapeViews()">
<h3>getTableShapeViews</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicdraw.uml.symbols.shapes.TableShapeView&gt;</span> <span class="element-name">getTableShapeViews</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The tableShapeViews that are considered in this graph.</div>
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
