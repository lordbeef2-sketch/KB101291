# JAVA OPENAPI: BaseEmfUml2XmiPlugin (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2XmiPlugin.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2XmiPlugin.html`
- source_sha256: `d06466a6e4b94077385b48f1dd49fa08d93358544f779f6390f9e454d5842538`
- captured_utc: `2026-07-14T16:55:17.887036+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi](package-summary.html)

## Class BaseEmfUml2XmiPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.plugins.Plugin](../plugins/Plugin.html)
com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2XmiPlugin

Direct Known Subclasses:
`[EmfUml2XmiPlugin](v2/EmfUml2XmiPlugin.html)`, `[EmfUml2XmiPlugin](v3/EmfUml2XmiPlugin.html)`, `[EmfUml2XmiPlugin](v4/EmfUml2XmiPlugin.html)`, `[EmfUml2XmiPlugin](v5/EmfUml2XmiPlugin.html)`

@OpenApipublic abstract classBaseEmfUml2XmiPlugin
extends [Plugin](../plugins/Plugin.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[BaseEmfUml2XmiPlugin](#%3Cinit%3E(int,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.lang.String,java.lang.String))(int version,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupId,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.emfuml2xmi.Namespace> supportedUmlNamespaces,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceJarRelativePath,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) externalToolExportXmiActionId)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[close](#close())()`
MagicDraw calls this method before exiting the application.
`protected abstract com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner`
`[createCleaner](#createCleaner())()`

`protected abstract com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction`
`[createCommandLineExporterAction](#createCommandLineExporterAction())()`

`protected abstract com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter`
`[createExporter](#createExporter(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)`

`protected abstract com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer`
`[createImporter](#createImporter(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)`

`protected abstract [BaseEmfOptionsGroup](envoptions/BaseEmfOptionsGroup.html)`
`[createOptionsGroup](#createOptionsGroup(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)`

