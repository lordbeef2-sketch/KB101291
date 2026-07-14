# JAVA OPENAPI: MethodExceptionHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/velocity/MethodExceptionHandler.html
- source_path: `com/nomagic/magicreport/engine/velocity/MethodExceptionHandler.html`
- source_sha256: `0c2f460aa9ae19232ec0bec023e563c5e885a3de3d4d35931ffb266537b96081`
- captured_utc: `2026-07-14T16:46:13.247977+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class MethodExceptionHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.apache.velocity.app.event.implement.PrintExceptions
com.nomagic.magicreport.engine.velocity.MethodExceptionHandler

All Implemented Interfaces:
`org.apache.velocity.app.event.EventHandler`, `org.apache.velocity.app.event.MethodExceptionEventHandler`, `org.apache.velocity.util.RuntimeServicesAware`

@OpenApiAllpublic classMethodExceptionHandler
extends org.apache.velocity.app.event.implement.PrintExceptions

Event handler called when a method throws an exception. By default Velocity return an exception Object in
 [`methodException(Class, String, Exception)`](#methodException(java.lang.Class,java.lang.String,java.lang.Exception)) and reference to method name is corrupted. This class will
 manage it manually to avoid error reference in Velocity.

Since:
Jun 18, 2007

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MethodExceptionHandler](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[methodException](#methodException(java.lang.Class,java.lang.String,java.lang.Exception))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)`
Render the method exception, and optionally the exception message and stack trace.
Methods inherited from class org.apache.velocity.app.event.implement.PrintExceptions
`methodException, setRuntimeServices`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MethodExceptionHandler
public MethodExceptionHandler()
 ============ METHOD DETAIL ========== 
Method Details
methodException
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) methodException([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Render the method exception, and optionally the exception message and stack trace. This method always return
 `null` to keep valid reference and property pass to
 [`VelocityReferenceHandler.invalidGetMethod(org.apache.velocity.context.Context, java.lang.String, java.lang.Object, java.lang.String, org.apache.velocity.util.introspection.Info)`](VelocityReferenceHandler.html#invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info))
Parameters:
`clazz` - the class of the object the method is being applied to
`method` - the method
`e` - the thrown exception
Returns:
an `null` object.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - an exception to be thrown instead inserting an object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class MethodExceptionHandler">Class MethodExceptionHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.apache.velocity.app.event.implement.PrintExceptions
<div class="inheritance">com.nomagic.magicreport.engine.velocity.MethodExceptionHandler</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>org.apache.velocity.app.event.EventHandler</code>, <code>org.apache.velocity.app.event.MethodExceptionEventHandler</code>, <code>org.apache.velocity.util.RuntimeServicesAware</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MethodExceptionHandler</span>
<span class="extends-implements">extends org.apache.velocity.app.event.implement.PrintExceptions</span></div>
<div class="block">Event handler called when a method throws an exception. By default Velocity return an exception Object in
 <a href="#methodException(java.lang.Class,java.lang.String,java.lang.Exception)"><code>methodException(Class, String, Exception)</code></a> and reference to method name is corrupted. This class will
 manage it manually to avoid error reference in Velocity.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 18, 2007</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MethodExceptionHandler</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#methodException(java.lang.Class,java.lang.String,java.lang.Exception)">methodException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Render the method exception, and optionally the exception message and stack trace.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.apache.velocity.app.event.implement.PrintExceptions">Methods inherited from class org.apache.velocity.app.event.implement.PrintExceptions</h3>
<code>methodException, setRuntimeServices</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>MethodExceptionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MethodExceptionHandler</span>()</div>
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
<section class="detail" id="methodException(java.lang.Class,java.lang.String,java.lang.Exception)">
<h3>methodException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">methodException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Render the method exception, and optionally the exception message and stack trace. This method always return
 <code>null</code> to keep valid reference and property pass to
 <a href="VelocityReferenceHandler.html#invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info)"><code>VelocityReferenceHandler.invalidGetMethod(org.apache.velocity.context.Context, java.lang.String, java.lang.Object, java.lang.String, org.apache.velocity.util.introspection.Info)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - the class of the object the method is being applied to</dd>
<dd><code>method</code> - the method</dd>
<dd><code>e</code> - the thrown exception</dd>
<dt>Returns:</dt>
<dd>an <code>null</code> object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - an exception to be thrown instead inserting an object</dd>
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
