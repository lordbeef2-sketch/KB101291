# JAVA OPENAPI: MofPlugin (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/mof/MofPlugin.html
- source_path: `com/nomagic/magicdraw/mof/MofPlugin.html`
- source_sha256: `20130759cbfc7ad2281549bae560654ada47014e0495bb52edebb8408fef367d`
- captured_utc: `2026-07-14T16:55:26.726136+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.mof](package-summary.html)

## Class MofPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.plugins.Plugin](../plugins/Plugin.html)
com.nomagic.magicdraw.mof.MofPlugin

@OpenApipublic classMofPlugin
extends [Plugin](../plugins/Plugin.html)
Plugin provides MOF (EMOF and CMOF) export/import functionality.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MofPlugin](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[close](#close())()`
MagicDraw calls this method before exiting the application.
`static void`
`[exportMof](#exportMof(com.nomagic.magicdraw.core.Project,java.util.Set,com.nomagic.magicdraw.mof.MofType,java.io.File,boolean,boolean,com.nomagic.task.ProgressStatus))([Project](../core/Project.html) project,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [MofType](MofType.html) mof,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) mofFile,
 boolean runValidation,
 boolean silent,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)`
Exports given project to MOF XMI.
`static void`
`[exportMof](#exportMof(com.nomagic.magicdraw.core.Project,java.util.Set,com.nomagic.magicdraw.mof.MofType,java.io.File,boolean,com.nomagic.task.ProgressStatus))([Project](../core/Project.html) project,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [MofType](MofType.html) mof,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) mofFile,
 boolean runValidation,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)`
Exports given project to MOF XMI.
`static void`
`[importMof](#importMof(java.io.File,com.nomagic.magicdraw.mof.MofDescriptor,java.io.File,com.nomagic.task.ProgressStatus,boolean))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) mofFile,
 [MofDescriptor](MofDescriptor.html) mof,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) umlFile,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus,
 boolean removeTemp)`
Imports given MOF to new project.
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
MofPlugin
public MofPlugin()
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
exportMof
@OpenApipublic static void exportMof([Project](../core/Project.html) project,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [MofType](MofType.html) mof,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) mofFile,
 boolean runValidation,
 boolean silent,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Exports given project to MOF XMI.
Parameters:
`project` - project to export.
`packages` - project packages to export.
`mof` - mof type.
`mofFile` - output file.
`runValidation` - run model validation when exporting.
`silent` - silent (wihtout user interruption) export
`progressStatus` - progress status.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
exportMof
@OpenApipublic static void exportMof([Project](../core/Project.html) project,
 [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> packages,
 [MofType](MofType.html) mof,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) mofFile,
 boolean runValidation,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Exports given project to MOF XMI.
Parameters:
`project` - project to export.
`packages` - project packages to export.
`mof` - mof type.
`mofFile` - output file.
`runValidation` - run model validation when exporting.
`progressStatus` - progress status.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
importMof
@OpenApipublic static void importMof([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) mofFile,
 [MofDescriptor](MofDescriptor.html) mof,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) umlFile,
 [ProgressStatus](../../task/ProgressStatus.html) progressStatus,
 boolean removeTemp)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Imports given MOF to new project.
Parameters:
`mofFile` - MOF file to import.
`mof` - MOF type.
`umlFile` - Transformed file.
`progressStatus` - progress status.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.mof</a></div>
<h1 class="title" title="Class MofPlugin">Class MofPlugin</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">com.nomagic.magicdraw.plugins.Plugin</a>
<div class="inheritance">com.nomagic.magicdraw.mof.MofPlugin</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MofPlugin</span>
<span class="extends-implements">extends <a href="../plugins/Plugin.html" title="class in com.nomagic.magicdraw.plugins">Plugin</a></span></div>
<div class="block">Plugin provides MOF (EMOF and CMOF) export/import functionality.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MofPlugin</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">MagicDraw calls this method before exiting the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportMof(com.nomagic.magicdraw.core.Project,java.util.Set,com.nomagic.magicdraw.mof.MofType,java.io.File,boolean,boolean,com.nomagic.task.ProgressStatus)">exportMof</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a href="MofType.html" title="class in com.nomagic.magicdraw.mof">MofType</a> mof,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> mofFile,
 boolean runValidation,
 boolean silent,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports given project to MOF XMI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#exportMof(com.nomagic.magicdraw.core.Project,java.util.Set,com.nomagic.magicdraw.mof.MofType,java.io.File,boolean,com.nomagic.task.ProgressStatus)">exportMof</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a href="MofType.html" title="class in com.nomagic.magicdraw.mof">MofType</a> mof,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> mofFile,
 boolean runValidation,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Exports given project to MOF XMI.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#importMof(java.io.File,com.nomagic.magicdraw.mof.MofDescriptor,java.io.File,com.nomagic.task.ProgressStatus,boolean)">importMof</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> mofFile,
 <a href="MofDescriptor.html" title="class in com.nomagic.magicdraw.mof">MofDescriptor</a> mof,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> umlFile,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus,
 boolean removeTemp)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Imports given MOF to new project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init()">init</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Plugin initialization method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSupported()">isSupported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
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
<section class="detail" id="&lt;init&gt;()">
<h3>MofPlugin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MofPlugin</span>()</div>
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
<section class="detail" id="exportMof(com.nomagic.magicdraw.core.Project,java.util.Set,com.nomagic.magicdraw.mof.MofType,java.io.File,boolean,boolean,com.nomagic.task.ProgressStatus)">
<h3>exportMof</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">exportMof</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a href="MofType.html" title="class in com.nomagic.magicdraw.mof">MofType</a> mof,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> mofFile,
 boolean runValidation,
 boolean silent,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports given project to MOF XMI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to export.</dd>
<dd><code>packages</code> - project packages to export.</dd>
<dd><code>mof</code> - mof type.</dd>
<dd><code>mofFile</code> - output file.</dd>
<dd><code>runValidation</code> - run model validation when exporting.</dd>
<dd><code>silent</code> - silent (wihtout user interruption) export</dd>
<dd><code>progressStatus</code> - progress status.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exportMof(com.nomagic.magicdraw.core.Project,java.util.Set,com.nomagic.magicdraw.mof.MofType,java.io.File,boolean,com.nomagic.task.ProgressStatus)">
<h3>exportMof</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">exportMof</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; packages,
 <a href="MofType.html" title="class in com.nomagic.magicdraw.mof">MofType</a> mof,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> mofFile,
 boolean runValidation,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Exports given project to MOF XMI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to export.</dd>
<dd><code>packages</code> - project packages to export.</dd>
<dd><code>mof</code> - mof type.</dd>
<dd><code>mofFile</code> - output file.</dd>
<dd><code>runValidation</code> - run model validation when exporting.</dd>
<dd><code>progressStatus</code> - progress status.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importMof(java.io.File,com.nomagic.magicdraw.mof.MofDescriptor,java.io.File,com.nomagic.task.ProgressStatus,boolean)">
<h3>importMof</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">importMof</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> mofFile,
 <a href="MofDescriptor.html" title="class in com.nomagic.magicdraw.mof">MofDescriptor</a> mof,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> umlFile,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus,
 boolean removeTemp)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Imports given MOF to new project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mofFile</code> - MOF file to import.</dd>
<dd><code>mof</code> - MOF type.</dd>
<dd><code>umlFile</code> - Transformed file.</dd>
<dd><code>progressStatus</code> - progress status.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
