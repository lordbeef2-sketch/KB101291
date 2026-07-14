# JAVA OPENAPI: SequenceDiagramShortcutsConfigurator (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/actions/SequenceDiagramShortcutsConfigurator.html
- source_path: `com/nomagic/magicdraw/ui/actions/SequenceDiagramShortcutsConfigurator.html`
- source_sha256: `19b56802a31425d5b1a1186aaabbcad903d822d0cc9e30d0a03a345013b68b2d`
- captured_utc: `2026-07-14T16:46:00.315806+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.actions](package-summary.html)

## Class SequenceDiagramShortcutsConfigurator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator](AnyDiagramShortcutsConfigurator.html)
[com.nomagic.magicdraw.ui.actions.BaseDiagramShortcutsConfigurator](BaseDiagramShortcutsConfigurator.html)
com.nomagic.magicdraw.ui.actions.SequenceDiagramShortcutsConfigurator

All Implemented Interfaces:
`[AMConfigurator](../../../actions/AMConfigurator.html)`, `[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

@OpenApiAllpublic classSequenceDiagramShortcutsConfigurator
extends [BaseDiagramShortcutsConfigurator](BaseDiagramShortcutsConfigurator.html)

Configure sequence diagram shortcuts.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SequenceDiagramShortcutsConfigurator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[configure](#configure(com.nomagic.actions.ActionsManager))([ActionsManager](../../../actions/ActionsManager.html) manager)`
Method for configuring manager.
Methods inherited from class com.nomagic.magicdraw.ui.actions.[BaseDiagramShortcutsConfigurator](BaseDiagramShortcutsConfigurator.html)
`[configureCommonActions](BaseDiagramShortcutsConfigurator.html#configureCommonActions(com.nomagic.actions.ActionsManager))`
Methods inherited from class com.nomagic.magicdraw.ui.actions.[AnyDiagramShortcutsConfigurator](AnyDiagramShortcutsConfigurator.html)
`[configureCommonActions](AnyDiagramShortcutsConfigurator.html#configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String)), [getPriority](AnyDiagramShortcutsConfigurator.html#getPriority())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SequenceDiagramShortcutsConfigurator
public SequenceDiagramShortcutsConfigurator()
 ============ METHOD DETAIL ========== 
Method Details
configure
public void configure([ActionsManager](../../../actions/ActionsManager.html) manager)
Description copied from interface: `[AMConfigurator](../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager))`
Method for configuring manager.
 During this call, new actions can be added to manager.
 Also existing actions can be removed from the given manager.
Specified by:
`[configure](../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager))` in interface `[AMConfigurator](../../../actions/AMConfigurator.html)`
Overrides:
`[configure](BaseDiagramShortcutsConfigurator.html#configure(com.nomagic.actions.ActionsManager))` in class `[BaseDiagramShortcutsConfigurator](BaseDiagramShortcutsConfigurator.html)`
Parameters:
`manager` - actions manager to be configured.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.actions</a></div>
<h1 class="title" title="Class SequenceDiagramShortcutsConfigurator">Class SequenceDiagramShortcutsConfigurator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator</a>
<div class="inheritance"><a href="BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">com.nomagic.magicdraw.ui.actions.BaseDiagramShortcutsConfigurator</a>
<div class="inheritance">com.nomagic.magicdraw.ui.actions.SequenceDiagramShortcutsConfigurator</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code>, <code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SequenceDiagramShortcutsConfigurator</span>
<span class="extends-implements">extends <a href="BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></span></div>
<div class="block">Configure sequence diagram shortcuts.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SequenceDiagramShortcutsConfigurator</a>()</code></div>
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
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.actions.BaseDiagramShortcutsConfigurator">Methods inherited from class com.nomagic.magicdraw.ui.actions.<a href="BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></h3>
<code><a href="BaseDiagramShortcutsConfigurator.html#configureCommonActions(com.nomagic.actions.ActionsManager)">configureCommonActions</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator">Methods inherited from class com.nomagic.magicdraw.ui.actions.<a href="AnyDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">AnyDiagramShortcutsConfigurator</a></h3>
<code><a href="AnyDiagramShortcutsConfigurator.html#configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String)">configureCommonActions</a>, <a href="AnyDiagramShortcutsConfigurator.html#getPriority()">getPriority</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>SequenceDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SequenceDiagramShortcutsConfigurator</span>()</div>
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
<section class="detail" id="configure(com.nomagic.actions.ActionsManager)">
<h3>configure</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager)">AMConfigurator</a></code></span></div>
<div class="block">Method for configuring manager.
 During this call, new actions can be added to manager.
 Also existing actions can be removed from the given manager.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager)">configure</a></code> in interface <code><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="BaseDiagramShortcutsConfigurator.html#configure(com.nomagic.actions.ActionsManager)">configure</a></code> in class <code><a href="BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></code></dd>
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
