# JAVA OPENAPI: WindowComponentContent (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ui/browser/WindowComponentContent.html
- source_path: `com/nomagic/magicdraw/ui/browser/WindowComponentContent.html`
- source_sha256: `835b06b7397c25d02e0ed4dabbdfc46727f4302907b4e87c2658364402faefa0`
- captured_utc: `2026-07-14T16:55:49.319390+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.browser](package-summary.html)

## Interface WindowComponentContent

@OpenApiAllpublic interfaceWindowComponentContent
The contents of the window component. Provides the real GUI component that is added to the window component.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)`
`[getDefaultFocusComponent](#getDefaultFocusComponent())()`
Returns the component which by default will get the focus.
`[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html)`
`[getWindowComponent](#getWindowComponent())()`
Returns the window content component.

============ METHOD DETAIL ========== 
Method Details
getWindowComponent
[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) getWindowComponent()
Returns the window content component. The returned component is shown in the window.
Returns:
component to show in the window.
getDefaultFocusComponent
@CheckForNull[Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) getDefaultFocusComponent()
Returns the component which by default will get the focus.
Returns:
component to get the focus.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.browser</a></div>
<h1 class="title" title="Interface WindowComponentContent">Interface WindowComponentContent</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">WindowComponentContent</span></div>
<div class="block">The contents of the window component. Provides the real GUI component that is added to the window component.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultFocusComponent()">getDefaultFocusComponent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the component which by default will get the focus.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWindowComponent()">getWindowComponent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the window content component.</div>
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
<section class="detail" id="getWindowComponent()">
<h3>getWindowComponent</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">getWindowComponent</span>()</div>
<div class="block">Returns the window content component. The returned component is shown in the window.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>component to show in the window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultFocusComponent()">
<h3>getDefaultFocusComponent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a></span> <span class="element-name">getDefaultFocusComponent</span>()</div>
<div class="block">Returns the component which by default will get the focus.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>component to get the focus.</dd>
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
