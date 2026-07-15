# JAVA OPENAPI: IChildEngine (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/IChildEngine.html
- source_path: `com/nomagic/magicreport/engine/IChildEngine.html`
- source_sha256: `fccb71ff80be078712b7373ec71bf45cb6e211716feea0060a50df8b9df869ec`
- captured_utc: `2026-07-14T16:58:36.290272+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Interface IChildEngine

All Superinterfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

All Known Implementing Classes:
`[DefaultImporterTool](../../reportwizard/tools/importer/DefaultImporterTool.html)`, `[DOCXImporterTool](../../reportwizard/tools/importer/DOCXImporterTool.html)`, `[ImportTool](../../reportwizard/tools/ImportTool.html)`

@OpenApiAllpublic interfaceIChildEngineextends [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

Provides an interface for child engine.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ITemplateEngine](ITemplateEngine.html)`
`[getParentEngine](#getParentEngine())()`
Get parent engine.
`void`
`[setParentEngine](#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](ITemplateEngine.html) iTemplateEngine)`
Set parent engine.

============ METHOD DETAIL ========== 
Method Details
getParentEngine
[ITemplateEngine](ITemplateEngine.html) getParentEngine()
Get parent engine.
Returns:
parent engine
setParentEngine
void setParentEngine([ITemplateEngine](ITemplateEngine.html) iTemplateEngine)
Set parent engine.
Parameters:
`iTemplateEngine` - parent engine

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Interface IChildEngine">Interface IChildEngine</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../reportwizard/tools/importer/DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code>, <code><a href="../../reportwizard/tools/importer/DOCXImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DOCXImporterTool</a></code>, <code><a href="../../reportwizard/tools/ImportTool.html" title="class in com.nomagic.reportwizard.tools">ImportTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IChildEngine</span><span class="extends-implements">
extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Provides an interface for child engine.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentEngine()">getParentEngine</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get parent engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">setParentEngine</a><wbr/>(<a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> iTemplateEngine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set parent engine.</div>
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
<section class="detail" id="getParentEngine()">
<h3>getParentEngine</h3>
<div class="member-signature"><span class="return-type"><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">getParentEngine</span>()</div>
<div class="block">Get parent engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent engine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>setParentEngine</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setParentEngine</span><wbr/><span class="parameters">(<a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> iTemplateEngine)</span></div>
<div class="block">Set parent engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>iTemplateEngine</code> - parent engine</dd>
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
