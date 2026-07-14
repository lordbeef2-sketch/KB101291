# JAVA OPENAPI: DependencyMatrixActionRegistry (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/dependencymatrix/configuration/DependencyMatrixActionRegistry.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/configuration/DependencyMatrixActionRegistry.html`
- source_sha256: `1529aa4f0525aa3624f05cb91b46785e8dbdc991fc3fd5175b4a1622e48dec6b`
- captured_utc: `2026-07-14T16:51:16.583143+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.configuration](package-summary.html)

## Class DependencyMatrixActionRegistry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixActionRegistry

@OpenApiAllpublic classDependencyMatrixActionRegistry
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Dependency matrix action registry - manages all configurators, which configures all actions which are applicable
 for dependency matrix, including filter area panel, and row/column elements. Users may get instance and add additional
 configurators which add remove actions according to element and matrix element provided.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DependencyMatrixActionRegistry](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addCellContextAMConfigurator](#addCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixCellAMConfigurator))([DependencyMatrixCellAMConfigurator](DependencyMatrixCellAMConfigurator.html) configurator)`

`void`
`[addContextConfigurator](#addContextConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixAMConfigurator))([DependencyMatrixAMConfigurator](DependencyMatrixAMConfigurator.html) configurator)`
Registers new configurator for dependency matrix action registry
`[ActionsManager](../../../actions/ActionsManager.html)`
`[configureCellContextAMConfigurator](#configureCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.ui.DependencyMatrixSelection))([PersistenceManager](../persistence/PersistenceManager.html) settings,
 [DependencyMatrixSelection](../ui/DependencyMatrixSelection.html) selection)`

`[ActionsManager](../../../actions/ActionsManager.html)`
`[configureContextActions](#configureContextActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,java.util.Collection,boolean))([PersistenceManager](../persistence/PersistenceManager.html) settings,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](../datamodel/ElementNode.html)> elementNodes,
 boolean forRow)`
Creates new Action manager and configures it with all registered row/column configurators
`static [DependencyMatrixActionRegistry](DependencyMatrixActionRegistry.html)`
`[getInstance](#getInstance())()`

`void`
`[removeCellContextAMConfigurator](#removeCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixCellAMConfigurator))([DependencyMatrixCellAMConfigurator](DependencyMatrixCellAMConfigurator.html) configurator)`

`void`
`[removeContextConfigurator](#removeContextConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixAMConfigurator))([DependencyMatrixAMConfigurator](DependencyMatrixAMConfigurator.html) configurator)`
Removes context configurator from the registry
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DependencyMatrixActionRegistry
public DependencyMatrixActionRegistry()
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [DependencyMatrixActionRegistry](DependencyMatrixActionRegistry.html) getInstance()
addContextConfigurator
public void addContextConfigurator([DependencyMatrixAMConfigurator](DependencyMatrixAMConfigurator.html) configurator)
Registers new configurator for dependency matrix action registry
Parameters:
`configurator` - configurator
removeContextConfigurator
public void removeContextConfigurator([DependencyMatrixAMConfigurator](DependencyMatrixAMConfigurator.html) configurator)
Removes context configurator from the registry
Parameters:
`configurator` - configurator to remove
configureContextActions
public [ActionsManager](../../../actions/ActionsManager.html) configureContextActions([PersistenceManager](../persistence/PersistenceManager.html) settings,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](../datamodel/ElementNode.html)> elementNodes,
 boolean forRow)
Creates new Action manager and configures it with all registered row/column configurators
Parameters:
`elementNodes` - describes currently selected nodes and cells in matrix
`forRow` - true if actions are configured for rows, false if for columns
`settings` - matrix settings
Returns:
new configured [`ActionsManager`](../../../actions/ActionsManager.html) instance
addCellContextAMConfigurator
public void addCellContextAMConfigurator([DependencyMatrixCellAMConfigurator](DependencyMatrixCellAMConfigurator.html) configurator)
removeCellContextAMConfigurator
public void removeCellContextAMConfigurator([DependencyMatrixCellAMConfigurator](DependencyMatrixCellAMConfigurator.html) configurator)
configureCellContextAMConfigurator
public [ActionsManager](../../../actions/ActionsManager.html) configureCellContextAMConfigurator([PersistenceManager](../persistence/PersistenceManager.html) settings,
 [DependencyMatrixSelection](../ui/DependencyMatrixSelection.html) selection)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.configuration</a></div>
