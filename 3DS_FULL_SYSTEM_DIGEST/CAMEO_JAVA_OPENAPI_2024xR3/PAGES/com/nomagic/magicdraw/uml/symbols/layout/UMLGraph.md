# JAVA OPENAPI: UMLGraph (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/UMLGraph.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/UMLGraph.html`
- source_sha256: `8442c95a1c92b603d66a9f4db1701c5db098b358f1f531f10175604ea5a59ea3`
- captured_utc: `2026-07-14T16:55:58.766496+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Class UMLGraph

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
y.base.Graph
y.layout.LayoutGraph
y.layout.DefaultLayoutGraph
[com.nomagic.magicdraw.uml.symbols.layout.BaseGraph](BaseGraph.html)
com.nomagic.magicdraw.uml.symbols.layout.UMLGraph

All Implemented Interfaces:
`y.base.GraphInterface`, `y.layout.GraphLayout`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public classUMLGraph
extends [BaseGraph](BaseGraph.html)

Deprecated.

UML graph data.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.[BaseGraph](BaseGraph.html)
`[currentTableCellView](BaseGraph.html#currentTableCellView), [currentTableShapeView](BaseGraph.html#currentTableShapeView), [doNotRepaint](BaseGraph.html#doNotRepaint), [EDGE_LABEL_ALL](BaseGraph.html#EDGE_LABEL_ALL), [EDGE_LABEL_AT_ENDS](BaseGraph.html#EDGE_LABEL_AT_ENDS), [EDGE_LABEL_NON_ENDS](BaseGraph.html#EDGE_LABEL_NON_ENDS), [EDGE_LABEL_NONE](BaseGraph.html#EDGE_LABEL_NONE), [edgeLabelDataMap](BaseGraph.html#edgeLabelDataMap), [edgeLabelFactory](BaseGraph.html#edgeLabelFactory), [grid](BaseGraph.html#grid), [LAYOUTABLE_NODE_FEATURE_ID](BaseGraph.html#LAYOUTABLE_NODE_FEATURE_ID), [mDataMap](BaseGraph.html#mDataMap), [mDiagramView](BaseGraph.html#mDiagramView), [mEdgeMap](BaseGraph.html#mEdgeMap), [mFakeElementsMap](BaseGraph.html#mFakeElementsMap), [mGroupKey](BaseGraph.html#mGroupKey), [mNodeId](BaseGraph.html#mNodeId), [mNodeMap](BaseGraph.html#mNodeMap), [mNotSupported](BaseGraph.html#mNotSupported), [mPaths](BaseGraph.html#mPaths), [mSelected](BaseGraph.html#mSelected), [nodeLabelFactory](BaseGraph.html#nodeLabelFactory), [nodeToTableShapeViewPlacement](BaseGraph.html#nodeToTableShapeViewPlacement), [partitionInfo](BaseGraph.html#partitionInfo), [SHRINKABLE_SHAPE_INSET_DP](BaseGraph.html#SHRINKABLE_SHAPE_INSET_DP), [tableShapeViews](BaseGraph.html#tableShapeViews)`
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
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Deprecated.
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBoundingBox](#getBoundingBox())()`
Deprecated.
`protected y.geom.YInsets`
`[getInsets](#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))([ShapeElement](../shapes/ShapeElement.html) shape)`
Deprecated.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)>`
`[getSpecialInnerManipulatedPresentationElements](#getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) view)`
Deprecated.
`protected boolean`
`[isCreatableNode](#isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) view)`
Deprecated.
`protected boolean`
`[isNotLayoutedChild](#isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../PresentationElement.html) view)`
Deprecated.
`protected void`
`[resetUnhandledPath](#resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement))(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 [PresentationElement](../PresentationElement.html) prEl)`
Deprecated.
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[BaseGraph](BaseGraph.html)
`[addEdgeSelectionProvider](BaseGraph.html#addEdgeSelectionProvider(java.lang.Object,java.util.Collection)), [addEdgeSelectionProvider](BaseGraph.html#addEdgeSelectionProvider(java.lang.Object,y.base.Edge)), [addGroupNodeInsetsProvider](BaseGraph.html#addGroupNodeInsetsProvider()), [addPaths](BaseGraph.html#addPaths(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [addToPathList](BaseGraph.html#addToPathList(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [addToPathList](BaseGraph.html#addToPathList(java.lang.Iterable)), [addToReversedList](BaseGraph.html#addToReversedList(y.base.Edge)), [adjustFakeAtEndShapeLabelOrientation](BaseGraph.html#adjustFakeAtEndShapeLabelOrientation(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [areParentToChildConnected](BaseGraph.html#areParentToChildConnected(java.lang.Iterable)), [belongsToHierarchy](BaseGraph.html#belongsToHierarchy(y.base.Edge)), [belongsToHierarchy](BaseGraph.html#belongsToHierarchy(y.base.Node)), [collectPathsRecursively](BaseGraph.html#collectPathsRecursively(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)), [containsHierarchy](BaseGraph.html#containsHierarchy()), [createAllNodeLabels](BaseGraph.html#createAllNodeLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)), [createAllPathLabels](BaseGraph.html#createAllPathLabels(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory,y.base.Edge,com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [createCommands](BaseGraph.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [createEdge](BaseGraph.html#createEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [createEdgesToNotLayoutableOnEdge](BaseGraph.html#createEdgesToNotLayoutableOnEdge(y.base.Node,java.util.Collection)), [createGroupBoundsCalculator](BaseGraph.html#createGroupBoundsCalculator()), [createHierarchicInfo](BaseGraph.html#createHierarchicInfo(java.util.Collection)), [createNode](BaseGraph.html#createNode(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [createNode](BaseGraph.html#createNode(java.lang.Object)), [createNodeData](BaseGraph.html#createNodeData(java.lang.Object,com.nomagic.magicdraw.uml.symbols.PresentationElement)), [createNodesData](BaseGraph.html#createNodesData(java.lang.Object,java.util.Collection)), [dispose](BaseGraph.html#dispose()), [doesNotHaveConnectedLayoutableEdges](BaseGraph.html#doesNotHaveConnectedLayoutableEdges(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [drawResults](BaseGraph.html#drawResults()), [getAnchoredShape](BaseGraph.html#getAnchoredShape()), [getCreateEdgeLabels](BaseGraph.html#getCreateEdgeLabels()), [getDataMap](BaseGraph.html#getDataMap()), [getDiagram](BaseGraph.html#getDiagram()), [getDoNotRepaintPaths](BaseGraph.html#getDoNotRepaintPaths()), [getEdge](BaseGraph.html#getEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)), [getEdgeLabelBoundingBox](BaseGraph.html#getEdgeLabelBoundingBox(y.base.Edge,y.layout.EdgeLabelLayout)), [getEdgeLabelDataMap](BaseGraph.html#getEdgeLabelDataMap()), [getEdgeMap](BaseGraph.html#getEdgeMap()), [getEnclosingShapeHalo](BaseGraph.html#getEnclosingShapeHalo(y.base.Node)), [getFakeElementsMap](BaseGraph.html#getFakeElementsMap()), [getID](BaseGraph.html#getID(y.base.Node)), [getInsetMap](BaseGraph.html#getInsetMap()), [getInsets](BaseGraph.html#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Insets)), [getLabelByCondition](BaseGraph.html#getLabelByCondition(java.util.function.Predicate)), [getLabelDescriptorsNotAtEnd](BaseGraph.html#getLabelDescriptorsNotAtEnd()), [getLayouterParameters](BaseGraph.html#getLayouterParameters()), [getNode](BaseGraph.html#getNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getNodeDirectly](BaseGraph.html#getNodeDirectly(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [getNodeHaloAdjustedSourcePointAbs](BaseGraph.html#getNodeHaloAdjustedSourcePointAbs(y.base.Edge)), [getNodeHaloAdjustedTargetPointAbs](BaseGraph.html#getNodeHaloAdjustedTargetPointAbs(y.base.Edge)), [getNodeLabelDataMap](BaseGraph.html#getNodeLabelDataMap()), [getNodeMap](BaseGraph.html#getNodeMap()), [getNodeToTableShapeAndCellStructure](BaseGraph.html#getNodeToTableShapeAndCellStructure()), [getNonSupportedSymbols](BaseGraph.html#getNonSupportedSymbols()), [getOuterBoundaryShape](BaseGraph.html#getOuterBoundaryShape()), [getParentId](BaseGraph.html#getParentId(y.base.Node)), [getPartitionGrid](BaseGraph.html#getPartitionGrid()), [getPartitionInfo](BaseGraph.html#getPartitionInfo()), [getPathElement](BaseGraph.html#getPathElement(y.base.Edge)), [getPlaceEdgeLabelsPositions](BaseGraph.html#getPlaceEdgeLabelsPositions()), [getPointsFromEdge](BaseGraph.html#getPointsFromEdge(y.base.Edge)), [getReversedList](BaseGraph.html#getReversedList()), [getSelected](BaseGraph.html#getSelected()), [getShapeElement](BaseGraph.html#getShapeElement(y.base.Node)), [getSphereCenterPoint](BaseGraph.html#getSphereCenterPoint()), [getSphereRadius](BaseGraph.html#getSphereRadius()), [getStyle](BaseGraph.html#getStyle()), [getTableShapeViews](BaseGraph.html#getTableShapeViews()), [ignoreCenterlines](BaseGraph.html#ignoreCenterlines(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [initializeData](BaseGraph.html#initializeData()), [isConsideredAsOuterBoundary](BaseGraph.html#isConsideredAsOuterBoundary(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isGroupNode](BaseGraph.html#isGroupNode(y.base.Node)), [isInSphereRadius](BaseGraph.html#isInSphereRadius(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)), [isLayoutableByProviders](BaseGraph.html#isLayoutableByProviders(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [isLayoutAnchoredShapeOwnerAsLabel](BaseGraph.html#isLayoutAnchoredShapeOwnerAsLabel(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner)), [isTreeOverlapping](BaseGraph.html#isTreeOverlapping(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape,int,java.lang.Iterable)), [makeSubTree](BaseGraph.html#makeSubTree(y.base.Node,java.lang.Class,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [makeSubTrees](BaseGraph.html#makeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [needToCreate](BaseGraph.html#needToCreate(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [placeLayoutedPathLabel](BaseGraph.html#placeLayoutedPathLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement,y.base.Edge,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [placePath](BaseGraph.html#placePath(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.paths.PathElement,y.base.Edge)), [placePaths](BaseGraph.html#placePaths(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,boolean,com.dassault_systemes.modeler.magic.diagram.command.MoveManager)), [removeGroupNodeInsetsProvider](BaseGraph.html#removeGroupNodeInsetsProvider()), [removeSubTrees](BaseGraph.html#removeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)), [resetLabel](BaseGraph.html#resetLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [reverseAndAddToNoReverseList](BaseGraph.html#reverseAndAddToNoReverseList(y.base.Edge)), [reverseEdge](BaseGraph.html#reverseEdge(y.base.Edge)), [reverseEdgeAndLabels](BaseGraph.html#reverseEdgeAndLabels(y.base.Edge)), [setAnchoredShape](BaseGraph.html#setAnchoredShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setCreateEdgeLabels](BaseGraph.html#setCreateEdgeLabels(int)), [setCreateNodeLabels](BaseGraph.html#setCreateNodeLabels(boolean)), [setEdgeLabelFactory](BaseGraph.html#setEdgeLabelFactory(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory)), [setGroupNode](BaseGraph.html#setGroupNode(y.base.Node,boolean)), [setLayouterParameters](BaseGraph.html#setLayouterParameters(java.util.Map)), [setMinimalGroupNodeSize](BaseGraph.html#setMinimalGroupNodeSize(y.base.Node,y.geom.YDimension)), [setNodeSizeEnsureNotZero](BaseGraph.html#setNodeSizeEnsureNotZero(java.awt.Rectangle,y.base.Node)), [setOuterBoundaryShape](BaseGraph.html#setOuterBoundaryShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)), [setParent](BaseGraph.html#setParent(y.base.Node,java.lang.Object)), [setPartitionGrid](BaseGraph.html#setPartitionGrid(y.layout.grid.PartitionGrid)), [setPartitionInfo](BaseGraph.html#setPartitionInfo(java.lang.Object)), [setPathBreakPoints](BaseGraph.html#setPathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List,java.awt.Point,java.awt.Point,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)), [setPathStyle](BaseGraph.html#setPathStyle(java.lang.String)), [setPlaceEdgeLabelsTo](BaseGraph.html#setPlaceEdgeLabelsTo(int)), [setPlaceNodeLabels](BaseGraph.html#setPlaceNodeLabels(boolean)), [setResetLabelsAtInit](BaseGraph.html#setResetLabelsAtInit(boolean)), [setSphereCenterPoint](BaseGraph.html#setSphereCenterPoint(java.awt.Point)), [setSphereRadius](BaseGraph.html#setSphereRadius(int)), [shouldCreateNodeLabels](BaseGraph.html#shouldCreateNodeLabels()), [shouldPlaceNodeLabels](BaseGraph.html#shouldPlaceNodeLabels()), [shouldResetLabelsAtInit](BaseGraph.html#shouldResetLabelsAtInit())`
Methods inherited from class y.layout.DefaultLayoutGraph
`createEdgeLayout, createGraphCopyFactory, createLabelFactory, createNodeLayout, getFeature, getFeature, getLabelLayout, getLabelLayout, getLayout, getLayout, setLabelLayout, setLabelLayout, setLabelLayout, setLayout, setLayout`
Methods inherited from class y.layout.LayoutGraph
`getCenter, getCenterX, getCenterY, getEdgeLabelLayout, getEdgeLayout, getEdgeList, getHeight, getLocation, getNodeLabelLayout, getNodeLayout, getPath, getPathList, getPointList, getPoints, getRectangle, getSize, getSourcePointAbs, getSourcePointRel, getTargetPointAbs, getTargetPointRel, getWidth, getX, getY, moveBy, setCenter, setCenter, setEndPointsAbs, setLocation, setLocation, setPath, setPath, setPoints, setPoints, setSize, setSize, setSourcePointAbs, setSourcePointRel, setTargetPointAbs, setTargetPointRel`
Methods inherited from class y.base.Graph
`addDataProvider, addGraphListener, changeEdge, changeEdge, changeEdge, clear, contains, contains, containsEdge, createCopy, createEdge, createEdge, createEdgeMap, createGraph, createNode, createNodeMap, disposeEdgeMap, disposeNodeMap, E, edgeCount, edgeObjects, edges, fireGraphEvent, firePostEvent, firePostEvent, firePreEvent, firePreEvent, firstEdge, firstNode, firstOutEdge, getDataProvider, getDataProviderKeys, getEdgeArray, getGraphCopyFactory, getGraphListeners, getNodeArray, getRegisteredEdgeMaps, getRegisteredNodeMaps, getSource, getTarget, hasListeners, hide, hide, isEmpty, lastEdge, lastNode, moveSubGraph, moveToFirst, moveToFirst, moveToLast, moveToLast, N, nodeCount, nodeObjects, nodes, printNodeSlotSize, reInsertEdge, reInsertNode, removeDataProvider, removeEdge, removeGraphListener, removeNode, setGraphCopyFactory, sortEdges, sortEdges, sortNodes, toString, unhide, unhide`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UMLGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Deprecated.
Construct UML Graph. with given parameter
Parameters:
`diagramView` - diagram for which to construct graph.
`selected` - selected elements
UMLGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
UMLGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3")public UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
Deprecated.
UMLGraph
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)public UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
Deprecated, for removal: This API element is subject to removal in a future version.
supportsSubgraph has no effect
 ============ METHOD DETAIL ========== 
