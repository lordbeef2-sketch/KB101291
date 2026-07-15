# JAVA OPENAPI: DocumentImpl (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/doc/javadoc/DocumentImpl.html
- source_path: `com/nomagic/reportwizard/tools/doc/javadoc/DocumentImpl.html`
- source_sha256: `6fab3d4c0c4d552736215a402886a1ee7beb7a5ad9c92a468424f6b186df37b4`
- captured_utc: `2026-07-14T16:46:15.517008+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.doc.javadoc](package-summary.html)

## Class DocumentImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.reportwizard.tools.doc.javadoc.DocumentImpl

All Implemented Interfaces:
`[Document](../Document.html)`

@OpenApiAllpublic classDocumentImpl
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Document](../Document.html)

The default JavaDoc document implementation.

Since:
Sep 3, 2008

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DocumentImpl](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.engine.ITool))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rawComment,
 [ITool](../../../../magicreport/engine/ITool.html) tool)`
Create a document.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Tag](../Tag.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Return tag of specified kind of this document item.
`[ITool.HTMLString](../../../../magicreport/engine/ITool.HTMLString.html)`
`[getComment](#getComment())()`
Return formatted text for this document.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)>`
`[getFirstSentenceTags](#getFirstSentenceTags())()`
Return the first sentence of the comment as a collection of tags.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)>`
`[getInlineTags](#getInlineTags())()`
Return comment as a collection of tags.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRawComment](#getRawComment())()`
Return the full unprocessed text of the comment.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)>`
`[getTags](#getTags())()`
Return all tags in this document item.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)>`
`[getTags](#getTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Return tags of specified kind of this document item.
`protected [ITool](../../../../magicreport/engine/ITool.html)`
`[getTool](#getTool())()`
Access to Tool.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DocumentImpl
public DocumentImpl([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rawComment,
 [ITool](../../../../magicreport/engine/ITool.html) tool)
Create a document. The `tool` uses to retrieve the system configuration from report engine. You
 can leave this parameter to null.
Parameters:
`rawComment` - raw comment.
`tool` - Document Tool
 ============ METHOD DETAIL ========== 
Method Details
get
public [Tag](../Tag.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Return tag of specified kind of this document item. If tags with same kind found, return the first tag of
 this kind.
Specified by:
`[get](../Document.html#get(java.lang.String))` in interface `[Document](../Document.html)`
Parameters:
`tagName` - tag name
Returns:
tag of specified kind of this document item; or `null` if no tag found.
getRawComment
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRawComment()
Return the full unprocessed text of the comment.
Specified by:
`[getRawComment](../Document.html#getRawComment())` in interface `[Document](../Document.html)`
Returns:
the full unprocessed text of the comment.
getTags
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)> getTags()
Return all tags in this document item.
Specified by:
`[getTags](../Document.html#getTags())` in interface `[Document](../Document.html)`
Returns:
collection of tags in this document item
getTags
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)> getTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Return tags of specified kind of this document item. Collection with zero length will be return if no
 matches found.
Specified by:
`[getTags](../Document.html#getTags(java.lang.String))` in interface `[Document](../Document.html)`
Parameters:
`tagName` - tag name
Returns:
collection of tags in this document item
getComment
public [ITool.HTMLString](../../../../magicreport/engine/ITool.HTMLString.html) getComment()
Return formatted text for this document.
Returns:
formatted text for this document
getInlineTags
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)> getInlineTags()
Return comment as a collection of tags.
Returns:
collection of tags.
getFirstSentenceTags
public [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](../Tag.html)> getFirstSentenceTags()
Return the first sentence of the comment as a collection of tags.
Returns:
collection of tags.
getTool
protected [ITool](../../../../magicreport/engine/ITool.html) getTool()
Access to Tool.
Returns:
[`ITool`](../../../../magicreport/engine/ITool.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.doc.javadoc</a></div>
<h1 class="title" title="Class DocumentImpl">Class DocumentImpl</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.reportwizard.tools.doc.javadoc.DocumentImpl</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DocumentImpl</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></span></div>
<div class="block">The default JavaDoc document implementation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.engine.ITool)">DocumentImpl</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rawComment,
 <a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a> tool)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a document.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return tag of specified kind of this document item.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getComment()">getComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return formatted text for this document.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstSentenceTags()">getFirstSentenceTags</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the first sentence of the comment as a collection of tags.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInlineTags()">getInlineTags</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return comment as a collection of tags.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRawComment()">getRawComment</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the full unprocessed text of the comment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTags()">getTags</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return all tags in this document item.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTags(java.lang.String)">getTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return tags of specified kind of this document item.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTool()">getTool</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Access to Tool.</div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.engine.ITool)">
<h3>DocumentImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DocumentImpl</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rawComment,
 <a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a> tool)</span></div>
<div class="block">Create a document. The <code>tool</code> uses to retrieve the system configuration from report engine. You
 can leave this parameter to null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rawComment</code> - raw comment.</dd>
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
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Return tag of specified kind of this document item. If tags with same kind found, return the first tag of
 this kind.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Document.html#get(java.lang.String)">get</a></code> in interface <code><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></code></dd>
<dt>Parameters:</dt>
<dd><code>tagName</code> - tag name</dd>
<dt>Returns:</dt>
<dd>tag of specified kind of this document item; or <code>null</code> if no tag found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRawComment()">
<h3>getRawComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRawComment</span>()</div>
<div class="block">Return the full unprocessed text of the comment.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Document.html#getRawComment()">getRawComment</a></code> in interface <code><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></code></dd>
<dt>Returns:</dt>
<dd>the full unprocessed text of the comment.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTags()">
<h3>getTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getTags</span>()</div>
<div class="block">Return all tags in this document item.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Document.html#getTags()">getTags</a></code> in interface <code><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></code></dd>
<dt>Returns:</dt>
<dd>collection of tags in this document item</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTags(java.lang.String)">
<h3>getTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Return tags of specified kind of this document item. Collection with zero length will be return if no
 matches found.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../Document.html#getTags(java.lang.String)">getTags</a></code> in interface <code><a href="../Document.html" title="interface in com.nomagic.reportwizard.tools.doc">Document</a></code></dd>
<dt>Parameters:</dt>
<dd><code>tagName</code> - tag name</dd>
<dt>Returns:</dt>
<dd>collection of tags in this document item</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getComment()">
<h3>getComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">getComment</span>()</div>
<div class="block">Return formatted text for this document.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>formatted text for this document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInlineTags()">
<h3>getInlineTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getInlineTags</span>()</div>
<div class="block">Return comment as a collection of tags.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of tags.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstSentenceTags()">
<h3>getFirstSentenceTags</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getFirstSentenceTags</span>()</div>
<div class="block">Return the first sentence of the comment as a collection of tags.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of tags.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTool()">
<h3>getTool</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></span> <span class="element-name">getTool</span>()</div>
<div class="block">Access to Tool.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><a href="../../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine"><code>ITool</code></a></dd>
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
