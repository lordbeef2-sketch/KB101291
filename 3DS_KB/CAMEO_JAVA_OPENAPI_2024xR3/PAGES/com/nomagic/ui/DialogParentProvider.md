# JAVA OPENAPI: DialogParentProvider (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/ui/DialogParentProvider.html
- source_path: `com/nomagic/ui/DialogParentProvider.html`
- source_sha256: `752c846bff49101859d267aecfb53ce9775b22ce74452356e84591be0fe450f7`
- captured_utc: `2026-07-14T16:56:09.790621+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Interface DialogParentProvider

All Known Implementing Classes:
`[MDDialogParentProvider](../magicdraw/ui/dialogs/MDDialogParentProvider.html)`

@OpenApiAllpublic interfaceDialogParentProvider

Dialog parent provider

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)`
`[getDialogOwner](#getDialogOwner())()`
Returns owner window(dialog or frame) for dialogs
`[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html)`
`[getDialogOwner](#getDialogOwner(java.awt.Component))([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) invoker)`
Returns parent window(dialog or frame) for a dialog which will be invoked by given component
`[Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html)`
`[getDialogParent](#getDialogParent())()`
Deprecated.
use [`getDialogOwner()`](#getDialogOwner()).

============ METHOD DETAIL ========== 
Method Details
getDialogParent
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)[Frame](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html) getDialogParent()
Deprecated.
use [`getDialogOwner()`](#getDialogOwner()). Frame is not always a good choice to pass as parent. Parent sometimes should be another dialog, not just a frame.
Returns parent frame for dialogs.
Returns:
parent
getDialogOwner
[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) getDialogOwner()
Returns owner window(dialog or frame) for dialogs
Returns:
owner window
getDialogOwner
[Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) getDialogOwner([Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) invoker)
Returns parent window(dialog or frame) for a dialog which will be invoked by given component
Parameters:
`invoker` - invoker component
Returns:
owner window of invoker component

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Interface DialogParentProvider">Interface DialogParentProvider</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../magicdraw/ui/dialogs/MDDialogParentProvider.html" title="class in com.nomagic.magicdraw.ui.dialogs">MDDialogParentProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DialogParentProvider</span></div>
<div class="block">Dialog parent provider</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDialogOwner()">getDialogOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns owner window(dialog or frame) for dialogs</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDialogOwner(java.awt.Component)">getDialogOwner</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> invoker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns parent window(dialog or frame) for a dialog which will be invoked by given component</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getDialogParent()">getDialogParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getDialogOwner()"><code>getDialogOwner()</code></a>.</div>
</div>
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
<section class="detail" id="getDialogParent()">
<h3>getDialogParent</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Frame.html" title="class or interface in java.awt">Frame</a></span> <span class="element-name">getDialogParent</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getDialogOwner()"><code>getDialogOwner()</code></a>. Frame is not always a good choice to pass as parent. Parent sometimes should be another dialog, not just a frame.</div>
</div>
<div class="block">Returns parent frame for dialogs.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDialogOwner()">
<h3>getDialogOwner</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></span> <span class="element-name">getDialogOwner</span>()</div>
<div class="block">Returns owner window(dialog or frame) for dialogs</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>owner window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDialogOwner(java.awt.Component)">
<h3>getDialogOwner</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a></span> <span class="element-name">getDialogOwner</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> invoker)</span></div>
<div class="block">Returns parent window(dialog or frame) for a dialog which will be invoked by given component</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>invoker</code> - invoker component</dd>
<dt>Returns:</dt>
<dd>owner window of invoker component</dd>
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
