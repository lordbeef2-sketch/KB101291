# JAVA OPENAPI: XLSXParseErrorException (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/ooxml/XLSXParseErrorException.html
- source_path: `com/nomagic/magicreport/engine/ooxml/XLSXParseErrorException.html`
- source_sha256: `2f11458b3365647ab68e6a735c451040cb2bf9316ed29e39baf8cbc3efdb661d`
- captured_utc: `2026-07-14T16:58:36.834278+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml](package-summary.html)

## Class XLSXParseErrorException

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
[java.lang.Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
[java.lang.RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)
[com.nomagic.magicreport.TemplateException](../../TemplateException.html)
[com.nomagic.magicreport.ParseErrorException](../../ParseErrorException.html)
com.nomagic.magicreport.engine.ooxml.XLSXParseErrorException

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classXLSXParseErrorException
extends [ParseErrorException](../../ParseErrorException.html)

Application-level exception thrown when a template has a syntax or other error which prevents it from being
 parsed. The exception message will be return in XLSX meaning.

Since:
Dec 14, 2009
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.ooxml.XLSXParseErrorException)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.[ParseErrorException](../../ParseErrorException.html)
`[columnNumber](../../ParseErrorException.html#columnNumber), [fullMessage](../../ParseErrorException.html#fullMessage), [lineNumber](../../ParseErrorException.html#lineNumber), [source](../../ParseErrorException.html#source), [template](../../ParseErrorException.html#template)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[XLSXParseErrorException](#%3Cinit%3E(com.nomagic.magicreport.ParseErrorException))([ParseErrorException](../../ParseErrorException.html) message)`
Constructs a new exception with the specified detail message.
`[XLSXParseErrorException](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Constructs a new exception with the specified detail message.
`[XLSXParseErrorException](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,java.lang.String%5B%5D,int,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](../../Template.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] position,
 int columnNumber,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)`
Constructs a new exception with the specified detail message.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCellNumber](#getCellNumber())()`
Return a cellNumber.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMessage](#getMessage())()`
Return a full message.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getSheetNumber](#getSheetNumber())()`
Return a sheet number.
`void`
`[setCellNumber](#setCellNumber(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) cellNumber)`
Set a cellNumber.
`void`
`[setSheetNumber](#setSheetNumber(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sheetNumber)`
Set a sheet number.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Return string representation of this exception.
Methods inherited from class com.nomagic.magicreport.[ParseErrorException](../../ParseErrorException.html)
`[copy](../../ParseErrorException.html#copy(java.lang.String)), [getColumnNumber](../../ParseErrorException.html#getColumnNumber()), [getFullMessage](../../ParseErrorException.html#getFullMessage()), [getLineNumber](../../ParseErrorException.html#getLineNumber()), [getShortMessage](../../ParseErrorException.html#getShortMessage()), [getSource](../../ParseErrorException.html#getSource()), [getSourceMessage](../../ParseErrorException.html#getSourceMessage()), [getTemplate](../../ParseErrorException.html#getTemplate()), [setColumnNumber](../../ParseErrorException.html#setColumnNumber(int)), [setFullMessage](../../ParseErrorException.html#setFullMessage(java.lang.String)), [setLineNumber](../../ParseErrorException.html#setLineNumber(int)), [setSource](../../ParseErrorException.html#setSource(java.lang.String)), [setTemplate](../../ParseErrorException.html#setTemplate(com.nomagic.magicreport.Template))`
Methods inherited from class java.lang.[Throwable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html)
`[addSuppressed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)), [fillInStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#fillInStackTrace()), [getCause](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getCause()), [getLocalizedMessage](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getLocalizedMessage()), [getStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getStackTrace()), [getSuppressed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#getSuppressed()), [initCause](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#initCause(java.lang.Throwable)), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace()), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintStream)), [printStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#printStackTrace(java.io.PrintWriter)), [setStackTrace](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement%5B%5D))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
XLSXParseErrorException
public XLSXParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
XLSXParseErrorException
public XLSXParseErrorException([ParseErrorException](../../ParseErrorException.html) message)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
XLSXParseErrorException
public XLSXParseErrorException([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message,
 [Template](../../Template.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[] position,
 int columnNumber,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) source)
Constructs a new exception with the specified detail message.
Parameters:
`message` - the detail message. The detail message is saved for later retrieval by the
 [`getMessage()`](#getMessage()) method.
`template` - template
`position` - position
`columnNumber` - column number
`source` - template content until offset of error character.
 ============ METHOD DETAIL ========== 
Method Details
getSheetNumber
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getSheetNumber()
Return a sheet number.
Returns:
the sheet number
setSheetNumber
public void setSheetNumber([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sheetNumber)
Set a sheet number.
Parameters:
`sheetNumber` - the sheet number to set
getCellNumber
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCellNumber()
Return a cellNumber.
Returns:
the cellNumber
setCellNumber
public void setCellNumber([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) cellNumber)
Set a cellNumber.
Parameters:
`cellNumber` - the cellNumber to set
getMessage
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMessage()
Return a full message.
Overrides:
`[getMessage](../../ParseErrorException.html#getMessage())` in class `[ParseErrorException](../../ParseErrorException.html)`
Returns:
the full message
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Return string representation of this exception.
Overrides:
`[toString](../../ParseErrorException.html#toString())` in class `[ParseErrorException](../../ParseErrorException.html)`
Returns:
a string representation of this exception

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml</a></div>
<h1 class="title" title="Class XLSXParseErrorException">Class XLSXParseErrorException</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Throwable.html" title="class or interface in java.lang">java.lang.Throwable</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">java.lang.Exception</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">java.lang.RuntimeException</a>
<div class="inheritance"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">com.nomagic.magicreport.TemplateException</a>
<div class="inheritance"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">com.nomagic.magicreport.ParseErrorException</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.XLSXParseErrorException</div>
</div>
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
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">XLSXParseErrorException</span>
<span class="extends-implements">extends <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Application-level exception thrown when a template has a syntax or other error which prevents it from being
 parsed. The exception message will be return in XLSX meaning.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Dec 14, 2009</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.ooxml.XLSXParseErrorException">Serialized Form</a></li>
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
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.ParseErrorException">Fields inherited from class com.nomagic.magicreport.<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></h3>
<code><a href="../../ParseErrorException.html#columnNumber">columnNumber</a>, <a href="../../ParseErrorException.html#fullMessage">fullMessage</a>, <a href="../../ParseErrorException.html#lineNumber">lineNumber</a>, <a href="../../ParseErrorException.html#source">source</a>, <a href="../../ParseErrorException.html#template">template</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.ParseErrorException)">XLSXParseErrorException</a><wbr/>(<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> message)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">XLSXParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.Template,java.lang.String%5B%5D,int,java.lang.String)">XLSXParseErrorException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] position,
 int columnNumber,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new exception with the specified detail message.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCellNumber()">getCellNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a cellNumber.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMessage()">getMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a full message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSheetNumber()">getSheetNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a sheet number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCellNumber(java.lang.String)">setCellNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cellNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a cellNumber.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSheetNumber(java.lang.String)">setSheetNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetNumber)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a sheet number.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return string representation of this exception.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.ParseErrorException">Methods inherited from class com.nomagic.magicreport.<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></h3>
