# JAVA OPENAPI: IDocumentCreator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/IDocumentCreator.html
- source_path: `com/nomagic/magicreport/format/IDocumentCreator.html`
- source_sha256: `89547b72c0ddca18bbb98804095157482712b176209c956e858ab327e3db3858`
- captured_utc: `2026-07-14T16:58:38.310295+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format](package-summary.html)

## Interface IDocumentCreator

All Known Implementing Classes:
`[AbstractDocumentCreator](html/AbstractDocumentCreator.html)`, `[DocBookCreator](html/DocBookCreator.html)`, `[DOCXCreator](html/DOCXCreator.html)`, `[ODFCreator](html/ODFCreator.html)`, `[PPTXCreator](html/PPTXCreator.html)`, `[RTFCreator](html/RTFCreator.html)`, `[XLSXCreator](html/XLSXCreator.html)`

@OpenApiAllpublic interfaceIDocumentCreator

A document creator interface. This interface provides methods to create a document.

Since:
May 21, 2009

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[convert](#convert(java.io.Reader,java.io.Writer))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)`
Convert the document content from reader into other document.
`void`
`[setDocumentPage](#setDocumentPage(com.nomagic.magicreport.DocumentPage))(com.nomagic.magicreport.DocumentPage page)`
set document page property.
`void`
`[setFormatter](#setFormatter(com.nomagic.magicreport.format.DefaultFormatter))([DefaultFormatter](DefaultFormatter.html) formatter)`
Set formatter.
`void`
`[setPaperHeight](#setPaperHeight(float))(float height)`
set height of paper.
`void`
`[setPaperWidth](#setPaperWidth(float))(float width)`
set width of paper.
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Set properties.
`void`
`[setStyledDocument](#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))([StyledDocument](html/StyledDocument.html) document)`
Associates the creator with a document.

============ METHOD DETAIL ========== 
Method Details
convert
void convert([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) reader,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) writer)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Convert the document content from reader into other document.
Parameters:
`reader` - the reader containing source.
`writer` - the writer containing converted document.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If any IO errors occur.
setStyledDocument
void setStyledDocument([StyledDocument](html/StyledDocument.html) document)
Associates the creator with a document.
Parameters:
`document` - [`StyledDocument`](html/StyledDocument.html)
setPaperWidth
void setPaperWidth(float width)
set width of paper.
Parameters:
`width` - paper width.
setPaperHeight
void setPaperHeight(float height)
set height of paper.
Parameters:
`height` - paper width.
setFormatter
void setFormatter([DefaultFormatter](DefaultFormatter.html) formatter)
Set formatter.
Parameters:
`formatter` - formatter
setProperties
void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Set properties.
Parameters:
`properties` - properties
setDocumentPage
void setDocumentPage(com.nomagic.magicreport.DocumentPage page)
set document page property.
Parameters:
`page` - page property.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format</a></div>
<h1 class="title" title="Interface IDocumentCreator">Interface IDocumentCreator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="html/AbstractDocumentCreator.html" title="class in com.nomagic.magicreport.format.html">AbstractDocumentCreator</a></code>, <code><a href="html/DocBookCreator.html" title="class in com.nomagic.magicreport.format.html">DocBookCreator</a></code>, <code><a href="html/DOCXCreator.html" title="class in com.nomagic.magicreport.format.html">DOCXCreator</a></code>, <code><a href="html/ODFCreator.html" title="class in com.nomagic.magicreport.format.html">ODFCreator</a></code>, <code><a href="html/PPTXCreator.html" title="class in com.nomagic.magicreport.format.html">PPTXCreator</a></code>, <code><a href="html/RTFCreator.html" title="class in com.nomagic.magicreport.format.html">RTFCreator</a></code>, <code><a href="html/XLSXCreator.html" title="class in com.nomagic.magicreport.format.html">XLSXCreator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IDocumentCreator</span></div>
<div class="block">A document creator interface. This interface provides methods to create a document.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 21, 2009</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#convert(java.io.Reader,java.io.Writer)">convert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Convert the document content from reader into other document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDocumentPage(com.nomagic.magicreport.DocumentPage)">setDocumentPage</a><wbr/>(com.nomagic.magicreport.DocumentPage page)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">set document page property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setFormatter(com.nomagic.magicreport.format.DefaultFormatter)">setFormatter</a><wbr/>(<a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a> formatter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set formatter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPaperHeight(float)">setPaperHeight</a><wbr/>(float height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">set height of paper.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPaperWidth(float)">setPaperWidth</a><wbr/>(float width)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">set width of paper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a><wbr/>(<a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> document)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Associates the creator with a document.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="convert(java.io.Reader,java.io.Writer)">
<h3>convert</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">convert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> reader,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> writer)</span>
      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Convert the document content from reader into other document.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reader</code> - the reader containing source.</dd>
<dd><code>writer</code> - the writer containing converted document.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If any IO errors occur.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">
<h3>setStyledDocument</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setStyledDocument</span><wbr/><span class="parameters">(<a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> document)</span></div>
<div class="block">Associates the creator with a document.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>document</code> - <a href="html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPaperWidth(float)">
<h3>setPaperWidth</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPaperWidth</span><wbr/><span class="parameters">(float width)</span></div>
<div class="block">set width of paper.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - paper width.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPaperHeight(float)">
<h3>setPaperHeight</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPaperHeight</span><wbr/><span class="parameters">(float height)</span></div>
<div class="block">set height of paper.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>height</code> - paper width.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFormatter(com.nomagic.magicreport.format.DefaultFormatter)">
<h3>setFormatter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setFormatter</span><wbr/><span class="parameters">(<a href="DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a> formatter)</span></div>
<div class="block">Set formatter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>formatter</code> - formatter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Set properties.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDocumentPage(com.nomagic.magicreport.DocumentPage)">
<h3>setDocumentPage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDocumentPage</span><wbr/><span class="parameters">(com.nomagic.magicreport.DocumentPage page)</span></div>
<div class="block">set document page property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>page</code> - page property.</dd>
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
