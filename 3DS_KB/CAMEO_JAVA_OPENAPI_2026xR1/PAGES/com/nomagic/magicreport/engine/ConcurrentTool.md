# JAVA OPENAPI: ConcurrentTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/ConcurrentTool.html
- source_path: `com/nomagic/magicreport/engine/ConcurrentTool.html`
- source_sha256: `9fbd2108f2b72ca3ed5bcf110cd0c05d9eee00aeb6a6e42921cbb63803215631`
- captured_utc: `2026-07-14T16:46:11.768957+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class ConcurrentTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](Tool.html)
com.nomagic.magicreport.engine.ConcurrentTool

All Implemented Interfaces:
`[ITool](ITool.html)`, `[IVariable](../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ExportTool2](../../magicdraw/magicreport/tools/ExportTool2.html)`, `[ExportTool3](../../magicdraw/magicreport/tools/ExportTool3.html)`, `[FileTool](tools/FileTool.html)`

@OpenApiAllpublic abstract classConcurrentTool
extends [Tool](Tool.html)

Provide concurrent task running in template engine. This class implements an unbounded thread-safe queue, which
 orders element FIFO (first-in-first-out). New task are inserted at the tail of the queue, and the queue
 retrieval operations obtain elements at the head of the queue. The tool extends from this class is ideally for
 process long task which doesn't want other task to wait until process is completed

Since:
Oct 18, 2007
See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.magicreport.engine.ConcurrentTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ConcurrentTool.ConsumeObject](ConcurrentTool.ConsumeObject.html)`
Inner class which acts as the reference for a file pending deletion.
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](ITool.html)
`[ITool.HTMLString](ITool.HTMLString.html), [ITool.RetainedString](ITool.RetainedString.html), [ITool.Void](ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.[Tool](Tool.html)
`[context](Tool.html#context), [properties](Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](ITool.html)
`[VOID](ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ConcurrentTool](#%3Cinit%3E())()`
Create concurrent tool.
`protected`
`[ConcurrentTool](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Create concurrent tool with name.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`abstract void`
`[consume](#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))([ConcurrentTool.ConsumeObject](ConcurrentTool.ConsumeObject.html) consumeObject)`
Consume a object.
`void`
`[destroy](#destroy())()`
Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.
`int`
`[getCustomPoolSize](#getCustomPoolSize())()`

`protected boolean`
`[isNoSpaceException](#isNoSpaceException(java.lang.Exception))([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)`

`boolean`
`[isRunning](#isRunning())()`
Returns true if the internal thread is running.
`boolean`
`[offer](#offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))([ConcurrentTool.ConsumeObject](ConcurrentTool.ConsumeObject.html) consumeObject)`
Inserts the specified element into this queue, if possible.
Methods inherited from class com.nomagic.magicreport.engine.[Tool](Tool.html)
`[clone](Tool.html#clone()), [getContext](Tool.html#getContext()), [getProperties](Tool.html#getProperties()), [getProperty](Tool.html#getProperty(java.lang.String)), [getProperty](Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](Tool.html#notifyObservers(java.lang.Object)), [setContext](Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](ITool.html)
`[clearTool](ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ConcurrentTool
protected ConcurrentTool()
Create concurrent tool.
ConcurrentTool
protected ConcurrentTool([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Create concurrent tool with name.
Parameters:
`name` - name of consume thread.
 ============ METHOD DETAIL ========== 
Method Details
getCustomPoolSize
public int getCustomPoolSize()
destroy
public void destroy()
Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.
isRunning
public boolean isRunning()
 throws [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
Returns true if the internal thread is running.
Returns:
true if the internal thread is running.
Throws:
`[Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)` - when exception occurs
offer
public boolean offer([ConcurrentTool.ConsumeObject](ConcurrentTool.ConsumeObject.html) consumeObject)
Inserts the specified element into this queue, if possible.
Parameters:
`consumeObject` - the consume object to insert.
Returns:
true if it was possible to add the consume object to this queue, else false
consume
public abstract void consume([ConcurrentTool.ConsumeObject](ConcurrentTool.ConsumeObject.html) consumeObject)
Consume a object.
Parameters:
`consumeObject` - consume object
isNoSpaceException
protected boolean isNoSpaceException([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class ConcurrentTool">Class ConcurrentTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.magicreport.engine.ConcurrentTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../magicdraw/magicreport/tools/ExportTool2.html" title="class in com.nomagic.magicdraw.magicreport.tools">ExportTool2</a></code>, <code><a href="../../magicdraw/magicreport/tools/ExportTool3.html" title="class in com.nomagic.magicdraw.magicreport.tools">ExportTool3</a></code>, <code><a href="tools/FileTool.html" title="class in com.nomagic.magicreport.engine.tools">FileTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ConcurrentTool</span>
<span class="extends-implements">extends <a href="Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">Provide concurrent task running in template engine. This class implements an unbounded thread-safe queue, which
 orders element FIFO (first-in-first-out). New task are inserted at the tail of the queue, and the queue
 retrieval operations obtain elements at the head of the queue. The tool extends from this class is ideally for
 process long task which doesn't want other task to wait until process is completed</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Oct 18, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.magicreport.engine.ConcurrentTool">Serialized Form</a></li>
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
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a></code></div>
<div class="col-last even-row-color">
<div class="block">Inner class which acts as the reference for a file pending deletion.</div>
</div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="Tool.html#context">context</a>, <a href="Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="ITool.html#VOID">VOID</a></code></div>
</section>
</li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ConcurrentTool</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create concurrent tool.</div>
</div>
<div class="col-first odd-row-color"><code>protected </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">ConcurrentTool</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create concurrent tool with name.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">consume</a><wbr/>(<a href="ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Consume a object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomPoolSize()">getCustomPoolSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRunning()">isRunning</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if the internal thread is running.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">offer</a><wbr/>(<a href="ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Inserts the specified element into this queue, if possible.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="Tool.html#clone()">clone</a>, <a href="Tool.html#getContext()">getContext</a>, <a href="Tool.html#getProperties()">getProperties</a>, <a href="Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="ITool.html#clearTool()">clearTool</a></code></div>
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
<h3>ConcurrentTool</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ConcurrentTool</span>()</div>
<div class="block">Create concurrent tool.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>ConcurrentTool</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ConcurrentTool</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Create concurrent tool with name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of consume thread.</dd>
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
<section class="detail" id="getCustomPoolSize()">
<h3>getCustomPoolSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getCustomPoolSize</span>()</div>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block">Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.</div>
</section>
</li>
<li>
<section class="detail" id="isRunning()">
<h3>isRunning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRunning</span>()
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></span></div>
<div class="block">Returns true if the internal thread is running.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the internal thread is running.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></code> - when exception occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">
<h3>offer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">offer</span><wbr/><span class="parameters">(<a href="ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</span></div>
<div class="block">Inserts the specified element into this queue, if possible.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumeObject</code> - the consume object to insert.</dd>
<dt>Returns:</dt>
<dd><tt>true</tt> if it was possible to add the consume object to this queue, else <tt>false</tt></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">
<h3>consume</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">consume</span><wbr/><span class="parameters">(<a href="ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</span></div>
<div class="block">Consume a object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>consumeObject</code> - consume object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNoSpaceException(java.lang.Exception)">
<h3>isNoSpaceException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNoSpaceException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span></div>
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
