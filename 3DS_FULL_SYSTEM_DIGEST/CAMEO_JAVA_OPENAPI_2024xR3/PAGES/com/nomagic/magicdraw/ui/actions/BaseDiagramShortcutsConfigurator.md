# JAVA OPENAPI: BaseDiagramShortcutsConfigurator (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/actions/BaseDiagramShortcutsConfigurator.html
- source_path: `com/nomagic/magicdraw/ui/actions/BaseDiagramShortcutsConfigurator.html`
- source_sha256: `42eaa02dca422ce535d35e6df67b75eade99bb1ce310e125558b3504b227865d`
- captured_utc: `2026-07-14T16:55:51.151410+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.actions](package-summary.html)

## Class BaseDiagramShortcutsConfigurator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator](AnyDiagramShortcutsConfigurator.html)
com.nomagic.magicdraw.ui.actions.BaseDiagramShortcutsConfigurator

All Implemented Interfaces:
`[AMConfigurator](../../../actions/AMConfigurator.html)`, `[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

Direct Known Subclasses:
`[ActivityDiagramShortcutsConfigurator](ActivityDiagramShortcutsConfigurator.html)`, `[ClassDiagramShortcutsConfigurator](ClassDiagramShortcutsConfigurator.html)`, `[CommunicationDiagramShortcutsConfigurator](CommunicationDiagramShortcutsConfigurator.html)`, `[ComponentDiagramShortcutsConfigurator](ComponentDiagramShortcutsConfigurator.html)`, `[DeploymentDiagramShortcutsConfigurator](DeploymentDiagramShortcutsConfigurator.html)`, `[ObjectDiagramShortcutsConfigurator](ObjectDiagramShortcutsConfigurator.html)`, `[PackageDiagramShortcutsConfigurator](PackageDiagramShortcutsConfigurator.html)`, `[ProfileDiagramShortcutsConfigurator](ProfileDiagramShortcutsConfigurator.html)`, `[SequenceDiagramShortcutsConfigurator](SequenceDiagramShortcutsConfigurator.html)`, `[StateDiagramShortcutsConfigurator](StateDiagramShortcutsConfigurator.html)`, `[UseCaseDiagramShortcutsConfigurator](UseCaseDiagramShortcutsConfigurator.html)`

@OpenApiAllpublic abstract classBaseDiagramShortcutsConfigurator
extends [AnyDiagramShortcutsConfigurator](AnyDiagramShortcutsConfigurator.html)

Configure shortcuts for any "symbolic" diagrams - diagrams those can have symbols. This configurator should not be used for matrix, table like diagrams.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BaseDiagramShortcutsConfigurator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[configure](#configure(com.nomagic.actions.ActionsManager))([ActionsManager](../../../actions/ActionsManager.html) manager)`
Method for configuring manager.
`void`
`[configureCommonActions](#configureCommonActions(com.nomagic.actions.ActionsManager))([ActionsManager](../../../actions/ActionsManager.html) manager)`
Configure common actions
Methods inherited from class com.nomagic.magicdraw.ui.actions.[AnyDiagramShortcutsConfigurator](AnyDiagramShortcutsConfigurator.html)
`[configureCommonActions](AnyDiagramShortcutsConfigurator.html#configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String)), [getPriority](AnyDiagramShortcutsConfigurator.html#getPriority())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseDiagramShortcutsConfigurator
public BaseDiagramShortcutsConfigurator()
 ============ METHOD DETAIL ========== 
Method Details
configureCommonActions
public void configureCommonActions([ActionsManager](../../../actions/ActionsManager.html) manager)
Configure common actions
Parameters:
`manager` - manager
configure
public void configure([ActionsManager](../../../actions/ActionsManager.html) manager)
Description copied from interface: `[AMConfigurator](../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager))`
Method for configuring manager.
 During this call, new actions can be added to manager.
 Also existing actions can be removed from the given manager.
Parameters:
`manager` - actions manager to be configured.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.actions</a></div>
<h1 class="title" title="Class BaseDiagramShortcutsConfigurator">Class BaseDiagramShortcutsConfigurator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator</a>
<div class="inheritance">com.nomagic.magicdraw.ui.actions.BaseDiagramShortcutsConfigurator</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code>, <code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ActivityDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ActivityDiagramShortcutsConfigurator</a></code>, <code><a href="ClassDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ClassDiagramShortcutsConfigurator</a></code>, <code><a href="CommunicationDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">CommunicationDiagramShortcutsConfigurator</a></code>, <code><a href="ComponentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ComponentDiagramShortcutsConfigurator</a></code>, <code><a href="DeploymentDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">DeploymentDiagramShortcutsConfigurator</a></code>, <code><a href="ObjectDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ObjectDiagramShortcutsConfigurator</a></code>, <code><a href="PackageDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">PackageDiagramShortcutsConfigurator</a></code>, <code><a href="ProfileDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">ProfileDiagramShortcutsConfigurator</a></code>, <code><a href="SequenceDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">SequenceDiagramShortcutsConfigurator</a></code>, <code><a href="StateDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">StateDiagramShortcutsConfigurator</a></code>, <code><a href="UseCaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">UseCaseDiagramShortcutsConfigurator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">BaseDiagramShortcutsConfigurator</span>
<span class="extends-implements">extends <a href="AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></span></div>
<div class="block">Configure shortcuts for any "symbolic" diagrams - diagrams those can have symbols. This configurator should not be used for matrix, table like diagrams.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../../../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../../../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">BaseDiagramShortcutsConfigurator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager)">configure</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Method for configuring manager.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureCommonActions(com.nomagic.actions.ActionsManager)">configureCommonActions</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configure common actions</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator">Methods inherited from class com.nomagic.magicdraw.ui.actions.<a href="AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></h3>
<code><a href="AnyDiagramShortcutsConfigurator.html#configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String)">configureCommonActions</a>, <a href="AnyDiagramShortcutsConfigurator.html#getPriority()">getPriority</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>BaseDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BaseDiagramShortcutsConfigurator</span>()</div>
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
<section class="detail" id="configureCommonActions(com.nomagic.actions.ActionsManager)">
<h3>configureCommonActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configureCommonActions</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block">Configure common actions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configure(com.nomagic.actions.ActionsManager)">
<h3>configure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager)">AMConfigurator</a></code></span></div>
<div class="block">Method for configuring manager.
 During this call, new actions can be added to manager.
 Also existing actions can be removed from the given manager.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - actions manager to be configured.</dd>
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