<code><a href="../../ParseErrorException.html#copy(java.lang.String)">copy</a>, <a href="../../ParseErrorException.html#getColumnNumber()">getColumnNumber</a>, <a href="../../ParseErrorException.html#getFullMessage()">getFullMessage</a>, <a href="../../ParseErrorException.html#getLineNumber()">getLineNumber</a>, <a href="../../ParseErrorException.html#getShortMessage()">getShortMessage</a>, <a href="../../ParseErrorException.html#getSource()">getSource</a>, <a href="../../ParseErrorException.html#getSourceMessage()">getSourceMessage</a>, <a href="../../ParseErrorException.html#getTemplate()">getTemplate</a>, <a href="../../ParseErrorException.html#setColumnNumber(int)">setColumnNumber</a>, <a href="../../ParseErrorException.html#setFullMessage(java.lang.String)">setFullMessage</a>, <a href="../../ParseErrorException.html#setLineNumber(int)">setLineNumber</a>, <a href="../../ParseErrorException.html#setSource(java.lang.String)">setSource</a>, <a href="../../ParseErrorException.html#setTemplate(com.nomagic.magicreport.Template)">setTemplate</a></code></div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>XLSXParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.ParseErrorException)">
<h3>XLSXParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXParseErrorException</span><wbr/><span class="parameters">(<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> message)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.Template,java.lang.String[],int,java.lang.String)">
<h3>XLSXParseErrorException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XLSXParseErrorException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message,
 <a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] position,
 int columnNumber,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Constructs a new exception with the specified detail message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - the detail message. The detail message is saved for later retrieval by the
           <a href="#getMessage()"><code>getMessage()</code></a> method.</dd>
<dd><code>template</code> - template</dd>
<dd><code>position</code> - position</dd>
<dd><code>columnNumber</code> - column number</dd>
<dd><code>source</code> - template content until offset of error character.</dd>
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
<section class="detail" id="getSheetNumber()">
<h3>getSheetNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSheetNumber</span>()</div>
<div class="block">Return a sheet number.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the sheet number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSheetNumber(java.lang.String)">
<h3>setSheetNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSheetNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sheetNumber)</span></div>
<div class="block">Set a sheet number.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sheetNumber</code> - the sheet number to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCellNumber()">
<h3>getCellNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCellNumber</span>()</div>
<div class="block">Return a cellNumber.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the cellNumber</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCellNumber(java.lang.String)">
<h3>setCellNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCellNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cellNumber)</span></div>
<div class="block">Set a cellNumber.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cellNumber</code> - the cellNumber to set</dd>
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
<dd><code><a href="../../ParseErrorException.html#getMessage()">getMessage</a></code> in class <code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code></dd>
<dt>Returns:</dt>
<dd>the full message</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Return string representation of this exception.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../ParseErrorException.html#toString()">toString</a></code> in class <code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code></dd>
<dt>Returns:</dt>
<dd>a string representation of this exception</dd>
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
