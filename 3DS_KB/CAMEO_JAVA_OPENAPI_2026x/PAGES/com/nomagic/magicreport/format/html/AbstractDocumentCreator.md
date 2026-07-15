# JAVA OPENAPI: AbstractDocumentCreator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/format/html/AbstractDocumentCreator.html
- source_path: `com/nomagic/magicreport/format/html/AbstractDocumentCreator.html`
- source_sha256: `0191b5da2d2dbb96b67147aa1bff8eab2d6fa28691aa824680749d00f0699cdf`
- captured_utc: `2026-07-14T16:58:38.730299+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.format.html](package-summary.html)

## Class AbstractDocumentCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.format.html.AbstractDocumentCreator

All Implemented Interfaces:
`[IDocumentCreator](../IDocumentCreator.html)`

Direct Known Subclasses:
`[DocBookCreator](DocBookCreator.html)`, `[DOCXCreator](DOCXCreator.html)`, `[ODFCreator](ODFCreator.html)`, `[PPTXCreator](PPTXCreator.html)`, `[RTFCreator](RTFCreator.html)`, `[XLSXCreator](XLSXCreator.html)`

@OpenApiAllpublic abstract classAbstractDocumentCreator
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [IDocumentCreator](../IDocumentCreator.html)

Abstract class for create content.

Since:
May 21, 2009

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractDocumentCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ImageTool](../../engine/tools/ImageTool.html)`
`[createImageTool](#createImageTool())()`
Create the new image tool from styled document.
`[DefaultFormatter](../DefaultFormatter.html)`
`[getFormatter](#getFormatter())()`
Return a formatter.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.osbcp.cssparser.PropertyValue>`
`[getStyleByCSSParser](#getStyleByCSSParser(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Re-arrange style by style name. 

 Using CSSParser.
`[StyledDocument](StyledDocument.html)`
`[getStyledDocument](#getStyledDocument())()`
Return an associated document.
`void`
`[setFormatter](#setFormatter(com.nomagic.magicreport.format.DefaultFormatter))([DefaultFormatter](../DefaultFormatter.html) formatter)`
Set a formatter.
`void`
`[setStyledDocument](#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))([StyledDocument](StyledDocument.html) styledDocument)`
Associates the creator with a document.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.format.[IDocumentCreator](../IDocumentCreator.html)
`[convert](../IDocumentCreator.html#convert(java.io.Reader,java.io.Writer)), [setDocumentPage](../IDocumentCreator.html#setDocumentPage(com.nomagic.magicreport.DocumentPage)), [setPaperHeight](../IDocumentCreator.html#setPaperHeight(float)), [setPaperWidth](../IDocumentCreator.html#setPaperWidth(float)), [setProperties](../IDocumentCreator.html#setProperties(java.util.Properties))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractDocumentCreator
public AbstractDocumentCreator()
 ============ METHOD DETAIL ========== 
Method Details
setStyledDocument
public void setStyledDocument([StyledDocument](StyledDocument.html) styledDocument)
Associates the creator with a document.
Specified by:
`[setStyledDocument](../IDocumentCreator.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`styledDocument` - [`StyledDocument`](StyledDocument.html)
getStyledDocument
public [StyledDocument](StyledDocument.html) getStyledDocument()
Return an associated document.
Returns:
[`StyledDocument`](StyledDocument.html)
getFormatter
public [DefaultFormatter](../DefaultFormatter.html) getFormatter()
Return a formatter.
Returns:
the formatter
setFormatter
public void setFormatter([DefaultFormatter](../DefaultFormatter.html) formatter)
Set a formatter.
Specified by:
`[setFormatter](../IDocumentCreator.html#setFormatter(com.nomagic.magicreport.format.DefaultFormatter))` in interface `[IDocumentCreator](../IDocumentCreator.html)`
Parameters:
`formatter` - the formatter to set
createImageTool
public [ImageTool](../../engine/tools/ImageTool.html) createImageTool()
Create the new image tool from styled document.
Returns:
the new image tool
getStyleByCSSParser
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.osbcp.cssparser.PropertyValue> getStyleByCSSParser([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Re-arrange style by style name. 

 Using CSSParser.
Parameters:
`value` - value set for converting
Returns:
set of style

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.format.html</a></div>
<h1 class="title" title="Class AbstractDocumentCreator">Class AbstractDocumentCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.format.html.AbstractDocumentCreator</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DocBookCreator.html" title="class in com.nomagic.magicreport.format.html">DocBookCreator</a></code>, <code><a href="DOCXCreator.html" title="class in com.nomagic.magicreport.format.html">DOCXCreator</a></code>, <code><a href="ODFCreator.html" title="class in com.nomagic.magicreport.format.html">ODFCreator</a></code>, <code><a href="PPTXCreator.html" title="class in com.nomagic.magicreport.format.html">PPTXCreator</a></code>, <code><a href="RTFCreator.html" title="class in com.nomagic.magicreport.format.html">RTFCreator</a></code>, <code><a href="XLSXCreator.html" title="class in com.nomagic.magicreport.format.html">XLSXCreator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractDocumentCreator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></span></div>
<div class="block">Abstract class for create content.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 21, 2009</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractDocumentCreator</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../engine/tools/ImageTool.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createImageTool()">createImageTool</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create the new image tool from styled document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFormatter()">getFormatter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a formatter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.osbcp.cssparser.PropertyValue&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleByCSSParser(java.lang.String)">getStyleByCSSParser</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Re-arrange style by style name.<br/>
 Using CSSParser.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyledDocument()">getStyledDocument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an associated document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFormatter(com.nomagic.magicreport.format.DefaultFormatter)">setFormatter</a><wbr/>(<a href="../DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a> formatter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a formatter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a><wbr/>(<a href="StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> styledDocument)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Associates the creator with a document.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.format.IDocumentCreator">Methods inherited from interface com.nomagic.magicreport.format.<a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></h3>
<code><a href="../IDocumentCreator.html#convert(java.io.Reader,java.io.Writer)">convert</a>, <a href="../IDocumentCreator.html#setDocumentPage(com.nomagic.magicreport.DocumentPage)">setDocumentPage</a>, <a href="../IDocumentCreator.html#setPaperHeight(float)">setPaperHeight</a>, <a href="../IDocumentCreator.html#setPaperWidth(float)">setPaperWidth</a>, <a href="../IDocumentCreator.html#setProperties(java.util.Properties)">setProperties</a></code></div>
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
<h3>AbstractDocumentCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractDocumentCreator</span>()</div>
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
<section class="detail" id="setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">
<h3>setStyledDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyledDocument</span><wbr/><span class="parameters">(<a href="StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a> styledDocument)</span></div>
<div class="block">Associates the creator with a document.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#setStyledDocument(com.nomagic.magicreport.format.html.StyledDocument)">setStyledDocument</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>styledDocument</code> - <a href="StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyledDocument()">
<h3>getStyledDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></span> <span class="element-name">getStyledDocument</span>()</div>
<div class="block">Return an associated document.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><a href="StyledDocument.html" title="interface in com.nomagic.magicreport.format.html"><code>StyledDocument</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFormatter()">
<h3>getFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a></span> <span class="element-name">getFormatter</span>()</div>
<div class="block">Return a formatter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the formatter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFormatter(com.nomagic.magicreport.format.DefaultFormatter)">
<h3>setFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFormatter</span><wbr/><span class="parameters">(<a href="../DefaultFormatter.html" title="class in com.nomagic.magicreport.format">DefaultFormatter</a> formatter)</span></div>
<div class="block">Set a formatter.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IDocumentCreator.html#setFormatter(com.nomagic.magicreport.format.DefaultFormatter)">setFormatter</a></code> in interface <code><a href="../IDocumentCreator.html" title="interface in com.nomagic.magicreport.format">IDocumentCreator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>formatter</code> - the formatter to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImageTool()">
<h3>createImageTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../engine/tools/ImageTool.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool</a></span> <span class="element-name">createImageTool</span>()</div>
<div class="block">Create the new image tool from styled document.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the new image tool</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyleByCSSParser(java.lang.String)">
<h3>getStyleByCSSParser</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.osbcp.cssparser.PropertyValue&gt;</span> <span class="element-name">getStyleByCSSParser</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Re-arrange style by style name.<br/>
 Using CSSParser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value set for converting</dd>
<dt>Returns:</dt>
<dd>set of style</dd>
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
