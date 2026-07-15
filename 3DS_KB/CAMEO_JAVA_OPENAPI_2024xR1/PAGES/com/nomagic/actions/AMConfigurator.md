# JAVA OPENAPI: AMConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/actions/AMConfigurator.html
- source_path: `com/nomagic/actions/AMConfigurator.html`
- source_sha256: `aba41a38917c7df4b827b3e304ca3a6ab2e0a9526d9fe712dd5e55da14cae11e`
- captured_utc: `2026-07-14T16:50:58.537902+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.actions](package-summary.html)

## Interface AMConfigurator

All Superinterfaces:
`[ConfiguratorWithPriority](../magicdraw/actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../magicdraw/utils/PriorityProvider.html)`, `[PriorityProvider](../utils/PriorityProvider.html)`

All Known Implementing Classes:
`[ActivityDiagramShortcutsConfigurator](../magicdraw/ui/actions/ActivityDiagramShortcutsConfigurator.html)`, `[AnyDiagramShortcutsConfigurator](../magicdraw/ui/actions/AnyDiagramShortcutsConfigurator.html)`, `[BaseDiagramShortcutsConfigurator](../magicdraw/ui/actions/BaseDiagramShortcutsConfigurator.html)`, `[BaseDiagramToolbarConfigurator](../magicdraw/ui/actions/BaseDiagramToolbarConfigurator.html)`, `[ClassDiagramShortcutsConfigurator](../magicdraw/ui/actions/ClassDiagramShortcutsConfigurator.html)`, `[CommunicationDiagramShortcutsConfigurator](../magicdraw/ui/actions/CommunicationDiagramShortcutsConfigurator.html)`, `[ComponentDiagramShortcutsConfigurator](../magicdraw/ui/actions/ComponentDiagramShortcutsConfigurator.html)`, `[DeploymentDiagramShortcutsConfigurator](../magicdraw/ui/actions/DeploymentDiagramShortcutsConfigurator.html)`, `[ObjectDiagramShortcutsConfigurator](../magicdraw/ui/actions/ObjectDiagramShortcutsConfigurator.html)`, `[PackageDiagramShortcutsConfigurator](../magicdraw/ui/actions/PackageDiagramShortcutsConfigurator.html)`, `[ProfileDiagramShortcutsConfigurator](../magicdraw/ui/actions/ProfileDiagramShortcutsConfigurator.html)`, `[SequenceDiagramShortcutsConfigurator](../magicdraw/ui/actions/SequenceDiagramShortcutsConfigurator.html)`, `[StateDiagramShortcutsConfigurator](../magicdraw/ui/actions/StateDiagramShortcutsConfigurator.html)`, `[UseCaseDiagramShortcutsConfigurator](../magicdraw/ui/actions/UseCaseDiagramShortcutsConfigurator.html)`

@OpenApiAllpublic interfaceAMConfiguratorextends [ConfiguratorWithPriority](../magicdraw/actions/ConfiguratorWithPriority.html)

Interface for configuring Actions manager.
 Configurator should add/remove necessary actions.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[configure](#configure(com.nomagic.actions.ActionsManager))([ActionsManager](ActionsManager.html) manager)`
Method for configuring manager.
`default int`
`[getPriority](#getPriority())()`
Returns priority of this configurator.

============ METHOD DETAIL ========== 
Method Details
configure
void configure([ActionsManager](ActionsManager.html) manager)
Method for configuring manager.
 During this call, new actions can be added to manager.
 Also existing actions can be removed from the given manager.
Parameters:
`manager` - actions manager to be configured.
getPriority
default int getPriority()
Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such a case configurator must have lower priority than others.
 
 

 The default implementation returns #LOW_PRIORITY
Specified by:
`[getPriority](../magicdraw/actions/ConfiguratorWithPriority.html#getPriority())` in interface `[ConfiguratorWithPriority](../magicdraw/actions/ConfiguratorWithPriority.html)`
Specified by:
`[getPriority](../utils/PriorityProvider.html#getPriority())` in interface `[PriorityProvider](../utils/PriorityProvider.html)`
Returns:
priority of this configurator.
See Also:
[`PriorityProvider.HIGH_PRIORITY`](../utils/PriorityProvider.html#HIGH_PRIORITY)
[`PriorityProvider.MEDIUM_PRIORITY`](../utils/PriorityProvider.html#MEDIUM_PRIORITY)
[`PriorityProvider.LOW_PRIORITY`](../utils/PriorityProvider.html#LOW_PRIORITY)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.actions</a></div>
<h1 class="title" title="Interface AMConfigurator">Interface AMConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../magicdraw/actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../magicdraw/utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../magicdraw/ui/actions/ActivityDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/BaseDiagramToolbarConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramToolbarConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ClassDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/CommunicationDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CommunicationDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ComponentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ComponentDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/DeploymentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">DeploymentDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ObjectDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ObjectDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/PackageDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">PackageDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ProfileDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ProfileDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/SequenceDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/StateDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/UseCaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">UseCaseDiagramShortcutsConfigurator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AMConfigurator</span><span class="extends-implements">
extends <a href="../magicdraw/actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></span></div>
<div class="block">Interface for configuring Actions manager.
 Configurator should add/remove necessary actions.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager)">configure</a><wbr/>(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method for configuring manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
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
<section class="detail" id="configure(com.nomagic.actions.ActionsManager)">
<h3>configure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Method for configuring manager.
 During this call, new actions can be added to manager.
 Also existing actions can be removed from the given manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - actions manager to be configured.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block">Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such a case configurator must have lower priority than others.
 <br/><br/>
 The default implementation returns #LOW_PRIORITY</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../magicdraw/actions/ConfiguratorWithPriority.html#getPriority()">getPriority</a></code> in interface <code><a href="../magicdraw/actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../utils/PriorityProvider.html#getPriority()">getPriority</a></code> in interface <code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
<dt>Returns:</dt>
<dd>priority of this configurator.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="../utils/PriorityProvider.html#HIGH_PRIORITY"><code>PriorityProvider.HIGH_PRIORITY</code></a></li>
<li><a href="../utils/PriorityProvider.html#MEDIUM_PRIORITY"><code>PriorityProvider.MEDIUM_PRIORITY</code></a></li>
<li><a href="../utils/PriorityProvider.html#LOW_PRIORITY"><code>PriorityProvider.LOW_PRIORITY</code></a></li>
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
