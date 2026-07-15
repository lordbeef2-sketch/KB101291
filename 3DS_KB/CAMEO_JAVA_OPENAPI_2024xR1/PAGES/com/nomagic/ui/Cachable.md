# JAVA OPENAPI: Cachable (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/ui/Cachable.html
- source_path: `com/nomagic/ui/Cachable.html`
- source_sha256: `4e0b3d25091fe4b387b6c89ef84fc410a8c3acddbce5127b94081a69c22be884`
- captured_utc: `2026-07-14T16:52:23.839037+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Interface Cachable

All Known Implementing Classes:
`com.nomagic.magicdraw.ui.dialogs.BaseDialog`, `[BrowserTabTree](../magicdraw/ui/browser/BrowserTabTree.html)`, `[ContainmentTree](../magicdraw/ui/browser/ContainmentTree.html)`, `[DiagramsTree](../magicdraw/ui/browser/DiagramsTree.html)`, `com.nomagic.ui.Dialog`, `[ElementSelectionDlg](../magicdraw/ui/dialogs/selection/ElementSelectionDlg.html)`, `[ExtensionsTree](../magicdraw/ui/browser/ExtensionsTree.html)`, `[InheritanceTree](../magicdraw/ui/browser/InheritanceTree.html)`, `[LockViewTree](../magicdraw/teamwork2/ui/LockViewTree.html)`, `[SearchResultsTree](../magicdraw/ui/browser/SearchResultsTree.html)`, `[SelectElementDlg](../magicdraw/ui/dialogs/SelectElementDlg.html)`, `com.nomagic.ui.SimpleBaseDialog`, `[Tree](../magicdraw/ui/browser/Tree.html)`

@OpenApiAllpublic interfaceCachable

Reusable objects used in caches. They are reset when object is returned to the cache.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[reset](#reset())()`
Cache managers invokes this method to free resources.

============ METHOD DETAIL ========== 
Method Details
reset
void reset()
Cache managers invokes this method to free resources. Usually this method must drop references to external objects
 in order to enable garbage collection of them.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Interface Cachable">Interface Cachable</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.nomagic.magicdraw.ui.dialogs.BaseDialog</code>, <code><a href="../magicdraw/ui/browser/BrowserTabTree.html" title="class in com.nomagic.magicdraw.ui.browser">BrowserTabTree</a></code>, <code><a href="../magicdraw/ui/browser/ContainmentTree.html" title="class in com.nomagic.magicdraw.ui.browser">ContainmentTree</a></code>, <code><a href="../magicdraw/ui/browser/DiagramsTree.html" title="class in com.nomagic.magicdraw.ui.browser">DiagramsTree</a></code>, <code>com.nomagic.ui.Dialog</code>, <code><a href="../magicdraw/ui/dialogs/selection/ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code>, <code><a href="../magicdraw/ui/browser/ExtensionsTree.html" title="class in com.nomagic.magicdraw.ui.browser">ExtensionsTree</a></code>, <code><a href="../magicdraw/ui/browser/InheritanceTree.html" title="class in com.nomagic.magicdraw.ui.browser">InheritanceTree</a></code>, <code><a href="../magicdraw/teamwork2/ui/LockViewTree.html" title="class in com.nomagic.magicdraw.teamwork2.ui">LockViewTree</a></code>, <code><a href="../magicdraw/ui/browser/SearchResultsTree.html" title="class in com.nomagic.magicdraw.ui.browser">SearchResultsTree</a></code>, <code><a href="../magicdraw/ui/dialogs/SelectElementDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementDlg</a></code>, <code>com.nomagic.ui.SimpleBaseDialog</code>, <code><a href="../magicdraw/ui/browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Cachable</span></div>
<div class="block">Reusable objects used in caches. They are reset when object is returned to the cache.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#reset()">reset</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Cache managers invokes this method to free resources.</div>
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
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">reset</span>()</div>
<div class="block">Cache managers invokes this method to free resources. Usually this method must drop references to external objects
 in order to enable garbage collection of them.</div>
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
