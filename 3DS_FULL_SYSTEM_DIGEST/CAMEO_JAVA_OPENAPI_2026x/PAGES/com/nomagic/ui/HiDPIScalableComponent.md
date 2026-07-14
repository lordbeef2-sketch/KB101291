# JAVA OPENAPI: HiDPIScalableComponent (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/ui/HiDPIScalableComponent.html
- source_path: `com/nomagic/ui/HiDPIScalableComponent.html`
- source_sha256: `5c4ea7b9206dfbbf52f982fc04bce7f30f3ccdcdd86659c6ab99763d3ca8df3e`
- captured_utc: `2026-07-14T16:58:41.686332+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui](package-summary.html)

## Interface HiDPIScalableComponent

All Known Implementing Classes:
`com.nomagic.magicdraw.ui.dialogs.BaseDialog`, `com.dassault_systemes.modeler.magic.ui.dialogs.selection.ConfigurableElementSelectionDlg`, `[DiagramWindow](../magicdraw/ui/DiagramWindow.html)`, `com.nomagic.ui.Dialog`, `com.nomagic.magicdraw.ui.editorwindows.EditorWindow`, `com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlg`, `[ElementSelectionDlg](../magicdraw/ui/dialogs/selection/ElementSelectionDlg.html)`, `[SelectElementDlg](../magicdraw/ui/dialogs/SelectElementDlg.html)`, `com.nomagic.ui.SimpleBaseDialog`

@OpenApiAllpublic interfaceHiDPIScalableComponent

A component which support scaling.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[isHiDPIScaled](#isHiDPIScaled())()`

`void`
`[scaleForHiDPI](#scaleForHiDPI())()`

`void`
`[setHiDPIScaled](#setHiDPIScaled(boolean))(boolean scaled)`

============ METHOD DETAIL ========== 
Method Details
isHiDPIScaled
boolean isHiDPIScaled()
setHiDPIScaled
void setHiDPIScaled(boolean scaled)
scaleForHiDPI
void scaleForHiDPI()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui</a></div>
<h1 class="title" title="Interface HiDPIScalableComponent">Interface HiDPIScalableComponent</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.nomagic.magicdraw.ui.dialogs.BaseDialog</code>, <code>com.dassault_systemes.modeler.magic.ui.dialogs.selection.ConfigurableElementSelectionDlg</code>, <code><a href="../magicdraw/ui/DiagramWindow.html" title="class in com.nomagic.magicdraw.ui">DiagramWindow</a></code>, <code>com.nomagic.ui.Dialog</code>, <code>com.nomagic.magicdraw.ui.editorwindows.EditorWindow</code>, <code>com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlg</code>, <code><a href="../magicdraw/ui/dialogs/selection/ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code>, <code><a href="../magicdraw/ui/dialogs/SelectElementDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementDlg</a></code>, <code>com.nomagic.ui.SimpleBaseDialog</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">HiDPIScalableComponent</span></div>
<div class="block">A component which support scaling.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isHiDPIScaled()">isHiDPIScaled</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#scaleForHiDPI()">scaleForHiDPI</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setHiDPIScaled(boolean)">setHiDPIScaled</a><wbr/>(boolean scaled)</code></div>
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
<section class="detail" id="isHiDPIScaled()">
<h3>isHiDPIScaled</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isHiDPIScaled</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHiDPIScaled(boolean)">
<h3>setHiDPIScaled</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setHiDPIScaled</span><wbr/><span class="parameters">(boolean scaled)</span></div>
</section>
</li>
<li>
<section class="detail" id="scaleForHiDPI()">
<h3>scaleForHiDPI</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">scaleForHiDPI</span>()</div>
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
