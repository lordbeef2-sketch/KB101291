# JAVA OPENAPI: ITool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/ITool.html
- source_path: `com/nomagic/magicreport/engine/ITool.html`
- source_sha256: `2524d1e7485d440152ecba8109f8d0bffa3f7486773a1b39cde3de4c80cd9882`
- captured_utc: `2026-07-14T16:58:36.534275+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface ITool

All Superinterfaces:
`[IVariable](../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

All Known Implementing Classes:
`[ArrayTool](tools/ArrayTool.html)`, `[BookmarkTool](tools/BookmarkTool.html)`, `[ChartTool](../../reportwizard/tools/ChartTool.html)`, `[ConcurrentTool](ConcurrentTool.html)`, `[DefaultImporterTool](../../reportwizard/tools/importer/DefaultImporterTool.html)`, `[DependencyMatrixTool](../../reportwizard/tools/DependencyMatrixTool.html)`, `[DialogTool](../../reportwizard/tools/DialogTool.html)`, `[DocBookTool](../../reportwizard/tools/DocBookTool.html)`, `[DOCXImporterTool](../../reportwizard/tools/importer/DOCXImporterTool.html)`, `[ExportTool2](../../magicdraw/magicreport/tools/ExportTool2.html)`, `[ExportTool3](../../magicdraw/magicreport/tools/ExportTool3.html)`, `[FileTool](tools/FileTool.html)`, `[GenericTableTool](../../reportwizard/tools/GenericTableTool.html)`, `[GroovyTool](../../reportwizard/tools/script/GroovyTool.html)`, `[GroupTool](tools/GroupTool.html)`, `[ImageTool](tools/ImageTool.html)`, `[ImportTool](../../reportwizard/tools/ImportTool.html)`, `[JavaDocTool](../../reportwizard/tools/doc/JavaDocTool.html)`, `[JavaScriptTool](../../reportwizard/tools/script/JavaScriptTool.html)`, `[MapTool](tools/MapTool.html)`, `[MathTool](../../reportwizard/tools/MathTool.html)`, `[ModelValidationTool](../../reportwizard/tools/ModelValidationTool.html)`, `[ProfilingTool](../../magicdraw/magicreport/tools/ProfilingTool.html)`, `[ProjectTool](../../magicdraw/magicreport/tools/ProjectTool.html)`, `[QueryTool](../../reportwizard/tools/QueryTool.html)`, `[ReportFileTool](../../magicdraw/magicreport/tools/ReportFileTool.html)`, `[ReportHelper](../../magicdraw/magicreport/helper/ReportHelper.html)`, `[SorterTool](../../magicdraw/magicreport/tools/SorterTool.html)`, `[SortTable](../../reportwizard/tools/dialog/SortTable.html)`, `[SortTool](tools/SortTool.html)`, `[TemplateTool](../../magicdraw/magicreport/tools/TemplateTool.html)`, `[TemplateTool](tools/TemplateTool.html)`, `[TextTool](../../reportwizard/tools/TextTool.html)`, `[Tool](Tool.html)`

@OpenApiAllpublic interfaceIToolextends [IVariable](../IVariable.html)

Interface for template tool. All template tool must implements this interface. The concept of the 'tool' is
 similar to Velocity template context. The idea is that the tool is a 'carrier' of data between the Java layer
 and the template layer.
 Tool gather objects of various types, and place them in the template. Tool is Java Bean object. The Java Bean
 consists of field, getter and setter of field, and empty Constructor.

Since:
Jan 23, 2008

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static class`
`[ITool.HTMLString](ITool.HTMLString.html)`
Direct command [`IFormatter`](../format/IFormatter.html) to render in HTML format.
`static class`
`[ITool.RetainedString](ITool.RetainedString.html)`
Direct command [`IFormatter`](../format/IFormatter.html) to keep the referenced String format.
`static class`
`[ITool.Void](ITool.Void.html)`
A void class uses to return in Velocity Tools when you want exactly not return anything to context.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [ITool.Void](ITool.Void.html)`
`[VOID](#VOID)`
Instead of void (null) in Velocity, return this object, if empty string is require for output.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[clearTool](#clearTool())()`

`[IContext](IContext.html)`
`[getContext](#getContext())()`
Return template context.
`[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[getProperties](#getProperties())()`
Return template engine properties.
`void`
`[setContext](#setContext(com.nomagic.magicreport.engine.IContext))([IContext](IContext.html) context)`
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties.

============ FIELD DETAIL =========== 
Field Details
VOID
static final [ITool.Void](ITool.Void.html) VOID
Instead of void (null) in Velocity, return this object, if empty string is require for output. The
 [`ITool.Void`](ITool.Void.html) uses to make sure that returning data from setter method is absolutely nothing. In general
 case, Velocity consider return `void` from setter method as `null` value, this cause
 the word 'null' printed out in report. To avoid this problem setter method may use [`VOID`](#VOID) as
 returning object.
 ============ METHOD DETAIL ========== 
Method Details
setProperties
void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties. Override current properties will not affect with the engine.
Parameters:
`properties` - template engine properties
getProperties
[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) getProperties()
Return template engine properties.
Returns:
template engine properties
setContext
void setContext([IContext](IContext.html) context)
This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context. This method automatically called by template engine.
Parameters:
`context` - template context
getContext
[IContext](IContext.html) getContext()
Return template context.
Returns:
template context
clearTool
default void clearTool()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface ITool">Interface ITool</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="tools/ArrayTool.html" title="class in com.nomagic.magicreport.engine.tools">ArrayTool</a></code>, <code><a href="tools/BookmarkTool.html" title="class in com.nomagic.magicreport.engine.tools">BookmarkTool</a></code>, <code><a href="../../reportwizard/tools/ChartTool.html" title="class in com.nomagic.reportwizard.tools">ChartTool</a></code>, <code><a href="ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code>, <code><a href="../../reportwizard/tools/importer/DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code>, <code><a href="../../reportwizard/tools/DependencyMatrixTool.html" title="class in com.nomagic.reportwizard.tools">DependencyMatrixTool</a></code>, <code><a href="../../reportwizard/tools/DialogTool.html" title="class in com.nomagic.reportwizard.tools">DialogTool</a></code>, <code><a href="../../reportwizard/tools/DocBookTool.html" title="class in com.nomagic.reportwizard.tools">DocBookTool</a></code>, <code><a href="../../reportwizard/tools/importer/DOCXImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DOCXImporterTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/ExportTool2.html" title="class in com.nomagic.magicdraw.magicreport.tools">ExportTool2</a></code>, <code><a href="../../magicdraw/magicreport/tools/ExportTool3.html" title="class in com.nomagic.magicdraw.magicreport.tools">ExportTool3</a></code>, <code><a href="tools/FileTool.html" title="class in com.nomagic.magicreport.engine.tools">FileTool</a></code>, <code><a href="../../reportwizard/tools/GenericTableTool.html" title="class in com.nomagic.reportwizard.tools">GenericTableTool</a></code>, <code><a href="../../reportwizard/tools/script/GroovyTool.html" title="class in com.nomagic.reportwizard.tools.script">GroovyTool</a></code>, <code><a href="tools/GroupTool.html" title="class in com.nomagic.magicreport.engine.tools">GroupTool</a></code>, <code><a href="tools/ImageTool.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool</a></code>, <code><a href="../../reportwizard/tools/ImportTool.html" title="class in com.nomagic.reportwizard.tools">ImportTool</a></code>, <code><a href="../../reportwizard/tools/doc/JavaDocTool.html" title="class in com.nomagic.reportwizard.tools.doc">JavaDocTool</a></code>, <code><a href="../../reportwizard/tools/script/JavaScriptTool.html" title="class in com.nomagic.reportwizard.tools.script">JavaScriptTool</a></code>, <code><a href="tools/MapTool.html" title="class in com.nomagic.magicreport.engine.tools">MapTool</a></code>, <code><a href="../../reportwizard/tools/MathTool.html" title="class in com.nomagic.reportwizard.tools">MathTool</a></code>, <code><a href="../../reportwizard/tools/ModelValidationTool.html" title="class in com.nomagic.reportwizard.tools">ModelValidationTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/ProfilingTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProfilingTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/ProjectTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectTool</a></code>, <code><a href="../../reportwizard/tools/QueryTool.html" title="class in com.nomagic.reportwizard.tools">QueryTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/ReportFileTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ReportFileTool</a></code>, <code><a href="../../magicdraw/magicreport/helper/ReportHelper.html" title="class in com.nomagic.magicdraw.magicreport.helper">ReportHelper</a></code>, <code><a href="../../magicdraw/magicreport/tools/SorterTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">SorterTool</a></code>, <code><a href="../../reportwizard/tools/dialog/SortTable.html" title="class in com.nomagic.reportwizard.tools.dialog">SortTable</a></code>, <code><a href="tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code>, <code><a href="../../magicdraw/magicreport/tools/TemplateTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">TemplateTool</a></code>, <code><a href="tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">TemplateTool</a></code>, <code><a href="../../reportwizard/tools/TextTool.html" title="class in com.nomagic.reportwizard.tools">TextTool</a></code>, <code><a href="Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ITool</span><span class="extends-implements">
extends <a href="../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></span></div>
<div class="block">Interface for template tool. All template tool must implements this interface. The concept of the 'tool' is
 similar to Velocity template context. The idea is that the tool is a 'carrier' of data between the Java layer
 and the template layer.
 <p>
 Tool gather objects of various types, and place them in the template. Tool is Java Bean object. The Java Bean
 consists of field, getter and setter of field, and empty Constructor.</p></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 23, 2008</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-last even-row-color">
<div class="block">Direct command <a href="../format/IFormatter.html" title="interface in com.nomagic.magicreport.format"><code>IFormatter</code></a> to render in HTML format.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Direct command <a href="../format/IFormatter.html" title="interface in com.nomagic.magicreport.format"><code>IFormatter</code></a> to keep the referenced String format.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-last even-row-color">
<div class="block">A void class uses to return in Velocity Tools when you want exactly not return anything to context.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a href="ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VOID">VOID</a></code></div>
<div class="col-last even-row-color">
<div class="block">Instead of void (null) in Velocity, return this object, if empty string is require for output.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#clearTool()">clearTool</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return template context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return template engine properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a><wbr/>(<a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="VOID">
<h3>VOID</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a href="ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">VOID</span></div>
<div class="block">Instead of void (null) in Velocity, return this object, if empty string is require for output. The
 <a href="ITool.Void.html" title="class in com.nomagic.magicreport.engine"><code>ITool.Void</code></a> uses to make sure that returning data from setter method is absolutely nothing. In general
 case, Velocity consider return <code>void</code> from setter method as <code>null</code> value, this cause
 the word 'null' printed out in report. To avoid this problem setter method may use <a href="#VOID"><code>VOID</code></a> as
 returning object.</div>
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
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template properties. Override current properties will not affect with the engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - template engine properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">getProperties</span>()</div>
<div class="block">Return template engine properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>template engine properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContext(com.nomagic.magicreport.engine.IContext)">
<h3>setContext</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setContext</span><wbr/><span class="parameters">(<a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a> context)</span></div>
<div class="block">This method is invoked by the template engine runtime, after class has been initializing, to set the
 template context. This method automatically called by template engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - template context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="return-type"><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Return template context.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>template context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearTool()">
<h3>clearTool</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">clearTool</span>()</div>
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
