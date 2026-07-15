# JAVA OPENAPI: DependencyExtractor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/dependencymatrix/datamodel/cell/DependencyExtractor.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/cell/DependencyExtractor.html`
- source_sha256: `e1cef58c04c9f18dd559fdf2009d7ee2d36d96b9261a8ddb8ff116d8f29cbae5`
- captured_utc: `2026-07-14T16:55:13.753991+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.cell](package-summary.html)

## Interface DependencyExtractor

All Superinterfaces:
`[SmartListenerConfigProvider](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html)`

@OpenApiAllpublic interfaceDependencyExtractorextends [SmartListenerConfigProvider](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html)

Dependency extractors are used in Dependency Matrix to extract dependencies between two elements.
 Additionally they may provide element smart listener configurations, navigation menu items.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[clear](#clear())()`
Method clearing up all used resources and memory.
`default void`
`[createNavigationActions](#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory))([PersistenceManager](../../persistence/PersistenceManager.html) persistenceManager,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](AbstractMatrixCell.html) value,
 [ActionsCategory](../../../../actions/ActionsCategory.html) navigateCategory)`
Creates navigation actions for the dependencies created with this extractor
`default void`
`[createNavigationActions](#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory))([PersistenceManager](../../persistence/PersistenceManager.html) persistenceManager,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) row,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) column,
 [AbstractMatrixCell](AbstractMatrixCell.html) value,
 [ActionsCategory](../../../../actions/ActionsCategory.html) navigateCategory)`
