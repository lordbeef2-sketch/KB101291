# JAVA OPENAPI: DocumentParser (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/doc/javadoc/DocumentParser.html
- source_path: `com/nomagic/reportwizard/tools/doc/javadoc/DocumentParser.html`
- source_sha256: `a3b160b733b2d764861afa4f3be38dc6db315889f4cf4afa2fd5e09fb038ea76`
- captured_utc: `2026-07-14T16:46:15.504007+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.doc.javadoc](package-summary.html)

## Class DocumentParser

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.doc.javadoc.DocumentParser

@OpenApiAllpublic classDocumentParser
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Parse the comment string into [`Document`](../Document.html).

Since:
Sep 3, 2008

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DocumentParser](#%3Cinit%3E(com.nomagic.magicreport.engine.ITool))([ITool](../../../../magicreport/engine/ITool.html) tool)`
Create the parser.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Document](../Document.html)`
`[getDocument](#getDocument())()`
Return a [`Document`](../Document.html) from comment string.
`void`
`[handleComment](#handleComment(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Called when a JavaDoc comment is encountered.
`void`
`[handleInlineTag](#handleInlineTag(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) blockTag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) inlineTag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Called when a JavaDoc inline tag is encountered.
`void`
`[handleTag](#handleTag(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)`
Called when a JavaDoc block tag is encountered.
`void`
`[parse](#parse(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commentText)`
Parse the comment string.
`void`
`[parseText](#parseText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commentText)`
Parse the comment string in plain text format.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DocumentParser
public DocumentParser([ITool](../../../../magicreport/engine/ITool.html) tool)
Create the parser.
Parameters:
`tool` - Document Tool
 ============ METHOD DETAIL ========== 
Method Details
getDocument
public [Document](../Document.html) getDocument()
Return a [`Document`](../Document.html) from comment string.
Returns:
a [`Document`](../Document.html)
parse
public void parse([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commentText)
 throws [DocumentException](DocumentException.html)
Parse the comment string. The JavaDoc comment must be started with /** and end with */.
Parameters:
`commentText` - input string with /** and end with invalid input: '*'
Throws:
`[DocumentException](DocumentException.html)` - when error while parsing document.
parseText
public void parseText([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) commentText)
 throws [DocumentException](DocumentException.html)
Parse the comment string in plain text format.
Parameters:
`commentText` - input string
Throws:
`[DocumentException](DocumentException.html)` - when error while parsing document.
handleTag
public void handleTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Called when a JavaDoc block tag is encountered.
Parameters:
`tagName` - tag name
`text` - text comment
handleInlineTag
public void handleInlineTag([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) blockTag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) inlineTag,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Called when a JavaDoc inline tag is encountered.
Parameters:
`blockTag` - block tag name
`inlineTag` - inline tag name
`text` - text comment
handleComment
public void handleComment([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) text)
Called when a JavaDoc comment is encountered.
Parameters:
`text` - text comment

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.doc.javadoc</a></div>
<h1 class="title" title="Class DocumentParser">Class DocumentParser</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.doc.javadoc.DocumentParser</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DocumentParser</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Parse the comment string into <a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc"><code>Document</code></a>.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Sep 3, 2008</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITool)">DocumentParser</a><wbr/>(<a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a> tool)</code></div>
<div class="col-last even-row-color">
<div class="block">Create the parser.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocument()">getDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a <a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc"><code>Document</code></a> from comment string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleComment(java.lang.String)">handleComment</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called when a JavaDoc comment is encountered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleInlineTag(java.lang.String,java.lang.String,java.lang.String)">handleInlineTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> blockTag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inlineTag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called when a JavaDoc inline tag is encountered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleTag(java.lang.String,java.lang.String)">handleTag</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called when a JavaDoc block tag is encountered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#parse(java.lang.String)">parse</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commentText)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Parse the comment string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#parseText(java.lang.String)">parseText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commentText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Parse the comment string in plain text format.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITool)">
<h3>DocumentParser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DocumentParser</span><wbr/><span class="parameters">(<a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a> tool)</span></div>
<div class="block">Create the parser.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tool</code> - Document Tool</dd>
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
<section class="detail" id="getDocument()">
<h3>getDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></span> <span class="element-name">getDocument</span>()</div>
<div class="block">Return a <a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc"><code>Document</code></a> from comment string.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a <a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc"><code>Document</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parse(java.lang.String)">
<h3>parse</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">parse</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commentText)</span>
           throws <span class="exceptions"><a href="DocumentException.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">DocumentException</a></span></div>
<div class="block">Parse the comment string. The JavaDoc comment must be started with /** and end with */.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>commentText</code> - input string with /** and end with <span class="invalid-tag">invalid input: '&amp;#42'</span></dd>
<dt>Throws:</dt>
<dd><code><a href="DocumentException.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">DocumentException</a></code> - when error while parsing document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="parseText(java.lang.String)">
<h3>parseText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">parseText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> commentText)</span>
               throws <span class="exceptions"><a href="DocumentException.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">DocumentException</a></span></div>
<div class="block">Parse the comment string in plain text format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>commentText</code> - input string</dd>
<dt>Throws:</dt>
<dd><code><a href="DocumentException.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">DocumentException</a></code> - when error while parsing document.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleTag(java.lang.String,java.lang.String)">
<h3>handleTag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">handleTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Called when a JavaDoc block tag is encountered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tagName</code> - tag name</dd>
<dd><code>text</code> - text comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleInlineTag(java.lang.String,java.lang.String,java.lang.String)">
<h3>handleInlineTag</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">handleInlineTag</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> blockTag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inlineTag,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Called when a JavaDoc inline tag is encountered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>blockTag</code> - block tag name</dd>
<dd><code>inlineTag</code> - inline tag name</dd>
<dd><code>text</code> - text comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleComment(java.lang.String)">
<h3>handleComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">handleComment</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Called when a JavaDoc comment is encountered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text comment</dd>
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
