# JAVA OPENAPI: DiagramLayouter (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/symbols/layout/DiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/DiagramLayouter.html`
- source_sha256: `8c540939768a4b4d183c42d11ef9dbf641f7dfbcfd98c0f6769c33fef158a196`
- captured_utc: `2026-07-14T16:52:10.926866+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Interface DiagramLayouter

All Known Implementing Classes:
`[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`, `[AbstractHierarchicDiagramLayouter](AbstractHierarchicDiagramLayouter.html)`, `[AbstractLinkDiagramLayouter](AbstractLinkDiagramLayouter.html)`, `[ActivityDiagramLayouter](activity/ActivityDiagramLayouter.html)`, `[BusinessProcessDiagramLayouter](BusinessProcessDiagramLayouter.html)`, `[CircularDiagramLayouter](CircularDiagramLayouter.html)`, `[ClassDiagramLayouter](ClassDiagramLayouter.html)`, `[CompositeStructureDiagramLayouter](composite/CompositeStructureDiagramLayouter.html)`, `[GridDiagramLayouter](grid/GridDiagramLayouter.html)`, `[HierarchicDiagramLayouter](HierarchicDiagramLayouter.html)`, `[OrderedHierarchicDiagramLayouter](orderedhier/OrderedHierarchicDiagramLayouter.html)`, `[OrganicDiagramLayouter](OrganicDiagramLayouter.html)`, `[OrganicLinkDiagramLayouter](OrganicLinkDiagramLayouter.html)`, `[OrthogonalDiagramLayouter](OrthogonalDiagramLayouter.html)`, `[OrthogonalLinkDiagramLayouter](OrthogonalLinkDiagramLayouter.html)`, `[StateDiagramLayouter](state/StateDiagramLayouter.html)`, `[SysML2DiagramLayouter](sysml2/SysML2DiagramLayouter.html)`, `[TreeDiagramLayouter](TreeDiagramLayouter.html)`

@OpenApipublic interfaceDiagramLayouter

Layout diagram symbols in diagram.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[canLayout](#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)`
Checks is diagram can be layouted
`void`
`[drawLayoutResults](#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([BaseGraph](BaseGraph.html) graph)`
Draws layout results
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOptionsID](#getOptionsID())()`

============ METHOD DETAIL ========== 
Method Details
canLayout
@OpenApiboolean canLayout([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe)
Checks is diagram can be layouted
Parameters:
`dpe` - diagram to layout
Returns:
true if it can be layouted, false otherwise
drawLayoutResults
@OpenApivoid drawLayoutResults([BaseGraph](BaseGraph.html) graph)
Draws layout results
Parameters:
`graph` - current graph that is layouted
getOptionsID
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOptionsID()
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
<dd><code><a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></code>, <code><a href="AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></code>, <code><a href="AbstractLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractLinkDiagramLayouter</a></code>, <code><a href="activity/ActivityDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.activity">ActivityDiagramLayouter</a></code>, <code><a href="BusinessProcessDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BusinessProcessDiagramLayouter</a></code>, <code><a href="CircularDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">CircularDiagramLayouter</a></code>, <code><a href="ClassDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">ClassDiagramLayouter</a></code>, <code><a href="composite/CompositeStructureDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.composite">CompositeStructureDiagramLayouter</a></code>, <code><a href="grid/GridDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.grid">GridDiagramLayouter</a></code>, <code><a href="HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">HierarchicDiagramLayouter</a></code>, <code><a href="orderedhier/OrderedHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.orderedhier">OrderedHierarchicDiagramLayouter</a></code>, <code><a href="OrganicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrganicDiagramLayouter</a></code>, <code><a href="OrganicLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrganicLinkDiagramLayouter</a></code>, <code><a href="OrthogonalDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrthogonalDiagramLayouter</a></code>, <code><a href="OrthogonalLinkDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">OrthogonalLinkDiagramLayouter</a></code>, <code><a href="state/StateDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.state">StateDiagramLayouter</a></code>, <code><a href="sysml2/SysML2DiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout.sysml2">SysML2DiagramLayouter</a></code>, <code><a href="TreeDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">TreeDiagramLayouter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramLayouter</span></div>
<div class="block">Layout diagram symbols in diagram.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">canLayout</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks is diagram can be layouted</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#drawLayoutResults(com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">drawLayoutResults</a><wbr/>(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Draws layout results</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOptionsID()">getOptionsID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="canLayout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>canLayout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">canLayout</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe)</span></div>
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
</span><span class="return-type">void</span> <span class="element-name">drawLayoutResults</span><wbr/><span class="parameters">(<a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
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
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOptionsID</span>()</div>
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