Method Details
getInsets
protected y.geom.YInsets getInsets([ShapeElement](../shapes/ShapeElement.html) shape)
Deprecated.
Overrides:
`[getInsets](BaseGraph.html#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement))` in class `[BaseGraph](BaseGraph.html)`
getBoundingBox
public [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBoundingBox()
Deprecated.
Specified by:
`getBoundingBox` in interface `y.layout.GraphLayout`
Overrides:
`[getBoundingBox](BaseGraph.html#getBoundingBox())` in class `[BaseGraph](BaseGraph.html)`
getSpecialInnerManipulatedPresentationElements
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](../PresentationElement.html)> getSpecialInnerManipulatedPresentationElements([PresentationElement](../PresentationElement.html) view)
Deprecated.
Overrides:
`[getSpecialInnerManipulatedPresentationElements](BaseGraph.html#getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[BaseGraph](BaseGraph.html)`
isCreatableNode
protected boolean isCreatableNode([PresentationElement](../PresentationElement.html) view)
Deprecated.
Overrides:
`[isCreatableNode](BaseGraph.html#isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[BaseGraph](BaseGraph.html)`
isNotLayoutedChild
protected boolean isNotLayoutedChild([PresentationElement](../PresentationElement.html) view)
Deprecated.
Overrides:
`[isNotLayoutedChild](BaseGraph.html#isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[BaseGraph](BaseGraph.html)`
resetUnhandledPath
protected void resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 [PresentationElement](../PresentationElement.html) prEl)
Deprecated.
Overrides:
`[resetUnhandledPath](BaseGraph.html#resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement))` in class `[BaseGraph](BaseGraph.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Class UMLGraph">Class UMLGraph</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">y.base.Graph
<div class="inheritance">y.layout.LayoutGraph
<div class="inheritance">y.layout.DefaultLayoutGraph
<div class="inheritance"><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.BaseGraph</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.UMLGraph</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>y.base.GraphInterface</code>, <code>y.layout.GraphLayout</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public class </span><span class="element-name type-name-label">UMLGraph</span>
<span class="extends-implements">extends <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">UML graph data.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.BaseGraph">Fields inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></h3>
<code><a href="BaseGraph.html#currentTableCellView">currentTableCellView</a>, <a href="BaseGraph.html#currentTableShapeView">currentTableShapeView</a>, <a href="BaseGraph.html#doNotRepaint">doNotRepaint</a>, <a href="BaseGraph.html#EDGE_LABEL_ALL">EDGE_LABEL_ALL</a>, <a href="BaseGraph.html#EDGE_LABEL_AT_ENDS">EDGE_LABEL_AT_ENDS</a>, <a href="BaseGraph.html#EDGE_LABEL_NON_ENDS">EDGE_LABEL_NON_ENDS</a>, <a href="BaseGraph.html#EDGE_LABEL_NONE">EDGE_LABEL_NONE</a>, <a href="BaseGraph.html#edgeLabelDataMap">edgeLabelDataMap</a>, <a href="BaseGraph.html#edgeLabelFactory">edgeLabelFactory</a>, <a href="BaseGraph.html#grid">grid</a>, <a href="BaseGraph.html#LAYOUTABLE_NODE_FEATURE_ID">LAYOUTABLE_NODE_FEATURE_ID</a>, <a href="BaseGraph.html#mDataMap">mDataMap</a>, <a href="BaseGraph.html#mDiagramView">mDiagramView</a>, <a href="BaseGraph.html#mEdgeMap">mEdgeMap</a>, <a href="BaseGraph.html#mFakeElementsMap">mFakeElementsMap</a>, <a href="BaseGraph.html#mGroupKey">mGroupKey</a>, <a href="BaseGraph.html#mNodeId">mNodeId</a>, <a href="BaseGraph.html#mNodeMap">mNodeMap</a>, <a href="BaseGraph.html#mNotSupported">mNotSupported</a>, <a href="BaseGraph.html#mPaths">mPaths</a>, <a href="BaseGraph.html#mSelected">mSelected</a>, <a href="BaseGraph.html#nodeLabelFactory">nodeLabelFactory</a>, <a href="BaseGraph.html#nodeToTableShapeViewPlacement">nodeToTableShapeViewPlacement</a>, <a href="BaseGraph.html#partitionInfo">partitionInfo</a>, <a href="BaseGraph.html#SHRINKABLE_SHAPE_INSET_DP">SHRINKABLE_SHAPE_INSET_DP</a>, <a href="BaseGraph.html#tableShapeViews">tableShapeViews</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected y.geom.YInsets</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">getInsets</a><wbr/>(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSpecialInnerManipulatedPresentationElements</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isCreatableNode</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isNotLayoutedChild</a><wbr/>(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">resetUnhandledPath</a><wbr/>(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> prEl)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.BaseGraph">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></h3>
<code><a href="BaseGraph.html#addEdgeSelectionProvider(java.lang.Object,java.util.Collection)">addEdgeSelectionProvider</a>, <a href="BaseGraph.html#addEdgeSelectionProvider(java.lang.Object,y.base.Edge)">addEdgeSelectionProvider</a>, <a href="BaseGraph.html#addGroupNodeInsetsProvider()">addGroupNodeInsetsProvider</a>, <a href="BaseGraph.html#addPaths(com.nomagic.magicdraw.uml.symbols.PresentationElement)">addPaths</a>, <a href="BaseGraph.html#addToPathList(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">addToPathList</a>, <a href="BaseGraph.html#addToPathList(java.lang.Iterable)">addToPathList</a>, <a href="BaseGraph.html#addToReversedList(y.base.Edge)">addToReversedList</a>, <a href="BaseGraph.html#adjustFakeAtEndShapeLabelOrientation(com.nomagic.magicdraw.uml.symbols.PresentationElement)">adjustFakeAtEndShapeLabelOrientation</a>, <a href="BaseGraph.html#areParentToChildConnected(java.lang.Iterable)">areParentToChildConnected</a>, <a href="BaseGraph.html#belongsToHierarchy(y.base.Edge)">belongsToHierarchy</a>, <a href="BaseGraph.html#belongsToHierarchy(y.base.Node)">belongsToHierarchy</a>, <a href="BaseGraph.html#collectPathsRecursively(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)">collectPathsRecursively</a>, <a href="BaseGraph.html#containsHierarchy()">containsHierarchy</a>, <a href="BaseGraph.html#createAllNodeLabels(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,y.base.Node)">createAllNodeLabels</a>, <a href="BaseGraph.html#createAllPathLabels(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory,y.base.Edge,com.nomagic.magicdraw.uml.symbols.paths.PathElement)">createAllPathLabels</a>, <a href="BaseGraph.html#createCommands(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">createCommands</a>, <a href="BaseGraph.html#createEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">createEdge</a>, <a href="BaseGraph.html#createEdgesToNotLayoutableOnEdge(y.base.Node,java.util.Collection)">createEdgesToNotLayoutableOnEdge</a>, <a href="BaseGraph.html#createGroupBoundsCalculator()">createGroupBoundsCalculator</a>, <a href="BaseGraph.html#createHierarchicInfo(java.util.Collection)">createHierarchicInfo</a>, <a href="BaseGraph.html#createNode(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">createNode</a>, <a href="BaseGraph.html#createNode(java.lang.Object)">createNode</a>, <a href="BaseGraph.html#createNodeData(java.lang.Object,com.nomagic.magicdraw.uml.symbols.PresentationElement)">createNodeData</a>, <a href="BaseGraph.html#createNodesData(java.lang.Object,java.util.Collection)">createNodesData</a>, <a href="BaseGraph.html#dispose()">dispose</a>, <a href="BaseGraph.html#doesNotHaveConnectedLayoutableEdges(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">doesNotHaveConnectedLayoutableEdges</a>, <a href="BaseGraph.html#drawResults()">drawResults</a>, <a href="BaseGraph.html#getAnchoredShape()">getAnchoredShape</a>, <a href="BaseGraph.html#getCreateEdgeLabels()">getCreateEdgeLabels</a>, <a href="BaseGraph.html#getDataMap()">getDataMap</a>, <a href="BaseGraph.html#getDiagram()">getDiagram</a>, <a href="BaseGraph.html#getDoNotRepaintPaths()">getDoNotRepaintPaths</a>, <a href="BaseGraph.html#getEdge(com.nomagic.magicdraw.uml.symbols.paths.PathElement)">getEdge</a>, <a href="BaseGraph.html#getEdgeLabelBoundingBox(y.base.Edge,y.layout.EdgeLabelLayout)">getEdgeLabelBoundingBox</a>, <a href="BaseGraph.html#getEdgeLabelDataMap()">getEdgeLabelDataMap</a>, <a href="BaseGraph.html#getEdgeMap()">getEdgeMap</a>, <a href="BaseGraph.html#getEnclosingShapeHalo(y.base.Node)">getEnclosingShapeHalo</a>, <a href="BaseGraph.html#getFakeElementsMap()">getFakeElementsMap</a>, <a href="BaseGraph.html#getID(y.base.Node)">getID</a>, <a href="BaseGraph.html#getInsetMap()">getInsetMap</a>, <a href="BaseGraph.html#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement,java.awt.Insets)">getInsets</a>, <a href="BaseGraph.html#getLabelByCondition(java.util.function.Predicate)">getLabelByCondition</a>, <a href="BaseGraph.html#getLabelDescriptorsNotAtEnd()">getLabelDescriptorsNotAtEnd</a>, <a href="BaseGraph.html#getLayouterParameters()">getLayouterParameters</a>, <a href="BaseGraph.html#getNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getNode</a>, <a href="BaseGraph.html#getNodeDirectly(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getNodeDirectly</a>, <a href="BaseGraph.html#getNodeHaloAdjustedSourcePointAbs(y.base.Edge)">getNodeHaloAdjustedSourcePointAbs</a>, <a href="BaseGraph.html#getNodeHaloAdjustedTargetPointAbs(y.base.Edge)">getNodeHaloAdjustedTargetPointAbs</a>, <a href="BaseGraph.html#getNodeLabelDataMap()">getNodeLabelDataMap</a>, <a href="BaseGraph.html#getNodeMap()">getNodeMap</a>, <a href="BaseGraph.html#getNodeToTableShapeAndCellStructure()">getNodeToTableShapeAndCellStructure</a>, <a href="BaseGraph.html#getNonSupportedSymbols()">getNonSupportedSymbols</a>, <a href="BaseGraph.html#getOuterBoundaryShape()">getOuterBoundaryShape</a>, <a href="BaseGraph.html#getParentId(y.base.Node)">getParentId</a>, <a href="BaseGraph.html#getPartitionGrid()">getPartitionGrid</a>, <a href="BaseGraph.html#getPartitionInfo()">getPartitionInfo</a>, <a href="BaseGraph.html#getPathElement(y.base.Edge)">getPathElement</a>, <a href="BaseGraph.html#getPlaceEdgeLabelsPositions()">getPlaceEdgeLabelsPositions</a>, <a href="BaseGraph.html#getPointsFromEdge(y.base.Edge)">getPointsFromEdge</a>, <a href="BaseGraph.html#getReversedList()">getReversedList</a>, <a href="BaseGraph.html#getSelected()">getSelected</a>, <a href="BaseGraph.html#getShapeElement(y.base.Node)">getShapeElement</a>, <a href="BaseGraph.html#getSphereCenterPoint()">getSphereCenterPoint</a>, <a href="BaseGraph.html#getSphereRadius()">getSphereRadius</a>, <a href="BaseGraph.html#getStyle()">getStyle</a>, <a href="BaseGraph.html#getTableShapeViews()">getTableShapeViews</a>, <a href="BaseGraph.html#ignoreCenterlines(com.nomagic.magicdraw.uml.symbols.PresentationElement)">ignoreCenterlines</a>, <a href="BaseGraph.html#initializeData()">initializeData</a>, <a href="BaseGraph.html#isConsideredAsOuterBoundary(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isConsideredAsOuterBoundary</a>, <a href="BaseGraph.html#isGroupNode(y.base.Node)">isGroupNode</a>, <a href="BaseGraph.html#isInSphereRadius(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">isInSphereRadius</a>, <a href="BaseGraph.html#isLayoutableByProviders(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isLayoutableByProviders</a>, <a href="BaseGraph.html#isLayoutAnchoredShapeOwnerAsLabel(com.nomagic.magicdraw.uml.symbols.paths.AnchoredShapeOwner)">isLayoutAnchoredShapeOwnerAsLabel</a>, <a href="BaseGraph.html#isTreeOverlapping(com.nomagic.magicdraw.uml.symbols.shapes.BaseTreeShape,int,java.lang.Iterable)">isTreeOverlapping</a>, <a href="BaseGraph.html#makeSubTree(y.base.Node,java.lang.Class,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">makeSubTree</a>, <a href="BaseGraph.html#makeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">makeSubTrees</a>, <a href="BaseGraph.html#needToCreate(com.nomagic.magicdraw.uml.symbols.PresentationElement)">needToCreate</a>, <a href="BaseGraph.html#placeLayoutedPathLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement,y.base.Edge,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">placeLayoutedPathLabel</a>, <a href="BaseGraph.html#placePath(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.paths.PathElement,y.base.Edge)">placePath</a>, <a href="BaseGraph.html#placePaths(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,boolean,com.dassault_systemes.modeler.magic.diagram.command.MoveManager)">placePaths</a>, <a href="BaseGraph.html#removeGroupNodeInsetsProvider()">removeGroupNodeInsetsProvider</a>, <a href="BaseGraph.html#removeSubTrees(com.dassault_systemes.modeler.foundation.editing.CompositeCommand,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">removeSubTrees</a>, <a href="BaseGraph.html#resetLabel(com.nomagic.magicdraw.uml.symbols.PresentationElement)">resetLabel</a>, <a href="BaseGraph.html#reverseAndAddToNoReverseList(y.base.Edge)">reverseAndAddToNoReverseList</a>, <a href="BaseGraph.html#reverseEdge(y.base.Edge)">reverseEdge</a>, <a href="BaseGraph.html#reverseEdgeAndLabels(y.base.Edge)">reverseEdgeAndLabels</a>, <a href="BaseGraph.html#setAnchoredShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setAnchoredShape</a>, <a href="BaseGraph.html#setCreateEdgeLabels(int)">setCreateEdgeLabels</a>, <a href="BaseGraph.html#setCreateNodeLabels(boolean)">setCreateNodeLabels</a>, <a href="BaseGraph.html#setEdgeLabelFactory(com.dassault_systemes.modeler.magic.diagram.ylayout.labels.EdgeLabelFactory)">setEdgeLabelFactory</a>, <a href="BaseGraph.html#setGroupNode(y.base.Node,boolean)">setGroupNode</a>, <a href="BaseGraph.html#setLayouterParameters(java.util.Map)">setLayouterParameters</a>, <a href="BaseGraph.html#setMinimalGroupNodeSize(y.base.Node,y.geom.YDimension)">setMinimalGroupNodeSize</a>, <a href="BaseGraph.html#setNodeSizeEnsureNotZero(java.awt.Rectangle,y.base.Node)">setNodeSizeEnsureNotZero</a>, <a href="BaseGraph.html#setOuterBoundaryShape(com.nomagic.magicdraw.uml.symbols.PresentationElement)">setOuterBoundaryShape</a>, <a href="BaseGraph.html#setParent(y.base.Node,java.lang.Object)">setParent</a>, <a href="BaseGraph.html#setPartitionGrid(y.layout.grid.PartitionGrid)">setPartitionGrid</a>, <a href="BaseGraph.html#setPartitionInfo(java.lang.Object)">setPartitionInfo</a>, <a href="BaseGraph.html#setPathBreakPoints(com.nomagic.magicdraw.uml.symbols.paths.PathElement,java.util.List,java.awt.Point,java.awt.Point,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">setPathBreakPoints</a>, <a href="BaseGraph.html#setPathStyle(java.lang.String)">setPathStyle</a>, <a href="BaseGraph.html#setPlaceEdgeLabelsTo(int)">setPlaceEdgeLabelsTo</a>, <a href="BaseGraph.html#setPlaceNodeLabels(boolean)">setPlaceNodeLabels</a>, <a href="BaseGraph.html#setResetLabelsAtInit(boolean)">setResetLabelsAtInit</a>, <a href="BaseGraph.html#setSphereCenterPoint(java.awt.Point)">setSphereCenterPoint</a>, <a href="BaseGraph.html#setSphereRadius(int)">setSphereRadius</a>, <a href="BaseGraph.html#shouldCreateNodeLabels()">shouldCreateNodeLabels</a>, <a href="BaseGraph.html#shouldPlaceNodeLabels()">shouldPlaceNodeLabels</a>, <a href="BaseGraph.html#shouldResetLabelsAtInit()">shouldResetLabelsAtInit</a></code></div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">
<h3>UMLGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Construct UML Graph. with given parameter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramView</code> - diagram for which to construct graph.</dd>
<dd><code>selected</code> - selected elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set)">
<h3>UMLGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">
<h3>UMLGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3")
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">
<h3>UMLGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
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
<section class="detail" id="getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">
<h3>getInsets</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">y.geom.YInsets</span> <span class="element-name">getInsets</span><wbr/><span class="parameters">(<a href="../shapes/ShapeElement.html" title="class in com.nomagic.magicdraw.uml.symbols.shapes">ShapeElement</a> shape)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseGraph.html#getInsets(com.nomagic.magicdraw.uml.symbols.shapes.ShapeElement)">getInsets</a></code> in class <code><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></dd>
</dl>
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
<dd><code><a href="BaseGraph.html#getBoundingBox()">getBoundingBox</a></code> in class <code><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getSpecialInnerManipulatedPresentationElements</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSpecialInnerManipulatedPresentationElements</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseGraph.html#getSpecialInnerManipulatedPresentationElements(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getSpecialInnerManipulatedPresentationElements</a></code> in class <code><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isCreatableNode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isCreatableNode</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseGraph.html#isCreatableNode(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isCreatableNode</a></code> in class <code><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isNotLayoutedChild</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNotLayoutedChild</span><wbr/><span class="parameters">(<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseGraph.html#isNotLayoutedChild(com.nomagic.magicdraw.uml.symbols.PresentationElement)">isNotLayoutedChild</a></code> in class <code><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>resetUnhandledPath</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resetUnhandledPath</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.magic.diagram.command.MoveManager moveManager,
 <a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> prEl)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="BaseGraph.html#resetUnhandledPath(com.dassault_systemes.modeler.magic.diagram.command.MoveManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">resetUnhandledPath</a></code> in class <code><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></dd>
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
