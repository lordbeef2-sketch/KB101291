# JAVA OPENAPI: EmfUml2XmiPlugin (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v4/EmfUml2XmiPlugin.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v4/EmfUml2XmiPlugin.html`
- source_sha256: `342785cc32f022a947ce96a4ed2e32bcf0e8cfabeebba775b4cd471b272550c7`
- captured_utc: `2026-07-14T16:55:19.163052+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v4](package-summary.html)

## Class EmfUml2XmiPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.plugins.Plugin](../../plugins/Plugin.html)
[com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)
com.nomagic.magicdraw.emfuml2xmi.v4.EmfUml2XmiPlugin

@OpenApipublic classEmfUml2XmiPlugin
extends [BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EmfUml2XmiPlugin](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner`
`[createCleaner](#createCleaner())()`

`protected com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction`
`[createCommandLineExporterAction](#createCommandLineExporterAction())()`

`protected com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter`
`[createExporter](#createExporter(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)`

`protected com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer`
`[createImporter](#createImporter(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)`

`protected [BaseEmfOptionsGroup](../envoptions/BaseEmfOptionsGroup.html)`
`[createOptionsGroup](#createOptionsGroup(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)`

`static [EmfUml2XmiPlugin](EmfUml2XmiPlugin.html)`
`[getInstance](#getInstance())()`
Returns instance of plugin.
`void`
`[init](#init())()`
Plugin initialization method.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)
`[close](../BaseEmfUml2XmiPlugin.html#close()), [disposeModel](../BaseEmfUml2XmiPlugin.html#disposeModel(java.util.Collection)), [exportModel](../BaseEmfUml2XmiPlugin.html#exportModel(com.nomagic.magicdraw.core.Project)), [exportXMI](../BaseEmfUml2XmiPlugin.html#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String)), [exportXMI](../BaseEmfUml2XmiPlugin.html#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus)), [getFileExtension](../BaseEmfUml2XmiPlugin.html#getFileExtension()), [getFormat](../BaseEmfUml2XmiPlugin.html#getFormat()), [getOptionsDir](../BaseEmfUml2XmiPlugin.html#getOptionsDir()), [getOptionsGroupID](../BaseEmfUml2XmiPlugin.html#getOptionsGroupID()), [getResourcesJarPath](../BaseEmfUml2XmiPlugin.html#getResourcesJarPath()), [getSupportedUmlUris](../BaseEmfUml2XmiPlugin.html#getSupportedUmlUris()), [imp0rt](../BaseEmfUml2XmiPlugin.html#imp0rt(java.lang.String)), [isSupported](../BaseEmfUml2XmiPlugin.html#isSupported())`
Methods inherited from class com.nomagic.magicdraw.plugins.[Plugin](../../plugins/Plugin.html)
`[getDescriptor](../../plugins/Plugin.html#getDescriptor())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EmfUml2XmiPlugin
public EmfUml2XmiPlugin()
 ============ METHOD DETAIL ========== 
Method Details
init
public void init()
Description copied from class: `[Plugin](../../plugins/Plugin.html#init())`
Plugin initialization method.
 Every plugin must override this method and do any action related to plugin initialization.
 For example registers actions configurators to MagicDraw application.
 This method is called by MagicDraw application during MagicDraw startup.
Overrides:
`[init](../BaseEmfUml2XmiPlugin.html#init())` in class `[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)`
getInstance
@OpenApipublic static [EmfUml2XmiPlugin](EmfUml2XmiPlugin.html) getInstance()
Returns instance of plugin.
createOptionsGroup
protected [BaseEmfOptionsGroup](../envoptions/BaseEmfOptionsGroup.html) createOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)
Specified by:
`[createOptionsGroup](../BaseEmfUml2XmiPlugin.html#createOptionsGroup(java.lang.String,java.lang.String))` in class `[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)`
createExporter
protected com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter createExporter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)
Specified by:
`[createExporter](../BaseEmfUml2XmiPlugin.html#createExporter(java.lang.String,java.lang.String))` in class `[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)`
createImporter
protected com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer createImporter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)
Specified by:
`[createImporter](../BaseEmfUml2XmiPlugin.html#createImporter(java.lang.String,java.lang.String))` in class `[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)`
createCleaner
protected com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner createCleaner()
Specified by:
`[createCleaner](../BaseEmfUml2XmiPlugin.html#createCleaner())` in class `[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)`
createCommandLineExporterAction
protected com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction createCommandLineExporterAction()
Specified by:
`[createCommandLineExporterAction](../BaseEmfUml2XmiPlugin.html#createCommandLineExporterAction())` in class `[BaseEmfUml2XmiPlugin](../BaseEmfUml2XmiPlugin.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v4</a></div>
<h1 class="title" title="Class EmfUml2XmiPlugin">Class EmfUml2XmiPlugin</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">com.nomagic.magicdraw.plugins.Plugin</a>
<div class="inheritance"><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2XmiPlugin</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v4.EmfUml2XmiPlugin</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">EmfUml2XmiPlugin</span>
<span class="extends-implements">extends <a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EmfUml2XmiPlugin</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCleaner()">createCleaner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommandLineExporterAction()">createCommandLineExporterAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createExporter(java.lang.String,java.lang.String)">createExporter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImporter(java.lang.String,java.lang.String)">createImporter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOptionsGroup(java.lang.String,java.lang.String)">createOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="EmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4">EmfUml2XmiPlugin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns instance of plugin.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init()">init</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Plugin initialization method.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2XmiPlugin">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.<a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></h3>
<code><a href="../BaseEmfUml2XmiPlugin.html#close()">close</a>, <a href="../BaseEmfUml2XmiPlugin.html#disposeModel(java.util.Collection)">disposeModel</a>, <a href="../BaseEmfUml2XmiPlugin.html#exportModel(com.nomagic.magicdraw.core.Project)">exportModel</a>, <a href="../BaseEmfUml2XmiPlugin.html#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String)">exportXMI</a>, <a href="../BaseEmfUml2XmiPlugin.html#exportXMI(com.nomagic.magicdraw.core.Project,java.lang.String,com.nomagic.task.ProgressStatus)">exportXMI</a>, <a href="../BaseEmfUml2XmiPlugin.html#getFileExtension()">getFileExtension</a>, <a href="../BaseEmfUml2XmiPlugin.html#getFormat()">getFormat</a>, <a href="../BaseEmfUml2XmiPlugin.html#getOptionsDir()">getOptionsDir</a>, <a href="../BaseEmfUml2XmiPlugin.html#getOptionsGroupID()">getOptionsGroupID</a>, <a href="../BaseEmfUml2XmiPlugin.html#getResourcesJarPath()">getResourcesJarPath</a>, <a href="../BaseEmfUml2XmiPlugin.html#getSupportedUmlUris()">getSupportedUmlUris</a>, <a href="../BaseEmfUml2XmiPlugin.html#imp0rt(java.lang.String)">imp0rt</a>, <a href="../BaseEmfUml2XmiPlugin.html#isSupported()">isSupported</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.plugins.Plugin">Methods inherited from class com.nomagic.magicdraw.plugins.<a href="../../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></h3>
<code><a href="../../plugins/Plugin.html#getDescriptor()">getDescriptor</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>EmfUml2XmiPlugin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EmfUml2XmiPlugin</span>()</div>
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
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../plugins/Plugin.html#init()">Plugin</a></code></span></div>
<div class="block">Plugin initialization method.
 Every plugin must override this method and do any action related to plugin initialization.
 For example registers actions configurators to MagicDraw application.
 This method is called by MagicDraw application during MagicDraw startup.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../BaseEmfUml2XmiPlugin.html#init()">init</a></code> in class <code><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="EmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4">EmfUml2XmiPlugin</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns instance of plugin.</div>
</section>
</li>
<li>
<section class="detail" id="createOptionsGroup(java.lang.String,java.lang.String)">
<h3>createOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></span> <span class="element-name">createOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2XmiPlugin.html#createOptionsGroup(java.lang.String,java.lang.String)">createOptionsGroup</a></code> in class <code><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createExporter(java.lang.String,java.lang.String)">
<h3>createExporter</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2Exporter</span> <span class="element-name">createExporter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2XmiPlugin.html#createExporter(java.lang.String,java.lang.String)">createExporter</a></code> in class <code><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImporter(java.lang.String,java.lang.String)">
<h3>createImporter</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.imp0rt.BaseEmfUml2Importer</span> <span class="element-name">createImporter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2XmiPlugin.html#createImporter(java.lang.String,java.lang.String)">createImporter</a></code> in class <code><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCleaner()">
<h3>createCleaner</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Cleaner</span> <span class="element-name">createCleaner</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2XmiPlugin.html#createCleaner()">createCleaner</a></code> in class <code><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommandLineExporterAction()">
<h3>createCommandLineExporterAction</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.export.commandline.BaseEclipseUml2CommandLineExporterAction</span> <span class="element-name">createCommandLineExporterAction</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2XmiPlugin.html#createCommandLineExporterAction()">createCommandLineExporterAction</a></code> in class <code><a href="../BaseEmfUml2XmiPlugin.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2XmiPlugin</a></code></dd>
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
