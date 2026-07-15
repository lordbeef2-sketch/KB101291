# JAVA OPENAPI: TemplateTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/magicreport/tools/TemplateTool.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/TemplateTool.html`
- source_sha256: `13c6766f90c313f7db1c75e6ce8c9e1353d2695642723a48c9bcce10a6d22eb7`
- captured_utc: `2026-07-14T16:45:37.782505+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class TemplateTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
[com.nomagic.magicreport.engine.tools.TemplateTool](../../../magicreport/engine/tools/TemplateTool.html)
com.nomagic.magicdraw.magicreport.tools.TemplateTool

All Implemented Interfaces:
`[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classTemplateTool
extends [TemplateTool](../../../magicreport/engine/tools/TemplateTool.html)

Additional features for template tool.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.TemplateTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.tools.[TemplateTool](../../../magicreport/engine/tools/TemplateTool.html)
`[CONTEXT_NAME](../../../magicreport/engine/tools/TemplateTool.html#CONTEXT_NAME)`
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TemplateTool](#%3Cinit%3E())()`
Default constructor.
`[TemplateTool](#%3Cinit%3E(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Create a tool with information from template bean.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCategory](#getCategory())()`
Gets category name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`
Gets description.
`com.nomagic.magicdraw.magicreport.ui.bean.ReportBean`
`[getReportData](#getReportData())()`
Gets selected report data.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.tools.ReportDataVariable>`
`[getReportDataVariables](#getReportDataVariables())()`
Get all report data variable as list of `ReportDataVariable`
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSelectedReportData](#getSelectedReportData())()`
Gets selected report data name.
`void`
`[setReportDataVariableMap](#setReportDataVariableMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> reportDataVariableMap)`
Set report data variable map
Methods inherited from class com.nomagic.magicreport.engine.tools.[TemplateTool](../../../magicreport/engine/tools/TemplateTool.html)
`[getFile](../../../magicreport/engine/tools/TemplateTool.html#getFile()), [getLatestInputFile](../../../magicreport/engine/tools/TemplateTool.html#getLatestInputFile()), [getLatestInputLocation](../../../magicreport/engine/tools/TemplateTool.html#getLatestInputLocation()), [getLatestOutputFile](../../../magicreport/engine/tools/TemplateTool.html#getLatestOutputFile()), [getLatestOutputLocation](../../../magicreport/engine/tools/TemplateTool.html#getLatestOutputLocation()), [getLocation](../../../magicreport/engine/tools/TemplateTool.html#getLocation()), [getMainOutputLocation](../../../magicreport/engine/tools/TemplateTool.html#getMainOutputLocation()), [getMainTemplateLocation](../../../magicreport/engine/tools/TemplateTool.html#getMainTemplateLocation()), [getName](../../../magicreport/engine/tools/TemplateTool.html#getName()), [getOutputFile](../../../magicreport/engine/tools/TemplateTool.html#getOutputFile()), [getOutputFileName](../../../magicreport/engine/tools/TemplateTool.html#getOutputFileName()), [getOutputFileNameNoExt](../../../magicreport/engine/tools/TemplateTool.html#getOutputFileNameNoExt()), [getOutputFileNoExt](../../../magicreport/engine/tools/TemplateTool.html#getOutputFileNoExt()), [getOutputLocation](../../../magicreport/engine/tools/TemplateTool.html#getOutputLocation()), [getResourcesLocation](../../../magicreport/engine/tools/TemplateTool.html#getResourcesLocation()), [getTemplateFile](../../../magicreport/engine/tools/TemplateTool.html#getTemplateFile()), [getTemplateLocation](../../../magicreport/engine/tools/TemplateTool.html#getTemplateLocation())`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[clone](../../../magicreport/engine/Tool.html#clone()), [getContext](../../../magicreport/engine/Tool.html#getContext()), [getProperties](../../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[clearTool](../../../magicreport/engine/ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TemplateTool
public TemplateTool()
Default constructor.
TemplateTool
public TemplateTool(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
Create a tool with information from template bean.
Parameters:
`templateBean` - template bean
 ============ METHOD DETAIL ========== 
Method Details
getDescription
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDescription()
Gets description.
Returns:
the description
getCategory
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCategory()
Gets category name.
Returns:
the category name
getSelectedReportData
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSelectedReportData()
Gets selected report data name.
Returns:
the selected report data name
getReportData
public com.nomagic.magicdraw.magicreport.ui.bean.ReportBean getReportData()
Gets selected report data.
Returns:
the selected report data
setReportDataVariableMap
public void setReportDataVariableMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> reportDataVariableMap)
Set report data variable map
Parameters:
`reportDataVariableMap` - map of report data variable
getReportDataVariables
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.magicreport.tools.ReportDataVariable> getReportDataVariables()
Get all report data variable as list of `ReportDataVariable`
Returns:
list of `ReportDataVariable`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class TemplateTool">Class TemplateTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance"><a href="../../../magicreport/engine/tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">com.nomagic.magicreport.engine.tools.TemplateTool</a>
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.TemplateTool</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TemplateTool</span>
<span class="extends-implements">extends <a href="../../../magicreport/engine/tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">TemplateTool</a></span></div>
<div class="block">Additional features for template tool.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.TemplateTool">Serialized Form</a></li>
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
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.tools.TemplateTool">Fields inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">TemplateTool</a></h3>
<code><a href="../../../magicreport/engine/tools/TemplateTool.html#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#context">context</a>, <a href="../../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TemplateTool</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">TemplateTool</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a tool with information from template bean.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCategory()">getCategory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets category name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets description.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.magicreport.ui.bean.ReportBean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReportData()">getReportData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets selected report data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.magicdraw.magicreport.tools.ReportDataVariable&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReportDataVariables()">getReportDataVariables</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all report data variable as list of <code>ReportDataVariable</code></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSelectedReportData()">getSelectedReportData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets selected report data name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReportDataVariableMap(java.util.Map)">setReportDataVariableMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; reportDataVariableMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set report data variable map</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.tools.TemplateTool">Methods inherited from class com.nomagic.magicreport.engine.tools.<a href="../../../magicreport/engine/tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">TemplateTool</a></h3>
<code><a href="../../../magicreport/engine/tools/TemplateTool.html#getFile()">getFile</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getLatestInputFile()">getLatestInputFile</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getLatestInputLocation()">getLatestInputLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getLatestOutputFile()">getLatestOutputFile</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getLatestOutputLocation()">getLatestOutputLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getLocation()">getLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getMainOutputLocation()">getMainOutputLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getMainTemplateLocation()">getMainTemplateLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getName()">getName</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getOutputFile()">getOutputFile</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getOutputFileName()">getOutputFileName</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getOutputFileNameNoExt()">getOutputFileNameNoExt</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getOutputFileNoExt()">getOutputFileNoExt</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getOutputLocation()">getOutputLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getResourcesLocation()">getResourcesLocation</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getTemplateFile()">getTemplateFile</a>, <a href="../../../magicreport/engine/tools/TemplateTool.html#getTemplateLocation()">getTemplateLocation</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<h3>TemplateTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateTool</span>()</div>
<div class="block">Default constructor.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>TemplateTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateTool</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
<div class="block">Create a tool with information from template bean.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateBean</code> - template bean</dd>
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
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
<div class="block">Gets description.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the description</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCategory()">
<h3>getCategory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCategory</span>()</div>
<div class="block">Gets category name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the category name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSelectedReportData()">
<h3>getSelectedReportData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSelectedReportData</span>()</div>
<div class="block">Gets selected report data name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the selected report data name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReportData()">
<h3>getReportData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.magicreport.ui.bean.ReportBean</span> <span class="element-name">getReportData</span>()</div>
<div class="block">Gets selected report data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the selected report data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReportDataVariableMap(java.util.Map)">
<h3>setReportDataVariableMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReportDataVariableMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; reportDataVariableMap)</span></div>
<div class="block">Set report data variable map</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reportDataVariableMap</code> - map of report data variable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReportDataVariables()">
<h3>getReportDataVariables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.magicreport.tools.ReportDataVariable&gt;</span> <span class="element-name">getReportDataVariables</span>()</div>
<div class="block">Get all report data variable as list of <code>ReportDataVariable</code></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of <code>ReportDataVariable</code></dd>
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
