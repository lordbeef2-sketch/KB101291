# JAVA OPENAPI: PriorityProvider (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/utils/PriorityProvider.html
- source_path: `com/nomagic/utils/PriorityProvider.html`
- source_sha256: `576267b0ae7fd2d09a218e2ec3c3536ea5e66d28d0b747640e489e21f5ecbcf3`
- captured_utc: `2026-07-14T16:56:40.983967+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.utils](package-summary.html)

## Interface PriorityProvider

All Known Subinterfaces:
`[AMConfigurator](../actions/AMConfigurator.html)`, `[BrowserContextAMConfigurator](../magicdraw/actions/BrowserContextAMConfigurator.html)`, `[BrowserTabTreeDragAndDropHandler](../magicdraw/ui/dnd/BrowserTabTreeDragAndDropHandler.html)`, `[BrowserToolbarAMConfigurator](../magicdraw/actions/BrowserToolbarAMConfigurator.html)`, `[ConfiguratorWithPriority](../magicdraw/actions/ConfiguratorWithPriority.html)`, `[DependencyMatrixAMConfigurator](../magicdraw/dependencymatrix/configuration/DependencyMatrixAMConfigurator.html)`, `[DependencyMatrixCellAMConfigurator](../magicdraw/dependencymatrix/configuration/DependencyMatrixCellAMConfigurator.html)`, `[DiagramContextAMConfigurator](../magicdraw/actions/DiagramContextAMConfigurator.html)`, `[DiagramContextToolbarAMConfigurator](../magicdraw/actions/DiagramContextToolbarAMConfigurator.html)`, `[PriorityProvider](../magicdraw/utils/PriorityProvider.html)`, `[RefreshManager.RefreshParticipant](../magicdraw/ui/RefreshManager.RefreshParticipant.html)`, `[RepresentationTextCreator.RepresentationTextProvider](../magicdraw/uml/RepresentationTextCreator.RepresentationTextProvider.html)`, `[TargetElementAMConfigurator](../magicdraw/actions/TargetElementAMConfigurator.html)`

All Known Implementing Classes:
`[ActivityDiagramContextAMConfigurator](../magicdraw/ui/actions/ActivityDiagramContextAMConfigurator.html)`, `[ActivityDiagramShortcutsConfigurator](../magicdraw/ui/actions/ActivityDiagramShortcutsConfigurator.html)`, `[AnyDiagramShortcutsConfigurator](../magicdraw/ui/actions/AnyDiagramShortcutsConfigurator.html)`, `[BaseDiagramContextAMConfigurator](../magicdraw/ui/actions/BaseDiagramContextAMConfigurator.html)`, `[BaseDiagramContextToolbarAMConfigurator](../magicdraw/ui/actions/BaseDiagramContextToolbarAMConfigurator.html)`, `[BaseDiagramShortcutsConfigurator](../magicdraw/ui/actions/BaseDiagramShortcutsConfigurator.html)`, `[BaseDiagramToolbarConfigurator](../magicdraw/ui/actions/BaseDiagramToolbarConfigurator.html)`, `[ClassDiagramContextAMConfigurator](../magicdraw/ui/actions/ClassDiagramContextAMConfigurator.html)`, `[ClassDiagramShortcutsConfigurator](../magicdraw/ui/actions/ClassDiagramShortcutsConfigurator.html)`, `[CollaborationDiagramContextAMConfigurator](../magicdraw/ui/actions/CollaborationDiagramContextAMConfigurator.html)`, `[CommunicationDiagramShortcutsConfigurator](../magicdraw/ui/actions/CommunicationDiagramShortcutsConfigurator.html)`, `[ComponentDiagramShortcutsConfigurator](../magicdraw/ui/actions/ComponentDiagramShortcutsConfigurator.html)`, `[CompositeStructureDiagramContextAMConfigurator](../magicdraw/ui/actions/CompositeStructureDiagramContextAMConfigurator.html)`, `[DeploymentDiagramShortcutsConfigurator](../magicdraw/ui/actions/DeploymentDiagramShortcutsConfigurator.html)`, `[DiagramTransferableDragAndDropHandler](../magicdraw/ui/dnd/DiagramTransferableDragAndDropHandler.html)`, `[ObjectDiagramShortcutsConfigurator](../magicdraw/ui/actions/ObjectDiagramShortcutsConfigurator.html)`, `[PackageDiagramShortcutsConfigurator](../magicdraw/ui/actions/PackageDiagramShortcutsConfigurator.html)`, `[ProfileDiagramShortcutsConfigurator](../magicdraw/ui/actions/ProfileDiagramShortcutsConfigurator.html)`, `[SequenceDiagramContextAMConfigurator](../magicdraw/ui/actions/SequenceDiagramContextAMConfigurator.html)`, `[SequenceDiagramShortcutsConfigurator](../magicdraw/ui/actions/SequenceDiagramShortcutsConfigurator.html)`, `[StateDiagramContextAMConfigurator](../magicdraw/ui/actions/StateDiagramContextAMConfigurator.html)`, `[StateDiagramShortcutsConfigurator](../magicdraw/ui/actions/StateDiagramShortcutsConfigurator.html)`, `[UseCaseDiagramShortcutsConfigurator](../magicdraw/ui/actions/UseCaseDiagramShortcutsConfigurator.html)`

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

@OpenApiAll
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html)public interfacePriorityProvider

An interface for marking objects that provide a priority.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[HIGH_PRIORITY](#HIGH_PRIORITY)`
High priority.
`static final int`
`[LOW_PRIORITY](#LOW_PRIORITY)`
Low priority.
`static final int`
`[MEDIUM_PRIORITY](#MEDIUM_PRIORITY)`
Medium priority.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`int`
`[getPriority](#getPriority())()`
Returns priority of this object.
`static void`
`[sort](#sort(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PriorityProvider](PriorityProvider.html)> providers)`
Sorts given list of providers by priority

