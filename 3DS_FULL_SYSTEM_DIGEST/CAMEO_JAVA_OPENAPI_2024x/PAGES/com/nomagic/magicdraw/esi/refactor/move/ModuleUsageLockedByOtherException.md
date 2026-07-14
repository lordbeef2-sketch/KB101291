# JAVA OPENAPI: ModuleUsageLockedByOtherException (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/esi/refactor/move/ModuleUsageLockedByOtherException.html
- source_path: `com/nomagic/magicdraw/esi/refactor/move/ModuleUsageLockedByOtherException.html`
- source_sha256: `453615d6c73b40c300ef56df12245bbab9f38bd6c459ff910eec81f055cdf83c`
- captured_utc: `2026-07-14T16:51:21.012201+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi.refactor.move](package-summary.html)

## Class ModuleUsageLockedByOtherException

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html)
[java.lang.Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
com.nomagic.magicdraw.esi.refactor.move.ModuleUsageLockedByOtherException

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classModuleUsageLockedByOtherException
extends [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)

Indicates that module usage is locked by another user

See Also:
[Serialized Form](../../../../../../serialized-form.html#com.nomagic.magicdraw.esi.refactor.move.ModuleUsageLockedByOtherException)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModuleUsageLockedByOtherException](#%3Cinit%3E(com.nomagic.magicdraw.core.modules.ModuleUsage,java.lang.String))([ModuleUsage](../../../core/modules/ModuleUsage.html) moduleUsage,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) user)`
Creates new instance of [`ModuleUsageLockedByOtherException`](ModuleUsageLockedByOtherException.html)
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ModuleUsage](../../../core/modules/ModuleUsage.html)`
`[getModuleUsage](#getModuleUsage())()`
Gets the module usage that could not be locked
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUser](#getUser())()`
Gets the user who has locked the usage
Methods inherited from class java.lang.[Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html)
`[addSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)), [fillInStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()), [getCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getCause()), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()), [getMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getMessage()), [getStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getStackTrace()), [getSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getSuppressed()), [initCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace()), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)), [setStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D)), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModuleUsageLockedByOtherException
public ModuleUsageLockedByOtherException([ModuleUsage](../../../core/modules/ModuleUsage.html) moduleUsage,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) user)
Creates new instance of [`ModuleUsageLockedByOtherException`](ModuleUsageLockedByOtherException.html)
Parameters:
`moduleUsage` - the module usage that could not be locked
`user` - the user who has locked the usage
 ============ METHOD DETAIL ========== 
Method Details
getModuleUsage
public [ModuleUsage](../../../core/modules/ModuleUsage.html) getModuleUsage()
Gets the module usage that could not be locked
Returns:
the module usage
getUser
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUser()
Gets the user who has locked the usage
Returns:
the user

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi.refactor.move</a></div>
<h1 class="title" title="Class ModuleUsageLockedByOtherException">Class ModuleUsageLockedByOtherException</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">java.lang.Throwable</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">java.lang.Exception</a>
<div class="inheritance">com.nomagic.magicdraw.esi.refactor.move.ModuleUsageLockedByOtherException</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ModuleUsageLockedByOtherException</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Indicates that module usage is locked by another user</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../serialized-form.html#com.nomagic.magicdraw.esi.refactor.move.ModuleUsageLockedByOtherException">Serialized Form</a></li>
</ul>
</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.modules.ModuleUsage,java.lang.String)">ModuleUsageLockedByOtherException</a><wbr/>(<a href="../../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates new instance of <a href="ModuleUsageLockedByOtherException.html" title="class in com.nomagic.magicdraw.esi.refactor.move"><code>ModuleUsageLockedByOtherException</code></a></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModuleUsage()">getModuleUsage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the module usage that could not be locked</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUser()">getUser</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the user who has locked the usage</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Throwable">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)" title="class or interface in java.lang">addSuppressed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()" title="class or interface in java.lang">fillInStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getCause()" title="class or interface in java.lang">getCause</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()" title="class or interface in java.lang">getLocalizedMessage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getMessage()" title="class or interface in java.lang">getMessage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getStackTrace()" title="class or interface in java.lang">getStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getSuppressed()" title="class or interface in java.lang">getSuppressed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)" title="class or interface in java.lang">initCause</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace()" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D)" title="class or interface in java.lang">setStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#toString()" title="class or interface in java.lang">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.modules.ModuleUsage,java.lang.String)">
<h3>ModuleUsageLockedByOtherException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModuleUsageLockedByOtherException</span><wbr/><span class="parameters">(<a href="../../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> moduleUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> user)</span></div>
<div class="block">Creates new instance of <a href="ModuleUsageLockedByOtherException.html" title="class in com.nomagic.magicdraw.esi.refactor.move"><code>ModuleUsageLockedByOtherException</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>moduleUsage</code> - the module usage that could not be locked</dd>
<dd><code>user</code> - the user who has locked the usage</dd>
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
<section class="detail" id="getModuleUsage()">
<h3>getModuleUsage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../core/modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a></span> <span class="element-name">getModuleUsage</span>()</div>
<div class="block">Gets the module usage that could not be locked</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the module usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUser()">
<h3>getUser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUser</span>()</div>
<div class="block">Gets the user who has locked the usage</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the user</dd>
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
