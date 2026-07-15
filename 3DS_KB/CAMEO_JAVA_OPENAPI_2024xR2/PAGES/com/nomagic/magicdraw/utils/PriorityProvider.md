# JAVA OPENAPI: PriorityProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/utils/PriorityProvider.html
- source_path: `com/nomagic/magicdraw/utils/PriorityProvider.html`
- source_sha256: `8d1e3d735733ed8ac0b1b23253cbe757505c8aac533cfbb14e7cd70d833154d8`
- captured_utc: `2026-07-14T16:56:00.974520+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.utils](package-summary.html)

## Interface PriorityProvider

All Superinterfaces:
`[PriorityProvider](../../utils/PriorityProvider.html)`

All Known Subinterfaces:
`[AMConfigurator](../../actions/AMConfigurator.html)`, `[BrowserContextAMConfigurator](../actions/BrowserContextAMConfigurator.html)`, `[BrowserTabTreeDragAndDropHandler](../ui/dnd/BrowserTabTreeDragAndDropHandler.html)`, `[BrowserToolbarAMConfigurator](../actions/BrowserToolbarAMConfigurator.html)`, `[ConfiguratorWithPriority](../actions/ConfiguratorWithPriority.html)`, `[DependencyMatrixAMConfigurator](../dependencymatrix/configuration/DependencyMatrixAMConfigurator.html)`, `[DependencyMatrixCellAMConfigurator](../dependencymatrix/configuration/DependencyMatrixCellAMConfigurator.html)`, `[DiagramContextAMConfigurator](../actions/DiagramContextAMConfigurator.html)`, `[DiagramContextToolbarAMConfigurator](../actions/DiagramContextToolbarAMConfigurator.html)`, `[RefreshManager.RefreshParticipant](../ui/RefreshManager.RefreshParticipant.html)`, `[RepresentationTextCreator.RepresentationTextProvider](../uml/RepresentationTextCreator.RepresentationTextProvider.html)`, `[TargetElementAMConfigurator](../actions/TargetElementAMConfigurator.html)`

All Known Implementing Classes:
`[ActivityDiagramContextAMConfigurator](../ui/actions/ActivityDiagramContextAMConfigurator.html)`, `[ActivityDiagramShortcutsConfigurator](../ui/actions/ActivityDiagramShortcutsConfigurator.html)`, `[AnyDiagramShortcutsConfigurator](../ui/actions/AnyDiagramShortcutsConfigurator.html)`, `[BaseDiagramContextAMConfigurator](../ui/actions/BaseDiagramContextAMConfigurator.html)`, `[BaseDiagramContextToolbarAMConfigurator](../ui/actions/BaseDiagramContextToolbarAMConfigurator.html)`, `[BaseDiagramShortcutsConfigurator](../ui/actions/BaseDiagramShortcutsConfigurator.html)`, `[BaseDiagramToolbarConfigurator](../ui/actions/BaseDiagramToolbarConfigurator.html)`, `[ClassDiagramContextAMConfigurator](../ui/actions/ClassDiagramContextAMConfigurator.html)`, `[ClassDiagramShortcutsConfigurator](../ui/actions/ClassDiagramShortcutsConfigurator.html)`, `[CollaborationDiagramContextAMConfigurator](../ui/actions/CollaborationDiagramContextAMConfigurator.html)`, `[CommunicationDiagramShortcutsConfigurator](../ui/actions/CommunicationDiagramShortcutsConfigurator.html)`, `[ComponentDiagramShortcutsConfigurator](../ui/actions/ComponentDiagramShortcutsConfigurator.html)`, `[CompositeStructureDiagramContextAMConfigurator](../ui/actions/CompositeStructureDiagramContextAMConfigurator.html)`, `[DeploymentDiagramShortcutsConfigurator](../ui/actions/DeploymentDiagramShortcutsConfigurator.html)`, `[DiagramTransferableDragAndDropHandler](../ui/dnd/DiagramTransferableDragAndDropHandler.html)`, `[ObjectDiagramShortcutsConfigurator](../ui/actions/ObjectDiagramShortcutsConfigurator.html)`, `[PackageDiagramShortcutsConfigurator](../ui/actions/PackageDiagramShortcutsConfigurator.html)`, `[ProfileDiagramShortcutsConfigurator](../ui/actions/ProfileDiagramShortcutsConfigurator.html)`, `[SequenceDiagramContextAMConfigurator](../ui/actions/SequenceDiagramContextAMConfigurator.html)`, `[SequenceDiagramShortcutsConfigurator](../ui/actions/SequenceDiagramShortcutsConfigurator.html)`, `[StateDiagramContextAMConfigurator](../ui/actions/StateDiagramContextAMConfigurator.html)`, `[StateDiagramShortcutsConfigurator](../ui/actions/StateDiagramShortcutsConfigurator.html)`, `[UseCaseDiagramShortcutsConfigurator](../ui/actions/UseCaseDiagramShortcutsConfigurator.html)`

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

@OpenApiAll
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html)public interfacePriorityProviderextends [PriorityProvider](../../utils/PriorityProvider.html)

An interface for marking objects that provide a priority.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
Static Methods
Modifier and Type
Method
Description
`static void`
`[sort](#sort(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PriorityProvider](PriorityProvider.html)> providers)`
Sorts given list of providers by priority
Methods inherited from interface com.nomagic.utils.[PriorityProvider](../../utils/PriorityProvider.html)
`[getPriority](../../utils/PriorityProvider.html#getPriority())`

============ METHOD DETAIL ========== 
Method Details
sort
static void sort([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PriorityProvider](PriorityProvider.html)> providers)
Description copied from interface: `[PriorityProvider](../../utils/PriorityProvider.html#sort(java.util.List))`
Sorts given list of providers by priority
Parameters:
`providers` - providers

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.utils</a></div>
<h1 class="title" title="Interface PriorityProvider">Interface PriorityProvider</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code>, <code><a href="../actions/BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a></code>, <code><a href="../ui/dnd/BrowserTabTreeDragAndDropHandler.html" title="interface in com.nomagic.magicdraw.ui.dnd">BrowserTabTreeDragAndDropHandler</a></code>, <code><a href="../actions/BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a></code>, <code><a href="../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../dependencymatrix/configuration/DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a></code>, <code><a href="../dependencymatrix/configuration/DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a></code>, <code><a href="../actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code>, <code><a href="../actions/DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a></code>, <code><a href="../ui/RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a></code>, <code><a href="../uml/RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a></code>, <code><a href="../actions/TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../ui/actions/ActivityDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/ActivityDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramContextToolbarAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextToolbarAMConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/BaseDiagramToolbarConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramToolbarConfigurator</a></code>, <code><a href="../ui/actions/ClassDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/ClassDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/CollaborationDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CollaborationDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/CommunicationDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CommunicationDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/ComponentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ComponentDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/CompositeStructureDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CompositeStructureDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/DeploymentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">DeploymentDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/dnd/DiagramTransferableDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandler</a></code>, <code><a href="../ui/actions/ObjectDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ObjectDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/PackageDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">PackageDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/ProfileDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ProfileDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/SequenceDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/SequenceDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/StateDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramContextAMConfigurator</a></code>, <code><a href="../ui/actions/StateDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramShortcutsConfigurator</a></code>, <code><a href="../ui/actions/UseCaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">UseCaseDiagramShortcutsConfigurator</a></code></dd>
</dl>
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PriorityProvider</span><span class="extends-implements">
extends <a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></span></div>
<div class="block">An interface for marking objects that provide a priority.</div>
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
<div class="caption"><span>Static Methods</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#sort(java.util.List)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a>&gt; providers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Sorts given list of providers by priority</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.utils.PriorityProvider">Methods inherited from interface com.nomagic.utils.<a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../utils/PriorityProvider.html#getPriority()">getPriority</a></code></div>
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
<section class="detail" id="sort(java.util.List)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a>&gt; providers)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../utils/PriorityProvider.html#sort(java.util.List)">PriorityProvider</a></code></span></div>
<div class="block">Sorts given list of providers by priority</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>providers</code> - providers</dd>
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
