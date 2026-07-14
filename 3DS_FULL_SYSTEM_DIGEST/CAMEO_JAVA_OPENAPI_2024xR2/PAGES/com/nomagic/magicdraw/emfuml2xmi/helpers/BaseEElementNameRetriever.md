# JAVA OPENAPI: BaseEElementNameRetriever (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/emfuml2xmi/helpers/BaseEElementNameRetriever.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/BaseEElementNameRetriever.html`
- source_sha256: `fcec500cbb86bf0806a754997182a9bdba9573da9b4f351296ee85749d5a6d49`
- captured_utc: `2026-07-14T16:55:16.648026+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.helpers](package-summary.html)

## Interface BaseEElementNameRetriever

All Known Subinterfaces:
`[BaseEmfUml2Helper](BaseEmfUml2Helper.html)`, `[EmfUml2ExportHelper](EmfUml2ExportHelper.html)`, `[EmfUml2ExportHelper](../v4/helpers/EmfUml2ExportHelper.html)`, `[EmfUml2ExportHelper](../v5/helpers/EmfUml2ExportHelper.html)`, `[EmfUml2Helper](EmfUml2Helper.html)`, `[EmfUml2Helper](../v4/helpers/EmfUml2Helper.html)`, `[EmfUml2Helper](../v5/helpers/EmfUml2Helper.html)`, `[EmfUml2ImportHelper](../imp0rt/EmfUml2ImportHelper.html)`, `[EmfUml2ImportHelper](../v4/imp0rt/EmfUml2ImportHelper.html)`, `[EmfUml2ImportHelper](../v5/imp0rt/EmfUml2ImportHelper.html)`

All Known Implementing Classes:
`[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`, `[EmfUml2ExportHelper](../v2/export/EmfUml2ExportHelper.html)`, `[EmfUml2Helper](../v2/EmfUml2Helper.html)`, `[EmfUml2ImportHelper](../v2/imp0rt/EmfUml2ImportHelper.html)`

@OpenApipublic interfaceBaseEElementNameRetriever

Retrieves the name of Eclipse UML2 model element.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEElementName](#getEElementName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)`
Returns element human name.

============ METHOD DETAIL ========== 
Method Details
getEElementName
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEElementName([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)
Returns element human name.
Parameters:
`eElement` -
Returns:
element type + qualified name

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.helpers</a></div>
<h1 class="title" title="Interface BaseEElementNameRetriever">Interface BaseEElementNameRetriever</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code>, <code><a href="EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2ExportHelper</a></code>, <code><a href="../v4/helpers/EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2ExportHelper</a></code>, <code><a href="../v5/helpers/EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2ExportHelper</a></code>, <code><a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></code>, <code><a href="../v4/helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2Helper</a></code>, <code><a href="../v5/helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2Helper</a></code>, <code><a href="../imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt">EmfUml2ImportHelper</a></code>, <code><a href="../v4/imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt">EmfUml2ImportHelper</a></code>, <code><a href="../v5/imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt">EmfUml2ImportHelper</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code>, <code><a href="../v2/export/EmfUml2ExportHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export">EmfUml2ExportHelper</a></code>, <code><a href="../v2/EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2Helper</a></code>, <code><a href="../v2/imp0rt/EmfUml2ImportHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.imp0rt">EmfUml2ImportHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BaseEElementNameRetriever</span></div>
<div class="block">Retrieves the name of Eclipse UML2 model element.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEElementName(java.lang.Object)">getEElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns element human name.</div>
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
<section class="detail" id="getEElementName(java.lang.Object)">
<h3>getEElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
<div class="block">Returns element human name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eElement</code> - </dd>
<dt>Returns:</dt>
<dd>element type + qualified name</dd>
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
