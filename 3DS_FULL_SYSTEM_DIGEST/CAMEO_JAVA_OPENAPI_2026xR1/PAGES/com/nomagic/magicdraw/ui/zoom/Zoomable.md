# JAVA OPENAPI: Zoomable (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/zoom/Zoomable.html
- source_path: `com/nomagic/magicdraw/ui/zoom/Zoomable.html`
- source_sha256: `ee42b452ee7ce2a6acfbdd6c3b6b496d180f1fffdd25bf6a1a549e24e3d8e083`
- captured_utc: `2026-07-14T16:46:03.494848+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.zoom](package-summary.html)

## Interface Zoomable

All Known Implementing Classes:
`[AdornmentNodeRenderer](../browser/AdornmentNodeRenderer.html)`, `com.nomagic.awt.HighlightTreeCellRenderer`, `com.nomagic.awt.StyledColorLabelTreeCellRenderer`

@OpenApiAllpublic interfaceZoomable

Interface for components that are able to paint their contents scaled (zoomed).
 zoomTo() method is only called then zoom factor changes.
 By default zoom factor is considered to be 1, and zoomTo(1) may not be called initially.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[zoomTo](#zoomTo(float))(float zoomFactor)`

============ METHOD DETAIL ========== 
Method Details
zoomTo
void zoomTo(float zoomFactor)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.zoom</a></div>
<h1 class="title" title="Interface Zoomable">Interface Zoomable</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../browser/AdornmentNodeRenderer.html" title="class in com.nomagic.magicdraw.ui.browser">AdornmentNodeRenderer</a></code>, <code>com.nomagic.awt.HighlightTreeCellRenderer</code>, <code>com.nomagic.awt.StyledColorLabelTreeCellRenderer</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Zoomable</span></div>
<div class="block">Interface for components that are able to paint their contents scaled (zoomed).
 zoomTo() method is only called then zoom factor changes.
 By default zoom factor is considered to be 1, and zoomTo(1) may not be called initially.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#zoomTo(float)">zoomTo</a><wbr/>(float zoomFactor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="zoomTo(float)">
<h3>zoomTo</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">zoomTo</span><wbr/><span class="parameters">(float zoomFactor)</span></div>
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
