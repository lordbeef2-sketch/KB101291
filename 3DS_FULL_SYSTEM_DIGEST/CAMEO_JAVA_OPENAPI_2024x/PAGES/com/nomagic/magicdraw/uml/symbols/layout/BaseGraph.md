# JAVA OPENAPI: BaseGraph (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/layout/BaseGraph.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/BaseGraph.html`
- source_sha256: `3df706666c985d4cb993dfd665ebc91332afb734c2b95518aac93ea49c6f174d`
- captured_utc: `2026-07-14T16:52:12.341884+00:00`

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

@OpenApipublic classBaseGraph
extends y.layout.DefaultLayoutGraph

UML graph data.

=========== FIELD SUMMARY =========== 
Field Summary
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
Deprecated.
supportsSubgraph has no effect
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
Deprecated.
supportsSubgraph has no effect
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Construct a graph with given parameter
`[BaseGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[getCreateEdgeLabels](#getCreateEdgeLabels())()`

`int`
`[getPlaceEdgeLabelsPositions](#getPlaceEdgeLabelsPositions())()`

`void`
`[initializeData](#initializeData())()`
Collects all data provided by diagram to nodes and edges.
`void`
`[setCreateEdgeLabels](#setCreateEdgeLabels(int))(int createEdgeLabels)`
Sets the label creation mode.
`void`
`[setCreateNodeLabels](#setCreateNodeLabels(boolean))(boolean shouldCreateNodeLabels)`

`void`
`[setPlaceEdgeLabelsTo](#setPlaceEdgeLabelsTo(int))(int placeEdgeLabelsTo)`
Sets the calculated label placement for labels.
`void`
`[setPlaceNodeLabels](#setPlaceNodeLabels(boolean))(boolean shouldPlaceNodeLabelsToCalculatedPositions)`

`boolean`
`[shouldCreateNodeLabels](#shouldCreateNodeLabels())()`

`boolean`
`[shouldPlaceNodeLabels](#shouldPlaceNodeLabels())()`
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
BaseGraph
@OpenApipublic BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Construct a graph with given parameter
Parameters:
`diagramView` - diagram for which to construct graph.
`selected` - selected elements
BaseGraph
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApipublic BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Deprecated.
supportsSubgraph has no effect
BaseGraph
@OpenApipublic BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
BaseGraph
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApipublic BaseGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
Deprecated.
supportsSubgraph has no effect
 ============ METHOD DETAIL ========== 
Method Details
initializeData
@OpenApipublic void initializeData()
Collects all data provided by diagram to nodes and edges.
setPlaceEdgeLabelsTo
@OpenApipublic void setPlaceEdgeLabelsTo(int placeEdgeLabelsTo)
Sets the calculated label placement for labels. Labels can be created for consideration only, but not placed at the calculated location.
 One of EDGE_LABEL_NONE, EDGE_LABEL_AT_ENDS, EDGE_LABEL_NON_ENDS , EDGE_LABEL_ALL.
 EDGE_LABEL_ALL by default.
Parameters:
`placeEdgeLabelsTo` - the edge placement mode
getPlaceEdgeLabelsPositions
@OpenApipublic int getPlaceEdgeLabelsPositions()
Returns:
the edge placement mode
setCreateEdgeLabels
@OpenApipublic void setCreateEdgeLabels(int createEdgeLabels)
Sets the label creation mode. One of EDGE_LABEL_NONE, EDGE_LABEL_AT_ENDS, EDGE_LABEL_NON_ENDS , EDGE_LABEL_ALL.
 EDGE_LABEL_ALL by default.
Parameters:
`createEdgeLabels` - edge placement mode
getCreateEdgeLabels
@OpenApipublic int getCreateEdgeLabels()
Returns:
the edge creation mode
setPlaceNodeLabels
@OpenApipublic void setPlaceNodeLabels(boolean shouldPlaceNodeLabelsToCalculatedPositions)
Parameters:
`shouldPlaceNodeLabelsToCalculatedPositions` - determines if node labels should be placed at the calculated graph position
shouldPlaceNodeLabels
@OpenApipublic boolean shouldPlaceNodeLabels()
Returns:
true if node labels should be set at the calculated position, false for the default position
setCreateNodeLabels
@OpenApipublic void setCreateNodeLabels(boolean shouldCreateNodeLabels)
Parameters:
`shouldCreateNodeLabels` - determines if node labels should be created and considered by the graph
shouldCreateNodeLabels
@OpenApipublic boolean shouldCreateNodeLabels()
Returns:
the node label creation mode

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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BaseGraph</span>
<span class="extends-implements">extends y.layout.DefaultLayoutGraph</span></div>
<div class="block">UML graph data.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
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
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block">Construct a graph with given parameter</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">BaseGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreateEdgeLabels()">getCreateEdgeLabels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPlaceEdgeLabelsPositions()">getPlaceEdgeLabelsPositions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#initializeData()">initializeData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all data provided by diagram to nodes and edges.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateEdgeLabels(int)">setCreateEdgeLabels</a><wbr/>(int createEdgeLabels)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the label creation mode.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCreateNodeLabels(boolean)">setCreateNodeLabels</a><wbr/>(boolean shouldCreateNodeLabels)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPlaceEdgeLabelsTo(int)">setPlaceEdgeLabelsTo</a><wbr/>(int placeEdgeLabelsTo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the calculated label placement for labels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPlaceNodeLabels(boolean)">setPlaceNodeLabels</a><wbr/>(boolean shouldPlaceNodeLabelsToCalculatedPositions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shouldCreateNodeLabels()">shouldCreateNodeLabels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#shouldPlaceNodeLabels()">shouldPlaceNodeLabels</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
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
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">
<h3>BaseGraph</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">BaseGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">initializeData</span>()</div>
<div class="block">Collects all data provided by diagram to nodes and edges.</div>
</section>
</li>
<li>
<section class="detail" id="setPlaceEdgeLabelsTo(int)">
<h3>setPlaceEdgeLabelsTo</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPlaceEdgeLabelsTo</span><wbr/><span class="parameters">(int placeEdgeLabelsTo)</span></div>
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
</span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPlaceEdgeLabelsPositions</span>()</div>
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateEdgeLabels</span><wbr/><span class="parameters">(int createEdgeLabels)</span></div>
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
</span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getCreateEdgeLabels</span>()</div>
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPlaceNodeLabels</span><wbr/><span class="parameters">(boolean shouldPlaceNodeLabelsToCalculatedPositions)</span></div>
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
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">shouldPlaceNodeLabels</span>()</div>
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCreateNodeLabels</span><wbr/><span class="parameters">(boolean shouldCreateNodeLabels)</span></div>
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
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">shouldCreateNodeLabels</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the node label creation mode</dd>
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
