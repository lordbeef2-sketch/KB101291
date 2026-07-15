# JAVA OPENAPI: StreamReader (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/license/utils/exec/StreamReader.html
- source_path: `com/nomagic/license/utils/exec/StreamReader.html`
- source_sha256: `03041f9f5c2656feac21a7939d99547f611f627088cdc26631c468bc35431f01`
- captured_utc: `2026-07-14T16:57:43.046368+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.license.utils.exec](package-summary.html)

## Class StreamReader

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.Thread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html)
com.nomagic.license.utils.exec.StreamReader

All Implemented Interfaces:
`[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`

@OpenApiAllpublic classStreamReader
extends [Thread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.lang.[Thread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html)
`[MAX_PRIORITY](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#MAX_PRIORITY), [MIN_PRIORITY](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#MIN_PRIORITY), [NORM_PRIORITY](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#NORM_PRIORITY)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StreamReader](#%3Cinit%3E(java.lang.String,java.lang.StringBuffer,java.io.InputStream))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html) buffer,
 [InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) stream)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
`[getException](#getException())()`

`void`
`[run](#run())()`
Methods inherited from class java.lang.[Thread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html)
`[activeCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#activeCount()), [checkAccess](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#checkAccess()), [clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#clone()), [countStackFrames](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#countStackFrames()), [currentThread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#currentThread()), [dumpStack](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#dumpStack()), [enumerate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#enumerate(java.lang.Thread%5B%5D)), [getAllStackTraces](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getAllStackTraces()), [getContextClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getContextClassLoader()), [getDefaultUncaughtExceptionHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getDefaultUncaughtExceptionHandler()), [getId](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getId()), [getName](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getName()), [getPriority](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getPriority()), [getStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getStackTrace()), [getState](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getState()), [getThreadGroup](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getThreadGroup()), [getUncaughtExceptionHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getUncaughtExceptionHandler()), [holdsLock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#holdsLock(java.lang.Object)), [interrupt](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#interrupt()), [interrupted](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#interrupted()), [isAlive](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isAlive()), [isDaemon](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isDaemon()), [isInterrupted](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isInterrupted()), [isVirtual](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isVirtual()), [join](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join()), [join](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join(long)), [join](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join(long,int)), [join](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join(java.time.Duration)), [ofPlatform](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#ofPlatform()), [ofVirtual](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#ofVirtual()), [onSpinWait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#onSpinWait()), [resume](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#resume()), [setContextClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setContextClassLoader(java.lang.ClassLoader)), [setDaemon](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setDaemon(boolean)), [setDefaultUncaughtExceptionHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setDefaultUncaughtExceptionHandler(java.lang.Thread.UncaughtExceptionHandler)), [setName](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setName(java.lang.String)), [setPriority](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setPriority(int)), [setUncaughtExceptionHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setUncaughtExceptionHandler(java.lang.Thread.UncaughtExceptionHandler)), [sleep](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#sleep(long)), [sleep](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#sleep(long,int)), [sleep](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#sleep(java.time.Duration)), [start](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#start()), [startVirtualThread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#startVirtualThread(java.lang.Runnable)), [stop](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#stop()), [suspend](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#suspend()), [threadId](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#threadId()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#toString()), [yield](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#yield())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StreamReader
public StreamReader([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [StringBuffer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html) buffer,
 [InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) stream)
Parameters:
`name` - thread name
`buffer` - buffer to fill
`stream` - input stream ( process output )
 ============ METHOD DETAIL ========== 
Method Details
run
public void run()
Specified by:
`[run](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html#run())` in interface `[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`
Overrides:
`[run](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#run())` in class `[Thread](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html)`
getException
public [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) getException()
Returns:
generated exception on thread execution, null if none occurred

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.license.utils.exec</a></div>
<h1 class="title" title="Class StreamReader">Class StreamReader</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html" title="class or interface in java.lang">java.lang.Thread</a>
<div class="inheritance">com.nomagic.license.utils.exec.StreamReader</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StreamReader</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html" title="class or interface in java.lang">Thread</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.lang.Thread">Fields inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html" title="class or interface in java.lang">Thread</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#MAX_PRIORITY" title="class or interface in java.lang">MAX_PRIORITY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#MIN_PRIORITY" title="class or interface in java.lang">MIN_PRIORITY</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#NORM_PRIORITY" title="class or interface in java.lang">NORM_PRIORITY</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.StringBuffer,java.io.InputStream)">StreamReader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> buffer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getException()">getException</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#run()">run</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Thread">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html" title="class or interface in java.lang">Thread</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#activeCount()" title="class or interface in java.lang">activeCount</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#checkAccess()" title="class or interface in java.lang">checkAccess</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#countStackFrames()" title="class or interface in java.lang">countStackFrames</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#currentThread()" title="class or interface in java.lang">currentThread</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#dumpStack()" title="class or interface in java.lang">dumpStack</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#enumerate(java.lang.Thread%5B%5D)" title="class or interface in java.lang">enumerate</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getAllStackTraces()" title="class or interface in java.lang">getAllStackTraces</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getContextClassLoader()" title="class or interface in java.lang">getContextClassLoader</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getDefaultUncaughtExceptionHandler()" title="class or interface in java.lang">getDefaultUncaughtExceptionHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getId()" title="class or interface in java.lang">getId</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getName()" title="class or interface in java.lang">getName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getPriority()" title="class or interface in java.lang">getPriority</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getStackTrace()" title="class or interface in java.lang">getStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getState()" title="class or interface in java.lang">getState</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getThreadGroup()" title="class or interface in java.lang">getThreadGroup</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#getUncaughtExceptionHandler()" title="class or interface in java.lang">getUncaughtExceptionHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#holdsLock(java.lang.Object)" title="class or interface in java.lang">holdsLock</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#interrupt()" title="class or interface in java.lang">interrupt</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#interrupted()" title="class or interface in java.lang">interrupted</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isAlive()" title="class or interface in java.lang">isAlive</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isDaemon()" title="class or interface in java.lang">isDaemon</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isInterrupted()" title="class or interface in java.lang">isInterrupted</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#isVirtual()" title="class or interface in java.lang">isVirtual</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join()" title="class or interface in java.lang">join</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join(long)" title="class or interface in java.lang">join</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join(long,int)" title="class or interface in java.lang">join</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#join(java.time.Duration)" title="class or interface in java.lang">join</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#ofPlatform()" title="class or interface in java.lang">ofPlatform</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#ofVirtual()" title="class or interface in java.lang">ofVirtual</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#onSpinWait()" title="class or interface in java.lang">onSpinWait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#resume()" title="class or interface in java.lang">resume</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setContextClassLoader(java.lang.ClassLoader)" title="class or interface in java.lang">setContextClassLoader</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setDaemon(boolean)" title="class or interface in java.lang">setDaemon</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setDefaultUncaughtExceptionHandler(java.lang.Thread.UncaughtExceptionHandler)" title="class or interface in java.lang">setDefaultUncaughtExceptionHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setName(java.lang.String)" title="class or interface in java.lang">setName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setPriority(int)" title="class or interface in java.lang">setPriority</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#setUncaughtExceptionHandler(java.lang.Thread.UncaughtExceptionHandler)" title="class or interface in java.lang">setUncaughtExceptionHandler</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#sleep(long)" title="class or interface in java.lang">sleep</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#sleep(long,int)" title="class or interface in java.lang">sleep</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#sleep(java.time.Duration)" title="class or interface in java.lang">sleep</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#start()" title="class or interface in java.lang">start</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#startVirtualThread(java.lang.Runnable)" title="class or interface in java.lang">startVirtualThread</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#stop()" title="class or interface in java.lang">stop</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#suspend()" title="class or interface in java.lang">suspend</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#threadId()" title="class or interface in java.lang">threadId</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#yield()" title="class or interface in java.lang">yield</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.StringBuffer,java.io.InputStream)">
<h3>StreamReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StreamReader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuffer.html" title="class or interface in java.lang">StringBuffer</a> buffer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - thread name</dd>
<dd><code>buffer</code> - buffer to fill</dd>
<dd><code>stream</code> - input stream ( process output )</dd>
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
<section class="detail" id="run()">
<h3>run</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">run</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html#run()" title="class or interface in java.lang">run</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html#run()" title="class or interface in java.lang">run</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html" title="class or interface in java.lang">Thread</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getException()">
<h3>getException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span> <span class="element-name">getException</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>generated exception on thread execution, null if none occurred</dd>
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
