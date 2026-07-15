# JAVA OPENAPI: OOXMLStreamWriter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/ooxml/OOXMLStreamWriter.html
- source_path: `com/nomagic/magicreport/engine/ooxml/OOXMLStreamWriter.html`
- source_sha256: `b39e8c394fde677f176c6493c8d193f6593d469cadc490fd564ec9e946573ac1`
- captured_utc: `2026-07-14T16:58:36.752278+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml](package-summary.html)

## Class OOXMLStreamWriter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
com.nomagic.magicreport.engine.ooxml.OOXMLStreamWriter

All Implemented Interfaces:
`[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`, `[Flushable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html)`, `[Appendable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Appendable.html)`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`

@OpenApiAllpublic classOOXMLStreamWriter
extends [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)

This class implements a writer that can be used for OOXML. The writer write data into content.xml by default.
 An OOXMLStreamWriter is also provide a bridge from character streams to byte streams: Characters written to it
 are encoded into bytes using a specified charset.

Since:
Oct 19, 2009

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [ZipOutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipOutputStream.html)`
`[zipOutputStream](#zipOutputStream)`
An internal output stream for ZIP file.
Fields inherited from class java.io.[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
`[lock](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#lock)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OOXMLStreamWriter](#%3Cinit%3E(java.io.OutputStream,java.lang.String))([OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) out,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)`
Create an OOXMLStreamWriter.
`[OOXMLStreamWriter](#%3Cinit%3E(java.io.OutputStream,java.lang.String,java.lang.String))([OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) out,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName)`
Create an OOXMLStreamWriter that uses the named charset.
`[OOXMLStreamWriter](#%3Cinit%3E(java.io.OutputStream,java.lang.String,java.lang.String,java.io.File))([OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) out,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) fileBuffer)`
Create an OOXMLStreamWriter that uses the named charset and file buffer.
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
`[closeEntry](#closeEntry())()`
Closes the current OOXML entry and positions the stream for writing the next entry.
`protected void`
`[ensureOpen](#ensureOpen())()`
Check to make sure that the stream has not been closed.
`void`
`[flush](#flush())()`
Flushes the stream.
`[OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)`
`[getOutputStream](#getOutputStream())()`
Returns an output stream for this writer.
`void`
`[putNextEntry](#putNextEntry(com.nomagic.magicreport.engine.ooxml.OOXMLEntry))([OOXMLEntry](OOXMLEntry.html) entry)`
Begins writing a new OOXML entry and positions the stream to the start of the entry data.
`void`
`[write](#write(byte%5B%5D,int,int))(byte[] buf,
 int offset,
 int length)`
Writes an array of bytes to the current OOXML entry data.
`void`
`[write](#write(char%5B%5D,int,int))(char[] cbuf,
 int offset,
 int length)`
Write characters into current entry.
`void`
`[write](#write(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Write text into current entry.
Methods inherited from class java.io.[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)
`[append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(char)), [append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence)), [append](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence,int,int)), [nullWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#nullWriter()), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D)), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(int)), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String,int,int))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
zipOutputStream
protected [ZipOutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipOutputStream.html) zipOutputStream
An internal output stream for ZIP file.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OOXMLStreamWriter
public OOXMLStreamWriter([OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) out,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create an OOXMLStreamWriter.
Parameters:
`out` - An OutputStream
`entryName` - target entry name
Throws:
`[ZipException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipException.html)` - if a ZIP file error has occurred
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
OOXMLStreamWriter
public OOXMLStreamWriter([OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) out,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create an OOXMLStreamWriter that uses the named charset.
Parameters:
`out` - An OutputStream
`entryName` - target entry name
`charsetName` - The name of a supported `java.nio.charset.Charset` `charset`
Throws:
`[ZipException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipException.html)` - if a ZIP file error has occurred
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
OOXMLStreamWriter
public OOXMLStreamWriter([OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) out,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) fileBuffer)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create an OOXMLStreamWriter that uses the named charset and file buffer. File buffer will be tracked and
 delete when this object has been destroyed.
Parameters:
`out` - An OutputStream
`entryName` - target entry name
`charsetName` - The name of a supported `java.nio.charset.Charset` `charset`
`fileBuffer` - use this file to buffer a OOXML content. If no fileBuffer is specified, content will be
 stored in memory.
Throws:
`[ZipException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipException.html)` - if a ZIP file error has occurred
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
 ============ METHOD DETAIL ========== 
Method Details
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
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#close())` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
flush
public void flush()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Flushes the stream.
Specified by:
`[flush](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html#flush())` in interface `[Flushable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html)`
Specified by:
`[flush](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#flush())` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
write
public void write(char[] cbuf,
 int offset,
 int length)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write characters into current entry.
Specified by:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D,int,int))` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Parameters:
`cbuf` - Array of characters
`offset` - Offset from which to start writing characters
`length` - Number of characters to write
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
write
public void write([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write text into current entry.
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String))` in class `[Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html)`
Parameters:
`text` - text
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
getOutputStream
public [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) getOutputStream()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Returns an output stream for this writer.
Returns:
an output stream for writing bytes to this writer.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
putNextEntry
public void putNextEntry([OOXMLEntry](OOXMLEntry.html) entry)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Begins writing a new OOXML entry and positions the stream to the start of the entry data.
Parameters:
`entry` - the OOXML entry to be written
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
closeEntry
public void closeEntry()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Closes the current OOXML entry and positions the stream for writing the next entry.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred
write
public void write(byte[] buf,
 int offset,
 int length)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Writes an array of bytes to the current OOXML entry data. This method will block until all the bytes are
 written.
Parameters:
`buf` - the data to be written
`offset` - the start offset in the data
`length` - the number of bytes that are written
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error has occurred

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml</a></div>
<h1 class="title" title="Class OOXMLStreamWriter">Class OOXMLStreamWriter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">java.io.Writer</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.OOXMLStreamWriter</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html" title="class or interface in java.io">Flushable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Appendable.html" title="class or interface in java.lang">Appendable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OOXMLStreamWriter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></span></div>
<div class="block">This class implements a writer that can be used for OOXML. The writer write data into content.xml by default.
 An OOXMLStreamWriter is also provide a bridge from character streams to byte streams: Characters written to it
 are encoded into bytes using a specified charset.</div>
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
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipOutputStream.html" title="class or interface in java.util.zip">ZipOutputStream</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#zipOutputStream">zipOutputStream</a></code></div>
<div class="col-last even-row-color">
<div class="block">An internal output stream for ZIP file.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.OutputStream,java.lang.String)">OOXMLStreamWriter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> out,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</code></div>
<div class="col-last even-row-color">
<div class="block">Create an OOXMLStreamWriter.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.OutputStream,java.lang.String,java.lang.String)">OOXMLStreamWriter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> out,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create an OOXMLStreamWriter that uses the named charset.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.OutputStream,java.lang.String,java.lang.String,java.io.File)">OOXMLStreamWriter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> out,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> fileBuffer)</code></div>
<div class="col-last even-row-color">
<div class="block">Create an OOXMLStreamWriter that uses the named charset and file buffer.</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeEntry()">closeEntry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes the current OOXML entry and positions the stream for writing the next entry.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureOpen()">ensureOpen</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check to make sure that the stream has not been closed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#flush()">flush</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Flushes the stream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutputStream()">getOutputStream</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an output stream for this writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#putNextEntry(com.nomagic.magicreport.engine.ooxml.OOXMLEntry)">putNextEntry</a><wbr/>(<a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a> entry)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Begins writing a new OOXML entry and positions the stream to the start of the entry data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(byte%5B%5D,int,int)">write</a><wbr/>(byte[] buf,
 int offset,
 int length)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Writes an array of bytes to the current OOXML entry data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(char%5B%5D,int,int)">write</a><wbr/>(char[] cbuf,
 int offset,
 int length)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write characters into current entry.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(java.lang.String)">write</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write text into current entry.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.Writer">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(char)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#append(java.lang.CharSequence,int,int)" title="class or interface in java.io">append</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#nullWriter()" title="class or interface in java.io">nullWriter</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D)" title="class or interface in java.io">write</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(int)" title="class or interface in java.io">write</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String,int,int)" title="class or interface in java.io">write</a></code></div>
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
<section class="detail" id="zipOutputStream">
<h3>zipOutputStream</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipOutputStream.html" title="class or interface in java.util.zip">ZipOutputStream</a></span> <span class="element-name">zipOutputStream</span></div>
<div class="block">An internal output stream for ZIP file.</div>
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
<section class="detail" id="&lt;init&gt;(java.io.OutputStream,java.lang.String)">
<h3>OOXMLStreamWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLStreamWriter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> out,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create an OOXMLStreamWriter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>out</code> - An OutputStream</dd>
<dd><code>entryName</code> - target entry name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipException.html" title="class or interface in java.util.zip">ZipException</a></code> - if a ZIP file error has occurred</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.io.OutputStream,java.lang.String,java.lang.String)">
<h3>OOXMLStreamWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLStreamWriter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> out,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create an OOXMLStreamWriter that uses the named charset.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>out</code> - An OutputStream</dd>
<dd><code>entryName</code> - target entry name</dd>
<dd><code>charsetName</code> - The name of a supported <code>java.nio.charset.Charset</code> <code>charset</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipException.html" title="class or interface in java.util.zip">ZipException</a></code> - if a ZIP file error has occurred</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.io.OutputStream,java.lang.String,java.lang.String,java.io.File)">
<h3>OOXMLStreamWriter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLStreamWriter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> out,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> fileBuffer)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create an OOXMLStreamWriter that uses the named charset and file buffer. File buffer will be tracked and
 delete when this object has been destroyed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>out</code> - An OutputStream</dd>
