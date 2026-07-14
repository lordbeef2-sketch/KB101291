# JAVA OPENAPI: BaseEmfUml2XmiPlugin (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2XmiPlugin.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2XmiPlugin.html`
- source_sha256: `665665961ae321e5e8b590c74f0c71b5f4265911ad6bc934d8f7ec41ea3c6681`
- captured_utc: `2026-07-14T16:51:18.411167+00:00`

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

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
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
`void`
`[imp0rt](#imp0rt(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) file)`
Imports (opens) given Eclipse UML2 XMI
Methods inherited from class com.nomagic.magicdraw.plugins.[Plugin](../plugins/Plugin.html)
`[getDescriptor](../plugins/Plugin.html#getDescriptor())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
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
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#imp0rt(java.lang.String)">imp0rt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Imports (opens) given Eclipse UML2 XMI</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
