# JAVA OPENAPI: DiagramLayouter (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/DiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/DiagramLayouter.html`
- source_sha256: `9fb8e77c302ea6fb5bcca4b7658309bf17c2cb186c5258f240addbc6613bb6f1`
- captured_utc: `2026-07-14T16:55:57.846485+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Interface DiagramLayouter

All Known Implementing Classes:
`[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`, `[AbstractHierarchicDiagramLayouter](AbstractHierarchicDiagramLayouter.html)`, `[AbstractLinkDiagramLayouter](AbstractLinkDiagramLayouter.html)`, `[ActivityDiagramLayouter](activity/ActivityDiagramLayouter.html)`, `[BusinessProcessDiagramLayouter](BusinessProcessDiagramLayouter.html)`, `[CircularDiagramLayouter](CircularDiagramLayouter.html)`, `[ClassDiagramLayouter](ClassDiagramLayouter.html)`, `[CompositeStructureDiagramLayouter](composite/CompositeStructureDiagramLayouter.html)`, `[GridDiagramLayouter](grid/GridDiagramLayouter.html)`, `[HierarchicDiagramLayouter](HierarchicDiagramLayouter.html)`, `[OrderedHierarchicDiagramLayouter](orderedhier/OrderedHierarchicDiagramLayouter.html)`, `[OrganicDiagramLayouter](OrganicDiagramLayouter.html)`, `[OrganicLinkDiagramLayouter](OrganicLinkDiagramLayouter.html)`, `[OrthogonalDiagramLayouter](OrthogonalDiagramLayouter.html)`, `[OrthogonalLinkDiagramLayouter](OrthogonalLinkDiagramLayouter.html)`, `[StateDiagramLayouter](state/StateDiagramLayouter.html)`, `[TreeDiagramLayouter](TreeDiagramLayouter.html)`

@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public interfaceDiagramLayouter

Deprecated.
diagram layouting should be done using [`Layouting`](Layouting.html) class

Layout diagram symbols in diagram.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[canLayout](#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)`
Deprecated.
`void`
`[drawLayoutResults](#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([BaseGraph](BaseGraph.html) graph)`
Deprecated, for removal: This API element is subject to removal in a future version.
outdated, should not be used
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOptionsID](#getOptionsID())()`
Deprecated, for removal: This API element is subject to removal in a future version.
`boolean`
`[layout](#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand))([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)`
Deprecated, for removal: This API element is subject to removal in a future version.

============ METHOD DETAIL ========== 
Method Details
layout
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)boolean layout([AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) options,
 [AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)
Deprecated, for removal: This API element is subject to removal in a future version.
Layouts diagram.
Parameters:
`options` - defined layouter options
`dpe` - diagram
`mc` - macro command to add layouting to
Returns:
true if layout was a success, false otherwise
canLayout
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)boolean canLayout([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)
Deprecated.
Checks is diagram can be layouted
Parameters:
`dpe` - diagram to layout
Returns:
true if it can be layouted, false otherwise
drawLayoutResults
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)void drawLayoutResults([BaseGraph](BaseGraph.html) graph)
Deprecated, for removal: This API element is subject to removal in a future version.
outdated, should not be used
Draws layout results
Parameters:
`graph` - current graph that is layouted
getOptionsID
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2024x Refresh3",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOptionsID()
Deprecated, for removal: This API element is subject to removal in a future version.
Returns:
options ID

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Interface DiagramLayouter">Interface DiagramLayouter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code>, <code><a href="AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></code>, <code><a href="AbstractLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractLinkDiagramLayouter</a></code>, <code><a href="activity/ActivityDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.activity">ActivityDiagramLayouter</a></code>, <code><a href="BusinessProcessDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BusinessProcessDiagramLayouter</a></code>, <code><a href="CircularDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">CircularDiagramLayouter</a></code>, <code><a href="ClassDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">ClassDiagramLayouter</a></code>, <code><a href="composite/CompositeStructureDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.composite">CompositeStructureDiagramLayouter</a></code>, <code><a href="grid/GridDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.grid">GridDiagramLayouter</a></code>, <code><a href="HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">HierarchicDiagramLayouter</a></code>, <code><a href="orderedhier/OrderedHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.orderedhier">OrderedHierarchicDiagramLayouter</a></code>, <code><a href="OrganicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrganicDiagramLayouter</a></code>, <code><a href="OrganicLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrganicLinkDiagramLayouter</a></code>, <code><a href="OrthogonalDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrthogonalDiagramLayouter</a></code>, <code><a href="OrthogonalLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrthogonalLinkDiagramLayouter</a></code>, <code><a href="state/StateDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.state">StateDiagramLayouter</a></code>, <code><a href="TreeDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">TreeDiagramLayouter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramLayouter</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">diagram layouting should be done using <a href="Layouting.html" title="class in com.nomagic.magicdraw.uml.symbols.layout"><code>Layouting</code></a> class</div>
</div>
<div class="block">Layout diagram symbols in diagram.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">canLayout</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">drawLayoutResults</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">outdated, should not be used</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getOptionsID()">getOptionsID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">layout</a><wbr/>(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
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
<section class="detail" id="layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.dassault_systemes.modeler.foundation.editing.CompositeCommand)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> options,
 <a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 @CheckForNull
 com.dassault_systemes.modeler.foundation.editing.CompositeCommand mc)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
<div class="block">Layouts diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - defined layouter options</dd>
<dd><code>dpe</code> - diagram</dd>
<dd><code>mc</code> - macro command to add layouting to</dd>
<dt>Returns:</dt>
<dd>true if layout was a success, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>canLayout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">boolean</span> <span class="element-name">canLayout</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Checks is diagram can be layouted</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dpe</code> - diagram to layout</dd>
<dt>Returns:</dt>
<dd>true if it can be layouted, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>drawLayoutResults</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type">void</span> <span class="element-name">drawLayoutResults</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment">outdated, should not be used</div>
</div>
<div class="block">Draws layout results</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>graph</code> - current graph that is layouted</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptionsID()">
<h3>getOptionsID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2024x Refresh3",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOptionsID</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>options ID</dd>
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
