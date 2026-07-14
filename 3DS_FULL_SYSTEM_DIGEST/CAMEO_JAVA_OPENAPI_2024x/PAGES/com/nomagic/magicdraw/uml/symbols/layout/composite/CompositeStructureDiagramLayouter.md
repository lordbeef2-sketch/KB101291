# JAVA OPENAPI: CompositeStructureDiagramLayouter (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/layout/composite/CompositeStructureDiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/composite/CompositeStructureDiagramLayouter.html`
- source_sha256: `45e4f363b90a8320390ee49094329bad5d1e0800e194c858511320b1fa1e1cdb`
- captured_utc: `2026-07-14T16:52:12.404885+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout.composite](package-summary.html)

## Class CompositeStructureDiagramLayouter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter](../AbstractDiagramLayouter.html)
[com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter](../AbstractHierarchicDiagramLayouter.html)
[com.nomagic.magicdraw.uml.symbols.layout.HierarchicDiagramLayouter](../HierarchicDiagramLayouter.html)
com.nomagic.magicdraw.uml.symbols.layout.composite.CompositeStructureDiagramLayouter

All Implemented Interfaces:
`[DiagramLayouter](../DiagramLayouter.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ClassDiagramLayouter](../ClassDiagramLayouter.html)`

@OpenApipublic classCompositeStructureDiagramLayouter
extends [HierarchicDiagramLayouter](../HierarchicDiagramLayouter.html)

Specialized layouter for composite diagram. It is used as a default layouter for composite
 structure diagrams and diagrams based on it.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CompositeStructureDiagramLayouter](#%3Cinit%3E())()`

`[CompositeStructureDiagramLayouter](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId)`
Construct Composite layouter
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected boolean`
`[layout](#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))([AbstractDiagramLayouterOptionsGroup](../../../../core/options/AbstractDiagramLayouterOptionsGroup.html) opt,
 [AbstractDiagramPresentationElement](../../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](../BaseGraph.html) graph)`
Layouts a diagram
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](../AbstractDiagramLayouter.html)
`[createGraph](../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)), [getSelected](../AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CompositeStructureDiagramLayouter
@OpenApipublic CompositeStructureDiagramLayouter()
CompositeStructureDiagramLayouter
@OpenApipublic CompositeStructureDiagramLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId)
Construct Composite layouter
Parameters:
`optionId` - activity diagram layouter options id
 ============ METHOD DETAIL ========== 
Method Details
layout
@OpenApiprotected boolean layout([AbstractDiagramLayouterOptionsGroup](../../../../core/options/AbstractDiagramLayouterOptionsGroup.html) opt,
 [AbstractDiagramPresentationElement](../../AbstractDiagramPresentationElement.html) dpe,
 [BaseGraph](../BaseGraph.html) graph)
Description copied from class: `[AbstractDiagramLayouter](../AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))`
Layouts a diagram
Overrides:
`[layout](../AbstractHierarchicDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))` in class `[AbstractHierarchicDiagramLayouter](../AbstractHierarchicDiagramLayouter.html)`
Parameters:
`opt` - layouter options
`dpe` - diagram to layout
`graph` - a constructed graph from the diagram
Returns:
true if it was layouted successfully , false otherwise.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout.composite</a></div>
<h1 class="title" title="Class CompositeStructureDiagramLayouter">Class CompositeStructureDiagramLayouter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter</a>
<div class="inheritance"><a href="../AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.AbstractHierarchicDiagramLayouter</a>
<div class="inheritance"><a href="../HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">com.nomagic.magicdraw.uml.symbols.layout.HierarchicDiagramLayouter</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.composite.CompositeStructureDiagramLayouter</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../DiagramLayouter.html" title="interface in com.nomagic.magicdraw.uml.symbols.layout">DiagramLayouter</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../ClassDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">ClassDiagramLayouter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CompositeStructureDiagramLayouter</span>
<span class="extends-implements">extends <a href="../HierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">HierarchicDiagramLayouter</a></span></div>
<div class="block">Specialized layouter for composite diagram. It is used as a default layouter for composite
 structure diagrams and diagrams based on it.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CompositeStructureDiagramLayouter</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">CompositeStructureDiagramLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId)</code></div>
<div class="col-last odd-row-color">
<div class="block">Construct Composite layouter</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a><wbr/>(<a href="../../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> opt,
 <a href="../../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Layouts a diagram</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="../AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="../AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">createGraph</a>, <a href="../AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getSelected</a></code></div>
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
<h3>CompositeStructureDiagramLayouter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">CompositeStructureDiagramLayouter</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>CompositeStructureDiagramLayouter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">CompositeStructureDiagramLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId)</span></div>
<div class="block">Construct Composite layouter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>optionId</code> - activity diagram layouter options id</dd>
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
<section class="detail" id="layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">
<h3>layout</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> opt,
 <a href="../../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a> graph)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">AbstractDiagramLayouter</a></code></span></div>
<div class="block">Layouts a diagram</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../AbstractHierarchicDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a></code> in class <code><a href="../AbstractHierarchicDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractHierarchicDiagramLayouter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>opt</code> - layouter options</dd>
<dd><code>dpe</code> - diagram to layout</dd>
<dd><code>graph</code> - a constructed graph from the diagram</dd>
<dt>Returns:</dt>
<dd>true if it was layouted successfully , false otherwise.</dd>
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
