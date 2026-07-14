# JAVA OPENAPI: EmfUML2FinalizeActivityManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/emfuml2xmi/EmfUML2FinalizeActivityManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/EmfUML2FinalizeActivityManager.html`
- source_sha256: `33f268c583a680604515786a30193e42ce076518db2e9c4645a969736873b677`
- captured_utc: `2026-07-14T16:57:55.876513+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi](package-summary.html)

## Interface EmfUML2FinalizeActivityManager

All Known Implementing Classes:
`com.nomagic.magicdraw.emfuml2xmi.export.convert.BaseEmfUml2ExportFinalizeActivityManager`, `com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2FinalizeActivityManager`, `com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.BaseEmfUml2ImportFinalizeActivityManager`, `[EmfUml2ExportFinalizeActivityManager](v2/export/convert/EmfUml2ExportFinalizeActivityManager.html)`, `[EmfUml2ExportFinalizeActivityManager](v3/export/convert/EmfUml2ExportFinalizeActivityManager.html)`, `[EmfUml2ExportFinalizeActivityManager](v4/export/convert/EmfUml2ExportFinalizeActivityManager.html)`, `[EmfUml2ExportFinalizeActivityManager](v5/export/convert/EmfUml2ExportFinalizeActivityManager.html)`, `[EmfUml2ImportFinalizeActivityManager](v2/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html)`, `[EmfUml2ImportFinalizeActivityManager](v3/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html)`, `[EmfUml2ImportFinalizeActivityManager](v4/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html)`, `[EmfUml2ImportFinalizeActivityManager](v5/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html)`

@OpenApiAllpublic interfaceEmfUML2FinalizeActivityManager

Registers finalize activities for Eclipse UML2 XMI export/import.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addActivity](#addActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity))([FinalizeActivity](FinalizeActivity.html) activity)`
Registers activity
`void`
`[removeActivity](#removeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity))([FinalizeActivity](FinalizeActivity.html) activity)`
Removes activity

============ METHOD DETAIL ========== 
Method Details
addActivity
void addActivity([FinalizeActivity](FinalizeActivity.html) activity)
Registers activity
Parameters:
`activity` - finalize activity.
removeActivity
void removeActivity([FinalizeActivity](FinalizeActivity.html) activity)
Removes activity
Parameters:
`activity` - finalize activity.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi</a></div>
<h1 class="title" title="Interface EmfUML2FinalizeActivityManager">Interface EmfUML2FinalizeActivityManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.nomagic.magicdraw.emfuml2xmi.export.convert.BaseEmfUml2ExportFinalizeActivityManager</code>, <code>com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2FinalizeActivityManager</code>, <code>com.nomagic.magicdraw.emfuml2xmi.imp0rt.convert.BaseEmfUml2ImportFinalizeActivityManager</code>, <code><a href="v2/export/convert/EmfUml2ExportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export.convert">EmfUml2ExportFinalizeActivityManager</a></code>, <code><a href="v3/export/convert/EmfUml2ExportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.export.convert">EmfUml2ExportFinalizeActivityManager</a></code>, <code><a href="v4/export/convert/EmfUml2ExportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.export.convert">EmfUml2ExportFinalizeActivityManager</a></code>, <code><a href="v5/export/convert/EmfUml2ExportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v5.export.convert">EmfUml2ExportFinalizeActivityManager</a></code>, <code><a href="v2/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.imp0rt.convert">EmfUml2ImportFinalizeActivityManager</a></code>, <code><a href="v3/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.imp0rt.convert">EmfUml2ImportFinalizeActivityManager</a></code>, <code><a href="v4/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt.convert">EmfUml2ImportFinalizeActivityManager</a></code>, <code><a href="v5/imp0rt/convert/EmfUml2ImportFinalizeActivityManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt.convert">EmfUml2ImportFinalizeActivityManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUML2FinalizeActivityManager</span></div>
<div class="block">Registers finalize activities for Eclipse UML2 XMI export/import.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addActivity</a><wbr/>(<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers activity</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">removeActivity</a><wbr/>(<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes activity</div>
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
<section class="detail" id="addActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">
<h3>addActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addActivity</span><wbr/><span class="parameters">(<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</span></div>
<div class="block">Registers activity</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activity</code> - finalize activity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">
<h3>removeActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeActivity</span><wbr/><span class="parameters">(<a href="FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</span></div>
<div class="block">Removes activity</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>activity</code> - finalize activity.</dd>
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
