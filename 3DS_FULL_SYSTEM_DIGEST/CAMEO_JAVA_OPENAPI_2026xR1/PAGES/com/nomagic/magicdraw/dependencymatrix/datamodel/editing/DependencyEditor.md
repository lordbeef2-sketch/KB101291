# JAVA OPENAPI: DependencyEditor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/dependencymatrix/datamodel/editing/DependencyEditor.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/datamodel/editing/DependencyEditor.html`
- source_sha256: `af0c7a55cfca7796ccf0c971c4a79257a93c7cd10d5e146e6f11cec0914a9190`
- captured_utc: `2026-07-14T16:45:32.070430+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.datamodel.editing](package-summary.html)

## Interface DependencyEditor

@OpenApiAllpublic interfaceDependencyEditor
Interface for mechanism, which is used to edit dependency matrix.
 
 Value editors may be registered inside `MatrixFactory`
 Value editors define which matrix cells are editable, and may add new add/remove dependency actions
 according to provided context
 
 NOTE: if `canCreate` returns `false`, no menu items
 will be created using `createAddActions`. The same applies to `canEdit`
 and `createEditActions` methods

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[canCreate](#canCreate(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell))([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell)`
Analyze specific cell and decides if there is any new dependencies which can be created for this pair of elements
`boolean`
`[canEdit](#canEdit(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell))([PersistenceManager](../../persistence/PersistenceManager.html) persistenceManager,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell)`
Analyze current cell, and decide if this there are at least one dependency, which can be deleted/edited.
`void`
`[clear](#clear())()`
Purpose of this method to clean up all unnecessary cache and objects
`void`
`[createAddActions](#createAddActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory))([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell,
 [ActionsCategory](../../../../actions/ActionsCategory.html) mainCategory,
 [ActionsCategory](../../../../actions/ActionsCategory.html) rowToColumn,
 [ActionsCategory](../../../../actions/ActionsCategory.html) columnToRow)`
Used to edit specific cell action categories when user initiates add relationships actions.
`void`
`[createEditActions](#createEditActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory))([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell,
 [ActionsCategory](../../../../actions/ActionsCategory.html) main,
 [ActionsCategory](../../../../actions/ActionsCategory.html) deleteActions)`
Analyze current cell, and create actions which can remove/edit specific dependencies from this cell
`void`
`[elementUpdated](#elementUpdated(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> element)`
This method is triggered when elements are updated but Build is not initiated.
`void`
`[init](#init(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.task.ProgressStatus))([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ProgressStatus](../../../../task/ProgressStatus.html) status)`
Initializes value editor.

