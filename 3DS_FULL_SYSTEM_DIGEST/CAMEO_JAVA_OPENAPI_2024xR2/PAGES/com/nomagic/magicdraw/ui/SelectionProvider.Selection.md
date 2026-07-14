# JAVA OPENAPI: SelectionProvider.Selection (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ui/SelectionProvider.Selection.html
- source_path: `com/nomagic/magicdraw/ui/SelectionProvider.Selection.html`
- source_sha256: `1f36c4fa7f67fbbb27468bdb6df6bad54060165e168d46719ffad3fade83c9a0`
- captured_utc: `2026-07-14T16:55:48.342377+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Interface SelectionProvider.Selection

Enclosing class:
[SelectionProvider](SelectionProvider.html)

@OpenApiAllpublic static interfaceSelectionProvider.Selection

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`[BaseElement](../uml/BaseElement.html)`
`[getMainElement](#getMainElement())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)>`
`[getSelected](#getSelected())()`

`default [BaseElement](../uml/BaseElement.html)`
`[getSelectedOrMainElement](#getSelectedOrMainElement())()`

`int`
`[getSize](#getSize())()`

============ METHOD DETAIL ========== 
Method Details
getSize
int getSize()
Returns:
number of selected elements
getSelected
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> getSelected()
Returns:
selected elements
getMainElement
@CheckForNull[BaseElement](../uml/BaseElement.html) getMainElement()
Returns:
main selected element
getSelectedOrMainElement
@CheckForNulldefault [BaseElement](../uml/BaseElement.html) getSelectedOrMainElement()
Returns:
selected element if only one element is selected or main element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Interface SelectionProvider.Selection">Interface SelectionProvider.Selection</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="SelectionProvider.html" title="class in com.nomagic.magicdraw.ui">SelectionProvider</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">SelectionProvider.Selection</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMainElement()">getMainElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSelected()">getSelected</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getSelectedOrMainElement()">getSelectedOrMainElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSize()">getSize</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getSize()">
<h3>getSize</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getSize</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>number of selected elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelected()">
<h3>getSelected</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getSelected</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>selected elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainElement()">
<h3>getMainElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getMainElement</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>main selected element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedOrMainElement()">
<h3>getSelectedOrMainElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a></span> <span class="element-name">getSelectedOrMainElement</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>selected element if only one element is selected or main element</dd>
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
