# JAVA OPENAPI: Document (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/doc/Document.html
- source_path: `com/nomagic/reportwizard/tools/doc/Document.html`
- source_sha256: `7ff2beb3317cf31f93bbae902af789d478341e9c448afb1169e623b90bd18770`
- captured_utc: `2026-07-14T16:58:40.071313+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.doc](package-summary.html)

## Interface Document

All Known Implementing Classes:
`[DocumentImpl](javadoc/DocumentImpl.html)`

@OpenApiAllpublic interfaceDocument

The interface represent to Comment Document.

Since:
Sep 3, 2008

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Tag](Tag.html)`
`[get](#get(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Return tag of specified kind of this document item.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRawComment](#getRawComment())()`
Return the full unprocessed text of the comment.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](Tag.html)>`
`[getTags](#getTags())()`
Return all tags in this document item.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](Tag.html)>`
`[getTags](#getTags(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)`
Return tags of specified kind of this document item.

============ METHOD DETAIL ========== 
Method Details
getRawComment
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRawComment()
Return the full unprocessed text of the comment.
Returns:
the full unprocessed text of the comment.
getTags
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](Tag.html)> getTags()
Return all tags in this document item.
Returns:
collection of tags in this document item
getTags
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](Tag.html)> getTags([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Return tags of specified kind of this document item.
Parameters:
`tagName` - tag name
Returns:
collection of tags in this document item
get
[Tag](Tag.html) get([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) tagName)
Return tag of specified kind of this document item. If tags with same kind found, return the first tag of
 this kind.
Parameters:
`tagName` - tag name
Returns:
tag of specified kind of this document item

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.doc</a></div>
<h1 class="title" title="Interface Document">Interface Document</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="javadoc/DocumentImpl.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">DocumentImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Document</span></div>
<div class="block">The interface represent to Comment Document.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Sep 3, 2008</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#get(java.lang.String)">get</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return tag of specified kind of this document item.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRawComment()">getRawComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the full unprocessed text of the comment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTags()">getTags</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return all tags in this document item.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTags(java.lang.String)">getTags</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return tags of specified kind of this document item.</div>
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
<section class="detail" id="getRawComment()">
<h3>getRawComment</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRawComment</span>()</div>
<div class="block">Return the full unprocessed text of the comment.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the full unprocessed text of the comment.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTags()">
<h3>getTags</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getTags</span>()</div>
<div class="block">Return all tags in this document item.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>collection of tags in this document item</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTags(java.lang.String)">
<h3>getTags</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getTags</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Return tags of specified kind of this document item.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tagName</code> - tag name</dd>
<dt>Returns:</dt>
<dd>collection of tags in this document item</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="get(java.lang.String)">
<h3>get</h3>
<div class="member-signature"><span class="return-type"><a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> tagName)</span></div>
<div class="block">Return tag of specified kind of this document item. If tags with same kind found, return the first tag of
 this kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tagName</code> - tag name</dd>
<dt>Returns:</dt>
<dd>tag of specified kind of this document item</dd>
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
