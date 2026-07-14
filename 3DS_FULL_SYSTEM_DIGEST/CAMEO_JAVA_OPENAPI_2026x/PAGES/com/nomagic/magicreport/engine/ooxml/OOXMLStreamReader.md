# JAVA OPENAPI: OOXMLStreamReader (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/ooxml/OOXMLStreamReader.html
- source_path: `com/nomagic/magicreport/engine/ooxml/OOXMLStreamReader.html`
- source_sha256: `e2499b559b480b0bf5cf0e6d74191263c2b5718c813341162bd051d55b9bb8bf`
- captured_utc: `2026-07-14T16:58:36.711277+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml](package-summary.html)

## Class OOXMLStreamReader

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)
com.nomagic.magicreport.engine.ooxml.OOXMLStreamReader

All Implemented Interfaces:
`[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`, `[Readable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Readable.html)`

@OpenApiAllpublic classOOXMLStreamReader
extends [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)

This class implements a reader that can be used for OOXML. The reader reader data from content.xml by default.
 An OOXMLStreamReader is also provide a bridge from byte streams to characters streams: It reads bytes and
 decodes them into characters using a specified charset

Since:
Oct 19, 2009

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [OOXMLEntry](OOXMLEntry.html)`
`[contentEntry](#contentEntry)`
Keep the entry for content reader.
`protected [InputStreamReader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStreamReader.html)`
`[contentReader](#contentReader)`
An internal reader for specified content entry.
`protected [ZipInputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipInputStream.html)`
`[zipInputStream](#zipInputStream)`
An internal input stream for ZIP file.
Fields inherited from class java.io.[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)
`[lock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#lock)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OOXMLStreamReader](#%3Cinit%3E(java.io.InputStream,java.lang.String))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) in,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)`
Create an OOXMLStreamReader that uses the named charset.
`[OOXMLStreamReader](#%3Cinit%3E(java.io.InputStream,java.lang.String,java.lang.String))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) in,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName)`
Create an OOXMLStreamReader that uses the named charset and entry.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[close](#close())()`
Close the stream.
`protected void`
`[ensureOpen](#ensureOpen())()`
Check to make sure that the stream has not been closed.
`[OOXMLEntry](OOXMLEntry.html)`
`[getContentEntry](#getContentEntry())()`
Returns the OOXML file entry for the reader, or null if not found.
`[OOXMLEntry](OOXMLEntry.html)`
`[getNextEntry](#getNextEntry())()`
Reads the next OOXML file entry and positions the stream at the beginning of the entry data.
`void`
`[init](#init(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)`
Initialize ODF stream.
`int`
`[read](#read(byte%5B%5D,int,int))(byte[] b,
 int off,
 int len)`
Reads from the current OOXML entry into an array of bytes.
`int`
`[read](#read(char%5B%5D,int,int))(char[] cbuf,
 int offset,
 int length)`
Read characters from content.xml into a portion of an array.
Methods inherited from class java.io.[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)
`[mark](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#mark(int)), [markSupported](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#markSupported()), [nullReader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#nullReader()), [read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read()), [read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D)), [read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(java.nio.CharBuffer)), [ready](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#ready()), [reset](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#reset()), [skip](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#skip(long)), [transferTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#transferTo(java.io.Writer))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
zipInputStream
protected [ZipInputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipInputStream.html) zipInputStream
An internal input stream for ZIP file.
contentReader
protected [InputStreamReader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStreamReader.html) contentReader
An internal reader for specified content entry.
contentEntry
protected [OOXMLEntry](OOXMLEntry.html) contentEntry
Keep the entry for content reader.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OOXMLStreamReader
public OOXMLStreamReader([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) in,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create an OOXMLStreamReader that uses the named charset.
Parameters:
`in` - An InputStream
`entryName` - target entry name
Throws:
`[UnsupportedEncodingException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/UnsupportedEncodingException.html)` - If the named charset is not supported
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
OOXMLStreamReader
public OOXMLStreamReader([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) in,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create an OOXMLStreamReader that uses the named charset and entry.
Parameters:
`in` - An InputStream
`entryName` - target entry name
`charsetName` - The name of a supported `java.nio.charset.Charset` `charset`
Throws:
`[UnsupportedEncodingException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/UnsupportedEncodingException.html)` - If the named charset is not supported
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
 ============ METHOD DETAIL ========== 
Method Details
init
public void init([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Initialize ODF stream.
Parameters:
`entryName` - name of target reading entry.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
getContentEntry
public [OOXMLEntry](OOXMLEntry.html) getContentEntry()
Returns the OOXML file entry for the reader, or null if not found.
Returns:
the OOXML file entry, or null if not found
ensureOpen
protected void ensureOpen()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Check to make sure that the stream has not been closed.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If stream has been closed
close
public void close()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Close the stream.
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close())` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close())` in interface `[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#close())` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
read
public int read(char[] cbuf,
 int offset,
 int length)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Read characters from content.xml into a portion of an array. This method will block until some input is
 available, an I/O error occurs, or the end of the stream is reached.
Specified by:
`[read](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D,int,int))` in class `[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
Parameters:
`cbuf` - Destination buffer
`offset` - Offset at which to start storing characters
`length` - Maximum number of characters to read
Returns:
The number of characters read, or -1 if the end of the stream has been reached
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
read
public int read(byte[] b,
 int off,
 int len)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Reads from the current OOXML entry into an array of bytes. Blocks until some input is available.
Parameters:
`b` - the buffer into which the data is read
`off` - the start offset of the data
`len` - the maximum number of bytes read
Returns:
the actual number of bytes read, or -1 if the end of the entry is reached
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
getNextEntry
public [OOXMLEntry](OOXMLEntry.html) getNextEntry()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Reads the next OOXML file entry and positions the stream at the beginning of the entry data.
Returns:
the next OOXML file entry, or null if there are no more entries
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml</a></div>
<h1 class="title" title="Class OOXMLStreamReader">Class OOXMLStreamReader</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">java.io.Reader</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.OOXMLStreamReader</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Readable.html" title="class or interface in java.lang">Readable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OOXMLStreamReader</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></span></div>
<div class="block">This class implements a reader that can be used for OOXML. The reader reader data from content.xml by default.
 An OOXMLStreamReader is also provide a bridge from byte streams to characters streams: It reads bytes and
 decodes them into characters using a specified charset</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Oct 19, 2009</dd>
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
<div class="col-first even-row-color"><code>protected <a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#contentEntry">contentEntry</a></code></div>
<div class="col-last even-row-color">
<div class="block">Keep the entry for content reader.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStreamReader.html" title="class or interface in java.io">InputStreamReader</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#contentReader">contentReader</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An internal reader for specified content entry.</div>
</div>
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipInputStream.html" title="class or interface in java.util.zip">ZipInputStream</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#zipInputStream">zipInputStream</a></code></div>
<div class="col-last even-row-color">
<div class="block">An internal input stream for ZIP file.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.InputStream,java.lang.String)">OOXMLStreamReader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> in,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</code></div>
<div class="col-last even-row-color">
<div class="block">Create an OOXMLStreamReader that uses the named charset.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.InputStream,java.lang.String,java.lang.String)">OOXMLStreamReader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> in,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create an OOXMLStreamReader that uses the named charset and entry.</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureOpen()">ensureOpen</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check to make sure that the stream has not been closed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentEntry()">getContentEntry</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the OOXML file entry for the reader, or null if not found.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNextEntry()">getNextEntry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reads the next OOXML file entry and positions the stream at the beginning of the entry data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(java.lang.String)">init</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize ODF stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#read(byte%5B%5D,int,int)">read</a><wbr/>(byte[] b,
 int off,
 int len)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reads from the current OOXML entry into an array of bytes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#read(char%5B%5D,int,int)">read</a><wbr/>(char[] cbuf,
 int offset,
 int length)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Read characters from content.xml into a portion of an array.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.Reader">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#mark(int)" title="class or interface in java.io">mark</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#markSupported()" title="class or interface in java.io">markSupported</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#nullReader()" title="class or interface in java.io">nullReader</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read()" title="class or interface in java.io">read</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D)" title="class or interface in java.io">read</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(java.nio.CharBuffer)" title="class or interface in java.io">read</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#ready()" title="class or interface in java.io">ready</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#reset()" title="class or interface in java.io">reset</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#skip(long)" title="class or interface in java.io">skip</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#transferTo(java.io.Writer)" title="class or interface in java.io">transferTo</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="zipInputStream">
<h3>zipInputStream</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipInputStream.html" title="class or interface in java.util.zip">ZipInputStream</a></span> <span class="element-name">zipInputStream</span></div>
<div class="block">An internal input stream for ZIP file.</div>
</section>
</li>
<li>
<section class="detail" id="contentReader">
<h3>contentReader</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStreamReader.html" title="class or interface in java.io">InputStreamReader</a></span> <span class="element-name">contentReader</span></div>
<div class="block">An internal reader for specified content entry.</div>
</section>
</li>
<li>
<section class="detail" id="contentEntry">
<h3>contentEntry</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a></span> <span class="element-name">contentEntry</span></div>
<div class="block">Keep the entry for content reader.</div>
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
<section class="detail" id="&lt;init&gt;(java.io.InputStream,java.lang.String)">
<h3>OOXMLStreamReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLStreamReader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> in,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create an OOXMLStreamReader that uses the named charset.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>in</code> - An InputStream</dd>
<dd><code>entryName</code> - target entry name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/UnsupportedEncodingException.html" title="class or interface in java.io">UnsupportedEncodingException</a></code> - If the named charset is not supported</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.io.InputStream,java.lang.String,java.lang.String)">
<h3>OOXMLStreamReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLStreamReader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> in,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create an OOXMLStreamReader that uses the named charset and entry.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>in</code> - An InputStream</dd>
<dd><code>entryName</code> - target entry name</dd>
<dd><code>charsetName</code> - The name of a supported <code>java.nio.charset.Charset</code> <code>charset</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/UnsupportedEncodingException.html" title="class or interface in java.io">UnsupportedEncodingException</a></code> - If the named charset is not supported</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
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
<section class="detail" id="init(java.lang.String)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</span>
          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Initialize ODF stream.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>entryName</code> - name of target reading entry.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentEntry()">
<h3>getContentEntry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a></span> <span class="element-name">getContentEntry</span>()</div>
<div class="block">Returns the OOXML file entry for the reader, or null if not found.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the OOXML file entry, or null if not found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureOpen()">
<h3>ensureOpen</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">ensureOpen</span>()
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Check to make sure that the stream has not been closed.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If stream has been closed</dd>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#close()" title="class or interface in java.io">close</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="read(char[],int,int)">
<h3>read</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">read</span><wbr/><span class="parameters">(char[] cbuf,
 int offset,
 int length)</span>
         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Read characters from content.xml into a portion of an array. This method will block until some input is
 available, an I/O error occurs, or the end of the stream is reached.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html#read(char%5B%5D,int,int)" title="class or interface in java.io">read</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></dd>
<dt>Parameters:</dt>
<dd><code>cbuf</code> - Destination buffer</dd>
<dd><code>offset</code> - Offset at which to start storing characters</dd>
<dd><code>length</code> - Maximum number of characters to read</dd>
<dt>Returns:</dt>
<dd>The number of characters read, or -1 if the end of the stream has been reached</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="read(byte[],int,int)">
<h3>read</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">read</span><wbr/><span class="parameters">(byte[] b,
 int off,
 int len)</span>
         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Reads from the current OOXML entry into an array of bytes. Blocks until some input is available.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - the buffer into which the data is read</dd>
<dd><code>off</code> - the start offset of the data</dd>
<dd><code>len</code> - the maximum number of bytes read</dd>
<dt>Returns:</dt>
<dd>the actual number of bytes read, or -1 if the end of the entry is reached</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNextEntry()">
<h3>getNextEntry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a></span> <span class="element-name">getNextEntry</span>()
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Reads the next OOXML file entry and positions the stream at the beginning of the entry data.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the next OOXML file entry, or null if there are no more entries</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
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
