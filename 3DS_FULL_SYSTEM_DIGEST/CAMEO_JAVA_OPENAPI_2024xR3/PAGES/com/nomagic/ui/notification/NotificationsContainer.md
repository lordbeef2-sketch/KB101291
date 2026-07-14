# JAVA OPENAPI: NotificationsContainer (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/ui/notification/NotificationsContainer.html
- source_path: `com/nomagic/ui/notification/NotificationsContainer.html`
- source_sha256: `c4a0f27c3683729d63f10f3cb66998170331bf7f34642d3807db7b5325948093`
- captured_utc: `2026-07-14T16:56:10.327625+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.ui.notification](package-summary.html)

## Interface NotificationsContainer

All Known Implementing Classes:
`com.nomagic.magicdraw.ui.dialogs.BaseDialog`, `com.dassault_systemes.modeler.magic.ui.dialogs.selection.ConfigurableElementSelectionDlg`, `com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlg`, `[ElementSelectionDlg](../../magicdraw/ui/dialogs/selection/ElementSelectionDlg.html)`, `[SelectElementDlg](../../magicdraw/ui/dialogs/SelectElementDlg.html)`, `com.nomagic.ui.SimpleBaseDialog`

@OpenApiAllpublic interfaceNotificationsContainer

Container level notifications can be displayed only in components that implements this interface.
 Those notifications will be displayed in designated area returned by getNotificationsContainer() method.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html)`
`[getNotificationsContainer](#getNotificationsContainer())()`
Returns area where notification are displayed

============ METHOD DETAIL ========== 
Method Details
getNotificationsContainer
[JComponent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html) getNotificationsContainer()
Returns area where notification are displayed
Returns:
area where notifications are displayed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.ui.notification</a></div>
<h1 class="title" title="Interface NotificationsContainer">Interface NotificationsContainer</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.nomagic.magicdraw.ui.dialogs.BaseDialog</code>, <code>com.dassault_systemes.modeler.magic.ui.dialogs.selection.ConfigurableElementSelectionDlg</code>, <code>com.dassault_systemes.modeler.magic.ui.dialogs.selection.ElementSelectionDlg</code>, <code><a href="../../magicdraw/ui/dialogs/selection/ElementSelectionDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs.selection">ElementSelectionDlg</a></code>, <code><a href="../../magicdraw/ui/dialogs/SelectElementDlg.html" title="class in com.nomagic.magicdraw.ui.dialogs">SelectElementDlg</a></code>, <code>com.nomagic.ui.SimpleBaseDialog</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">NotificationsContainer</span></div>
<div class="block">Container level notifications can be displayed only in components that implements this interface.
 Those notifications will be displayed in designated area returned by getNotificationsContainer() method.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNotificationsContainer()">getNotificationsContainer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns area where notification are displayed</div>
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
<section class="detail" id="getNotificationsContainer()">
<h3>getNotificationsContainer</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JComponent.html" title="class or interface in javax.swing">JComponent</a></span> <span class="element-name">getNotificationsContainer</span>()</div>
<div class="block">Returns area where notification are displayed</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>area where notifications are displayed</dd>
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
