# JAVA OPENAPI: DependencyMatrixConfigurator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependencymatrix/configuration/DependencyMatrixConfigurator.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/configuration/DependencyMatrixConfigurator.html`
- source_sha256: `308c42a2a37e6e0ea431b1558e7265500371f0e69abd711ac794ec8956cb29c0`
- captured_utc: `2026-07-14T16:57:53.392485+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.configuration](package-summary.html)

## Class DependencyMatrixConfigurator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator

@OpenApiAllpublic classDependencyMatrixConfigurator
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
This class allows to customize standard matrix behaviour and view. Custom matrix configurator must be derived
 from this class and registered in configurators registry with custom matrix descriptor.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE](#DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE)`
Default dependency matrix diagram type
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DependencyMatrixConfigurator](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramType)`
create new instance of the configurator
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[configureDependencyHandlers](#configureDependencyHandlers(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyExtractor](../datamodel/cell/DependencyExtractor.html)> extractors,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEditor](../datamodel/editing/DependencyEditor.html)> editors)`
Creates Matrix Dependency handlers, which are responsible for extracting and editing dependencies shown in the matrix
`[TableCellRenderer](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html)`
`[createColumnCellRenderer](#createColumnCellRenderer())()`
Create renderer, which is responsible for displaying table header header row elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.
`[TableCellRenderer](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html)`
`[createRowCellRenderer](#createRowCellRenderer())()`
Create renderer, which is responsible for displaying row header column elements
 Make sure that provided TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.
