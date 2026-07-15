# JAVA OPENAPI: UMLGraph (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/layout/UMLGraph.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/UMLGraph.html`
- source_sha256: `f316978ce16fac5bfa2dfaecbe81859d99c15d73e142248a6fae73a7e11355ba`
- captured_utc: `2026-07-14T16:52:12.292883+00:00`

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

@OpenApipublic classUMLGraph
extends [BaseGraph](BaseGraph.html)

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
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Deprecated.
supportsSubgraph has no effect
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
Deprecated.
supportsSubgraph has no effect
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)`
Construct UML Graph.
`[UMLGraph](#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)`
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[BaseGraph](BaseGraph.html)
`[getCreateEdgeLabels](BaseGraph.html#getCreateEdgeLabels()), [getPlaceEdgeLabelsPositions](BaseGraph.html#getPlaceEdgeLabelsPositions()), [initializeData](BaseGraph.html#initializeData()), [setCreateEdgeLabels](BaseGraph.html#setCreateEdgeLabels(int)), [setCreateNodeLabels](BaseGraph.html#setCreateNodeLabels(boolean)), [setPlaceEdgeLabelsTo](BaseGraph.html#setPlaceEdgeLabelsTo(int)), [setPlaceNodeLabels](BaseGraph.html#setPlaceNodeLabels(boolean)), [shouldCreateNodeLabels](BaseGraph.html#shouldCreateNodeLabels()), [shouldPlaceNodeLabels](BaseGraph.html#shouldPlaceNodeLabels())`
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
@OpenApipublic UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Construct UML Graph. with given parameter
Parameters:
`diagramView` - diagram for which to construct graph.
`selected` - selected elements
UMLGraph
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApipublic UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected)
Deprecated.
supportsSubgraph has no effect
UMLGraph
@OpenApipublic UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
UMLGraph
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApipublic UMLGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView,
 boolean supportsSubgraph,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> selected,
 boolean resetLabelPositions)
Deprecated.
supportsSubgraph has no effect

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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">UMLGraph</span>
<span class="extends-implements">extends <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</code></div>
<div class="col-last even-row-color">
<div class="block">Construct UML Graph.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">UMLGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
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
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.BaseGraph">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></h3>
<code><a href="BaseGraph.html#getCreateEdgeLabels()">getCreateEdgeLabels</a>, <a href="BaseGraph.html#getPlaceEdgeLabelsPositions()">getPlaceEdgeLabelsPositions</a>, <a href="BaseGraph.html#initializeData()">initializeData</a>, <a href="BaseGraph.html#setCreateEdgeLabels(int)">setCreateEdgeLabels</a>, <a href="BaseGraph.html#setCreateNodeLabels(boolean)">setCreateNodeLabels</a>, <a href="BaseGraph.html#setPlaceEdgeLabelsTo(int)">setPlaceEdgeLabelsTo</a>, <a href="BaseGraph.html#setPlaceNodeLabels(boolean)">setPlaceNodeLabels</a>, <a href="BaseGraph.html#shouldCreateNodeLabels()">shouldCreateNodeLabels</a>, <a href="BaseGraph.html#shouldPlaceNodeLabels()">shouldPlaceNodeLabels</a></code></div>
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
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
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
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 boolean supportsSubgraph,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">supportsSubgraph has no effect</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.util.Set,boolean)">
<h3>UMLGraph</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; selected,
 boolean resetLabelPositions)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,boolean,java.util.Set,boolean)">
<h3>UMLGraph</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">UMLGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView,
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
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
