# JAVA OPENAPI: DiagramAction (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/actions/DiagramAction.html
- source_path: `com/nomagic/magicdraw/actions/DiagramAction.html`
- source_sha256: `59dd79fbdcfb8772b3c9687742256d9fcc04c967035ee1b2446bf83ea68ab0c0`
- captured_utc: `2026-07-14T16:45:07.442102+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Interface DiagramAction

All Known Implementing Classes:
`[DefaultActiveDiagramAction](../ui/actions/DefaultActiveDiagramAction.html)`, `[DefaultDiagramAction](../ui/actions/DefaultDiagramAction.html)`, `[DefaultDiagramStateAction](../ui/actions/DefaultDiagramStateAction.html)`, `[DefaultDiagramTriStateAction](../ui/actions/DefaultDiagramTriStateAction.html)`, `[DiagramContextToolbarAction](../ui/actions/DiagramContextToolbarAction.html)`

@OpenApiAllpublic interfaceDiagramAction

The interface for diagram actions.
 Diagram action works with elements in diagram.
 Every diagram action must have ability to set diagram.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[setDiagram](#setDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement))([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram)`
Sets diagram for action.

============ METHOD DETAIL ========== 
Method Details
setDiagram
void setDiagram(@CheckForNull
 [DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram)
Sets diagram for action.
Parameters:
`diagram` - the given diagram.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Interface DiagramAction">Interface DiagramAction</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../ui/actions/DefaultActiveDiagramAction.html" title="class in com.nomagic.magicdraw.ui.actions">DefaultActiveDiagramAction</a></code>, <code><a href="../ui/actions/DefaultDiagramAction.html" title="class in com.nomagic.magicdraw.ui.actions">DefaultDiagramAction</a></code>, <code><a href="../ui/actions/DefaultDiagramStateAction.html" title="class in com.nomagic.magicdraw.ui.actions">DefaultDiagramStateAction</a></code>, <code><a href="../ui/actions/DefaultDiagramTriStateAction.html" title="class in com.nomagic.magicdraw.ui.actions">DefaultDiagramTriStateAction</a></code>, <code><a href="../ui/actions/DiagramContextToolbarAction.html" title="class in com.nomagic.magicdraw.ui.actions">DiagramContextToolbarAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramAction</span></div>
<div class="block">The interface for diagram actions.
 Diagram action works with elements in diagram.
 Every diagram action must have ability to set diagram.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">setDiagram</a><wbr/>(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets diagram for  action.</div>
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
<section class="detail" id="setDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement)">
<h3>setDiagram</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDiagram</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram)</span></div>
<div class="block">Sets diagram for  action.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the given diagram.</dd>
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