============ METHOD DETAIL ========== 
Method Details
init
void init([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 @CheckForNull
 [ProgressStatus](../../../../task/ProgressStatus.html) status)
Initializes value editor. This method is executed during matrix rebuild
Parameters:
`settings` - matrix settings
`status` - progress status
createAddActions
void createAddActions([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell,
 [ActionsCategory](../../../../actions/ActionsCategory.html) mainCategory,
 [ActionsCategory](../../../../actions/ActionsCategory.html) rowToColumn,
 [ActionsCategory](../../../../actions/ActionsCategory.html) columnToRow)
Used to edit specific cell action categories when user initiates add relationships actions. It may be either
 popup menu items or double click action
Parameters:
`settings` - matrix settings
`row` - row element
`column` - column element
`cell` - cell value
`mainCategory` - whole menu category
`rowToColumn` - column to row dependency category
`columnToRow` - row to column dependency category
createEditActions
void createEditActions([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell,
 [ActionsCategory](../../../../actions/ActionsCategory.html) main,
 [ActionsCategory](../../../../actions/ActionsCategory.html) deleteActions)
Analyze current cell, and create actions which can remove/edit specific dependencies from this cell
Parameters:
`settings` - matrix settings
`row` - row element
`column` - column element
`cell` - current cell
`main` - main action category
`deleteActions` - add remove dependency actions to this category
canCreate
boolean canCreate([PersistenceManager](../../persistence/PersistenceManager.html) settings,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 @CheckForNull
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell)
Analyze specific cell and decides if there is any new dependencies which can be created for this pair of elements
 
 IMPORTANT: Make this method as fast as possible. Performance of this method highly influences overall performance of
 the Dependency matrix component
Parameters:
`settings` - matrix settings
`row` - row element
`column` - column element
`cell` - matrix cell
Returns:
`true` if at least one relation can be created
canEdit
boolean canEdit([PersistenceManager](../../persistence/PersistenceManager.html) persistenceManager,
 [ElementNode](../ElementNode.html) row,
 [ElementNode](../ElementNode.html) column,
 [AbstractMatrixCell](../cell/AbstractMatrixCell.html) cell)
Analyze current cell, and decide if this there are at least one dependency, which can be deleted/edited.
 
 IMPORTANT: Make this method as fast as possible. Performance of this method highly influences overall performance of
 the Dependency matrix component
Parameters:
`persistenceManager` - matrix settings
`row` - row element
`column` - column element
`cell` - matrix cell
Returns:
`true` if there is at least one dependency which can be deleted.
elementUpdated
void elementUpdated([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> element)
This method is triggered when elements are updated but Build is not initiated. All caches should be cleared
Parameters:
`element` - updated element
clear
void clear()
Purpose of this method to clean up all unnecessary cache and objects

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.datamodel.editing</a></div>
<h1 class="title" title="Interface DependencyEditor">Interface DependencyEditor</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DependencyEditor</span></div>
<div class="block">Interface for mechanism, which is used to edit dependency matrix.
 <p></p>
 Value editors may be registered inside <code>MatrixFactory</code>
 Value editors define which matrix cells are editable, and may add new add/remove dependency actions
 according to provided context
 <p></p>
 NOTE: if <code>canCreate</code> returns <code>false</code>, no menu items
 will be created using <code>createAddActions</code>. The same applies to <code>canEdit</code>
 and <code>createEditActions</code> methods</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canCreate(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">canCreate</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Analyze specific cell and decides if there is any new dependencies which can be created for this pair of elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canEdit(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">canEdit</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> persistenceManager,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Analyze current cell, and decide if this there are at least one dependency, which can be deleted/edited.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Purpose of this method to clean up all unnecessary cache and objects</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createAddActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory)">createAddActions</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> mainCategory,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> rowToColumn,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> columnToRow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Used to edit specific cell action categories when user initiates add relationships actions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createEditActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory)">createEditActions</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> main,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> deleteActions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Analyze current cell, and create actions which can remove/edit specific dependencies from this cell</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#elementUpdated(java.util.Collection)">elementUpdated</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is triggered when elements are updated but Build is not initiated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.task.ProgressStatus)">init</a><wbr/>(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Initializes value editor.</div>
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
<div class="block">Initializes value editor. This method is executed during matrix rebuild</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>settings</code> - matrix settings</dd>
<dd><code>status</code> - progress status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAddActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory)">
<h3>createAddActions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">createAddActions</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> mainCategory,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> rowToColumn,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> columnToRow)</span></div>
<div class="block">Used to edit specific cell action categories when user initiates add relationships actions. It may be either
 popup menu items or double click action</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>settings</code> - matrix settings</dd>
<dd><code>row</code> - row element</dd>
<dd><code>column</code> - column element</dd>
<dd><code>cell</code> - cell value</dd>
<dd><code>mainCategory</code> - whole menu category</dd>
<dd><code>rowToColumn</code> - column to row dependency category</dd>
<dd><code>columnToRow</code> - row to column dependency category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEditActions(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell,com.nomagic.actions.ActionsCategory,com.nomagic.actions.ActionsCategory)">
<h3>createEditActions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">createEditActions</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> main,
 <a href="../../../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> deleteActions)</span></div>
<div class="block">Analyze current cell, and create actions which can remove/edit specific dependencies from this cell</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>settings</code> - matrix settings</dd>
<dd><code>row</code> - row element</dd>
<dd><code>column</code> - column element</dd>
<dd><code>cell</code> - current cell</dd>
<dd><code>main</code> - main action category</dd>
<dd><code>deleteActions</code> - add remove dependency actions to this category</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canCreate(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">
<h3>canCreate</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canCreate</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> settings,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 @CheckForNull
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</span></div>
<div class="block">Analyze specific cell and decides if there is any new dependencies which can be created for this pair of elements
 <p></p>
 IMPORTANT: Make this method as fast as possible. Performance of this method highly influences overall performance of
 the Dependency matrix component</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>settings</code> - matrix settings</dd>
<dd><code>row</code> - row element</dd>
<dd><code>column</code> - column element</dd>
<dd><code>cell</code> - matrix cell</dd>
<dt>Returns:</dt>
<dd><code>true</code> if at least one relation can be created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canEdit(com.nomagic.magicdraw.dependencymatrix.persistence.PersistenceManager,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.ElementNode,com.nomagic.magicdraw.dependencymatrix.datamodel.cell.AbstractMatrixCell)">
<h3>canEdit</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canEdit</span><wbr/><span class="parameters">(<a href="../../persistence/PersistenceManager.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">PersistenceManager</a> persistenceManager,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> row,
 <a href="../ElementNode.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel">ElementNode</a> column,
 <a href="../cell/AbstractMatrixCell.html" title="class in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">AbstractMatrixCell</a> cell)</span></div>
<div class="block">Analyze current cell, and decide if this there are at least one dependency, which can be deleted/edited.
 <p></p>
 IMPORTANT: Make this method as fast as possible. Performance of this method highly influences overall performance of
 the Dependency matrix component</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>persistenceManager</code> - matrix settings</dd>
<dd><code>row</code> - row element</dd>
<dd><code>column</code> - column element</dd>
<dd><code>cell</code> - matrix cell</dd>
<dt>Returns:</dt>
<dd><code>true</code> if there is at least one dependency which can be deleted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementUpdated(java.util.Collection)">
<h3>elementUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">elementUpdated</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; element)</span></div>
<div class="block">This method is triggered when elements are updated but Build is not initiated. All caches should be cleared</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - updated element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">clear</span>()</div>
<div class="block">Purpose of this method to clean up all unnecessary cache and objects</div>
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
