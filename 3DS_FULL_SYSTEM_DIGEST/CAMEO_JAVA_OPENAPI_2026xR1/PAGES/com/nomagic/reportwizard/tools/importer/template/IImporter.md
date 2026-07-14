# JAVA OPENAPI: IImporter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/importer/template/IImporter.html
- source_path: `com/nomagic/reportwizard/tools/importer/template/IImporter.html`
- source_sha256: `bbc0c4b4ebc01725c45eb2cac316fa3977b85b92910db435519deaaeccf79fde`
- captured_utc: `2026-07-14T16:46:15.805011+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.importer.template](package-summary.html)

## Interface IImporter

All Known Implementing Classes:
`[AbstractImporter](AbstractImporter.html)`, `[HtmlImporter](HtmlImporter.html)`, `[RtfImporter](RtfImporter.html)`, `[TxtImporter](TxtImporter.html)`, `[XmlImporter](XmlImporter.html)`

@OpenApiAllpublic interfaceIImporter

Interface for Document dependent importers.

Since:
Jan 22, 2009

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html)`
`[getReader](#getReader())()`
initialize reader invalid input: '&' writer.
`[ITool.RetainedString](../../../../magicreport/engine/ITool.RetainedString.html)`
`[postFormat](#postFormat(java.io.StringWriter))([StringWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html) writer)`
Apply necessary document dependent formatting.

============ METHOD DETAIL ========== 
Method Details
getReader
[Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) getReader()
initialize reader invalid input: '&' writer.
Returns:
the reader for the template
postFormat
[ITool.RetainedString](../../../../magicreport/engine/ITool.RetainedString.html) postFormat([StringWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html) writer)
Apply necessary document dependent formatting.
Parameters:
`writer` - the writer to post format
Returns:
the final output.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.importer.template</a></div>
<h1 class="title" title="Interface IImporter">Interface IImporter</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">AbstractImporter</a></code>, <code><a href="HtmlImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">HtmlImporter</a></code>, <code><a href="RtfImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">RtfImporter</a></code>, <code><a href="TxtImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">TxtImporter</a></code>, <code><a href="XmlImporter.html" title="class in com.nomagic.reportwizard.tools.importer.template">XmlImporter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IImporter</span></div>
<div class="block">Interface for Document dependent importers.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 22, 2009</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReader()">getReader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">initialize reader <span class="invalid-tag">invalid input: '&amp;'</span> writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#postFormat(java.io.StringWriter)">postFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html" title="class or interface in java.io">StringWriter</a> writer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Apply necessary document dependent formatting.</div>
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
<section class="detail" id="getReader()">
<h3>getReader</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a></span> <span class="element-name">getReader</span>()</div>
<div class="block">initialize reader <span class="invalid-tag">invalid input: '&amp;'</span> writer.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the reader for the template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postFormat(java.io.StringWriter)">
<h3>postFormat</h3>
<div class="member-signature"><span class="return-type"><a href="../../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></span> <span class="element-name">postFormat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/StringWriter.html" title="class or interface in java.io">StringWriter</a> writer)</span></div>
<div class="block">Apply necessary document dependent formatting.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>writer</code> - the writer to post format</dd>
<dt>Returns:</dt>
<dd>the final output.</dd>
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
