# JAVA OPENAPI: AnyDiagramShortcutsConfigurator (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/actions/AnyDiagramShortcutsConfigurator.html
- source_path: `com/nomagic/magicdraw/ui/actions/AnyDiagramShortcutsConfigurator.html`
- source_sha256: `6397785d7a79baa952c5ba5157e7a08814b57c24d364d150d96399c02dc82d96`
- captured_utc: `2026-07-14T16:45:59.849799+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.actions](package-summary.html)

## Class AnyDiagramShortcutsConfigurator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator

All Implemented Interfaces:
`[AMConfigurator](../../../actions/AMConfigurator.html)`, `[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

Direct Known Subclasses:
`[BaseDiagramShortcutsConfigurator](BaseDiagramShortcutsConfigurator.html)`

@OpenApiAllpublic abstract classAnyDiagramShortcutsConfigurator
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [AMConfigurator](../../../actions/AMConfigurator.html)

Configure shortcuts for all diagrams - symbolic and others.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AnyDiagramShortcutsConfigurator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[configureCommonActions](#configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String))([ActionsManager](../../../actions/ActionsManager.html) manager,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramType)`
Configure actions in given manager
`int`
`[getPriority](#getPriority())()`
Returns priority of this configurator.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.actions.[AMConfigurator](../../../actions/AMConfigurator.html)
`[configure](../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AnyDiagramShortcutsConfigurator
public AnyDiagramShortcutsConfigurator()
 ============ METHOD DETAIL ========== 
Method Details
configureCommonActions
public void configureCommonActions([ActionsManager](../../../actions/ActionsManager.html) manager,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramType)
Configure actions in given manager
Parameters:
`manager` - manager
`diagramType` - optional diagram type
getPriority
public int getPriority()
Description copied from interface: `[AMConfigurator](../../../actions/AMConfigurator.html#getPriority())`
Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such a case configurator must have lower priority than others.
 
 

 The default implementation returns #LOW_PRIORITY
Specified by:
`[getPriority](../../../actions/AMConfigurator.html#getPriority())` in interface `[AMConfigurator](../../../actions/AMConfigurator.html)`
Specified by:
`[getPriority](../../actions/ConfiguratorWithPriority.html#getPriority())` in interface `[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`
Specified by:
`[getPriority](../../../utils/PriorityProvider.html#getPriority())` in interface `[PriorityProvider](../../../utils/PriorityProvider.html)`
Returns:
priority of this configurator.
See Also:
[`PriorityProvider.HIGH_PRIORITY`](../../../utils/PriorityProvider.html#HIGH_PRIORITY)
[`PriorityProvider.MEDIUM_PRIORITY`](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)
[`PriorityProvider.LOW_PRIORITY`](../../../utils/PriorityProvider.html#LOW_PRIORITY)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.actions</a></div>
<h1 class="title" title="Class AnyDiagramShortcutsConfigurator">Class AnyDiagramShortcutsConfigurator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ui.actions.AnyDiagramShortcutsConfigurator</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code>, <code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="BaseDiagramShortcutsConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramShortcutsConfigurator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AnyDiagramShortcutsConfigurator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></span></div>
<div class="block">Configure shortcuts for all diagrams - symbolic and others.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AnyDiagramShortcutsConfigurator</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String)">configureCommonActions</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configure actions in given manager</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPriority()">getPriority</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns priority of this configurator.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.AMConfigurator">Methods inherited from interface com.nomagic.actions.<a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></h3>
<code><a href="../../../actions/AMConfigurator.html#configure(com.nomagic.actions.ActionsManager)">configure</a></code></div>
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
<h3>AnyDiagramShortcutsConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AnyDiagramShortcutsConfigurator</span>()</div>
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
<section class="detail" id="configureCommonActions(com.nomagic.actions.ActionsManager,java.lang.String)">
<h3>configureCommonActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configureCommonActions</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Configure actions in given manager</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager</dd>
<dd><code>diagramType</code> - optional diagram type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPriority()">
<h3>getPriority</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPriority</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="../../../actions/AMConfigurator.html#getPriority()">AMConfigurator</a></code></span></div>
<div class="block">Returns priority of this configurator. All configurators are sorted by priority before configuration.
 This is very important if one configurator expects input from other configurators.
 In such a case configurator must have lower priority than others.
 <br/><br/>
 The default implementation returns #LOW_PRIORITY</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../actions/AMConfigurator.html#getPriority()">getPriority</a></code> in interface <code><a href="../../../actions/AMConfigurator.html" title="interface in com.nomagic.actions">AMConfigurator</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../actions/ConfiguratorWithPriority.html#getPriority()">getPriority</a></code> in interface <code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../../../utils/PriorityProvider.html#getPriority()">getPriority</a></code> in interface <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
<dt>Returns:</dt>
<dd>priority of this configurator.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../../utils/PriorityProvider.html#HIGH_PRIORITY"><code>PriorityProvider.HIGH_PRIORITY</code></a></li>
<li><a href="../../../utils/PriorityProvider.html#MEDIUM_PRIORITY"><code>PriorityProvider.MEDIUM_PRIORITY</code></a></li>
<li><a href="../../../utils/PriorityProvider.html#LOW_PRIORITY"><code>PriorityProvider.LOW_PRIORITY</code></a></li>
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