<h1 class="title" title="Class DependencyMatrixActionRegistry">Class DependencyMatrixActionRegistry</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixActionRegistry</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DependencyMatrixActionRegistry</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Dependency matrix action registry - manages all configurators, which configures all actions which are applicable
 for dependency matrix, including filter area panel, and row/column elements. Users may get instance and add additional
 configurators which add remove actions according to element and matrix element provided.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DependencyMatrixActionRegistry</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixCellAMConfigurator)">addCellContextAMConfigurator</a><wbr/>(<a href="DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContextConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixAMConfigurator)">addContextConfigurator</a><wbr/>(<a href="DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers new configurator for dependency matrix action registry</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.ui.DependencyMatrixSelection)">configureCellContextAMConfigurator</a><wbr/>(<a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ui/DependencyMatrixSelection.html" title="interface in com.nomagic.magicdraw.dependencymatrix.ui">DependencyMatrixSelection</a> selection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureContextActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,java.util.Collection,boolean)">configureContextActions</a><wbr/>(<a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt; elementNodes,
 boolean forRow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates new Action manager and configures it with all registered row/column configurators</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyMatrixActionRegistry.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixActionRegistry</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixCellAMConfigurator)">removeCellContextAMConfigurator</a><wbr/>(<a href="DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeContextConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixAMConfigurator)">removeContextConfigurator</a><wbr/>(<a href="DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes context configurator from the registry</div>
</div>
</div>
</div>
</div>
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
<h3>DependencyMatrixActionRegistry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DependencyMatrixActionRegistry</span>()</div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyMatrixActionRegistry.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixActionRegistry</a></span> <span class="element-name">getInstance</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addContextConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixAMConfigurator)">
<h3>addContextConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addContextConfigurator</span><wbr/><span class="parameters">(<a href="DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a> configurator)</span></div>
<div class="block">Registers new configurator for dependency matrix action registry</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeContextConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixAMConfigurator)">
<h3>removeContextConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeContextConfigurator</span><wbr/><span class="parameters">(<a href="DependencyMatrixAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixAMConfigurator</a> configurator)</span></div>
<div class="block">Removes context configurator from the registry</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - configurator to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureContextActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,java.util.Collection,boolean)">
<h3>configureContextActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">configureContextActions</span><wbr/><span class="parameters">(<a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt; elementNodes,
 boolean forRow)</span></div>
<div class="block">Creates new Action manager and configures it with all registered row/column configurators</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementNodes</code> - describes currently selected nodes and cells in matrix</dd>
<dd><code>forRow</code> - true if actions are configured for rows, false if for columns</dd>
<dd><code>settings</code> - matrix settings</dd>
<dt>Returns:</dt>
<dd>new configured <a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions"><code>ActionsManager</code></a> instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixCellAMConfigurator)">
<h3>addCellContextAMConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addCellContextAMConfigurator</span><wbr/><span class="parameters">(<a href="DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a> configurator)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixCellAMConfigurator)">
<h3>removeCellContextAMConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeCellContextAMConfigurator</span><wbr/><span class="parameters">(<a href="DependencyMatrixCellAMConfigurator.html" title="interface in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixCellAMConfigurator</a> configurator)</span></div>
</section>
</li>
<li>
<section class="detail" id="configureCellContextAMConfigurator(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.ui.DependencyMatrixSelection)">
<h3>configureCellContextAMConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a></span> <span class="element-name">configureCellContextAMConfigurator</span><wbr/><span class="parameters">(<a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ui/DependencyMatrixSelection.html" title="interface in com.nomagic.magicdraw.dependencymatrix.ui">DependencyMatrixSelection</a> selection)</span></div>
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
