# JAVA OPENAPI: TemplateException (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/TemplateException.html
- source_path: `com/nomagic/magicreport/TemplateException.html`
- source_sha256: `b657156ec1213f8c02cb2c900565a032483e2b96e7128186ef5819a9434db37e`
- captured_utc: `2026-07-14T16:46:11.704956+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class TemplateException

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
[java.lang.Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
[java.lang.RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)
com.nomagic.magicreport.TemplateException

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

Direct Known Subclasses:
`[InitializationEngineException](InitializationEngineException.html)`, `[ParseErrorException](ParseErrorException.html)`

@OpenApiAllpublic classTemplateException
extends [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)

Base class for Template runtime exceptions thrown to the application layer.

Since:
Jun 11, 2007
See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.TemplateException)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TemplateException](#%3Cinit%3E())()`
Constructs a new exception with `null` as its detail message.
`[TemplateException](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Constructs a new exception with the specified detail message.
`[TemplateException](#%3Cinit%3E(java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)`
Constructs a new exception with the specified detail message and cause.
`[TemplateException](#%3Cinit%3E(java.lang.Throwable))([Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)`
Constructs a new exception with the specified cause and a detail message of
 (cause==null ? null : cause.toString()) (which typically contains the class and detail message of
 cause).
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class java.lang.[Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
`[addSuppressed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)), [fillInStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()), [getCause](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()), [getMessage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()), [getStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getStackTrace()), [getSuppressed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getSuppressed()), [initCause](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace()), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)), [setStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TemplateException
public TemplateException()
Constructs a new exception with `null` as its detail message.
TemplateException
public TemplateException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`Throwable.getMessage()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()) method.
TemplateException
public TemplateException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)
Constructs a new exception with the specified detail message and cause.
 Note that the detail message associated with `cause` is *not* automatically incorporated in
 this exception's detail message.
Parameters:
`message` - the detail message (which is saved for later retrieval by the [`Throwable.getMessage()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()) method).
`cause` - the cause (which is saved for later retrieval by the [`Throwable.getCause()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()) method). (A
 null value is permitted, and indicates that the cause is nonexistent or unknown.)
TemplateException
public TemplateException([Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)
Constructs a new exception with the specified cause and a detail message of
 (cause==null ? null : cause.toString()) (which typically contains the class and detail message of
 cause). This constructor is useful for exceptions that are little more than wrappers for other
 throwables (for example, [`PrivilegedActionException`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/security/PrivilegedActionException.html)).
Parameters:
`cause` - the cause (which is saved for later retrieval by the [`Throwable.getCause()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()) method). (A
 null value is permitted, and indicates that the cause is nonexistent or unknown.)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class TemplateException">Class TemplateException</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">java.lang.Throwable</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">java.lang.Exception</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">java.lang.RuntimeException</a>
<div class="inheritance">com.nomagic.magicreport.TemplateException</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code>, <code><a href="ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">TemplateException</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span></div>
<div class="block">Base class for Template runtime exceptions thrown to the application layer.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.TemplateException">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">TemplateException</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with <code>null</code> as its detail message.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">TemplateException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Throwable)">TemplateException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with the specified detail message and cause.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Throwable)">TemplateException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new exception with the specified cause and a detail message of
 <tt>(cause==null ? null : cause.toString())</tt> (which typically contains the class and detail message of
 <tt>cause</tt>).</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Throwable">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)" title="class or interface in java.lang">addSuppressed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()" title="class or interface in java.lang">fillInStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()" title="class or interface in java.lang">getCause</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()" title="class or interface in java.lang">getLocalizedMessage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()" title="class or interface in java.lang">getMessage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getStackTrace()" title="class or interface in java.lang">getStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getSuppressed()" title="class or interface in java.lang">getSuppressed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)" title="class or interface in java.lang">initCause</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace()" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D)" title="class or interface in java.lang">setStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#toString()" title="class or interface in java.lang">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>TemplateException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateException</span>()</div>
<div class="block">Constructs a new exception with <code>null</code> as its detail message.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>TemplateException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()" title="class or interface in java.lang"><code>Throwable.getMessage()</code></a> method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Throwable)">
<h3>TemplateException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</span></div>
<div class="block">Constructs a new exception with the specified detail message and cause.
 <p>
 Note that the detail message associated with <code>cause</code> is <i>not</i> automatically incorporated in
 this exception's detail message.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message (which is saved for later retrieval by the <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()" title="class or interface in java.lang"><code>Throwable.getMessage()</code></a> method).</dd>
<dd><code>cause</code> - the cause (which is saved for later retrieval by the <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()" title="class or interface in java.lang"><code>Throwable.getCause()</code></a> method). (A
           <tt>null</tt> value is permitted, and indicates that the cause is nonexistent or unknown.)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Throwable)">
<h3>TemplateException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TemplateException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</span></div>
<div class="block">Constructs a new exception with the specified cause and a detail message of
 <tt>(cause==null ? null : cause.toString())</tt> (which typically contains the class and detail message of
 <tt>cause</tt>). This constructor is useful for exceptions that are little more than wrappers for other
 throwables (for example, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/security/PrivilegedActionException.html" title="class or interface in java.security"><code>PrivilegedActionException</code></a>).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cause</code> - the cause (which is saved for later retrieval by the <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()" title="class or interface in java.lang"><code>Throwable.getCause()</code></a> method). (A
           <tt>null</tt> value is permitted, and indicates that the cause is nonexistent or unknown.)</dd>
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
