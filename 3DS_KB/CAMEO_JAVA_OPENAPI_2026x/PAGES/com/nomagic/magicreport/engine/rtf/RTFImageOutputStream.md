# JAVA OPENAPI: RTFImageOutputStream (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/rtf/RTFImageOutputStream.html
- source_path: `com/nomagic/magicreport/engine/rtf/RTFImageOutputStream.html`
- source_sha256: `dfbd8b8165b8acab8b1c4a5881a07c9df2235b66279646947f30f63ef9a9b23e`
- captured_utc: `2026-07-14T16:58:36.903285+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.rtf](package-summary.html)

## Class RTFImageOutputStream

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.io.OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)
com.nomagic.magicreport.engine.rtf.RTFImageOutputStream

All Implemented Interfaces:
`[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`, `[Flushable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html)`, `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`

@OpenApiAllpublic classRTFImageOutputStream
extends [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)

The RTF image output stream.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[WMF_PLACEABLE_HEADER_SIZE](#WMF_PLACEABLE_HEADER_SIZE)`
The number of WMF header length.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RTFImageOutputStream](#%3Cinit%3E(java.io.Writer,java.lang.String))([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageType)`
Create RTF image output stream.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[close](#close())()`
Closes this output stream and releases any system resources associated with this stream.
`long`
`[getTotalWrittenChars](#getTotalWrittenChars())()`
Return total characters has been written.
`void`
`[write](#write(byte%5B%5D,int,int))(byte[] b,
 int off,
 int len)`
Writes `len` bytes from the specified byte array starting at offset `off` to this byte
 RTF image output stream.
`void`
`[write](#write(int))(int b)`
Writes the specified byte to this RTF image output stream.
`protected void`
`[writeHex](#writeHex(byte))(byte b)`
Write hexadecimal string.
Methods inherited from class java.io.[OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)
`[flush](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#flush()), [nullOutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#nullOutputStream()), [write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#write(byte%5B%5D))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
WMF_PLACEABLE_HEADER_SIZE
public static final int WMF_PLACEABLE_HEADER_SIZE
The number of WMF header length.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.rtf.RTFImageOutputStream.WMF_PLACEABLE_HEADER_SIZE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RTFImageOutputStream
public RTFImageOutputStream([Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageType)
Create RTF image output stream.
Parameters:
`writer` - the stream to write the converted image
`imageType` - target image type
 ============ METHOD DETAIL ========== 
Method Details
writeHex
protected void writeHex(byte b)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Write hexadecimal string.
Parameters:
`b` - a byte
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when IO error occurred
write
public void write(int b)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Writes the specified byte to this RTF image output stream.
Specified by:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#write(int))` in class `[OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)`
Parameters:
`b` - the byte to be written.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error occurs. In particular, an `IOException` may be thrown if the
 output stream has been closed.
write
public void write(byte[] b,
 int off,
 int len)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Writes `len` bytes from the specified byte array starting at offset `off` to this byte
 RTF image output stream.
Overrides:
`[write](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#write(byte%5B%5D,int,int))` in class `[OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)`
Parameters:
`b` - the data.
`off` - the start offset in the data.
`len` - the number of bytes to write.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error occurs. In particular, an `IOException` may be thrown if the
 output stream has been closed.
getTotalWrittenChars
public long getTotalWrittenChars()
Return total characters has been written.
Returns:
the total written characters
close
public void close()
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Closes this output stream and releases any system resources associated with this stream. A closed stream
 cannot perform output operations and cannot be reopened.
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close())` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html)`
Specified by:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close())` in interface `[Closeable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html)`
Overrides:
`[close](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#close())` in class `[OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html)`
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error occurs.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.rtf</a></div>
<h1 class="title" title="Class RTFImageOutputStream">Class RTFImageOutputStream</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">java.io.OutputStream</a>
<div class="inheritance">com.nomagic.magicreport.engine.rtf.RTFImageOutputStream</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Flushable.html" title="class or interface in java.io">Flushable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">RTFImageOutputStream</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></span></div>
<div class="block">The RTF image output stream.</div>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WMF_PLACEABLE_HEADER_SIZE">WMF_PLACEABLE_HEADER_SIZE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The number of WMF header length.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.io.Writer,java.lang.String)">RTFImageOutputStream</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageType)</code></div>
<div class="col-last even-row-color">
<div class="block">Create RTF image output stream.</div>
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
<div class="block">Closes this output stream and releases any system resources associated with this stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTotalWrittenChars()">getTotalWrittenChars</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return total characters has been written.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(byte%5B%5D,int,int)">write</a><wbr/>(byte[] b,
 int off,
 int len)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Writes <code>len</code> bytes from the specified byte array starting at offset <code>off</code> to this byte
 RTF image output stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#write(int)">write</a><wbr/>(int b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Writes the specified byte to this RTF image output stream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#writeHex(byte)">writeHex</a><wbr/>(byte b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Write hexadecimal string.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.io.OutputStream">Methods inherited from class java.io.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#flush()" title="class or interface in java.io">flush</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#nullOutputStream()" title="class or interface in java.io">nullOutputStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#write(byte%5B%5D)" title="class or interface in java.io">write</a></code></div>
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
<section class="detail" id="WMF_PLACEABLE_HEADER_SIZE">
<h3>WMF_PLACEABLE_HEADER_SIZE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">WMF_PLACEABLE_HEADER_SIZE</span></div>
<div class="block">The number of WMF header length.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.rtf.RTFImageOutputStream.WMF_PLACEABLE_HEADER_SIZE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;(java.io.Writer,java.lang.String)">
<h3>RTFImageOutputStream</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RTFImageOutputStream</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageType)</span></div>
<div class="block">Create RTF image output stream.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>writer</code> - the stream to write the converted image</dd>
<dd><code>imageType</code> - target image type</dd>
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
<section class="detail" id="writeHex(byte)">
<h3>writeHex</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">writeHex</span><wbr/><span class="parameters">(byte b)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Write hexadecimal string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>b</code> - a byte</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when IO error occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(int b)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Writes the specified byte to this RTF image output stream.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#write(int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></code></dd>
<dt>Parameters:</dt>
<dd><code>b</code> - the byte to be written.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error occurs. In particular, an <code>IOException</code> may be thrown if the
            output stream has been closed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write(byte[],int,int)">
<h3>write</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">write</span><wbr/><span class="parameters">(byte[] b,
 int off,
 int len)</span>
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Writes <code>len</code> bytes from the specified byte array starting at offset <code>off</code> to this byte
 RTF image output stream.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#write(byte%5B%5D,int,int)" title="class or interface in java.io">write</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></code></dd>
<dt>Parameters:</dt>
<dd><code>b</code> - the data.</dd>
<dd><code>off</code> - the start offset in the data.</dd>
<dd><code>len</code> - the number of bytes to write.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error occurs. In particular, an <code>IOException</code> may be thrown if the
            output stream has been closed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTotalWrittenChars()">
<h3>getTotalWrittenChars</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getTotalWrittenChars</span>()</div>
<div class="block">Return total characters has been written.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the total written characters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="close()">
<h3>close</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">close</span>()
           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Closes this output stream and releases any system resources associated with this stream. A closed stream
 cannot perform output operations and cannot be reopened.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html#close()" title="class or interface in java.lang">close</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/AutoCloseable.html" title="class or interface in java.lang">AutoCloseable</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html#close()" title="class or interface in java.io">close</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Closeable.html" title="class or interface in java.io">Closeable</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html#close()" title="class or interface in java.io">close</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a></code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error occurs.</dd>
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
