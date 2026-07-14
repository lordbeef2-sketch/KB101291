# JAVA OPENAPI: MemoryReader (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/MemoryReader.html
- source_path: `com/nomagic/magicreport/engine/MemoryReader.html`
- source_sha256: `64ce7fa06ec67ac07cbef53325df811f37f2deff6e3be88bfb490b807b37da61`
- captured_utc: `2026-07-14T16:46:12.007961+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class MemoryReader

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)
com.nomagic.magicreport.engine.MemoryReader

All Implemented Interfaces:
`[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`, `[Readable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Readable.html)`

@OpenApiAllpublic classMemoryReader
extends [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)

A character stream whose source is memory.

Since:
Sep 3, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.io.[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)
`[lock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#lock)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MemoryReader](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)`
Create a new memory reader.
`[MemoryReader](#%3Cinit%3E(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) s)`
Create a new memory reader.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[close](#close())()`
Close the stream.
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getBuffer](#getBuffer())()`
Return the string buffer itself.
`void`
`[mark](#mark(int))(int readAheadLimit)`
Mark the present position in the stream.
`boolean`
`[markSupported](#markSupported())()`
Tell whether this stream supports the mark() operation, which it does.
`int`
`[read](#read())()`
Read a single character.
`int`
`[read](#read(char%5B%5D,int,int))(char[] cbuf,
 int off,
 int len)`
Read characters into a portion of an array.
`boolean`
`[ready](#ready())()`
Tell whether this stream is ready to be read.
`void`
`[reset](#reset())()`
Reset the stream to the most recent mark, or to the beginning of the string if it has never been marked.
`long`
`[skip](#skip(long))(long ns)`
Skips the specified number of characters in the stream.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Return the buffer's current value as a string.
Methods inherited from class java.io.[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)
`[nullReader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#nullReader()), [read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D)), [read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(java.nio.CharBuffer)), [transferTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#transferTo(java.io.Writer))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MemoryReader
public MemoryReader([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) s)
Create a new memory reader.
Parameters:
`s` - StringBuilder providing the character stream.
MemoryReader
public MemoryReader([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)
Create a new memory reader.
Parameters:
`s` - String providing the character stream.
 ============ METHOD DETAIL ========== 
Method Details
read
public int read()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Read a single character.
Overrides:
`[read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read())` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Returns:
The character read, or -1 if the end of the stream has been reached
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
read
public int read(char[] cbuf,
 int off,
 int len)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Read characters into a portion of an array.
Specified by:
`[read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D,int,int))` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Parameters:
`cbuf` - Destination buffer
`off` - Offset at which to start writing characters
`len` - Maximum number of characters to read
Returns:
The number of characters read, or -1 if the end of the stream has been reached
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
skip
public long skip(long ns)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Skips the specified number of characters in the stream. Returns the number of characters that were skipped.
 The `ns` parameter may be negative, even though the `skip` method of the
 [`Reader`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) superclass throws an exception in this case. Negative values of `ns` cause the
 stream to skip backwards. Negative return values indicate a skip backwards. It is not possible to skip
 backwards past the beginning of the string.
 If the entire string has been read or skipped, then this method has no effect and always returns 0.
Overrides:
`[skip](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#skip(long))` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Parameters:
`ns` - The number of characters to skip
Returns:
The number of characters actually skipped
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
ready
public boolean ready()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Tell whether this stream is ready to be read.
Overrides:
`[ready](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#ready())` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Returns:
True if the next read() is guaranteed not to block for input
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If the stream is closed
markSupported
public boolean markSupported()
Tell whether this stream supports the mark() operation, which it does.
Overrides:
`[markSupported](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#markSupported())` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Returns:
true if and only if this stream supports the mark operation.
mark
public void mark(int readAheadLimit)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Mark the present position in the stream. Subsequent calls to reset() will reposition the stream to this
 point.
Overrides:
`[mark](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#mark(int))` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Parameters:
`readAheadLimit` - Limit on the number of characters that may be read while still preserving the mark.
 Because the stream's input comes from a string, there is no actual limit, so this argument must
 not be negative, but is otherwise ignored.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - If readAheadLimit is < 0
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
reset
public void reset()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Reset the stream to the most recent mark, or to the beginning of the string if it has never been marked.
Overrides:
`[reset](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#reset())` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
close
public void close()
Close the stream.
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close())` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close())` in interface `[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#close())` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
getBuffer
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getBuffer()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Return the string buffer itself.
Returns:
StringBuilder holding the current buffer value.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - the stream has been closed
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Return the buffer's current value as a string.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Returns:
buffer value

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class MemoryReader">Class MemoryReader</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">java.io.Reader</a>
<div class="inheritance">com.nomagic.magicreport.engine.MemoryReader</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Readable.html" title="class or interface in java.lang">Readable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MemoryReader</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></span></div>
<div class="block">A character stream whose source is memory.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Sep 3, 2007</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.io.Reader">Fields inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#lock" title="class or interface in java.io">lock</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">MemoryReader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a new memory reader.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.StringBuilder)">MemoryReader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> s)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a new memory reader.</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBuffer()">getBuffer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the string buffer itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#mark(int)">mark</a><wbr/>(int readAheadLimit)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Mark the present position in the stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markSupported()">markSupported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tell whether this stream supports the mark() operation, which it does.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#read()">read</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read a single character.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#read(char%5B%5D,int,int)">read</a><wbr/>(char[] cbuf,
 int off,
 int len)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read characters into a portion of an array.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ready()">ready</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tell whether this stream is ready to be read.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reset()">reset</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reset the stream to the most recent mark, or to the beginning of the string if it has never been marked.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#skip(long)">skip</a><wbr/>(long ns)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Skips the specified number of characters in the stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the buffer's current value as a string.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.Reader">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#nullReader()" title="class or interface in java.io">nullReader</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D)" title="class or interface in java.io">read</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(java.nio.CharBuffer)" title="class or interface in java.io">read</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#transferTo(java.io.Writer)" title="class or interface in java.io">transferTo</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.StringBuilder)">