<dd><code>entryName</code> - target entry name</dd>
<dd><code>charsetName</code> - The name of a supported <code>java.nio.charset.Charset</code> <code>charset</code></dd>
<dd><code>fileBuffer</code> - use this file to buffer a OOXML content. If no fileBuffer is specified, content will be
           stored in memory.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipException.html" title="class or interface in java.util.zip">ZipException</a></code> - if a ZIP file error has occurred</dd>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#close()" title="class or interface in java.io">close</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="flush()">
<h3>flush</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">flush</span>()
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Flushes the stream.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html#flush()" title="class or interface in java.io">flush</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html" title="class or interface in java.io">Flushable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#flush()" title="class or interface in java.io">flush</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(char[],int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(char[] cbuf,
 int offset,
 int length)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write characters into current entry.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(char%5B%5D,int,int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>cbuf</code> - Array of characters</dd>
<dd><code>offset</code> - Offset from which to start writing characters</dd>
<dd><code>length</code> - Number of characters to write</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(java.lang.String)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write text into current entry.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html#write(java.lang.String)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>text</code> - text</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutputStream()">
<h3>getOutputStream</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></span> <span class="element-name">getOutputStream</span>()
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Returns an output stream for this writer.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an output stream for writing bytes to this writer.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="putNextEntry(com.nomagic.magicreport.engine.ooxml.OOXMLEntry)">
<h3>putNextEntry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">putNextEntry</span><wbr/><span class="parameters">(<a href="OOXMLEntry.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLEntry</a> entry)</span>
                  throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Begins writing a new OOXML entry and positions the stream to the start of the entry data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>entry</code> - the OOXML entry to be written</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeEntry()">
<h3>closeEntry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeEntry</span>()
                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Closes the current OOXML entry and positions the stream for writing the next entry.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(byte[],int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(byte[] buf,
 int offset,
 int length)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Writes an array of bytes to the current OOXML entry data. This method will block until all the bytes are
 written.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>buf</code> - the data to be written</dd>
<dd><code>offset</code> - the start offset in the data</dd>
<dd><code>length</code> - the number of bytes that are written</dd>
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
