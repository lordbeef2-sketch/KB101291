# JAVA OPENAPI: DOCXImporterTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/importer/DOCXImporterTool.html
- source_path: `com/nomagic/reportwizard/tools/importer/DOCXImporterTool.html`
- source_sha256: `2f0c2173d498c8c9a6e808af28834758c9762adde92902e492de7a61adb5fecd`
- captured_utc: `2026-07-14T16:46:16.143015+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.importer](package-summary.html)

## Class DOCXImporterTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
[com.nomagic.reportwizard.tools.ImportTool](../ImportTool.html)
[com.nomagic.reportwizard.tools.importer.DefaultImporterTool](DefaultImporterTool.html)
com.nomagic.reportwizard.tools.importer.DOCXImporterTool

All Implemented Interfaces:
`[IChildEngine](../../../magicreport/engine/IChildEngine.html)`, `[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html)`

@OpenApiAllpublic classDOCXImporterTool
extends [DefaultImporterTool](DefaultImporterTool.html)

This tool will allow user to import docx template.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.reportwizard.tools.importer.DOCXImporterTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DOCXImporterTool](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../../../magicreport/engine/ITemplateEngine.html) iTemplateEngine)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[importer](#importer(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) importedFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) importedSectionName)`
Gets the String content of the imported file.
`protected boolean`
`[isSupport](#isSupport(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) engineType)`
CHeck supported engine type
`protected void`
`[setupEngine](#setupEngine(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../../../magicreport/engine/ITemplateEngine.html) engine)`
Set up engine. 

 Add properties and context to engine.
Methods inherited from class com.nomagic.reportwizard.tools.importer.[DefaultImporterTool](DefaultImporterTool.html)
`[getCanonicalTemplate](DefaultImporterTool.html#getCanonicalTemplate(java.lang.String)), [getEngineType](DefaultImporterTool.html#getEngineType()), [getTemplateFile](DefaultImporterTool.html#getTemplateFile(java.lang.String)), [importer](DefaultImporterTool.html#importer(java.lang.Object,java.lang.String)), [importer](DefaultImporterTool.html#importer(java.lang.String,java.lang.String)), [setEngineType](DefaultImporterTool.html#setEngineType(java.lang.String)), [setTemplateEngine](DefaultImporterTool.html#setTemplateEngine(java.lang.String))`
Methods inherited from class com.nomagic.reportwizard.tools.[ImportTool](../ImportTool.html)
`[fileImporter](../ImportTool.html#fileImporter(java.lang.Object,java.lang.String)), [getParentEngine](../ImportTool.html#getParentEngine()), [importer](../ImportTool.html#importer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [include](../ImportTool.html#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [include](../ImportTool.html#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [include](../ImportTool.html#include(java.lang.String)), [include](../ImportTool.html#include(java.lang.String,java.lang.String)), [includeSection](../ImportTool.html#includeSection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [includeSection](../ImportTool.html#includeSection(java.lang.String,java.lang.String)), [isParentSupportChild](../ImportTool.html#isParentSupportChild(java.lang.String)), [setParentEngine](../ImportTool.html#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)), [setupTool](../ImportTool.html#setupTool(com.nomagic.reportwizard.tools.importer.DefaultImporterTool)), [update](../ImportTool.html#update(java.util.Observable,java.lang.Object))`
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
DOCXImporterTool
public DOCXImporterTool([ITemplateEngine](../../../magicreport/engine/ITemplateEngine.html) iTemplateEngine)
Constructor.
Parameters:
`iTemplateEngine` - parent engine
 ============ METHOD DETAIL ========== 
Method Details
importer
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) importer([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) importedFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) importedSectionName)
Description copied from class: `[DefaultImporterTool](DefaultImporterTool.html#importer(java.io.File,java.lang.String))`
Gets the String content of the imported file. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.
Overrides:
`[importer](DefaultImporterTool.html#importer(java.io.File,java.lang.String))` in class `[DefaultImporterTool](DefaultImporterTool.html)`
Parameters:
`importedFile` - the childTemplate file to be evaluated
`importedSectionName` - if there is a section else this is null
Returns:
the evaluated and validated output from childTemplate
isSupport
protected boolean isSupport([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) engineType)
Description copied from class: `[DefaultImporterTool](DefaultImporterTool.html#isSupport(java.lang.String))`
CHeck supported engine type
Overrides:
`[isSupport](DefaultImporterTool.html#isSupport(java.lang.String))` in class `[DefaultImporterTool](DefaultImporterTool.html)`
Parameters:
`engineType` - engine type
Returns:
true if the specific engine is supported, otherwise; false
setupEngine
protected void setupEngine([ITemplateEngine](../../../magicreport/engine/ITemplateEngine.html) engine)
Description copied from class: `[DefaultImporterTool](DefaultImporterTool.html#setupEngine(com.nomagic.magicreport.engine.ITemplateEngine))`
Set up engine. 

 Add properties and context to engine.
