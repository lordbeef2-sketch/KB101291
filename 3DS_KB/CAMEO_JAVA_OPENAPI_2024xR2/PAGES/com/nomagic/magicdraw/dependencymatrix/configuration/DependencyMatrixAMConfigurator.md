# JAVA OPENAPI: DependencyMatrixAMConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/dependencymatrix/configuration/DependencyMatrixAMConfigurator.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/configuration/DependencyMatrixAMConfigurator.html`
- source_sha256: `72782f0818a105be9daab9a62674b056668ff06a51353adc79b2e7a43d9a3160`
- captured_utc: `2026-07-14T16:55:12.704984+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.configuration](package-summary.html)

## Interface DependencyMatrixAMConfigurator

All Superinterfaces:
`[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

@OpenApiAllpublic interfaceDependencyMatrixAMConfiguratorextends [ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)

Configurator interface used to customize Dependency matrix row, column and filter panel menu actions.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`default void`
`[configure](#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,java.util.Collection,boolean))([ActionsManager](../../../actions/ActionsManager.html) manager,
 [PersistenceManager](../persistence/PersistenceManager.html) settings,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean forRow)`
Deprecated.
use {@link DependencyMatrixAMConfigurator#configure(com.nomagic.actions.ActionsManager, java.util.Collection, boolean, com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager))
`default void`
`[configure](#configure(com.nomagic.actions.ActionsManager,java.util.Collection,boolean,com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager))([ActionsManager](../../../actions/ActionsManager.html) manager,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](../datamodel/ElementNode.html)> elementNodes,
 boolean forRow,
 [PersistenceManager](../persistence/PersistenceManager.html) settings)`
Method for configuring context menu actions.
Methods inherited from interface com.nomagic.magicdraw.actions.[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)
`[getPriority](../../actions/ConfiguratorWithPriority.html#getPriority())`

============ METHOD DETAIL ========== 
Method Details
configure
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void configure([ActionsManager](../../../actions/ActionsManager.html) manager,
 [PersistenceManager](../persistence/PersistenceManager.html) settings,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 boolean forRow)
Deprecated.
use {@link DependencyMatrixAMConfigurator#configure(com.nomagic.actions.ActionsManager, java.util.Collection, boolean, com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager))
configure
default void configure([ActionsManager](../../../actions/ActionsManager.html) manager,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[ElementNode](../datamodel/ElementNode.html)> elementNodes,
 boolean forRow,
 [PersistenceManager](../persistence/PersistenceManager.html) settings)
Method for configuring context menu actions. During this call, new actions can be added to dependency matrix menu.
 Also existing actions can be removed from the given manager.
 
 Using this configurator three menu types may be configured: row element menu, column element menu, filter area
 menu. If `elements` collection is empty - the click was on the filter area, otherwise
 `forRow` variable shows if it is row or column elements.
Parameters:
`manager` - manager to be configured.
`elementNodes` - currently selected row or column nodes
`forRow` - true if configuring actions for selected rows, false - for selected column nodes
`settings` - dependency Matrix Settings

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.configuration</a></div>
<h1 class="title" title="Interface DependencyMatrixAMConfigurator">Interface DependencyMatrixAMConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DependencyMatrixAMConfigurator</span><span class="extends-implements">
extends <a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></span></div>
<div class="block">Configurator interface used to customize Dependency matrix row, column and filter panel menu actions.</div>
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
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,java.util.Collection,boolean)">configure</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean forRow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link DependencyMatrixAMConfigurator#configure(com.nomagic.actions.ActionsManager, java.util.Collection, boolean, com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager))</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager,java.util.Collection,boolean,com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager)">configure</a><wbr/>(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt; elementNodes,
 boolean forRow,
 <a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Method for configuring context menu actions.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.ConfiguratorWithPriority">Methods inherited from interface com.nomagic.magicdraw.actions.<a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></h3>
<code><a href="../../actions/ConfiguratorWithPriority.html#getPriority()">getPriority</a></code></div>
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
<section class="detail" id="configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,java.util.Collection,boolean)">
<h3>configure</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 boolean forRow)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use {@link DependencyMatrixAMConfigurator#configure(com.nomagic.actions.ActionsManager, java.util.Collection, boolean, com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager))</div>
</div>
</section>
</li>
<li>
<section class="detail" id="configure(com.nomagic.actions.ActionsManager,java.util.Collection,boolean,com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager)">
<h3>configure</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a>&gt; elementNodes,
 boolean forRow,
 <a href="../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings)</span></div>
<div class="block">Method for configuring context menu actions. During this call, new actions can be added to dependency matrix menu.
 Also existing actions can be removed from the given manager.
 <p></p>
 Using this configurator three menu types may be configured: row element menu, column element menu, filter area
 menu. If <code>elements</code> collection is empty - the click was on the filter area, otherwise
 <code>forRow</code> variable shows if it is row or column elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - manager to be configured.</dd>
<dd><code>elementNodes</code> - currently selected row or column nodes</dd>
<dd><code>forRow</code> - true if configuring actions for selected rows, false - for selected column nodes</dd>
<dd><code>settings</code> - dependency Matrix Settings</dd>
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
