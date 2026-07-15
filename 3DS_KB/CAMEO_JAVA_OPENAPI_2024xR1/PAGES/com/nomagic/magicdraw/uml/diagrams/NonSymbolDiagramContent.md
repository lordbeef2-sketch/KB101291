# JAVA OPENAPI: NonSymbolDiagramContent (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/diagrams/NonSymbolDiagramContent.html
- source_path: `com/nomagic/magicdraw/uml/diagrams/NonSymbolDiagramContent.html`
- source_sha256: `5d6621d7a5bdab92859fff1d363b35465267ac7446e1caa1bb5b7fd7b0314feb`
- captured_utc: `2026-07-14T16:52:08.409831+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.diagrams](package-summary.html)

## Interface NonSymbolDiagramContent<C extends [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)>

@OpenApiAllpublic interfaceNonSymbolDiagramContent<C extends [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)>
Non symbol diagram content.
 There are three situations when this content is created:
 Diagram is shown
Diagram is printed
Diagram is saved to image

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[activate](#activate())()`
Activate component.
`[C](NonSymbolDiagramContent.html)`
`[createComponent](#createComponent())()`
Create content component.
`void`
`[dispose](#dispose())()`
Dispose component.
`[Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html)`
`[getComponentFullSize](#getComponentFullSize(C))([C](NonSymbolDiagramContent.html) component)`
Get component full size - used when preparing to print/save diagram to image.
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getPaintableBounds](#getPaintableBounds(C))([C](NonSymbolDiagramContent.html) component)`
Get component paintable bounds - bounds used to print/save diagram to the image.

============ METHOD DETAIL ========== 
Method Details
createComponent
[C](NonSymbolDiagramContent.html) createComponent()
Create content component.
Returns:
content component.
activate
void activate()
Activate component.
 Method implementation must initialize the component if it is not initialized yet.
dispose
void dispose()
Dispose component.
getComponentFullSize
[Dimension](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html) getComponentFullSize([C](NonSymbolDiagramContent.html) component)
Get component full size - used when preparing to print/save diagram to image.
Parameters:
`component` - component.
Returns:
component full size.
getPaintableBounds
[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getPaintableBounds([C](NonSymbolDiagramContent.html) component)
Get component paintable bounds - bounds used to print/save diagram to the image.
Parameters:
`component` - component.
Returns:
bounds to paint/print.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.diagrams</a></div>
<h1 class="title" title="Interface NonSymbolDiagramContent">Interface NonSymbolDiagramContent&lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a>&gt;</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">NonSymbolDiagramContent&lt;C extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a>&gt;</span></div>
<div class="block">Non symbol diagram content.
 There are three situations when this content is created:
 <ul>
<li>Diagram is shown</li>
<li>Diagram is printed</li>
<li>Diagram is saved to image</li>
</ul></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#activate()">activate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Activate component.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="NonSymbolDiagramContent.html" title="type parameter in NonSymbolDiagramContent">C</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createComponent()">createComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create content component.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Dispose component.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getComponentFullSize(C)">getComponentFullSize</a><wbr/>(<a href="NonSymbolDiagramContent.html" title="type parameter in NonSymbolDiagramContent">C</a> component)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get component full size - used when preparing to print/save diagram to image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPaintableBounds(C)">getPaintableBounds</a><wbr/>(<a href="NonSymbolDiagramContent.html" title="type parameter in NonSymbolDiagramContent">C</a> component)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get component paintable bounds - bounds used to print/save diagram to the image.</div>
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
<section class="detail" id="createComponent()">
<h3>createComponent</h3>
<div class="member-signature"><span class="return-type"><a href="NonSymbolDiagramContent.html" title="type parameter in NonSymbolDiagramContent">C</a></span> <span class="element-name">createComponent</span>()</div>
<div class="block">Create content component.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>content component.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activate()">
<h3>activate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">activate</span>()</div>
<div class="block">Activate component.
 Method implementation must initialize the component if it is not initialized yet.</div>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Dispose component.</div>
</section>
</li>
<li>
<section class="detail" id="getComponentFullSize(C)">
<h3 id="getComponentFullSize(java.awt.Component)">getComponentFullSize</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Dimension.html" title="class or interface in java.awt">Dimension</a></span> <span class="element-name">getComponentFullSize</span><wbr/><span class="parameters">(<a href="NonSymbolDiagramContent.html" title="type parameter in NonSymbolDiagramContent">C</a> component)</span></div>
<div class="block">Get component full size - used when preparing to print/save diagram to image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>component</code> - component.</dd>
<dt>Returns:</dt>
<dd>component full size.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPaintableBounds(C)">
<h3 id="getPaintableBounds(java.awt.Component)">getPaintableBounds</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getPaintableBounds</span><wbr/><span class="parameters">(<a href="NonSymbolDiagramContent.html" title="type parameter in NonSymbolDiagramContent">C</a> component)</span></div>
<div class="block">Get component paintable bounds - bounds used to print/save diagram to the image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>component</code> - component.</dd>
<dt>Returns:</dt>
<dd>bounds to paint/print.</dd>
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
