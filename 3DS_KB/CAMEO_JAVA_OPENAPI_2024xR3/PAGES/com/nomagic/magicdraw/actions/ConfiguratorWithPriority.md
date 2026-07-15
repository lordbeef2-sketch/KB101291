# JAVA OPENAPI: ConfiguratorWithPriority (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/actions/ConfiguratorWithPriority.html
- source_path: `com/nomagic/magicdraw/actions/ConfiguratorWithPriority.html`
- source_sha256: `b1af12a6d43ee9fee693b581046a85d83cb804a7fe742f1f09a218017a91364c`
- captured_utc: `2026-07-14T16:55:02.962868+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Interface ConfiguratorWithPriority

All Superinterfaces:
`[PriorityProvider](../utils/PriorityProvider.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`

All Known Subinterfaces:
`[AMConfigurator](../../actions/AMConfigurator.html)`, `[BrowserContextAMConfigurator](BrowserContextAMConfigurator.html)`, `[BrowserTabTreeDragAndDropHandler](../ui/dnd/BrowserTabTreeDragAndDropHandler.html)`, `[BrowserToolbarAMConfigurator](BrowserToolbarAMConfigurator.html)`, `[DependencyMatrixAMConfigurator](../dependencymatrix/configuration/DependencyMatrixAMConfigurator.html)`, `[DependencyMatrixCellAMConfigurator](../dependencymatrix/configuration/DependencyMatrixCellAMConfigurator.html)`, `[DiagramContextAMConfigurator](DiagramContextAMConfigurator.html)`, `[DiagramContextToolbarAMConfigurator](DiagramContextToolbarAMConfigurator.html)`, `[TargetElementAMConfigurator](TargetElementAMConfigurator.html)`

All Known Implementing Classes:
`[ActivityDiagramContextAMConfigurator](../ui/actions/ActivityDiagramContextAMConfigurator.html)`, `[ActivityDiagramShortcutsConfigurator](../ui/actions/ActivityDiagramShortcutsConfigurator.html)`, `[AnyDiagramShortcutsConfigurator](../ui/actions/AnyDiagramShortcutsConfigurator.html)`, `[BaseDiagramContextAMConfigurator](../ui/actions/BaseDiagramContextAMConfigurator.html)`, `[BaseDiagramContextToolbarAMConfigurator](../ui/actions/BaseDiagramContextToolbarAMConfigurator.html)`, `[BaseDiagramShortcutsConfigurator](../ui/actions/BaseDiagramShortcutsConfigurator.html)`, `[BaseDiagramToolbarConfigurator](../ui/actions/BaseDiagramToolbarConfigurator.html)`, `[ClassDiagramContextAMConfigurator](../ui/actions/ClassDiagramContextAMConfigurator.html)`, `[ClassDiagramShortcutsConfigurator](../ui/actions/ClassDiagramShortcutsConfigurator.html)`, `[CollaborationDiagramContextAMConfigurator](../ui/actions/CollaborationDiagramContextAMConfigurator.html)`, `[CommunicationDiagramShortcutsConfigurator](../ui/actions/CommunicationDiagramShortcutsConfigurator.html)`, `[ComponentDiagramShortcutsConfigurator](../ui/actions/ComponentDiagramShortcutsConfigurator.html)`, `[CompositeStructureDiagramContextAMConfigurator](../ui/actions/CompositeStructureDiagramContextAMConfigurator.html)`, `[DeploymentDiagramShortcutsConfigurator](../ui/actions/DeploymentDiagramShortcutsConfigurator.html)`, `[DiagramTransferableDragAndDropHandler](../ui/dnd/DiagramTransferableDragAndDropHandler.html)`, `[ObjectDiagramShortcutsConfigurator](../ui/actions/ObjectDiagramShortcutsConfigurator.html)`, `[PackageDiagramShortcutsConfigurator](../ui/actions/PackageDiagramShortcutsConfigurator.html)`, `[ProfileDiagramShortcutsConfigurator](../ui/actions/ProfileDiagramShortcutsConfigurator.html)`, `[SequenceDiagramContextAMConfigurator](../ui/actions/SequenceDiagramContextAMConfigurator.html)`, `[SequenceDiagramShortcutsConfigurator](../ui/actions/SequenceDiagramShortcutsConfigurator.html)`, `[StateDiagramContextAMConfigurator](../ui/actions/StateDiagramContextAMConfigurator.html)`, `[StateDiagramShortcutsConfigurator](../ui/actions/StateDiagramShortcutsConfigurator.html)`, `[UseCaseDiagramShortcutsConfigurator](../ui/actions/UseCaseDiagramShortcutsConfigurator.html)`

@OpenApiAllpublic interfaceConfiguratorWithPriorityextends [PriorityProvider](../utils/PriorityProvider.html)

Common priority handling for all configurators

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`int`
`[getPriority](#getPriority())()`
Returns priority of this configurator.

============ METHOD DETAIL ========== 
Method Details
getPriority
int getPriority()
Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such a case configurator must have lower priority than others.
Specified by:
`[getPriority](../../utils/PriorityProvider.html#getPriority())` in interface `[PriorityProvider](../../utils/PriorityProvider.html)`
Returns:
priority of this configurator.
See Also:
[`PriorityProvider.HIGH_PRIORITY`](../../utils/PriorityProvider.html#HIGH_PRIORITY)
[`PriorityProvider.MEDIUM_PRIORITY`](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)
[`PriorityProvider.LOW_PRIORITY`](../../utils/PriorityProvider.html#LOW_PRIORITY)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Interface ConfiguratorWithPriority">Interface ConfiguratorWithPriority</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code>, <code><a href="BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a></code>, <code><a href="../ui/dnd/BrowserTabTreeDragAndDropHandler.html" title="interface in com.nomagic.magicdraw.ui.dnd">BrowserTabTreeDragAndDropHandler</a></code>, <code><a href="BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a></code>, <code><a href="../dependencymatrix/configuration/DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a></code>, <code><a href="../dependencymatrix/configuration/DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a></code>, <code><a href="DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code>, <code><a href="DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a></code>, <code><a href="TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../ui/actions/ActivityDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/ActivityDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramContextToolbarAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextToolbarAMConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramToolbarConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramToolbarConfigurator</a></code>, <code><a href="../ui/actions/ClassDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/ClassDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/CollaborationDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CollaborationDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/CommunicationDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CommunicationDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/ComponentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ComponentDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/CompositeStructureDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CompositeStructureDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/DeploymentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">DeploymentDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/dnd/DiagramTransferableDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandler</a></code>, <code><a href="../ui/actions/ObjectDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ObjectDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/PackageDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">PackageDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/ProfileDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ProfileDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/SequenceDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/SequenceDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/StateDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/StateDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/UseCaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">UseCaseDiagramShortcutsConfigurator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ConfiguratorWithPriority</span><span class="extends-implements">
extends <a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></span></div>
<div class="block">Common priority handling for all configurators</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns priority of this configurator.</div>
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
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block">Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such a case configurator must have lower priority than others.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../utils/PriorityProvider.html#getPriority()">getPriority</a></code> in interface <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
<dt>Returns:</dt>
<dd>priority of this configurator.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../../utils/PriorityProvider.html#HIGH_PRIORITY"><code>PriorityProvider.HIGH_PRIORITY</code></a></li>
<li><a href="../../utils/PriorityProvider.html#MEDIUM_PRIORITY"><code>PriorityProvider.MEDIUM_PRIORITY</code></a></li>
<li><a href="../../utils/PriorityProvider.html#LOW_PRIORITY"><code>PriorityProvider.LOW_PRIORITY</code></a></li>
</ul>
</dd>
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
