# JAVA OPENAPI: BrowserAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/actions/BrowserAction.html
- source_path: `com/nomagic/magicdraw/actions/BrowserAction.html`
- source_sha256: `520c6bde3757df75d6b3457cbd38d3d759ef6f5fc16b1a9b912b66db62ac04c3`
- captured_utc: `2026-07-14T16:50:59.582915+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Interface BrowserAction

All Known Implementing Classes:
`[DefaultBrowserAction](../ui/browser/actions/DefaultBrowserAction.html)`, `[DefaultBrowserStateAction](../ui/browser/actions/DefaultBrowserStateAction.html)`

@OpenApiAllpublic interfaceBrowserAction

The interface for all browser actions.
 Browser action is used in browser tree and can use selected nodes from tree.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[setTree](#setTree(com.nomagic.magicdraw.ui.browser.Tree))([Tree](../ui/browser/Tree.html) tree)`
Set tree for this action.

============ METHOD DETAIL ========== 
Method Details
setTree
void setTree(@CheckForNull
 [Tree](../ui/browser/Tree.html) tree)
Set tree for this action.
 MagicDraw will set specific browser for configured actions in browser.
 You do not need to call this method explicitly by yourself.
Parameters:
`tree` - the specific instance of tree.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Interface BrowserAction">Interface BrowserAction</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../ui/browser/actions/DefaultBrowserAction.html" title="class in com.nomagic.magicdraw.ui.browser.actions">DefaultBrowserAction</a></code>, <code><a href="../ui/browser/actions/DefaultBrowserStateAction.html" title="class in com.nomagic.magicdraw.ui.browser.actions">DefaultBrowserStateAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BrowserAction</span></div>
<div class="block">The interface for all browser actions.
 Browser action is used in browser tree and can use selected nodes from tree.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTree(com.nomagic.magicdraw.ui.browser.Tree)">setTree</a><wbr/>(<a href="../ui/browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set tree for this action.</div>
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
<section class="detail" id="setTree(com.nomagic.magicdraw.ui.browser.Tree)">
<h3>setTree</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTree</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../ui/browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
<div class="block">Set tree for this action.
 MagicDraw will set specific browser for configured actions in browser.
 You do not need to call this method explicitly by yourself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tree</code> - the specific instance of tree.</dd>
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