============ FIELD DETAIL =========== 
Field Details
HIGH_PRIORITY
static final int HIGH_PRIORITY
High priority.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.utils.PriorityProvider.HIGH_PRIORITY)
MEDIUM_PRIORITY
static final int MEDIUM_PRIORITY
Medium priority.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.utils.PriorityProvider.MEDIUM_PRIORITY)
LOW_PRIORITY
static final int LOW_PRIORITY
Low priority.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.utils.PriorityProvider.LOW_PRIORITY)
 ============ METHOD DETAIL ========== 
Method Details
getPriority
int getPriority()
Returns priority of this object.
Returns:
priority of this object.
sort
static void sort([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [PriorityProvider](PriorityProvider.html)> providers)
Sorts given list of providers by priority
Parameters:
`providers` - providers

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.utils</a></div>
<h1 class="title" title="Interface PriorityProvider">Interface PriorityProvider</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code>, <code><a href="../magicdraw/actions/BrowserContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/dnd/BrowserTabTreeDragAndDropHandler.html" title="interface in com.nomagic.magicdraw.ui.dnd">BrowserTabTreeDragAndDropHandler</a></code>, <code><a href="../magicdraw/actions/BrowserToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">BrowserToolbarAMConfigurator</a></code>, <code><a href="../magicdraw/actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../magicdraw/dependencymatrix/configuration/DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a></code>, <code><a href="../magicdraw/dependencymatrix/configuration/DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a></code>, <code><a href="../magicdraw/actions/DiagramContextAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/actions/DiagramContextToolbarAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">DiagramContextToolbarAMConfigurator</a></code>, <code><a href="../magicdraw/utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../magicdraw/ui/RefreshManager.RefreshParticipant.html" title="interface in com.nomagic.magicdraw.ui">RefreshManager.RefreshParticipant</a></code>, <code><a href="../magicdraw/uml/RepresentationTextCreator.RepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.uml">RepresentationTextCreator.RepresentationTextProvider</a></code>, <code><a href="../magicdraw/actions/TargetElementAMConfigurator.html" title="interface in com.nomagic.magicdraw.actions">TargetElementAMConfigurator</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../magicdraw/ui/actions/ActivityDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ActivityDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/BaseDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/BaseDiagramContextToolbarAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextToolbarAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/BaseDiagramToolbarConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramToolbarConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ClassDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ClassDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/CollaborationDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CollaborationDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/CommunicationDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CommunicationDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ComponentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ComponentDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/CompositeStructureDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CompositeStructureDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/DeploymentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">DeploymentDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/dnd/DiagramTransferableDragAndDropHandler.html" title="class in com.nomagic.magicdraw.ui.dnd">DiagramTransferableDragAndDropHandler</a></code>, <code><a href="../magicdraw/ui/actions/ObjectDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ObjectDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/PackageDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">PackageDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/ProfileDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ProfileDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/SequenceDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/SequenceDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/StateDiagramContextAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramContextAMConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/StateDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramShortcutsConfigurator</a></code>, <code><a href="../magicdraw/ui/actions/UseCaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">UseCaseDiagramShortcutsConfigurator</a></code></dd>
</dl>
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PriorityProvider</span></div>
<div class="block">An interface for marking objects that provide a priority.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HIGH_PRIORITY">HIGH_PRIORITY</a></code></div>
<div class="col-last even-row-color">
<div class="block">High priority.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOW_PRIORITY">LOW_PRIORITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Low priority.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Medium priority.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns priority of this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#sort(java.util.List)">sort</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a>&gt; providers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Sorts given list of providers by priority</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="HIGH_PRIORITY">
<h3>HIGH_PRIORITY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">HIGH_PRIORITY</span></div>
<div class="block">High priority.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.utils.PriorityProvider.HIGH_PRIORITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MEDIUM_PRIORITY">
<h3>MEDIUM_PRIORITY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MEDIUM_PRIORITY</span></div>
<div class="block">Medium priority.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.utils.PriorityProvider.MEDIUM_PRIORITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOW_PRIORITY">
<h3>LOW_PRIORITY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOW_PRIORITY</span></div>
<div class="block">Low priority.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.utils.PriorityProvider.LOW_PRIORITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block">Returns priority of this object.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>priority of this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sort(java.util.List)">
<h3>sort</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type">void</span> <span class="element-name">sort</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a>&gt; providers)</span></div>
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
