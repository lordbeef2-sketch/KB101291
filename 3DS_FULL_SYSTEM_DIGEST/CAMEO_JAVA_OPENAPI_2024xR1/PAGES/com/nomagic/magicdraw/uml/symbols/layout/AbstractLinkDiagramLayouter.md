# JAVA OPENAPI: AbstractLinkDiagramLayouter (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/symbols/layout/AbstractLinkDiagramLayouter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/AbstractLinkDiagramLayouter.html`
- source_sha256: `40c2f1e35a9b95d97e5847512bb7df7fdd1581624285c31431f86f7b44a9853c`
- captured_utc: `2026-07-14T16:52:10.841863+00:00`

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

@OpenApipublic abstract classAbstractLinkDiagramLayouter
extends [AbstractDiagramLayouter](AbstractDiagramLayouter.html)

Layout the diagram symbols in diagram.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractLinkDiagramLayouter](#%3Cinit%3E(java.lang.String,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths)`
Construct AbstractLinkDiagramLayouter with the given argument.
`[AbstractLinkDiagramLayouter](#%3Cinit%3E(java.lang.String,boolean,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)`
Deprecated.
supportsSubgraph has no effect
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [BaseGraph](BaseGraph.html)`
`[createGraph](#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) optionsGroup)`
Constructs a graph for layout
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)>`
`[getSelected](#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView)`
Collects a set of selected layoutable presentation elements in a diagram
Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.[AbstractDiagramLayouter](AbstractDiagramLayouter.html)
`[isTypeSupported](AbstractDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)), [layout](AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractLinkDiagramLayouter
@OpenApipublic AbstractLinkDiagramLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths)
Construct AbstractLinkDiagramLayouter with the given argument.
Parameters:
`optionId` - String.
`nodes` - boolean.
`paths` - boolean.
AbstractLinkDiagramLayouter
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public AbstractLinkDiagramLayouter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)
Deprecated.
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
@OpenApiprotected [BaseGraph](BaseGraph.html) createGraph([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) dpe,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) optionsGroup)
Constructs a graph for layout
Overrides:
`[createGraph](AbstractDiagramLayouter.html#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`dpe` - shapes and edges are taken from this diagram
`optionsGroup` - layouter options
Returns:
a created UMLGraph
getSelected
@OpenApipublic [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../PresentationElement.html)> getSelected([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagramView)
Description copied from class: `[AbstractDiagramLayouter](AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))`
Collects a set of selected layoutable presentation elements in a diagram
Overrides:
`[getSelected](AbstractDiagramLayouter.html#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))` in class `[AbstractDiagramLayouter](AbstractDiagramLayouter.html)`
Parameters:
`diagramView` - the diagram that elements were selected in
Returns:
the selected paths and any paths that are connected to selected shapes. Paths connected
 by other shape element on shape edge are also included

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
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractLinkDiagramLayouter</span>
<span class="extends-implements">extends <a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></span></div>
<div class="block">Layout the diagram symbols in diagram.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean,boolean)">AbstractLinkDiagramLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths)</code></div>
<div class="col-last even-row-color">
<div class="block">Construct AbstractLinkDiagramLayouter with the given argument.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean,boolean,boolean)">AbstractLinkDiagramLayouter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGraph(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">createGraph</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> optionsGroup)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Constructs a graph for layout</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">getSelected</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects a set of selected layoutable presentation elements in a diagram</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.layout.AbstractDiagramLayouter">Methods inherited from class com.nomagic.magicdraw.uml.symbols.layout.<a href="AbstractDiagramLayouter.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">AbstractDiagramLayouter</a></h3>
<code><a href="AbstractDiagramLayouter.html#isTypeSupported(com.nomagic.magicdraw.uml.AbstractDiagramType)">isTypeSupported</a>, <a href="AbstractDiagramLayouter.html#layout(com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.layout.BaseGraph)">layout</a></code></div>
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
</span><span class="modifiers">public</span> <span class="element-name">AbstractLinkDiagramLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths)</span></div>
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
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">AbstractLinkDiagramLayouter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionId,
 boolean nodes,
 boolean paths,
 boolean supportsSubgraph)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
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
</span><span class="modifiers">protected</span> <span class="return-type"><a href="BaseGraph.html" title="class in com.nomagic.magicdraw.uml.symbols.layout">BaseGraph</a></span> <span class="element-name">createGraph</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> dpe,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> optionsGroup)</span></div>
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
<section class="detail" id="getSelected(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>getSelected</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getSelected</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagramView)</span></div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
