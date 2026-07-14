# JAVA OPENAPI: PresentationElementRendererProvider (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/PresentationElementRendererProvider.html
- source_path: `com/nomagic/magicdraw/uml/symbols/PresentationElementRendererProvider.html`
- source_sha256: `eba247b10436d418b73bfd96ff2451707211e8dc116cdcf94a1db729bd3d1573`
- captured_utc: `2026-07-14T16:46:06.320884+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Interface PresentationElementRendererProvider

@OpenApiAllpublic interfacePresentationElementRendererProvider
Provides the presentation element renderer.
 Provider should be registered with the [`PresentationElementRendererManager`](PresentationElementRendererManager.html).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`[PresentationElementRenderer](PresentationElementRenderer.html)`
`[getRenderer](#getRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](PresentationElement.html) presentationElement)`
Returns a renderer for given presentation element.
`default boolean`
`[isForUMLProjectOnly](#isForUMLProjectOnly())()`

============ METHOD DETAIL ========== 
Method Details
getRenderer
@CheckForNull[PresentationElementRenderer](PresentationElementRenderer.html) getRenderer([PresentationElement](PresentationElement.html) presentationElement)
Returns a renderer for given presentation element.
Parameters:
`presentationElement` - presentation element to render.
Returns:
presentation element renderer, that customizes the presentation element.
isForUMLProjectOnly
default boolean isForUMLProjectOnly()
Returns:
true if this provider is for a UML based project only.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Interface PresentationElementRendererProvider">Interface PresentationElementRendererProvider</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PresentationElementRendererProvider</span></div>
<div class="block">Provides the presentation element renderer.
 Provider should be registered with the <a href="PresentationElementRendererManager.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElementRendererManager</code></a>.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getRenderer</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a renderer for given presentation element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isForUMLProjectOnly()">isForUMLProjectOnly</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
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
<section class="detail" id="getRenderer(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getRenderer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="PresentationElementRenderer.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElementRenderer</a></span> <span class="element-name">getRenderer</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement)</span></div>
<div class="block">Returns a renderer for given presentation element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - presentation element to render.</dd>
<dt>Returns:</dt>
<dd>presentation element renderer, that customizes the presentation element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isForUMLProjectOnly()">
<h3>isForUMLProjectOnly</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isForUMLProjectOnly</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this provider is for a UML based project only.</dd>
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