`[TableCellRenderer](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html)`
`[createTableCellRenderer](#createTableCellRenderer())()`
Create renderer, which is responsible for displaying cell elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.
`static [DependencyMatrixConfigurator](DependencyMatrixConfigurator.html)`
`[getConfigurator](#getConfigurator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Returns registered configurator for this diagram
`static [DependencyMatrixConfigurator](DependencyMatrixConfigurator.html)`
`[getConfigurator](#getConfigurator(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramType)`
Returns registered configurator for this diagram
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDiagramType](#getDiagramType())()`
Diagram type of the current configurator
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getRegisteredMatrixTypes](#getRegisteredMatrixTypes())()`
Returns list of all dependency matrix types
`static void`
`[registerConfiguration](#registerConfiguration(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator))([DependencyMatrixConfigurator](DependencyMatrixConfigurator.html) configurator)`
Registers new configurator in the matrix configurator registry
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE
Default dependency matrix diagram type
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator.DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DependencyMatrixConfigurator
public DependencyMatrixConfigurator([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramType)
create new instance of the configurator
Parameters:
`diagramType` - diagram type name
 ============ METHOD DETAIL ========== 
Method Details
getConfigurator
@CheckForNullpublic static [DependencyMatrixConfigurator](DependencyMatrixConfigurator.html) getConfigurator([Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Returns registered configurator for this diagram
Parameters:
`diagram` - diagram instance
Returns:
configurator used to create this kind of Dependency Matrix
getConfigurator
@CheckForNullpublic static [DependencyMatrixConfigurator](DependencyMatrixConfigurator.html) getConfigurator([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) diagramType)
Returns registered configurator for this diagram
Parameters:
`diagramType` - diagram type name
Returns:
configurator used to create this kind of Dependency Matrix
registerConfiguration
public static void registerConfiguration([DependencyMatrixConfigurator](DependencyMatrixConfigurator.html) configurator)
Registers new configurator in the matrix configurator registry
Parameters:
`configurator` - new registered configurator
getDiagramType
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDiagramType()
Diagram type of the current configurator
Returns:
diagram type
createTableCellRenderer
public [TableCellRenderer](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html) createTableCellRenderer()
Create renderer, which is responsible for displaying cell elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.
Returns:
new cell renderer component
createColumnCellRenderer
public [TableCellRenderer](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html) createColumnCellRenderer()
Create renderer, which is responsible for displaying table header header row elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.
Returns:
new column renderer component
createRowCellRenderer
public [TableCellRenderer](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html) createRowCellRenderer()
Create renderer, which is responsible for displaying row header column elements
 Make sure that provided TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.
Returns:
new row renderer component
configureDependencyHandlers
public void configureDependencyHandlers([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyExtractor](../datamodel/cell/DependencyExtractor.html)> extractors,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[DependencyEditor](../datamodel/editing/DependencyEditor.html)> editors)
Creates Matrix Dependency handlers, which are responsible for extracting and editing dependencies shown in the matrix
 
 In order to add custom dependency extraction algorithms use [`DependencyExtractor`](../datamodel/cell/DependencyExtractor.html)
 In order to add custom dependency editors (add and remove dependency actions) use [`DependencyEditor`](../datamodel/editing/DependencyEditor.html)
Parameters:
`extractors` - dependency extractor instances
`editors` - Dependency editor instances
getRegisteredMatrixTypes
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getRegisteredMatrixTypes()
Returns list of all dependency matrix types
Returns:
all known dependency matrix types.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.configuration</a></div>
<h1 class="title" title="Class DependencyMatrixConfigurator">Class DependencyMatrixConfigurator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DependencyMatrixConfigurator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This class allows to customize standard matrix behaviour and view. Custom matrix configurator must be derived
 from this class and registered in configurators registry with custom matrix descriptor.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE">DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Default dependency matrix diagram type</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">DependencyMatrixConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last even-row-color">
<div class="block">create new instance of the configurator</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configureDependencyHandlers(java.util.Collection,java.util.Collection)">configureDependencyHandlers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/cell/DependencyExtractor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyExtractor</a>&gt; extractors,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/editing/DependencyEditor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.editing">DependencyEditor</a>&gt; editors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates Matrix Dependency handlers, which are responsible for extracting and editing dependencies shown in the matrix</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createColumnCellRenderer()">createColumnCellRenderer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create renderer, which is responsible for displaying table header header row elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRowCellRenderer()">createRowCellRenderer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create renderer, which is responsible for displaying row header column elements
 Make sure that provided TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTableCellRenderer()">createTableCellRenderer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create renderer, which is responsible for displaying cell elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyMatrixConfigurator.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixConfigurator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfigurator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getConfigurator</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns registered configurator for this diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyMatrixConfigurator.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixConfigurator</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfigurator(java.lang.String)">getConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns registered configurator for this diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType()">getDiagramType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Diagram type of the current configurator</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRegisteredMatrixTypes()">getRegisteredMatrixTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns list of all dependency matrix types</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerConfiguration(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator)">registerConfiguration</a><wbr/>(<a href="DependencyMatrixConfigurator.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Registers new configurator in the matrix configurator registry</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE">
<h3>DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE</span></div>
<div class="block">Default dependency matrix diagram type</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator.DEFAULT_DEPENDENCY_MATRIX_DIAGRAM_TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>DependencyMatrixConfigurator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DependencyMatrixConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">create new instance of the configurator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type name</dd>
</dl>
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
<section class="detail" id="getConfigurator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyMatrixConfigurator.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixConfigurator</a></span> <span class="element-name">getConfigurator</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Returns registered configurator for this diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram instance</dd>
<dt>Returns:</dt>
<dd>configurator used to create this kind of Dependency Matrix</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConfigurator(java.lang.String)">
<h3>getConfigurator</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyMatrixConfigurator.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixConfigurator</a></span> <span class="element-name">getConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> diagramType)</span></div>
<div class="block">Returns registered configurator for this diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagramType</code> - diagram type name</dd>
<dt>Returns:</dt>
<dd>configurator used to create this kind of Dependency Matrix</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerConfiguration(com.nomagic.magicdraw.dependencymatrix.configuration.DependencyMatrixConfigurator)">
<h3>registerConfiguration</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">registerConfiguration</span><wbr/><span class="parameters">(<a href="DependencyMatrixConfigurator.html" title="class in com.nomagic.magicdraw.dependencymatrix.configuration">DependencyMatrixConfigurator</a> configurator)</span></div>
<div class="block">Registers new configurator in the matrix configurator registry</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurator</code> - new registered configurator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiagramType()">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiagramType</span>()</div>
<div class="block">Diagram type of the current configurator</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>diagram type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTableCellRenderer()">
<h3>createTableCellRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></span> <span class="element-name">createTableCellRenderer</span>()</div>
<div class="block">Create renderer, which is responsible for displaying cell elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>new cell renderer component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createColumnCellRenderer()">
<h3>createColumnCellRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></span> <span class="element-name">createColumnCellRenderer</span>()</div>
<div class="block">Create renderer, which is responsible for displaying table header header row elements
 Make sure that TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>new column renderer component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRowCellRenderer()">
<h3>createRowCellRenderer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/table/TableCellRenderer.html" title="class or interface in javax.swing.table">TableCellRenderer</a></span> <span class="element-name">createRowCellRenderer</span>()</div>
<div class="block">Create renderer, which is responsible for displaying row header column elements
 Make sure that provided TableCellRenderer also implements com.nomagic.magicdraw.ui.zoom.Zoomable interface to properly display scaled (zoomed) matrix.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>new row renderer component</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureDependencyHandlers(java.util.Collection,java.util.Collection)">
<h3>configureDependencyHandlers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configureDependencyHandlers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/cell/DependencyExtractor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyExtractor</a>&gt; extractors,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../datamodel/editing/DependencyEditor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.editing">DependencyEditor</a>&gt; editors)</span></div>
<div class="block">Creates Matrix Dependency handlers, which are responsible for extracting and editing dependencies shown in the matrix
 <p></p>
 In order to add custom dependency extraction algorithms use <a href="../datamodel/cell/DependencyExtractor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.cell"><code>DependencyExtractor</code></a>
 In order to add custom dependency editors (add and remove dependency actions) use <a href="../datamodel/editing/DependencyEditor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.editing"><code>DependencyEditor</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>extractors</code> - dependency extractor instances</dd>
<dd><code>editors</code> - Dependency editor instances</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRegisteredMatrixTypes()">
<h3>getRegisteredMatrixTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRegisteredMatrixTypes</span>()</div>
<div class="block">Returns list of all dependency matrix types</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all known dependency matrix types.</dd>
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
