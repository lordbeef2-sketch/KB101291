# JAVA OPENAPI: MemoryWriter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/MemoryWriter.html
- source_path: `com/nomagic/magicreport/engine/MemoryWriter.html`
- source_sha256: `c5c5004fad1363e82e13b57bd04f026f6c1550012fb9bba1f9c62880fc9e06ef`
- captured_utc: `2026-07-14T16:46:12.039962+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class MemoryWriter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
com.nomagic.magicreport.engine.MemoryWriter

All Implemented Interfaces:
`[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`, `[Flushable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html)`, `[Appendable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Appendable.html)`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`

@OpenApiAllpublic classMemoryWriter
extends [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)

A character stream that collects its output in a memory.

Since:
Apr 30, 2008

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.io.[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
`[lock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#lock)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MemoryWriter](#%3Cinit%3E())()`
Create a new memory writer using the default initial string-buffer size.
`[MemoryWriter](#%3Cinit%3E(int))(int initialSize)`
Create a new memory writer using the specified initial string-buffer size.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[close](#close())()`
Close the stream.
`void`
`[flush](#flush())()`
Flush the stream.
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getBuffer](#getBuffer())()`
Return the string buffer itself.
`long`
`[size](#size())()`
Return the size of current written data.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Return the buffer's current value as a string.
`void`
`[write](#write(char%5B%5D,int,int))(char[] cbuf,
 int off,
 int len)`
Write a portion of an array of characters.
`void`
`[write](#write(int))(int c)`
Write a single character.
`void`
`[write](#write(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str)`
Write a string.
`void`
`[write](#write(java.lang.String,int,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str,
 int off,
 int len)`
Write a portion of a string.
Methods inherited from class java.io.[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
`[append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(char)), [append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence)), [append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence,int,int)), [nullWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#nullWriter()), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MemoryWriter
public MemoryWriter()
Create a new memory writer using the default initial string-buffer size.
MemoryWriter
public MemoryWriter(int initialSize)
Create a new memory writer using the specified initial string-buffer size.
Parameters:
`initialSize` - The number of `char` values that will fit into this buffer before it is
 automatically expanded
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - If `initialSize` is negative
 ============ METHOD DETAIL ========== 
Method Details
write
public void write(int c)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write a single character.
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(int))` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Parameters:
`c` - character
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
write
public void write(char[] cbuf,
 int off,
 int len)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write a portion of an array of characters.
Specified by:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D,int,int))` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Parameters:
`cbuf` - Array of characters
`off` - Offset from which to start writing characters
`len` - Number of characters to write
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
write
public void write([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str)
Write a string.
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String))` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Parameters:
`str` - string to write
write
public void write([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str,
 int off,
 int len)
Write a portion of a string.
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String,int,int))` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Parameters:
`str` - String to be written
`off` - Offset from which to start writing characters
`len` - Number of characters to write
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Return the buffer's current value as a string.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
current value as a string.
flush
public void flush()
Flush the stream.
Specified by:
`[flush](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html#flush())` in interface `[Flushable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html)`
Specified by:
`[flush](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#flush())` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
close
public void close()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Close the stream.
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close())` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close())` in interface `[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#close())` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
getBuffer
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getBuffer()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Return the string buffer itself.
Returns:
StringBuilder holding the current buffer value.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - the stream has been closed
size
public long size()
Return the size of current written data.
Returns:
writer size

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class MemoryWriter">Class MemoryWriter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">java.io.Writer</a>
<div class="inheritance">com.nomagic.magicreport.engine.MemoryWriter</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html" title="class or interface in java.io">Flushable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Appendable.html" title="class or interface in java.lang">Appendable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MemoryWriter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></span></div>
<div class="block">A character stream that collects its output in a memory.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Apr 30, 2008</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MemoryWriter</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create a new memory writer using the default initial string-buffer size.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int)">MemoryWriter</a><wbr/>(int initialSize)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a new memory writer using the specified initial string-buffer size.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#close()">close</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Close the stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#flush()">flush</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Flush the stream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBuffer()">getBuffer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the string buffer itself.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#size()">size</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the size of current written data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the buffer's current value as a string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(char%5B%5D,int,int)">write</a><wbr/>(char[] cbuf,
 int off,
 int len)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a portion of an array of characters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(int)">write</a><wbr/>(int c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a single character.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.String)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.String,int,int)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 int off,
 int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write a portion of a string.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.Writer">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(char)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence,int,int)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#nullWriter()" title="class or interface in java.io">nullWriter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D)" title="class or interface in java.io">write</a></code></div>
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
<h3>MemoryWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MemoryWriter</span>()</div>
<div class="block">Create a new memory writer using the default initial string-buffer size.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(int)">
<h3>MemoryWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MemoryWriter</span><wbr/><span class="parameters">(int initialSize)</span></div>
<div class="block">Create a new memory writer using the specified initial string-buffer size.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initialSize</code> - The number of <code>char</code> values that will fit into this buffer before it is
           automatically expanded</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - If <code>initialSize</code> is negative</dd>
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
<section class="detail" id="write(int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(int c)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write a single character.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>c</code> - character</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
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
<div class="block">Write a portion of an array of characters.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D,int,int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>cbuf</code> - Array of characters</dd>
<dd><code>off</code> - Offset from which to start writing characters</dd>
<dd><code>len</code> - Number of characters to write</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(java.lang.String)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</span></div>
<div class="block">Write a string.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>str</code> - string to write</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(java.lang.String,int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 int off,
 int len)</span></div>
<div class="block">Write a portion of a string.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String,int,int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>str</code> - String to be written</dd>
<dd><code>off</code> - Offset from which to start writing characters</dd>
<dd><code>len</code> - Number of characters to write</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Return the buffer's current value as a string.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>current value as a string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flush()">
<h3>flush</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flush</span>()</div>
<div class="block">Flush the stream.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html#flush()" title="class or interface in java.io">flush</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html" title="class or interface in java.io">Flushable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#flush()" title="class or interface in java.io">flush</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">close</span>()
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Close the stream.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang">close</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close()" title="class or interface in java.io">close</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#close()" title="class or interface in java.io">close</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBuffer()">
<h3>getBuffer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getBuffer</span>()
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Return the string buffer itself.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>StringBuilder holding the current buffer value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - the stream has been closed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="size()">
<h3>size</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">size</span>()</div>
<div class="block">Return the size of current written data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>writer size</dd>
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
