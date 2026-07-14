# JAVA OPENAPI: ParseErrorException (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/ParseErrorException.html
- source_path: `com/nomagic/magicreport/ParseErrorException.html`
- source_sha256: `26ee0ee175d14c82d686a1bb57f842dd375f2e9943fff1b846b91db4a984567e`
- captured_utc: `2026-07-14T16:46:11.477953+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Class ParseErrorException

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
[java.lang.Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
[java.lang.RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)
[com.nomagic.magicreport.TemplateException](TemplateException.html)
com.nomagic.magicreport.ParseErrorException

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

Direct Known Subclasses:
`[PPTXParseErrorException](engine/ooxml/PPTXParseErrorException.html)`, `[XLSXParseErrorException](engine/ooxml/XLSXParseErrorException.html)`

@OpenApiAllpublic classParseErrorException
extends [TemplateException](TemplateException.html)

Application-level exception thrown when a template has a syntax or other error which prevents it from being
 parsed.

Since:
Jun 11, 2007
See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.magicreport.ParseErrorException)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected int`
`[columnNumber](#columnNumber)`
The column number of the parsing error, or -1 if not defined.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[fullMessage](#fullMessage)`
Message in detailed.
`protected int`
`[lineNumber](#lineNumber)`
The line number of the parsing error, or -1 if not defined.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[source](#source)`
Contains content to template until error offset.
`protected [Template](Template.html)`
`[template](#template)`
Contains reference to error template.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ParseErrorException](#%3Cinit%3E())()`
Constructs a new exception with `null` as its detail message.
`[ParseErrorException](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Constructs a new exception with the specified detail message.
`[ParseErrorException](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template)`
Constructs a new exception with the specified detail message.
`[ParseErrorException](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template,
 int lineNumber)`
Constructs a new exception with the specified detail message.
`[ParseErrorException](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template,
 int lineNumber,
 int columnNumber)`
Constructs a new exception with the specified detail message.
`[ParseErrorException](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,int,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template,
 int lineNumber,
 int columnNumber,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Constructs a new exception with the specified detail message.
`[ParseErrorException](#%3Cinit%3E(java.lang.String,java.lang.Throwable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)`
Constructs a new exception with the specified detail message and cause.
`[ParseErrorException](#%3Cinit%3E(java.lang.Throwable))([Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)`
Constructs a new exception with the specified cause and a detail message of
 (cause==null ? null : cause.toString()) (which typically contains the class and detail message of
 cause).
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ParseErrorException](ParseErrorException.html)`
`[copy](#copy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Creates and returns a copy of this object.
`int`
`[getColumnNumber](#getColumnNumber())()`
Return the column number of the parsing error, or -1 if not defined.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getFullMessage](#getFullMessage())()`
Return a full message.
`int`
`[getLineNumber](#getLineNumber())()`
Return the line number of the parsing error, or -1 if not defined.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMessage](#getMessage())()`
Return a full message.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getShortMessage](#getShortMessage())()`
Return string representation of this exception without velocityMessageToHumanReadable
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSource](#getSource())()`
Return a source.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSourceMessage](#getSourceMessage())()`
Return a message without customize.
`[Template](Template.html)`
`[getTemplate](#getTemplate())()`
Return the template containing the error, or null if not defined.
`void`
`[setColumnNumber](#setColumnNumber(int))(int columnNumber)`
Set a column number of the parsing error.
`void`
`[setFullMessage](#setFullMessage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fullMessage)`
Set a full message.
`void`
`[setLineNumber](#setLineNumber(int))(int lineNumber)`
Set a line number of the parsing error.
`void`
`[setSource](#setSource(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Set a source.
`void`
`[setTemplate](#setTemplate(com.nomagic.magicreport.Template))([Template](Template.html) template)`
Set a template containing the error.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Return string representation of this exception
Methods inherited from class java.lang.[Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
`[addSuppressed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)), [fillInStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()), [getCause](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()), [getStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getStackTrace()), [getSuppressed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getSuppressed()), [initCause](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace()), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)), [setStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
columnNumber
protected int columnNumber
The column number of the parsing error, or -1 if not defined.
lineNumber
protected int lineNumber
The line number of the parsing error, or -1 if not defined.
template
protected [Template](Template.html) template
Contains reference to error template.
source
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source
Contains content to template until error offset.
fullMessage
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fullMessage
Message in detailed.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ParseErrorException
public ParseErrorException()
Constructs a new exception with `null` as its detail message.
ParseErrorException
public ParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
ParseErrorException
public ParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
`template` - template
ParseErrorException
public ParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template,
 int lineNumber)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
`template` - template
`lineNumber` - line number
ParseErrorException
public ParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template,
 int lineNumber,
 int columnNumber)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
`template` - template
`lineNumber` - line number
`columnNumber` - column number
ParseErrorException
public ParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](Template.html) template,
 int lineNumber,
 int columnNumber,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
`template` - template
`lineNumber` - line number
`columnNumber` - column number
`source` - template content until offset of error character.
ParseErrorException
public ParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)
Constructs a new exception with the specified detail message and cause.
 Note that the detail message associated with `cause` is *not* automatically incorporated in
 this exception's detail message.
Parameters:
`message` - the detail message (which is saved for later retrieval by the [`getMessage()`](#getMessage()) method).
`cause` - the cause (which is saved for later retrieval by the [`Throwable.getCause()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()) method). (A
 null value is permitted, and indicates that the cause is nonexistent or unknown.)
ParseErrorException
public ParseErrorException([Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html) cause)
Constructs a new exception with the specified cause and a detail message of
 (cause==null ? null : cause.toString()) (which typically contains the class and detail message of
 cause). This constructor is useful for exceptions that are little more than wrappers for other
 throwables (for example, [`PrivilegedActionException`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/security/PrivilegedActionException.html)).
Parameters:
`cause` - the cause (which is saved for later retrieval by the [`Throwable.getCause()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()) method). (A
 null value is permitted, and indicates that the cause is nonexistent or unknown.)
 ============ METHOD DETAIL ========== 
Method Details
setColumnNumber
public void setColumnNumber(int columnNumber)
Set a column number of the parsing error.
Parameters:
`columnNumber` - column number of the parsing error
setLineNumber
public void setLineNumber(int lineNumber)
Set a line number of the parsing error.
Parameters:
`lineNumber` - the line number of the parsing error
setTemplate
public void setTemplate([Template](Template.html) template)
Set a template containing the error.
Parameters:
`template` - the template containing the error
getColumnNumber
public int getColumnNumber()
Return the column number of the parsing error, or -1 if not defined.
Returns:
column number of the parsing error, or -1 if not defined
getLineNumber
public int getLineNumber()
Return the line number of the parsing error, or -1 if not defined.
Returns:
line number of the parsing error, or -1 if not defined
getTemplate
public [Template](Template.html) getTemplate()
Return the template containing the error, or null if not defined.
Returns:
the template containing the parsing error, or null if not defined
getSource
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSource()
Return a source.
Returns:
the source
setSource
public void setSource([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Set a source.
Parameters:
`source` - the source to set
setFullMessage
public void setFullMessage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fullMessage)
Set a full message.
Parameters:
`fullMessage` - the full message to set
getFullMessage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getFullMessage()
Return a full message.
Returns:
a full message.
getSourceMessage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSourceMessage()
Return a message without customize.
Returns:
a message.
getMessage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMessage()
Return a full message.
Overrides:
`[getMessage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage())` in class `[Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)`
Returns:
the full message
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Return string representation of this exception
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#toString())` in class `[Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)`
Returns:
a string representation of this exception
getShortMessage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getShortMessage()
Return string representation of this exception without velocityMessageToHumanReadable
Returns:
copy
public [ParseErrorException](ParseErrorException.html) copy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Creates and returns a copy of this object.
Parameters:
`message` - a new message
Returns:
a copy of this instance.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Class ParseErrorException">Class ParseErrorException</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">java.lang.Throwable</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">java.lang.Exception</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">java.lang.RuntimeException</a>
<div class="inheritance"><a href="TemplateException.html" title="class in com.nomagic.magicreport">com.nomagic.magicreport.TemplateException</a>
<div class="inheritance">com.nomagic.magicreport.ParseErrorException</div>
</div>
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
<dd><code><a href="engine/ooxml/PPTXParseErrorException.html" title="class in com.nomagic.magicreport.engine.ooxml">PPTXParseErrorException</a></code>, <code><a href="engine/ooxml/XLSXParseErrorException.html" title="class in com.nomagic.magicreport.engine.ooxml">XLSXParseErrorException</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ParseErrorException</span>
<span class="extends-implements">extends <a href="TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Application-level exception thrown when a template has a syntax or other error which prevents it from being
 parsed.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.magicreport.ParseErrorException">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#columnNumber">columnNumber</a></code></div>
<div class="col-last even-row-color">
<div class="block">The column number of the parsing error, or -1 if not defined.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#fullMessage">fullMessage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Message in detailed.</div>
</div>
<div class="col-first even-row-color"><code>protected int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#lineNumber">lineNumber</a></code></div>
<div class="col-last even-row-color">
<div class="block">The line number of the parsing error, or -1 if not defined.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#source">source</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains content to template until error offset.</div>
</div>
<div class="col-first even-row-color"><code>protected <a href="Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#template">template</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains reference to error template.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ParseErrorException</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with <code>null</code> as its detail message.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,int)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 int lineNumber)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,int,int)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 int lineNumber,
 int columnNumber)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,int,int,java.lang.String)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 int lineNumber,
 int columnNumber,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.Throwable)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with the specified detail message and cause.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Throwable)">ParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</code></div>
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
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.lang.String)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates and returns a copy of this object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getColumnNumber()">getColumnNumber</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the column number of the parsing error, or -1 if not defined.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFullMessage()">getFullMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a full message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineNumber()">getLineNumber</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the line number of the parsing error, or -1 if not defined.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessage()">getMessage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a full message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShortMessage()">getShortMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return string representation of this exception without velocityMessageToHumanReadable</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSource()">getSource</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceMessage()">getSourceMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a message without customize.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplate()">getTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the template containing the error, or null if not defined.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setColumnNumber(int)">setColumnNumber</a><wbr/>(int columnNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a column number of the parsing error.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFullMessage(java.lang.String)">setFullMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fullMessage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a full message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLineNumber(int)">setLineNumber</a><wbr/>(int lineNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a line number of the parsing error.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSource(java.lang.String)">setSource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTemplate(com.nomagic.magicreport.Template)">setTemplate</a><wbr/>(<a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a template containing the error.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return string representation of this exception</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Throwable">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)" title="class or interface in java.lang">addSuppressed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()" title="class or interface in java.lang">fillInStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()" title="class or interface in java.lang">getCause</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()" title="class or interface in java.lang">getLocalizedMessage</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getStackTrace()" title="class or interface in java.lang">getStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getSuppressed()" title="class or interface in java.lang">getSuppressed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)" title="class or interface in java.lang">initCause</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace()" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)" title="class or interface in java.lang">printStackTrace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D)" title="class or interface in java.lang">setStackTrace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="columnNumber">
<h3>columnNumber</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">columnNumber</span></div>
<div class="block">The column number of the parsing error, or -1 if not defined.</div>
</section>
</li>
<li>
<section class="detail" id="lineNumber">
<h3>lineNumber</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">lineNumber</span></div>
<div class="block">The line number of the parsing error, or -1 if not defined.</div>
</section>
</li>
<li>
<section class="detail" id="template">
<h3>template</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">template</span></div>
<div class="block">Contains reference to error template.</div>
</section>
</li>
<li>
<section class="detail" id="source">
<h3>source</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">source</span></div>
<div class="block">Contains content to template until error offset.</div>
</section>
</li>
<li>
<section class="detail" id="fullMessage">
<h3>fullMessage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">fullMessage</span></div>
<div class="block">Message in detailed.</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span>()</div>
<div class="block">Constructs a new exception with <code>null</code> as its detail message.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.Template)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
<dd><code>template</code> - template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.Template,int)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 int lineNumber)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
<dd><code>template</code> - template</dd>
<dd><code>lineNumber</code> - line number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.Template,int,int)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 int lineNumber,
 int columnNumber)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
