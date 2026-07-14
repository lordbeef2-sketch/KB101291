# JAVA OPENAPI: PermissionException (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/esi/persistence/security/PermissionException.html
- source_path: `com/nomagic/magicdraw/esi/persistence/security/PermissionException.html`
- source_sha256: `707b713df17ea4406475988bcf42d0da38d937304dad950d52181b159f757d38`
- captured_utc: `2026-07-14T16:51:20.964201+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi.persistence.security](package-summary.html)

## Class PermissionException

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html)
[java.lang.Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
com.nomagic.magicdraw.esi.persistence.security.PermissionException

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classPermissionException
extends [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)

Signals that a problem occurred during permissions set/get.

Version:
1.0
See Also:
[Serialized Form](../../../../../../serialized-form.html#com.nomagic.magicdraw.esi.persistence.security.PermissionException)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
``
`[PermissionException](#%3Cinit%3E())()`
Creates and initializes a new `PermissionException` instance.
``
`[PermissionException](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)`
Creates and initializes a new `PermissionException` instance from the specified parameter.
``
`[PermissionException](#%3Cinit%3E(java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) cause)`
Creates and initializes a new `PermissionException` instance from the specified parameters.
`protected`
`[PermissionException](#%3Cinit%3E(java.lang.String,java.lang.Throwable,boolean,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) cause,
 boolean enableSuppression,
 boolean writableStackTrace)`
Creates and initializes a new `PermissionException` instance from the specified parameters.
``
`[PermissionException](#%3Cinit%3E(java.lang.Throwable))([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) cause)`
Creates and initializes a new `PermissionException` instance from the specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html)
`[addSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)), [fillInStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()), [getCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getCause()), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()), [getMessage](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getMessage()), [getStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getStackTrace()), [getSuppressed](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#getSuppressed()), [initCause](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace()), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)), [printStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)), [setStackTrace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D)), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PermissionException
public PermissionException()
Creates and initializes a new `PermissionException` instance.
PermissionException
public PermissionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message)
Creates and initializes a new `PermissionException` instance from the specified parameter.
Parameters:
`message` - an error message.
PermissionException
public PermissionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) cause)
Creates and initializes a new `PermissionException` instance from the specified parameters.
Parameters:
`cause` - a cause of the problem.
`message` - an error message.
PermissionException
public PermissionException([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) cause)
Creates and initializes a new `PermissionException` instance from the specified parameters.
Parameters:
`cause` - a cause of the problem.
PermissionException
protected PermissionException([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html) cause,
 boolean enableSuppression,
 boolean writableStackTrace)
Creates and initializes a new `PermissionException` instance from the specified parameters.
Parameters:
`message` - an error message.
`cause` - a cause of the problem.
`enableSuppression` - whether or not suppression is enabled or disabled.
`writableStackTrace` - whether or not the stack trace should be writable.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi.persistence.security</a></div>
<h1 class="title" title="Class PermissionException">Class PermissionException</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">java.lang.Throwable</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">java.lang.Exception</a>
<div class="inheritance">com.nomagic.magicdraw.esi.persistence.security.PermissionException</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PermissionException</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Signals that a problem occurred during permissions set/get.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../serialized-form.html#com.nomagic.magicdraw.esi.persistence.security.PermissionException">Serialized Form</a></li>
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
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code> </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PermissionException</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>PermissionException</code> instance.</div>
</div>
<div class="col-first odd-row-color"><code> </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">PermissionException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameter.</div>
</div>
<div class="col-first even-row-color"><code> </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Throwable)">PermissionException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameters.</div>
</div>
<div class="col-first odd-row-color"><code>protected </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Throwable,boolean,boolean)">PermissionException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause,
 boolean enableSuppression,
 boolean writableStackTrace)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameters.</div>
</div>
<div class="col-first even-row-color"><code> </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Throwable)">PermissionException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameters.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
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
<section class="detail" id="&lt;init&gt;()">
<h3>PermissionException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PermissionException</span>()</div>
<div class="block">Creates and initializes a new <code>PermissionException</code> instance.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>PermissionException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PermissionException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - an error message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Throwable)">
<h3>PermissionException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PermissionException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</span></div>
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cause</code> - a cause of the problem.</dd>
<dd><code>message</code> - an error message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Throwable)">
<h3>PermissionException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PermissionException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</span></div>
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cause</code> - a cause of the problem.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Throwable,boolean,boolean)">
<h3>PermissionException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">PermissionException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause,
 boolean enableSuppression,
 boolean writableStackTrace)</span></div>
<div class="block">Creates and initializes a new <code>PermissionException</code> instance from the specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - an error message.</dd>
<dd><code>cause</code> - a cause of the problem.</dd>
<dd><code>enableSuppression</code> - whether or not suppression is enabled or disabled.</dd>
<dd><code>writableStackTrace</code> - whether or not the stack trace should be writable.</dd>
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
