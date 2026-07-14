# JAVA OPENAPI: AbstractImporter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/importer/template/AbstractImporter.html
- source_path: `com/nomagic/reportwizard/tools/importer/template/AbstractImporter.html`
- source_sha256: `7c2a4edae4c6d68f719fae46806b3119c194207806eb4c00adc7014fb716cf17`
- captured_utc: `2026-07-14T16:58:40.581319+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.importer.template](package-summary.html)

## Class AbstractImporter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.importer.template.AbstractImporter

All Implemented Interfaces:
`[IImporter](IImporter.html)`

Direct Known Subclasses:
`[HtmlImporter](HtmlImporter.html)`, `[RtfImporter](RtfImporter.html)`, `[TxtImporter](TxtImporter.html)`, `[XmlImporter](XmlImporter.html)`

@OpenApiAllpublic abstract classAbstractImporter
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IImporter](IImporter.html)

the Abstract Importer implementation.

Since:
Jan 22, 2009

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected org.apache.logging.log4j.Logger`
`[log](#log)`
the logger for IImporter instances.
`protected [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
`[reader](#reader)`
the reader containing the content.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractImporter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`protected abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDocumentBody](#getDocumentBody(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Get the HTML Body.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getDocumentSection](#getDocumentSection(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
Get a Section in an Html document.
`[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
`[getReader](#getReader())()`
initialize reader invalid input: '&' writer.
`[ITool.RetainedString](../../../../magicreport/engine/ITool.RetainedString.html)`
`[postFormat](#postFormat(java.io.StringWriter))([StringWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html) writer)`
Apply necessary document dependent formatting.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
log
protected org.apache.logging.log4j.Logger log
the logger for IImporter instances.
reader
protected [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader
the reader containing the content.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractImporter
public AbstractImporter()
 ============ METHOD DETAIL ========== 
Method Details
getReader
public [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) getReader()
initialize reader invalid input: '&' writer.
Specified by:
`[getReader](IImporter.html#getReader())` in interface `[IImporter](IImporter.html)`
Returns:
the reader for the template
postFormat
public [ITool.RetainedString](../../../../magicreport/engine/ITool.RetainedString.html) postFormat([StringWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html) writer)
Apply necessary document dependent formatting.
Specified by:
`[postFormat](IImporter.html#postFormat(java.io.StringWriter))` in interface `[IImporter](IImporter.html)`
Parameters:
`writer` - the writer to post format
Returns:
the final output.
getDocumentBody
protected abstract [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDocumentBody([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Get the HTML Body.
Parameters:
`file` - holding the document
Returns:
the Text
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if reading the file failed
getDocumentSection
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getDocumentSection([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Get a Section in an Html document.
Parameters:
`file` - holding the document.
`section` - the section name
Returns:
the section text
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if reading the section failed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.importer.template</a></div>
<h1 class="title" title="Class AbstractImporter">Class AbstractImporter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.importer.template.AbstractImporter</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="IImporter.html" title="interface in com.nomagic.reportwizard.tools.importer.template">IImporter</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="HtmlImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">HtmlImporter</a></code>, <code><a href="RtfImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">RtfImporter</a></code>, <code><a href="TxtImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">TxtImporter</a></code>, <code><a href="XmlImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">XmlImporter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractImporter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="IImporter.html" title="interface in com.nomagic.reportwizard.tools.importer.template">IImporter</a></span></div>
<div class="block">the Abstract Importer implementation.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 22, 2009</dd>
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
<div class="col-first even-row-color"><code>protected org.apache.logging.log4j.Logger</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#log">log</a></code></div>
<div class="col-last even-row-color">
<div class="block">the logger for IImporter instances.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#reader">reader</a></code></div>
<div class="col-last odd-row-color">
<div class="block">the reader containing the content.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractImporter</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDocumentBody(java.io.File)">getDocumentBody</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get the HTML Body.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentSection(java.io.File,java.lang.String)">getDocumentSection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get a Section in an Html document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReader()">getReader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">initialize reader <span class="invalid-tag">invalid input: '&amp;'</span> writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#postFormat(java.io.StringWriter)">postFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html" title="class or interface in java.io">StringWriter</a> writer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Apply necessary document dependent formatting.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="log">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">org.apache.logging.log4j.Logger</span> <span class="element-name">log</span></div>
<div class="block">the logger for IImporter instances.</div>
</section>
</li>
<li>
<section class="detail" id="reader">
<h3>reader</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></span> <span class="element-name">reader</span></div>
<div class="block">the reader containing the content.</div>
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
<h3>AbstractImporter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractImporter</span>()</div>
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
<section class="detail" id="getReader()">
<h3>getReader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></span> <span class="element-name">getReader</span>()</div>
<div class="block">initialize reader <span class="invalid-tag">invalid input: '&amp;'</span> writer.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IImporter.html#getReader()">getReader</a></code> in interface <code><a href="IImporter.html" title="interface in com.nomagic.reportwizard.tools.importer.template">IImporter</a></code></dd>
<dt>Returns:</dt>
<dd>the reader for the template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postFormat(java.io.StringWriter)">
<h3>postFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">postFormat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html" title="class or interface in java.io">StringWriter</a> writer)</span></div>
<div class="block">Apply necessary document dependent formatting.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="IImporter.html#postFormat(java.io.StringWriter)">postFormat</a></code> in interface <code><a href="IImporter.html" title="interface in com.nomagic.reportwizard.tools.importer.template">IImporter</a></code></dd>
<dt>Parameters:</dt>
<dd><code>writer</code> - the writer to post format</dd>
<dt>Returns:</dt>
<dd>the final output.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentBody(java.io.File)">
<h3>getDocumentBody</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDocumentBody</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get the HTML Body.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - holding the document</dd>
<dt>Returns:</dt>
<dd>the Text</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if reading the file failed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentSection(java.io.File,java.lang.String)">
<h3>getDocumentSection</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDocumentSection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get a Section in an Html document.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - holding the document.</dd>
<dd><code>section</code> - the section name</dd>
<dt>Returns:</dt>
<dd>the section text</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if reading the section failed</dd>
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
