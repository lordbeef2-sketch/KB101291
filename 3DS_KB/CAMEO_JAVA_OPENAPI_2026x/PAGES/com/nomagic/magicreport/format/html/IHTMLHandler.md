# JAVA OPENAPI: IHTMLHandler (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/IHTMLHandler.html
- source_path: `com/nomagic/magicreport/format/html/IHTMLHandler.html`
- source_sha256: `9f8a42616e50aaa89ae1b63c0fec7fefca49ee5cf7da105270c2d0c547f5d7a7`
- captured_utc: `2026-07-14T16:58:39.064303+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Interface IHTMLHandler

All Known Implementing Classes:
`[DocBookCreator](DocBookCreator.html)`, `[DOCXCreator](DOCXCreator.html)`, `[ODFCreator](ODFCreator.html)`, `[PPTXCreator](PPTXCreator.html)`, `[RTFCreator](RTFCreator.html)`, `[XLSXCreator](XLSXCreator.html)`

@OpenApiAllpublic interfaceIHTMLHandler

Receive notification of the logical content of a HTML document.

Since:
May 21, 2009

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[characters](#characters(char%5B%5D))(char[] data)`
Receive notification of character data inside a tag.
`void`
`[comment](#comment(char%5B%5D))(char[] data)`
Receive notification of comment data.
`void`
`[endDocument](#endDocument())()`
Receive notification of end document.
`void`
`[endTag](#endTag(javax.swing.text.html.HTML.Tag))([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag)`
Receive notification of the end of a tag.
`void`
`[startTag](#startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet))([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag,
 [AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attributes)`
Receive notification of the start of a tag.

============ METHOD DETAIL ========== 
Method Details
comment
void comment(char[] data)
Receive notification of comment data.
Parameters:
`data` - An array holding the characters in the document.
startTag
void startTag([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag,
 [AttributeSet](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html) attributes)
Receive notification of the start of a tag.
Parameters:
`tag` - HTML Tag.
`attributes` - The attributes attached to the tag. If there are no attributes, it shall be an empty
 Attributes object.
endTag
void endTag([HTML.Tag](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html) tag)
Receive notification of the end of a tag.
Parameters:
`tag` - HTML Tag.
characters
void characters(char[] data)
Receive notification of character data inside a tag.
Parameters:
`data` - The characters.
endDocument
void endDocument()
Receive notification of end document.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Interface IHTMLHandler">Interface IHTMLHandler</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="DocBookCreator.html" title="class in com.nomagic.magicreport.format.html">DocBookCreator</a></code>, <code><a href="DOCXCreator.html" title="class in com.nomagic.magicreport.format.html">DOCXCreator</a></code>, <code><a href="ODFCreator.html" title="class in com.nomagic.magicreport.format.html">ODFCreator</a></code>, <code><a href="PPTXCreator.html" title="class in com.nomagic.magicreport.format.html">PPTXCreator</a></code>, <code><a href="RTFCreator.html" title="class in com.nomagic.magicreport.format.html">RTFCreator</a></code>, <code><a href="XLSXCreator.html" title="class in com.nomagic.magicreport.format.html">XLSXCreator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IHTMLHandler</span></div>
<div class="block">Receive notification of the logical content of a HTML document.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#characters(char%5B%5D)">characters</a><wbr/>(char[] data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Receive notification of character data inside a tag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#comment(char%5B%5D)">comment</a><wbr/>(char[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Receive notification of comment data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#endDocument()">endDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Receive notification of end document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#endTag(javax.swing.text.html.HTML.Tag)">endTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Receive notification of the end of a tag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet)">startTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Receive notification of the start of a tag.</div>
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
<section class="detail" id="comment(char[])">
<h3>comment</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">comment</span><wbr/><span class="parameters">(char[] data)</span></div>
<div class="block">Receive notification of comment data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - An array holding the characters in the document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startTag(javax.swing.text.html.HTML.Tag,javax.swing.text.AttributeSet)">
<h3>startTag</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">startTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/AttributeSet.html" title="class or interface in javax.swing.text">AttributeSet</a> attributes)</span></div>
<div class="block">Receive notification of the start of a tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - HTML Tag.</dd>
<dd><code>attributes</code> - The attributes attached to the tag. If there are no attributes, it shall be an empty
           Attributes object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endTag(javax.swing.text.html.HTML.Tag)">
<h3>endTag</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">endTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/html/HTML.Tag.html" title="class or interface in javax.swing.text.html">HTML.Tag</a> tag)</span></div>
<div class="block">Receive notification of the end of a tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tag</code> - HTML Tag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="characters(char[])">
<h3>characters</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">characters</span><wbr/><span class="parameters">(char[] data)</span></div>
<div class="block">Receive notification of character data inside a tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - The characters.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="endDocument()">
<h3>endDocument</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">endDocument</span>()</div>
<div class="block">Receive notification of end document.</div>
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
