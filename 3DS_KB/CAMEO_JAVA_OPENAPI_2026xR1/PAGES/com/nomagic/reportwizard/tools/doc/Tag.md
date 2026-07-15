# JAVA OPENAPI: Tag (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/doc/Tag.html
- source_path: `com/nomagic/reportwizard/tools/doc/Tag.html`
- source_sha256: `bc80690ff5554c13de73a430abe1e50daecedad98804e4eecc719cd3484eb967`
- captured_utc: `2026-07-14T16:46:15.416005+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.doc](package-summary.html)

## Interface Tag

All Known Implementing Classes:
`[CodeTag](javadoc/CodeTag.html)`, `[LinkPlainTag](javadoc/LinkPlainTag.html)`, `[LinkTag](javadoc/LinkTag.html)`, `[LiteralTag](javadoc/LiteralTag.html)`, `[ParamTag](javadoc/ParamTag.html)`, `[SeeTag](javadoc/SeeTag.html)`, `[SerialFieldTag](javadoc/SerialFieldTag.html)`, `[TagImpl](javadoc/TagImpl.html)`, `[TextTag](javadoc/TextTag.html)`, `[ThrowsTag](javadoc/ThrowsTag.html)`, `[ValueTag](javadoc/ValueTag.html)`

@OpenApiAllpublic interfaceTag

The interface represent a simple documentation tag, such as @since, @author, @version.

Since:
Sep 3, 2008

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](Tag.html)>`
`[getInlineTags](#getInlineTags())()`
Return a collection of tags.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getKind](#getKind())()`
Return the kind of this tag.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRawText](#getRawText())()`
Return the text of this tag.
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html)`
`[getText](#getText())()`
Return the text of this tag.

============ METHOD DETAIL ========== 
Method Details
getKind
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getKind()
Return the kind of this tag.
Returns:
the kind of this tag
getText
[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html) getText()
Return the text of this tag.
Returns:
the text of this tag
getRawText
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRawText()
Return the text of this tag.
Returns:
the text of this tag
getInlineTags
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Tag](Tag.html)> getInlineTags()
Return a collection of tags. For a documentation comment with embedded tags.
Returns:
a collection of in-line tags

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.doc</a></div>
<h1 class="title" title="Interface Tag">Interface Tag</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="javadoc/CodeTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">CodeTag</a></code>, <code><a href="javadoc/LinkPlainTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">LinkPlainTag</a></code>, <code><a href="javadoc/LinkTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">LinkTag</a></code>, <code><a href="javadoc/LiteralTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">LiteralTag</a></code>, <code><a href="javadoc/ParamTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">ParamTag</a></code>, <code><a href="javadoc/SeeTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">SeeTag</a></code>, <code><a href="javadoc/SerialFieldTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">SerialFieldTag</a></code>, <code><a href="javadoc/TagImpl.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">TagImpl</a></code>, <code><a href="javadoc/TextTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">TextTag</a></code>, <code><a href="javadoc/ThrowsTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">ThrowsTag</a></code>, <code><a href="javadoc/ValueTag.html" title="class in com.nomagic.reportwizard.tools.doc.javadoc">ValueTag</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Tag</span></div>
<div class="block">The interface represent a simple documentation tag, such as @since, @author, @version.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInlineTags()">getInlineTags</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return a collection of tags.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getKind()">getKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the kind of this tag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRawText()">getRawText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the text of this tag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return the text of this tag.</div>
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
<section class="detail" id="getKind()">
<h3>getKind</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getKind</span>()</div>
<div class="block">Return the kind of this tag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the kind of this tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="return-type"><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></span> <span class="element-name">getText</span>()</div>
<div class="block">Return the text of this tag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the text of this tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRawText()">
<h3>getRawText</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRawText</span>()</div>
<div class="block">Return the text of this tag.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the text of this tag</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInlineTags()">
<h3>getInlineTags</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Tag.html" title="interface in com.nomagic.reportwizard.tools.doc">Tag</a>&gt;</span> <span class="element-name">getInlineTags</span>()</div>
<div class="block">Return a collection of tags. For a documentation comment with embedded tags.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a collection of in-line tags</dd>
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