<dd><code>template</code> - template</dd>
<dd><code>lineNumber</code> - line number</dd>
<dd><code>columnNumber</code> - column number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.Template,int,int,java.lang.String)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 int lineNumber,
 int columnNumber,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
<dd><code>template</code> - template</dd>
<dd><code>lineNumber</code> - line number</dd>
<dd><code>columnNumber</code> - column number</dd>
<dd><code>source</code> - template content until offset of error character.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.Throwable)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</span></div>
<div class="block">Constructs a new exception with the specified detail message and cause.
 <p>
 Note that the detail message associated with <code>cause</code> is <i>not</i> automatically incorporated in
 this exception's detail message.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message (which is saved for later retrieval by the <a href="#getMessage()"><code>getMessage()</code></a> method).</dd>
<dd><code>cause</code> - the cause (which is saved for later retrieval by the <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()" title="class or interface in java.lang"><code>Throwable.getCause()</code></a> method). (A
           <tt>null</tt> value is permitted, and indicates that the cause is nonexistent or unknown.)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Throwable)">
<h3>ParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a> cause)</span></div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="setColumnNumber(int)">
<h3>setColumnNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColumnNumber</span><wbr/><span class="parameters">(int columnNumber)</span></div>
<div class="block">Set a column number of the parsing error.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>columnNumber</code> - column number of the parsing error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLineNumber(int)">
<h3>setLineNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLineNumber</span><wbr/><span class="parameters">(int lineNumber)</span></div>
<div class="block">Set a line number of the parsing error.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineNumber</code> - the line number of the parsing error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTemplate(com.nomagic.magicreport.Template)">
<h3>setTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTemplate</span><wbr/><span class="parameters">(<a href="Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span></div>
<div class="block">Set a template containing the error.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the template containing the error</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColumnNumber()">
<h3>getColumnNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getColumnNumber</span>()</div>
<div class="block">Return the column number of the parsing error, or -1 if not defined.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>column number of the parsing error, or -1 if not defined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLineNumber()">
<h3>getLineNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLineNumber</span>()</div>
<div class="block">Return the line number of the parsing error, or -1 if not defined.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>line number of the parsing error, or -1 if not defined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplate()">
<h3>getTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">getTemplate</span>()</div>
<div class="block">Return the template containing the error, or null if not defined.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the template containing the parsing error, or null if not defined</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSource()">
<h3>getSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSource</span>()</div>
<div class="block">Return a source.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the source</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSource(java.lang.String)">
<h3>setSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSource</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Set a source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - the source to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFullMessage(java.lang.String)">
<h3>setFullMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFullMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fullMessage)</span></div>
<div class="block">Set a full message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fullMessage</code> - the full message to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFullMessage()">
<h3>getFullMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFullMessage</span>()</div>
<div class="block">Return a full message.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a full message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceMessage()">
<h3>getSourceMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSourceMessage</span>()</div>
<div class="block">Return a message without customize.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a message.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMessage()">
<h3>getMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMessage</span>()</div>
<div class="block">Return a full message.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getMessage()" title="class or interface in java.lang">getMessage</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></code></dd>
<dt>Returns:</dt>
<dd>the full message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Return string representation of this exception</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">Throwable</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShortMessage()">
<h3>getShortMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShortMessage</span>()</div>
<div class="block">Return string representation of this exception without velocityMessageToHumanReadable</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.lang.String)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Creates and returns a copy of this object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - a new message</dd>
<dt>Returns:</dt>
<dd>a copy of this instance.</dd>
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
