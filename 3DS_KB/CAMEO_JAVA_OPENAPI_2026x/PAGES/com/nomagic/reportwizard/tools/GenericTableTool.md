# JAVA OPENAPI: GenericTableTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/GenericTableTool.html
- source_path: `com/nomagic/reportwizard/tools/GenericTableTool.html`
- source_sha256: `503123f8ea7917bea9c02140831f3115f677cd57b7e82223f704f49cd1c02586`
- captured_utc: `2026-07-14T16:58:40.141314+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools](package-summary.html)

## Class GenericTableTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../magicreport/engine/Tool.html)
com.nomagic.reportwizard.tools.GenericTableTool

All Implemented Interfaces:
`[ITool](../../magicreport/engine/ITool.html)`, `[IVariable](../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classGenericTableTool
extends [Tool](../../magicreport/engine/Tool.html)

A custom tool for accessing Generic Table data to get row elements, column name and cell value.

Since:
Jan 25, 2012
See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.reportwizard.tools.GenericTableTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[context](../../magicreport/engine/Tool.html#context), [properties](../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[VOID](../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[GenericTableTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[clearTablesCache](#clearTablesCache())()`
Deprecated.
use [`clearTablesCache(Project)`](#clearTablesCache(com.nomagic.magicdraw.core.Project)) instead.
`void`
`[clearTablesCache](#clearTablesCache(com.nomagic.magicdraw.core.Project))([Project](../../magicdraw/core/Project.html) project)`
Use this method after use generic table.
`[ITool.Void](../../magicreport/engine/ITool.Void.html)`
`[closeTable](#closeTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Close specific diagram table.
`[ITool.Void](../../magicreport/engine/ITool.Void.html)`
`[closeTable](#closeTable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramName)`
Close specific diagram name.
`[ITool.Void](../../magicreport/engine/ITool.Void.html)`
`[closeTables](#closeTables())()`
Close all diagram tables
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)>`
`[filterDiagramTables](#filterDiagramTables(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> elements)`

`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getCellValue](#getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`

`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getCellValue](#getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`

`com.nomagic.magicdraw.properties.ui.jideui.PropertyColumn`
`[getColumnById](#getColumnById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.lang.String))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getColumnIds](#getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getColumnNames](#getColumnNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> columnIds)`

`com.nomagic.diagramtable.Table`
`[getDiagramTable](#getDiagramTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`

`int`
`[getLevel](#getLevel(com.nomagic.diagramtable.rows.DiagramTableRow))(com.nomagic.diagramtable.rows.DiagramTableRow row)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.diagramtable.rows.DiagramTableRow>`
`[getRows](#getRows(com.nomagic.diagramtable.Table))(com.nomagic.diagramtable.Table table)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.diagramtable.rows.DiagramTableRow>`
`[getRows](#getRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getStringCellValue](#getStringCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`

`[Table](generictable/Table.html)`
`[getTable](#getTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Get generic table instance from diagram element.
`[Table](generictable/Table.html)`
`[getTable](#getTable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramName)`
Get generic table instance from diagram name.
`boolean`
`[hasAnnotation](#hasAnnotation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[clone](../../magicreport/engine/Tool.html#clone()), [getContext](../../magicreport/engine/Tool.html#getContext()), [getProperties](../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[clearTool](../../magicreport/engine/ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
GenericTableTool
public GenericTableTool()
 ============ METHOD DETAIL ========== 
Method Details
getTable
@CheckForNullpublic [Table](generictable/Table.html) getTable([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Get generic table instance from diagram element.
Parameters:
`diagram` - diagram object.
Returns:
generic table instance
getTable
@CheckForNullpublic [Table](generictable/Table.html) getTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramName)
Get generic table instance from diagram name.
Parameters:
`diagramName` - diagram name
Returns:
generic table of instance
closeTables
public [ITool.Void](../../magicreport/engine/ITool.Void.html) closeTables()
Close all diagram tables
closeTable
public [ITool.Void](../../magicreport/engine/ITool.Void.html) closeTable([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Close specific diagram table.
Parameters:
`diagram` - diagram object.
closeTable
public [ITool.Void](../../magicreport/engine/ITool.Void.html) closeTable([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramName)
Close specific diagram name.
Parameters:
`diagramName` - diagram name
getDiagramTable
public com.nomagic.diagramtable.Table getDiagramTable([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
clearTablesCache
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void clearTablesCache()
Deprecated.
use [`clearTablesCache(Project)`](#clearTablesCache(com.nomagic.magicdraw.core.Project)) instead.
Use this method after use generic table.
clearTablesCache
public void clearTablesCache([Project](../../magicdraw/core/Project.html) project)
Use this method after use generic table.
Parameters:
`project` - project which is used to get cache.
getRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.diagramtable.rows.DiagramTableRow> getRows(com.nomagic.diagramtable.Table table)
getRows
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.diagramtable.rows.DiagramTableRow> getRows([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram)
getColumnNames
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getColumnNames([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> columnIds)
getColumnIds
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getColumnIds([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram)
getColumnById
@CheckForNullpublic com.nomagic.magicdraw.properties.ui.jideui.PropertyColumn getColumnById([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)
getStringCellValue
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getStringCellValue([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)
filterDiagramTables
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> filterDiagramTables([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)> elements)
hasAnnotation
public boolean hasAnnotation([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)
getLevel
public int getLevel(com.nomagic.diagramtable.rows.DiagramTableRow row)
getCellValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getCellValue([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)
getCellValue
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getCellValue([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) tableDiagram,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) rowElement,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) columnId)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools</a></div>
<h1 class="title" title="Class GenericTableTool">Class GenericTableTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.GenericTableTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">GenericTableTool</span>
<span class="extends-implements">extends <a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">A custom tool for accessing Generic Table data to get row elements, column name and cell value.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 25, 2012</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.reportwizard.tools.GenericTableTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#context">context</a>, <a href="../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">GenericTableTool</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#clearTablesCache()">clearTablesCache</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#clearTablesCache(com.nomagic.magicdraw.core.Project)"><code>clearTablesCache(Project)</code></a> instead.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTablesCache(com.nomagic.magicdraw.core.Project)">clearTablesCache</a><wbr/>(<a href="../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Use this method after use generic table.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">closeTable</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close specific diagram table.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeTable(java.lang.String)">closeTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close specific diagram name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeTables()">closeTables</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close all diagram tables</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterDiagramTables(java.util.Collection)">filterDiagramTables</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">getCellValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">getCellValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.properties.ui.jideui.PropertyColumn</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.lang.String)">getColumnById</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getColumnIds</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">getColumnNames</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; columnIds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.diagramtable.Table</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getDiagramTable</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLevel(com.nomagic.diagramtable.rows.DiagramTableRow)">getLevel</a><wbr/>(com.nomagic.diagramtable.rows.DiagramTableRow row)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.diagramtable.rows.DiagramTableRow&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRows(com.nomagic.diagramtable.Table)">getRows</a><wbr/>(com.nomagic.diagramtable.Table table)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.diagramtable.rows.DiagramTableRow&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getRows</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">getStringCellValue</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="generictable/Table.html" title="class in com.nomagic.reportwizard.tools.generictable">Table</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getTable</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get generic table instance from diagram element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="generictable/Table.html" title="class in com.nomagic.reportwizard.tools.generictable">Table</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTable(java.lang.String)">getTable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get generic table instance from diagram name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAnnotation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">hasAnnotation</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<h3>GenericTableTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GenericTableTool</span>()</div>
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
<section class="detail" id="getTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getTable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="generictable/Table.html" title="class in com.nomagic.reportwizard.tools.generictable">Table</a></span> <span class="element-name">getTable</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Get generic table instance from diagram element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram object.</dd>
<dt>Returns:</dt>
<dd>generic table instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTable(java.lang.String)">
<h3>getTable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="generictable/Table.html" title="class in com.nomagic.reportwizard.tools.generictable">Table</a></span> <span class="element-name">getTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramName)</span></div>
<div class="block">Get generic table instance from diagram name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramName</code> - diagram name</dd>
<dt>Returns:</dt>
<dd>generic table of instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeTables()">
<h3>closeTables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">closeTables</span>()</div>
<div class="block">Close all diagram tables</div>
</section>
</li>
<li>
<section class="detail" id="closeTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>closeTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">closeTable</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Close specific diagram table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeTable(java.lang.String)">
<h3>closeTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">closeTable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramName)</span></div>
<div class="block">Close specific diagram name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramName</code> - diagram name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getDiagramTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.diagramtable.Table</span> <span class="element-name">getDiagramTable</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTablesCache()">
<h3>clearTablesCache</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTablesCache</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#clearTablesCache(com.nomagic.magicdraw.core.Project)"><code>clearTablesCache(Project)</code></a> instead.</div>
</div>
<div class="block">Use this method after use generic table.</div>
</section>
</li>
<li>
<section class="detail" id="clearTablesCache(com.nomagic.magicdraw.core.Project)">
<h3>clearTablesCache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTablesCache</span><wbr/><span class="parameters">(<a href="../../magicdraw/core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Use this method after use generic table.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which is used to get cache.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRows(com.nomagic.diagramtable.Table)">
<h3>getRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.diagramtable.rows.DiagramTableRow&gt;</span> <span class="element-name">getRows</span><wbr/><span class="parameters">(com.nomagic.diagramtable.Table table)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRows(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getRows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.diagramtable.rows.DiagramTableRow&gt;</span> <span class="element-name">getRows</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnNames(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.util.List)">
<h3>getColumnNames</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnNames</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; columnIds)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnIds(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getColumnIds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getColumnIds</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram)</span></div>
</section>
</li>
<li>
<section class="detail" id="getColumnById(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,java.lang.String)">
<h3>getColumnById</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.properties.ui.jideui.PropertyColumn</span> <span class="element-name">getColumnById</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStringCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">
<h3>getStringCellValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStringCellValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
</section>
</li>
<li>
<section class="detail" id="filterDiagramTables(java.util.Collection)">
<h3>filterDiagramTables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt;</span> <span class="element-name">filterDiagramTables</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a>&gt; elements)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasAnnotation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">
<h3>hasAnnotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAnnotation</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
</section>
</li>
<li>
<section class="detail" id="getLevel(com.nomagic.diagramtable.rows.DiagramTableRow)">
<h3>getLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLevel</span><wbr/><span class="parameters">(com.nomagic.diagramtable.rows.DiagramTableRow row)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.diagramtable.rows.DiagramTableRow,java.lang.String)">
<h3>getCellValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCellValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 com.nomagic.diagramtable.rows.DiagramTableRow row,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCellValue(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>getCellValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getCellValue</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> tableDiagram,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> rowElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> columnId)</span></div>
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