`void`
`[disposeModel](#disposeModel(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements)`
Disposes given elements.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[exportModel](#exportModel(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Exports given project to Eclipse UML2 Model
`void`
`[exportXMI](#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) destinationDir)`
Exports given project to Eclipse UML2 XMI
`void`
`[exportXMI](#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) destinationDir,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)`
Exports given project to Eclipse UML2 XMI
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileExtension](#getFileExtension())()`

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFormat](#getFormat())()`
Returns Eclipse UML2 XMI format supported by plugin.
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOptionsDir](#getOptionsDir())()`

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getOptionsGroupID](#getOptionsGroupID())()`
Returns plugin'e environment options group id.
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getResourcesJarPath](#getResourcesJarPath())()`

`final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getSupportedUmlUris](#getSupportedUmlUris())()`

`void`
`[imp0rt](#imp0rt(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) file)`
Imports (opens) given Eclipse UML2 XMI
`void`
`[init](#init())()`
Plugin initialization method.
`boolean`
`[isSupported](#isSupported())()`
MagicDraw calls this method to identify if this plugin is supported.
Methods inherited from class com.nomagic.magicdraw.plugins.[Plugin](../plugins/Plugin.html)
`[getDescriptor](../plugins/Plugin.html#getDescriptor())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseEmfUml2XmiPlugin
protected BaseEmfUml2XmiPlugin(int version,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupId,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.emfuml2xmi.Namespace> supportedUmlNamespaces,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) resourceJarRelativePath,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) externalToolExportXmiActionId)
 ============ METHOD DETAIL ========== 
Method Details
init
public void init()
Description copied from class: `[Plugin](../plugins/Plugin.html#init())`
Plugin initialization method.
 Every plugin must override this method and do any action related to plugin initialization.
 For example registers actions configurators to MagicDraw application.
 This method is called by MagicDraw application during MagicDraw startup.
Specified by:
`[init](../plugins/Plugin.html#init())` in class `[Plugin](../plugins/Plugin.html)`
getFormat
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFormat()
Returns Eclipse UML2 XMI format supported by plugin.
Returns:
Eclipse UML2 XMI format.
getFileExtension
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileExtension()
getOptionsGroupID
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOptionsGroupID()
Returns plugin'e environment options group id.
Returns:
options group id.
createExporter
protected abstract com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter createExporter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)
createImporter
protected abstract com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer createImporter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)
createCleaner
protected abstract com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner createCleaner()
createOptionsGroup
protected abstract [BaseEmfOptionsGroup](envoptions/BaseEmfOptionsGroup.html) createOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)
createCommandLineExporterAction
protected abstract com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction createCommandLineExporterAction()
exportXMI
@OpenApipublic void exportXMI([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) destinationDir)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Exports given project to Eclipse UML2 XMI
Parameters:
`project` - project to export
`destinationDir` - destination directory
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
exportXMI
@OpenApipublic void exportXMI([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) destinationDir,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Exports given project to Eclipse UML2 XMI
Parameters:
`project` - project to export
`destinationDir` - destination directory
`progressStatus` - export progress status
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
exportModel
@OpenApipublic [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) exportModel([Project](../core/Project.html) project)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Exports given project to Eclipse UML2 Model
Parameters:
`project` - project to export
Returns:
map of exported model (MagicDraw model (or profile) -> Eclipse UML2 model (or profile))
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
disposeModel
@OpenApipublic void disposeModel([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements)
Disposes given elements.
Parameters:
`elements` - collection of Eclipse UML2 element.
imp0rt
@OpenApipublic void imp0rt([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) file)
Imports (opens) given Eclipse UML2 XMI
Parameters:
`file` - Eclipse UML2 XMI file path
close
public boolean close()
Description copied from class: `[Plugin](../plugins/Plugin.html#close())`
MagicDraw calls this method before exiting the application.
 If at least one plugin returns 'false', MagicDraw application will not exit.
 Override this method and do any exit specific action(your plugin state saving for example).
Specified by:
`[close](../plugins/Plugin.html#close())` in class `[Plugin](../plugins/Plugin.html)`
Returns:
true, if plugin can be closed normally; false, if plugin cannot be closed and MagicDraw
 application can not exit
isSupported
public boolean isSupported()
Description copied from class: `[Plugin](../plugins/Plugin.html#isSupported())`
MagicDraw calls this method to identify if this plugin is supported.
 Plugin is initialized and started only if this method returns `true`.
 Override this method to check specific conditions for the plugin supportability.
Specified by:
`[isSupported](../plugins/Plugin.html#isSupported())` in class `[Plugin](../plugins/Plugin.html)`
Returns:
true, if plugin is supported; false, if plugin is not supported
getResourcesJarPath
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getResourcesJarPath()
getOptionsDir
public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOptionsDir()
getSupportedUmlUris
public final [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getSupportedUmlUris()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi</a></div>
<h1 class="title" title="Class BaseEmfUml2XmiPlugin">Class BaseEmfUml2XmiPlugin</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">com.nomagic.magicdraw.plugins.Plugin</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2XmiPlugin</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="v2/EmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2XmiPlugin</a></code>, <code><a href="v3/EmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3">EmfUml2XmiPlugin</a></code>, <code><a href="v4/EmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4">EmfUml2XmiPlugin</a></code>, <code><a href="v5/EmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v5">EmfUml2XmiPlugin</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">BaseEmfUml2XmiPlugin</span>
<span class="extends-implements">extends <a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.lang.String,java.lang.String)">BaseEmfUml2XmiPlugin</a><wbr/>(int version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.emfuml2xmi.Namespace&gt; supportedUmlNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceJarRelativePath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> externalToolExportXmiActionId)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">MagicDraw calls this method before exiting the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCleaner()">createCleaner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createCommandLineExporterAction()">createCommandLineExporterAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createExporter(java.lang.String,java.lang.String)">createExporter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createImporter(java.lang.String,java.lang.String)">createImporter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a href="envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOptionsGroup(java.lang.String,java.lang.String)">createOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeModel(java.util.Collection)">disposeModel</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disposes given elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exportModel(com.nomagic.magicdraw.core.Project)">exportModel</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Exports given project to Eclipse UML2 Model</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String)">exportXMI</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> destinationDir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Exports given project to Eclipse UML2 XMI</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus)">exportXMI</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> destinationDir,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Exports given project to Eclipse UML2 XMI</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileExtension()">getFileExtension</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFormat()">getFormat</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Eclipse UML2 XMI format supported by plugin.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptionsDir()">getOptionsDir</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptionsGroupID()">getOptionsGroupID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin'e environment options group id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourcesJarPath()">getResourcesJarPath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSupportedUmlUris()">getSupportedUmlUris</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#imp0rt(java.lang.String)">imp0rt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Imports (opens) given Eclipse UML2 XMI</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init()">init</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Plugin initialization method.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSupported()">isSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">MagicDraw calls this method to identify if this plugin is supported.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.plugins.Plugin">Methods inherited from class com.nomagic.magicdraw.plugins.<a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></h3>
<code><a href="../plugins/Plugin.html#getDescriptor()">getDescriptor</a></code></div>
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
<section class="detail" id="&lt;init&gt;(int,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.lang.String,java.lang.String)">
<h3>BaseEmfUml2XmiPlugin</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">BaseEmfUml2XmiPlugin</span><wbr/><span class="parameters">(int version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.emfuml2xmi.Namespace&gt; supportedUmlNamespaces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resourceJarRelativePath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> externalToolExportXmiActionId)</span></div>
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
<section class="detail" id="init()">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../plugins/Plugin.html#init()">Plugin</a></code></span></div>
<div class="block">Plugin initialization method.
 Every plugin must override this method and do any action related to plugin initialization.
 For example registers actions configurators to MagicDraw application.
 This method is called by MagicDraw application during MagicDraw startup.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../plugins/Plugin.html#init()">init</a></code> in class <code><a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFormat()">
<h3>getFormat</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFormat</span>()</div>
<div class="block">Returns Eclipse UML2 XMI format supported by plugin.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Eclipse UML2 XMI format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileExtension()">
<h3>getFileExtension</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileExtension</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOptionsGroupID()">
<h3>getOptionsGroupID</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOptionsGroupID</span>()</div>
<div class="block">Returns plugin'e environment options group id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>options group id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExporter(java.lang.String,java.lang.String)">
<h3>createExporter</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter</span> <span class="element-name">createExporter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</span></div>
</section>
</li>
<li>
<section class="detail" id="createImporter(java.lang.String,java.lang.String)">
<h3>createImporter</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer</span> <span class="element-name">createImporter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</span></div>
</section>
</li>
<li>
<section class="detail" id="createCleaner()">
<h3>createCleaner</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner</span> <span class="element-name">createCleaner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="createOptionsGroup(java.lang.String,java.lang.String)">
<h3>createOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a href="envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></span> <span class="element-name">createOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</span></div>
</section>
</li>
<li>
<section class="detail" id="createCommandLineExporterAction()">
<h3>createCommandLineExporterAction</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction</span> <span class="element-name">createCommandLineExporterAction</span>()</div>
</section>
</li>
<li>
<section class="detail" id="exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>exportXMI</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">exportXMI</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> destinationDir)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports given project to Eclipse UML2 XMI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to export</dd>
<dd><code>destinationDir</code> - destination directory</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus)">
<h3>exportXMI</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">exportXMI</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> destinationDir,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span>
               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports given project to Eclipse UML2 XMI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to export</dd>
