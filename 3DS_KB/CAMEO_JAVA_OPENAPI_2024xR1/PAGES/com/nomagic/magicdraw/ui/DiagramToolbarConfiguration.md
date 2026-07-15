# JAVA OPENAPI: DiagramToolbarConfiguration (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/ui/DiagramToolbarConfiguration.html
- source_path: `com/nomagic/magicdraw/ui/DiagramToolbarConfiguration.html`
- source_sha256: `ce89b1407309a6d6a02b10353935cf3a9ffceec49c9014b67975a7fb05c0fdea`
- captured_utc: `2026-07-14T16:52:00.536728+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Class DiagramToolbarConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.actions.ActionsManager](../../actions/ActionsManager.html)
[com.nomagic.magicdraw.actions.MDActionsManager](../actions/MDActionsManager.html)
com.nomagic.magicdraw.ui.DiagramToolbarConfiguration

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classDiagramToolbarConfiguration
extends [MDActionsManager](../actions/MDActionsManager.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.actions.[ActionsManager](../../actions/ActionsManager.html)
`[ActionsManager.ActionPropertyChangeListener](../../actions/ActionsManager.ActionPropertyChangeListener.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.actions.[ActionsManager](../../actions/ActionsManager.html)
`[SHORTCUTS_MODIFIED](../../actions/ActionsManager.html#SHORTCUTS_MODIFIED)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramToolbarConfiguration](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addCustomDiagramToolbarCategory](#addCustomDiagramToolbarCategory(com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration))([DiagramInnerToolbarConfiguration](../actions/DiagramInnerToolbarConfiguration.html) category)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](../../actions/NMAction.html)>`
`[getSortedActions](#getSortedActions())()`
Methods inherited from class com.nomagic.actions.[ActionsManager](../../actions/ActionsManager.html)
`[addActionNearTheGiven](../../actions/ActionsManager.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)), [addActionNearTheGiven](../../actions/ActionsManager.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction,com.nomagic.actions.ActionsCategory)), [addCategory](../../actions/ActionsManager.html#addCategory(int,com.nomagic.actions.ActionsCategory)), [addCategory](../../actions/ActionsManager.html#addCategory(com.nomagic.actions.ActionsCategory)), [addCategory](../../actions/ActionsManager.html#addCategory(com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,boolean)), [addCategory](../../actions/ActionsManager.html#addCategory(java.lang.String,com.nomagic.actions.ActionsCategory,boolean)), [constructNoneAction](../../actions/ActionsManager.html#constructNoneAction()), [dropCache](../../actions/ActionsManager.html#dropCache()), [forEach](../../actions/ActionsManager.html#forEach(java.util.function.Consumer)), [forEachIncludingSelf](../../actions/ActionsManager.html#forEachIncludingSelf(java.util.function.Consumer)), [getActionFor](../../actions/ActionsManager.html#getActionFor(java.lang.String)), [getActionFor](../../actions/ActionsManager.html#getActionFor(javax.swing.KeyStroke)), [getActionParent](../../actions/ActionsManager.html#getActionParent(com.nomagic.actions.NMAction)), [getActionsCategoryRecursively](../../actions/ActionsManager.html#getActionsCategoryRecursively(java.util.List,java.lang.String)), [getAllActions](../../actions/ActionsManager.html#getAllActions()), [getAllOrderedActions](../../actions/ActionsManager.html#getAllOrderedActions(boolean)), [getCategories](../../actions/ActionsManager.html#getCategories()), [getCategory](../../actions/ActionsManager.html#getCategory(java.lang.String)), [getIdToActionMap](../../actions/ActionsManager.html#getIdToActionMap()), [getLastActionsCategory](../../actions/ActionsManager.html#getLastActionsCategory()), [getParent](../../actions/ActionsManager.html#getParent()), [isEmpty](../../actions/ActionsManager.html#isEmpty()), [makeCopy](../../actions/ActionsManager.html#makeCopy()), [markShortcutsModified](../../actions/ActionsManager.html#markShortcutsModified(javax.swing.Action)), [removeAction](../../actions/ActionsManager.html#removeAction(com.nomagic.actions.NMAction)), [removeAction](../../actions/ActionsManager.html#removeAction(com.nomagic.actions.NMAction,com.nomagic.actions.NMAction)), [removeAction](../../actions/ActionsManager.html#removeAction(java.lang.String)), [removeAllActions](../../actions/ActionsManager.html#removeAllActions()), [removeCategory](../../actions/ActionsManager.html#removeCategory(com.nomagic.actions.ActionsCategory)), [removeIf](../../actions/ActionsManager.html#removeIf(java.util.function.Predicate)), [setCategories](../../actions/ActionsManager.html#setCategories(java.util.List)), [setParent](../../actions/ActionsManager.html#setParent(com.nomagic.actions.ActionsManager)), [updateCommandKeysFrom](../../actions/ActionsManager.html#updateCommandKeysFrom(com.nomagic.actions.ActionsManager)), [updateShortcutsFrom](../../actions/ActionsManager.html#updateShortcutsFrom(com.nomagic.actions.ActionsManager)), [updateStateForAllActions](../../actions/ActionsManager.html#updateStateForAllActions())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramToolbarConfiguration
public DiagramToolbarConfiguration()
 ============ METHOD DETAIL ========== 
Method Details
getSortedActions
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[NMAction](../../actions/NMAction.html)> getSortedActions()
addCustomDiagramToolbarCategory
public void addCustomDiagramToolbarCategory([DiagramInnerToolbarConfiguration](../actions/DiagramInnerToolbarConfiguration.html) category)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Class DiagramToolbarConfiguration">Class DiagramToolbarConfiguration</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">com.nomagic.actions.ActionsManager</a>
<div class="inheritance"><a href="../actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">com.nomagic.magicdraw.actions.MDActionsManager</a>
<div class="inheritance">com.nomagic.magicdraw.ui.DiagramToolbarConfiguration</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramToolbarConfiguration</span>
<span class="extends-implements">extends <a href="../actions/MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.actions.ActionsManager">Nested classes/interfaces inherited from class com.nomagic.actions.<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></h2>
<code><a href="../../actions/ActionsManager.ActionPropertyChangeListener.html" title="class in com.nomagic.actions">ActionsManager.ActionPropertyChangeListener</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.actions.ActionsManager">Fields inherited from class com.nomagic.actions.<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></h3>
<code><a href="../../actions/ActionsManager.html#SHORTCUTS_MODIFIED">SHORTCUTS_MODIFIED</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramToolbarConfiguration</a>()</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCustomDiagramToolbarCategory(com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration)">addCustomDiagramToolbarCategory</a><wbr/>(<a href="../actions/DiagramInnerToolbarConfiguration.html" title="class in com.nomagic.magicdraw.actions">DiagramInnerToolbarConfiguration</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSortedActions()">getSortedActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.actions.ActionsManager">Methods inherited from class com.nomagic.actions.<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></h3>
<code><a href="../../actions/ActionsManager.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction)">addActionNearTheGiven</a>, <a href="../../actions/ActionsManager.html#addActionNearTheGiven(java.lang.String,boolean,com.nomagic.actions.NMAction,com.nomagic.actions.ActionsCategory)">addActionNearTheGiven</a>, <a href="../../actions/ActionsManager.html#addCategory(int,com.nomagic.actions.ActionsCategory)">addCategory</a>, <a href="../../actions/ActionsManager.html#addCategory(com.nomagic.actions.ActionsCategory)">addCategory</a>, <a href="../../actions/ActionsManager.html#addCategory(com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,boolean)">addCategory</a>, <a href="../../actions/ActionsManager.html#addCategory(java.lang.String,com.nomagic.actions.ActionsCategory,boolean)">addCategory</a>, <a href="../../actions/ActionsManager.html#constructNoneAction()">constructNoneAction</a>, <a href="../../actions/ActionsManager.html#dropCache()">dropCache</a>, <a href="../../actions/ActionsManager.html#forEach(java.util.function.Consumer)">forEach</a>, <a href="../../actions/ActionsManager.html#forEachIncludingSelf(java.util.function.Consumer)">forEachIncludingSelf</a>, <a href="../../actions/ActionsManager.html#getActionFor(java.lang.String)">getActionFor</a>, <a href="../../actions/ActionsManager.html#getActionFor(javax.swing.KeyStroke)">getActionFor</a>, <a href="../../actions/ActionsManager.html#getActionParent(com.nomagic.actions.NMAction)">getActionParent</a>, <a href="../../actions/ActionsManager.html#getActionsCategoryRecursively(java.util.List,java.lang.String)">getActionsCategoryRecursively</a>, <a href="../../actions/ActionsManager.html#getAllActions()">getAllActions</a>, <a href="../../actions/ActionsManager.html#getAllOrderedActions(boolean)">getAllOrderedActions</a>, <a href="../../actions/ActionsManager.html#getCategories()">getCategories</a>, <a href="../../actions/ActionsManager.html#getCategory(java.lang.String)">getCategory</a>, <a href="../../actions/ActionsManager.html#getIdToActionMap()">getIdToActionMap</a>, <a href="../../actions/ActionsManager.html#getLastActionsCategory()">getLastActionsCategory</a>, <a href="../../actions/ActionsManager.html#getParent()">getParent</a>, <a href="../../actions/ActionsManager.html#isEmpty()">isEmpty</a>, <a href="../../actions/ActionsManager.html#makeCopy()">makeCopy</a>, <a href="../../actions/ActionsManager.html#markShortcutsModified(javax.swing.Action)">markShortcutsModified</a>, <a href="../../actions/ActionsManager.html#removeAction(com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../actions/ActionsManager.html#removeAction(com.nomagic.actions.NMAction,com.nomagic.actions.NMAction)">removeAction</a>, <a href="../../actions/ActionsManager.html#removeAction(java.lang.String)">removeAction</a>, <a href="../../actions/ActionsManager.html#removeAllActions()">removeAllActions</a>, <a href="../../actions/ActionsManager.html#removeCategory(com.nomagic.actions.ActionsCategory)">removeCategory</a>, <a href="../../actions/ActionsManager.html#removeIf(java.util.function.Predicate)">removeIf</a>, <a href="../../actions/ActionsManager.html#setCategories(java.util.List)">setCategories</a>, <a href="../../actions/ActionsManager.html#setParent(com.nomagic.actions.ActionsManager)">setParent</a>, <a href="../../actions/ActionsManager.html#updateCommandKeysFrom(com.nomagic.actions.ActionsManager)">updateCommandKeysFrom</a>, <a href="../../actions/ActionsManager.html#updateShortcutsFrom(com.nomagic.actions.ActionsManager)">updateShortcutsFrom</a>, <a href="../../actions/ActionsManager.html#updateStateForAllActions()">updateStateForAllActions</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>DiagramToolbarConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramToolbarConfiguration</span>()</div>
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
<section class="detail" id="getSortedActions()">
<h3>getSortedActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../actions/NMAction.html" title="class in com.nomagic.actions">NMAction</a>&gt;</span> <span class="element-name">getSortedActions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addCustomDiagramToolbarCategory(com.nomagic.magicdraw.actions.DiagramInnerToolbarConfiguration)">
<h3>addCustomDiagramToolbarCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCustomDiagramToolbarCategory</span><wbr/><span class="parameters">(<a href="../actions/DiagramInnerToolbarConfiguration.html" title="class in com.nomagic.magicdraw.actions">DiagramInnerToolbarConfiguration</a> category)</span></div>
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