<h3>MemoryReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MemoryReader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> s)</span></div>
<div class="block">Create a new memory reader.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - StringBuilder providing the character stream.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>MemoryReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MemoryReader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Create a new memory reader.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - String providing the character stream.</dd>
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
<section class="detail" id="read()">
<h3>read</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">read</span>()
         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Read a single character.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read()" title="class or interface in java.io">read</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Returns:</dt>
<dd>The character read, or -1 if the end of the stream has been reached</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="read(char[],int,int)">
<h3>read</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">read</span><wbr/><span class="parameters">(char[] cbuf,
 int off,
 int len)</span>
         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Read characters into a portion of an array.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D,int,int)" title="class or interface in java.io">read</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Parameters:</dt>
<dd><code>cbuf</code> - Destination buffer</dd>
<dd><code>off</code> - Offset at which to start writing characters</dd>
<dd><code>len</code> - Maximum number of characters to read</dd>
<dt>Returns:</dt>
<dd>The number of characters read, or -1 if the end of the stream has been reached</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="skip(long)">
<h3>skip</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">skip</span><wbr/><span class="parameters">(long ns)</span>
          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Skips the specified number of characters in the stream. Returns the number of characters that were skipped.
 <p>
 The <code>ns</code> parameter may be negative, even though the <code>skip</code> method of the
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io"><code>Reader</code></a> superclass throws an exception in this case. Negative values of <code>ns</code> cause the
 stream to skip backwards. Negative return values indicate a skip backwards. It is not possible to skip
 backwards past the beginning of the string.
 <p>
 If the entire string has been read or skipped, then this method has no effect and always returns 0.</p></p></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#skip(long)" title="class or interface in java.io">skip</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Parameters:</dt>
<dd><code>ns</code> - The number of characters to skip</dd>
<dt>Returns:</dt>
<dd>The number of characters actually skipped</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ready()">
<h3>ready</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">ready</span>()
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Tell whether this stream is ready to be read.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#ready()" title="class or interface in java.io">ready</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Returns:</dt>
<dd>True if the next read() is guaranteed not to block for input</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If the stream is closed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markSupported()">
<h3>markSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">markSupported</span>()</div>
<div class="block">Tell whether this stream supports the mark() operation, which it does.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#markSupported()" title="class or interface in java.io">markSupported</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Returns:</dt>
<dd>true if and only if this stream supports the mark operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mark(int)">
<h3>mark</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">mark</span><wbr/><span class="parameters">(int readAheadLimit)</span>
          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Mark the present position in the stream. Subsequent calls to reset() will reposition the stream to this
 point.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#mark(int)" title="class or interface in java.io">mark</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Parameters:</dt>
<dd><code>readAheadLimit</code> - Limit on the number of characters that may be read while still preserving the mark.
           Because the stream's input comes from a string, there is no actual limit, so this argument must
           not be negative, but is otherwise ignored.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - If readAheadLimit is &lt; 0</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reset</span>()
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Reset the stream to the most recent mark, or to the beginning of the string if it has never been marked.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#reset()" title="class or interface in java.io">reset</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">close</span>()</div>
<div class="block">Close the stream.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang">close</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close()" title="class or interface in java.io">close</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#close()" title="class or interface in java.io">close</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
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
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Return the buffer's current value as a string.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>buffer value</dd>
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
