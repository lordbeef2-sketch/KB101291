# JAVA OPENAPI: DOCXLimitedBufferedWriter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/ooxml/DOCXLimitedBufferedWriter.html
- source_path: `com/nomagic/magicreport/engine/ooxml/DOCXLimitedBufferedWriter.html`
- source_sha256: `e9495a6becf81ef6976f4b407ac955cdab2dae2c8e964885391fb758eb52e96a`
- captured_utc: `2026-07-14T16:58:36.665277+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml](package-summary.html)

## Class DOCXLimitedBufferedWriter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
[java.io.BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)
com.nomagic.magicreport.engine.ooxml.DOCXLimitedBufferedWriter

All Implemented Interfaces:
`[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`, `[Flushable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html)`, `[Appendable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Appendable.html)`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`

@OpenApiAllpublic classDOCXLimitedBufferedWriter
extends [BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.io.[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
`[lock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#lock)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DOCXLimitedBufferedWriter](#%3Cinit%3E(java.io.Writer,int,com.nomagic.magicreport.engine.velocity.DOCXEngine,long))([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) out,
 int sz,
 [DOCXEngine](../velocity/DOCXEngine.html) engine,
 long maxByte)`

`[DOCXLimitedBufferedWriter](#%3Cinit%3E(java.io.Writer,com.nomagic.magicreport.engine.velocity.DOCXEngine,long))([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) out,
 [DOCXEngine](../velocity/DOCXEngine.html) engine,
 long maxByte)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`long`
`[getCurrentByte](#getCurrentByte())()`

`void`
`[setErrorMessage](#setErrorMessage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) error)`

`void`
`[setSkipCheck](#setSkipCheck(boolean))(boolean isSkipCheck)`

`void`
`[updateRemainByte](#updateRemainByte(long))(long externalUsedBtype)`

`void`
`[write](#write(char%5B%5D,int,int))(char[] cbuf,
 int off,
 int len)`

`void`
`[write](#write(int))(int c)`

`void`
`[write](#write(java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s,
 int off,
 int len)`
Methods inherited from class java.io.[BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#close()), [flush](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#flush()), [newLine](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#newLine())`
Methods inherited from class java.io.[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
`[append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(char)), [append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence)), [append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence,int,int)), [nullWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#nullWriter()), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D)), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DOCXLimitedBufferedWriter
public DOCXLimitedBufferedWriter([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) out,
 [DOCXEngine](../velocity/DOCXEngine.html) engine,
 long maxByte)
DOCXLimitedBufferedWriter
public DOCXLimitedBufferedWriter([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) out,
 int sz,
 [DOCXEngine](../velocity/DOCXEngine.html) engine,
 long maxByte)
 ============ METHOD DETAIL ========== 
Method Details
write
public void write(int c)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#write(int))` in class `[BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
write
public void write(char[] cbuf,
 int off,
 int len)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#write(char%5B%5D,int,int))` in class `[BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
write
public void write([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s,
 int off,
 int len)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#write(java.lang.String,int,int))` in class `[BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
updateRemainByte
public void updateRemainByte(long externalUsedBtype)
setErrorMessage
public void setErrorMessage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) error)
getCurrentByte
public long getCurrentByte()
setSkipCheck
public void setSkipCheck(boolean isSkipCheck)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml</a></div>
<h1 class="title" title="Class DOCXLimitedBufferedWriter">Class DOCXLimitedBufferedWriter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">java.io.Writer</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">java.io.BufferedWriter</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.DOCXLimitedBufferedWriter</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html" title="class or interface in java.io">Flushable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Appendable.html" title="class or interface in java.lang">Appendable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DOCXLimitedBufferedWriter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.io.Writer">Fields inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#lock" title="class or interface in java.io">lock</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.Writer,int,com.nomagic.magicreport.engine.velocity.DOCXEngine,long)">DOCXLimitedBufferedWriter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> out,
 int sz,
 <a href="../velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a> engine,
 long maxByte)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.Writer,com.nomagic.magicreport.engine.velocity.DOCXEngine,long)">DOCXLimitedBufferedWriter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> out,
 <a href="../velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a> engine,
 long maxByte)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentByte()">getCurrentByte</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setErrorMessage(java.lang.String)">setErrorMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> error)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSkipCheck(boolean)">setSkipCheck</a><wbr/>(boolean isSkipCheck)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateRemainByte(long)">updateRemainByte</a><wbr/>(long externalUsedBtype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(char%5B%5D,int,int)">write</a><wbr/>(char[] cbuf,
 int off,
 int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(int)">write</a><wbr/>(int c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.String,int,int)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s,
 int off,
 int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.BufferedWriter">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#close()" title="class or interface in java.io">close</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#flush()" title="class or interface in java.io">flush</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#newLine()" title="class or interface in java.io">newLine</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.Writer">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(char)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence,int,int)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#nullWriter()" title="class or interface in java.io">nullWriter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D)" title="class or interface in java.io">write</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String)" title="class or interface in java.io">write</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.io.Writer,com.nomagic.magicreport.engine.velocity.DOCXEngine,long)">
<h3>DOCXLimitedBufferedWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DOCXLimitedBufferedWriter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> out,
 <a href="../velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a> engine,
 long maxByte)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.io.Writer,int,com.nomagic.magicreport.engine.velocity.DOCXEngine,long)">
<h3>DOCXLimitedBufferedWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DOCXLimitedBufferedWriter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> out,
 int sz,
 <a href="../velocity/DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a> engine,
 long maxByte)</span></div>
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
<section class="detail" id="write(int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(int c)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#write(int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(char[],int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(char[] cbuf,
 int off,
 int len)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#write(char%5B%5D,int,int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(java.lang.String,int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s,
 int off,
 int len)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html#write(java.lang.String,int,int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateRemainByte(long)">
<h3>updateRemainByte</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateRemainByte</span><wbr/><span class="parameters">(long externalUsedBtype)</span></div>
</section>
</li>
<li>
<section class="detail" id="setErrorMessage(java.lang.String)">
<h3>setErrorMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setErrorMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> error)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCurrentByte()">
<h3>getCurrentByte</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getCurrentByte</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSkipCheck(boolean)">
<h3>setSkipCheck</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSkipCheck</span><wbr/><span class="parameters">(boolean isSkipCheck)</span></div>
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