Deprecated.
use [`createNavigationActions(PersistenceManager, ElementNode, ElementNode, AbstractMatrixCell, ActionsCategory)`](#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory))
`void`
`[elementUpdated](#elementUpdated(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> element)`
This element properties have been changed according to registered smart listeners.
`default [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)>`
`[getDependencies](#getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))([ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column)`
Extract and return dependencies between those two row and column elements
 which are used in creating new matrix cell
`default [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)>`
`[getDependencies](#getDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) row,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) column)`
Deprecated.
use [`getDependencies(ElementNode, ElementNode)`](#getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))
`void`
`[init](#init(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.task.ProgressStatus))([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ProgressStatus](../../../../task/ProgressStatus.html) status)`
This method is called when matrix settings are changed and whole matrix is being rebuilt.
Methods inherited from interface com.nomagic.uml2.ext.jmi.smartlistener.[SmartListenerConfigProvider](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html)
`[getListenerConfigurations](../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html#getListenerConfigurations())`

============ METHOD DETAIL ========== 
Method Details
init
void init([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 @CheckForNull
 [ProgressStatus](../../../../task/ProgressStatus.html) status)
This method is called when matrix settings are changed and whole matrix is being rebuilt.
 This way we can use it to update internal extractor settings according to new Dependency Matrix settings
Parameters:
`settings` - current matrix settings
`status` - progress status
getDependencies
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> getDependencies([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) row,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) column)
Deprecated.
use [`getDependencies(ElementNode, ElementNode)`](#getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode))
getDependencies
default [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[DependencyEntry](DependencyEntry.html)> getDependencies([ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column)
Extract and return dependencies between those two row and column elements
 which are used in creating new matrix cell
Parameters:
`row` - row element
`column` - column element
Returns:
list of extracted dependencies
createNavigationActions
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void createNavigationActions([PersistenceManager](../../persistence/PersistenceManager.html) persistenceManager,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) row,
 [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) column,
 [AbstractMatrixCell](AbstractMatrixCell.html) value,
 [ActionsCategory](../../../../actions/ActionsCategory.html) navigateCategory)
Deprecated.
use [`createNavigationActions(PersistenceManager, ElementNode, ElementNode, AbstractMatrixCell, ActionsCategory)`](#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory))
createNavigationActions
default void createNavigationActions([PersistenceManager](../../persistence/PersistenceManager.html) persistenceManager,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](AbstractMatrixCell.html) value,
 [ActionsCategory](../../../../actions/ActionsCategory.html) navigateCategory)
Creates navigation actions for the dependencies created with this extractor
Parameters:
`persistenceManager` - matrix settings
`row` - row element
`column` - column element
`value` - cell value
`navigateCategory` - navigate category from the right click
elementUpdated
void elementUpdated([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> element)
This element properties have been changed according to registered smart listeners. This method may be left empty,
 unless there are some cache or data structures which should be created on such event
Parameters:
`element` - updated elements
clear
void clear()
Method clearing up all used resources and memory.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.cell</a></div>
<h1 class="title" title="Interface DependencyExtractor">Interface DependencyExtractor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfigProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DependencyExtractor</span><span class="extends-implements">
extends <a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfigProvider</a></span></div>
<div class="block">Dependency extractors are used in Dependency Matrix to extract dependencies between two elements.
 Additionally they may provide element smart listener configurations, navigation menu items.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method clearing up all used resources and memory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory)">createNavigationActions</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> persistenceManager,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> value,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> navigateCategory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Creates navigation actions for the dependencies created with this extractor</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory)">createNavigationActions</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> persistenceManager,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> row,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> column,
 <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> value,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> navigateCategory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory)"><code>createNavigationActions(PersistenceManager, ElementNode, ElementNode, AbstractMatrixCell, ActionsCategory)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#elementUpdated(java.util.Collection)">elementUpdated</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This element properties have been changed according to registered smart listeners.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">getDependencies</a><wbr/>(<a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Extract and return dependencies between those two row and column elements
 which are used in creating new matrix cell</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#getDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getDependencies</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> row,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> column)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)"><code>getDependencies(ElementNode, ElementNode)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.task.ProgressStatus)">init</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is called when matrix settings are changed and whole matrix is being rebuilt.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfigProvider">Methods inherited from interface com.nomagic.uml2.ext.jmi.smartlistener.<a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html" title="interface in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfigProvider</a></h3>
<code><a href="../../../../uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html#getListenerConfigurations()">getListenerConfigurations</a></code></div>
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
<section class="detail" id="init(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.task.ProgressStatus)">
<h3>init</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 @CheckForNull
 <a href="../../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</span></div>
<div class="block">This method is called when matrix settings are changed and whole matrix is being rebuilt.
 This way we can use it to update internal extractor settings according to new Dependency Matrix settings</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>settings</code> - current matrix settings</dd>
<dd><code>status</code> - progress status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDependencies(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getDependencies</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</span> <span class="element-name">getDependencies</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> row,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> column)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)"><code>getDependencies(ElementNode, ElementNode)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDependencies(com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode)">
<h3>getDependencies</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="DependencyEntry.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyEntry</a>&gt;</span> <span class="element-name">getDependencies</span><wbr/><span class="parameters">(<a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column)</span></div>
<div class="block">Extract and return dependencies between those two row and column elements
 which are used in creating new matrix cell</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>row</code> - row element</dd>
<dd><code>column</code> - column element</dd>
<dt>Returns:</dt>
<dd>list of extracted dependencies</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory)">
<h3>createNavigationActions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">createNavigationActions</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> persistenceManager,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> row,
 <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> column,
 <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> value,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> navigateCategory)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory)"><code>createNavigationActions(PersistenceManager, ElementNode, ElementNode, AbstractMatrixCell, ActionsCategory)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="createNavigationActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory)">
<h3>createNavigationActions</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">createNavigationActions</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> persistenceManager,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> value,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> navigateCategory)</span></div>
<div class="block">Creates navigation actions for the dependencies created with this extractor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>persistenceManager</code> - matrix settings</dd>
<dd><code>row</code> - row element</dd>
<dd><code>column</code> - column element</dd>
<dd><code>value</code> - cell value</dd>
<dd><code>navigateCategory</code> - navigate category from the right click</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementUpdated(java.util.Collection)">
<h3>elementUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">elementUpdated</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; element)</span></div>
<div class="block">This element properties have been changed according to registered smart listeners. This method may be left empty,
 unless there are some cache or data structures which should be created on such event</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - updated elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">clear</span>()</div>
<div class="block">Method clearing up all used resources and memory.</div>
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