<dd><code>destinationDir</code> - destination directory</dd>
<dd><code>progressStatus</code> - export progress status</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportModel(com.nomagic.magicdraw.core.Project)">
<h3>exportModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">exportModel</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span>
                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports given project to Eclipse UML2 Model</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to export</dd>
<dt>Returns:</dt>
<dd>map of exported model (MagicDraw model (or profile) -&gt; Eclipse UML2 model (or profile))</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeModel(java.util.Collection)">
<h3>disposeModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disposeModel</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements)</span></div>
<div class="block">Disposes given elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - collection of Eclipse UML2 element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="imp0rt(java.lang.String)">
<h3>imp0rt</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">imp0rt</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</span></div>
<div class="block">Imports (opens) given Eclipse UML2 XMI</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - Eclipse UML2 XMI file path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">close</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../plugins/Plugin.html#close()">Plugin</a></code></span></div>
<div class="block">MagicDraw calls this method before exiting the application.
 If at least one plugin returns 'false', MagicDraw application will not exit.
 Override this method and do any exit specific action(your plugin state saving for example).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../plugins/Plugin.html#close()">close</a></code> in class <code><a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></code></dd>
<dt>Returns:</dt>
<dd>true, if plugin can be closed normally; false, if plugin cannot be closed and MagicDraw
 application can not exit</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupported()">
<h3>isSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSupported</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../plugins/Plugin.html#isSupported()">Plugin</a></code></span></div>
<div class="block">MagicDraw calls this method to identify if this plugin is supported.
 Plugin is initialized and started only if this method returns <code>true</code>.
 Override this method to check specific conditions for the plugin supportability.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../plugins/Plugin.html#isSupported()">isSupported</a></code> in class <code><a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></code></dd>
<dt>Returns:</dt>
<dd>true, if plugin is supported; false, if plugin is not supported</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResourcesJarPath()">
<h3>getResourcesJarPath</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResourcesJarPath</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOptionsDir()">
<h3>getOptionsDir</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getOptionsDir</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSupportedUmlUris()">
<h3>getSupportedUmlUris</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getSupportedUmlUris</span>()</div>
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