Overrides:
`[setupEngine](DefaultImporterTool.html#setupEngine(com.nomagic.magicreport.engine.ITemplateEngine))` in class `[DefaultImporterTool](DefaultImporterTool.html)`
Parameters:
`engine` - current engine

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.importer</a></div>
<h1 class="title" title="Class DOCXImporterTool">Class DOCXImporterTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance"><a href="../ImportTool.html" title="class in com.nomagic.reportwizard.tools">com.nomagic.reportwizard.tools.ImportTool</a>
<div class="inheritance"><a href="DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">com.nomagic.reportwizard.tools.importer.DefaultImporterTool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.importer.DOCXImporterTool</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../magicreport/engine/IChildEngine.html" title="interface in com.nomagic.magicreport.engine">IChildEngine</a></code>, <code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DOCXImporterTool</span>
<span class="extends-implements">extends <a href="DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></span></div>
<div class="block">This tool will allow user to import docx template.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.reportwizard.tools.importer.DOCXImporterTool">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine)">DOCXImporterTool</a><wbr/>(<a href="../../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> iTemplateEngine)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importer(java.io.File,java.lang.String)">importer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> importedFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> importedSectionName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the String content of the imported file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSupport(java.lang.String)">isSupport</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> engineType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">CHeck supported engine type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setupEngine(com.nomagic.magicreport.engine.ITemplateEngine)">setupEngine</a><wbr/>(<a href="../../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set up engine.<br/>
 Add properties and context to engine.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.reportwizard.tools.importer.DefaultImporterTool">Methods inherited from class com.nomagic.reportwizard.tools.importer.<a href="DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></h3>
<code><a href="DefaultImporterTool.html#getCanonicalTemplate(java.lang.String)">getCanonicalTemplate</a>, <a href="DefaultImporterTool.html#getEngineType()">getEngineType</a>, <a href="DefaultImporterTool.html#getTemplateFile(java.lang.String)">getTemplateFile</a>, <a href="DefaultImporterTool.html#importer(java.lang.Object,java.lang.String)">importer</a>, <a href="DefaultImporterTool.html#importer(java.lang.String,java.lang.String)">importer</a>, <a href="DefaultImporterTool.html#setEngineType(java.lang.String)">setEngineType</a>, <a href="DefaultImporterTool.html#setTemplateEngine(java.lang.String)">setTemplateEngine</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.reportwizard.tools.ImportTool">Methods inherited from class com.nomagic.reportwizard.tools.<a href="../ImportTool.html" title="class in com.nomagic.reportwizard.tools">ImportTool</a></h3>
<code><a href="../ImportTool.html#fileImporter(java.lang.Object,java.lang.String)">fileImporter</a>, <a href="../ImportTool.html#getParentEngine()">getParentEngine</a>, <a href="../ImportTool.html#importer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">importer</a>, <a href="../ImportTool.html#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">include</a>, <a href="../ImportTool.html#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">include</a>, <a href="../ImportTool.html#include(java.lang.String)">include</a>, <a href="../ImportTool.html#include(java.lang.String,java.lang.String)">include</a>, <a href="../ImportTool.html#includeSection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">includeSection</a>, <a href="../ImportTool.html#includeSection(java.lang.String,java.lang.String)">includeSection</a>, <a href="../ImportTool.html#isParentSupportChild(java.lang.String)">isParentSupportChild</a>, <a href="../ImportTool.html#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">setParentEngine</a>, <a href="../ImportTool.html#setupTool(com.nomagic.reportwizard.tools.importer.DefaultImporterTool)">setupTool</a>, <a href="../ImportTool.html#update(java.util.Observable,java.lang.Object)">update</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>DOCXImporterTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DOCXImporterTool</span><wbr/><span class="parameters">(<a href="../../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> iTemplateEngine)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>iTemplateEngine</code> - parent engine</dd>
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
<section class="detail" id="importer(java.io.File,java.lang.String)">
<h3>importer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">importer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> importedFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> importedSectionName)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="DefaultImporterTool.html#importer(java.io.File,java.lang.String)">DefaultImporterTool</a></code></span></div>
<div class="block">Gets the String content of the imported file. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultImporterTool.html#importer(java.io.File,java.lang.String)">importer</a></code> in class <code><a href="DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>importedFile</code> - the childTemplate file to be evaluated</dd>
<dd><code>importedSectionName</code> - if there is a section else this is null</dd>
<dt>Returns:</dt>
<dd>the evaluated and validated output from childTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupport(java.lang.String)">
<h3>isSupport</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isSupport</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> engineType)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="DefaultImporterTool.html#isSupport(java.lang.String)">DefaultImporterTool</a></code></span></div>
<div class="block">CHeck supported engine type</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultImporterTool.html#isSupport(java.lang.String)">isSupport</a></code> in class <code><a href="DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>engineType</code> - engine type</dd>
<dt>Returns:</dt>
<dd>true if the specific engine is supported, otherwise; false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setupEngine(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>setupEngine</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setupEngine</span><wbr/><span class="parameters">(<a href="../../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="DefaultImporterTool.html#setupEngine(com.nomagic.magicreport.engine.ITemplateEngine)">DefaultImporterTool</a></code></span></div>
<div class="block">Set up engine.<br/>
 Add properties and context to engine.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultImporterTool.html#setupEngine(com.nomagic.magicreport.engine.ITemplateEngine)">setupEngine</a></code> in class <code><a href="DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>engine</code> - current engine</dd>
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
