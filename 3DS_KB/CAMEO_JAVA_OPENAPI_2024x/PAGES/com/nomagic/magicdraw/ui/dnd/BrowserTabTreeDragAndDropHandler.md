# JAVA OPENAPI: BrowserTabTreeDragAndDropHandler (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/dnd/BrowserTabTreeDragAndDropHandler.html
- source_path: `com/nomagic/magicdraw/ui/dnd/BrowserTabTreeDragAndDropHandler.html`
- source_sha256: `cf9bce450318162c01a29642ad16fa402a9bc7205a2306c25945e0428c0be9e0`
- captured_utc: `2026-07-14T16:52:05.499793+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dnd](package-summary.html)

## Interface BrowserTabTreeDragAndDropHandler

All Superinterfaces:
`[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`, `[PriorityProvider](../../../utils/PriorityProvider.html)`

@OpenApiAllpublic interfaceBrowserTabTreeDragAndDropHandlerextends [ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)

Enables to perform custom drop action on BrowserTabTree node.
 Use [`BrowserTabTreeDragAndDropHandlerFactory`](BrowserTabTreeDragAndDropHandlerFactory.html) and
 register it to [`BrowserTabTreeDragAndDropHandlerRegistry.register(BrowserTabTreeDragAndDropHandlerFactory)`](BrowserTabTreeDragAndDropHandlerRegistry.html#register(com.nomagic.magicdraw.ui.dnd.BrowserTabTreeDragAndDropHandlerFactory))

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[canImportToNode](#canImportToNode(com.nomagic.magicdraw.ui.browser.Node,javax.swing.TransferHandler.TransferSupport))([Node](../browser/Node.html) node,
 [TransferHandler.TransferSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html) support)`
Check whether the transfer information is valid to be imported to the node
`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getTransferredData](#getTransferredData(javax.swing.TransferHandler.TransferSupport))([TransferHandler.TransferSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html) support)`
Extract transferred data here.
`void`
`[importDataToNode](#importDataToNode(com.nomagic.magicdraw.ui.browser.Node,com.nomagic.magicdraw.ui.dnd.DroppedData,com.nomagic.magicdraw.ui.browser.Tree))([Node](../browser/Node.html) node,
 [DroppedData](DroppedData.html) droppedData,
 [Tree](../browser/Tree.html) tree)`
Does actual import of the data.
Methods inherited from interface com.nomagic.magicdraw.actions.[ConfiguratorWithPriority](../../actions/ConfiguratorWithPriority.html)
`[getPriority](../../actions/ConfiguratorWithPriority.html#getPriority())`

============ METHOD DETAIL ========== 
Method Details
canImportToNode
boolean canImportToNode([Node](../browser/Node.html) node,
 [TransferHandler.TransferSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html) support)
Check whether the transfer information is valid to be imported to the node
Parameters:
`node` - whether valid for importing
`support` - data that is being imported
Returns:
true if possible to import to node
getTransferredData
@CheckForNull[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getTransferredData([TransferHandler.TransferSupport](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html) support)
Extract transferred data here. TransferSupport can not be later accessed in importDataToNode method.
 If you return null here, then drop operation will be rejected
Parameters:
`support` - transfer support
Returns:
object that will be accessible as droppedData.getTransferredData() in importDataToNode method
importDataToNode
void importDataToNode([Node](../browser/Node.html) node,
 [DroppedData](DroppedData.html) droppedData,
 [Tree](../browser/Tree.html) tree)
Does actual import of the data. Called after drop is complete to enable displaying GUI components during the import
Parameters:
`node` - node to drop data on
`droppedData` - holds transferred data and some additional info from the TransferSupport, since TransferSupport is no longer available
`tree` - tree to which the node belongs

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dnd</a></div>
<h1 class="title" title="Interface BrowserTabTreeDragAndDropHandler">Interface BrowserTabTreeDragAndDropHandler</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BrowserTabTreeDragAndDropHandler</span><span class="extends-implements">
extends <a href="../../actions/ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></span></div>
<div class="block">Enables to perform custom drop action on BrowserTabTree node.
 Use <a href="BrowserTabTreeDragAndDropHandlerFactory.html" title="interface in com.nomagic.magicdraw.ui.dnd"><code>BrowserTabTreeDragAndDropHandlerFactory</code></a> and
 register it to <a href="BrowserTabTreeDragAndDropHandlerRegistry.html#register(com.nomagic.magicdraw.ui.dnd.BrowserTabTreeDragAndDropHandlerFactory)"><code>BrowserTabTreeDragAndDropHandlerRegistry.register(BrowserTabTreeDragAndDropHandlerFactory)</code></a></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canImportToNode(com.nomagic.magicdraw.ui.browser.Node,javax.swing.TransferHandler.TransferSupport)">canImportToNode</a><wbr/>(<a href="../browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing">TransferHandler.TransferSupport</a> support)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check whether the transfer information is valid to be imported to the node</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTransferredData(javax.swing.TransferHandler.TransferSupport)">getTransferredData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing">TransferHandler.TransferSupport</a> support)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Extract transferred data here.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importDataToNode(com.nomagic.magicdraw.ui.browser.Node,com.nomagic.magicdraw.ui.dnd.DroppedData,com.nomagic.magicdraw.ui.browser.Tree)">importDataToNode</a><wbr/>(<a href="../browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a href="DroppedData.html" title="class in com.nomagic.magicdraw.ui.dnd">DroppedData</a> droppedData,
 <a href="../browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Does actual import of the data.</div>
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
<section class="detail" id="canImportToNode(com.nomagic.magicdraw.ui.browser.Node,javax.swing.TransferHandler.TransferSupport)">
<h3>canImportToNode</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canImportToNode</span><wbr/><span class="parameters">(<a href="../browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing">TransferHandler.TransferSupport</a> support)</span></div>
<div class="block">Check whether the transfer information is valid to be imported to the node</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - whether valid for importing</dd>
<dd><code>support</code> - data that is being imported</dd>
<dt>Returns:</dt>
<dd>true if possible to import to node</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransferredData(javax.swing.TransferHandler.TransferSupport)">
<h3>getTransferredData</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getTransferredData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/TransferHandler.TransferSupport.html" title="class or interface in javax.swing">TransferHandler.TransferSupport</a> support)</span></div>
<div class="block">Extract transferred data here. TransferSupport can not be later accessed in importDataToNode method.
 If you return null here, then drop operation will be rejected</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>support</code> - transfer support</dd>
<dt>Returns:</dt>
<dd>object that will be accessible as droppedData.getTransferredData() in importDataToNode method</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importDataToNode(com.nomagic.magicdraw.ui.browser.Node,com.nomagic.magicdraw.ui.dnd.DroppedData,com.nomagic.magicdraw.ui.browser.Tree)">
<h3>importDataToNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">importDataToNode</span><wbr/><span class="parameters">(<a href="../browser/Node.html" title="class in com.nomagic.magicdraw.ui.browser">Node</a> node,
 <a href="DroppedData.html" title="class in com.nomagic.magicdraw.ui.dnd">DroppedData</a> droppedData,
 <a href="../browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
<div class="block">Does actual import of the data. Called after drop is complete to enable displaying GUI components during the import</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - node to drop data on</dd>
<dd><code>droppedData</code> - holds transferred data and some additional info from the TransferSupport, since TransferSupport is no longer available</dd>
<dd><code>tree</code> - tree to which the node belongs</dd>
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
