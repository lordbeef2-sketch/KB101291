# JAVA OPENAPI: IReportWizardEventListener (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/magicreport/IReportWizardEventListener.html
- source_path: `com/nomagic/magicdraw/magicreport/IReportWizardEventListener.html`
- source_sha256: `e121ed46e9d0fc96c82a573a9c381d60b799245e126477ea0c945fbca26ffa42`
- captured_utc: `2026-07-14T16:55:21.785082+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport](package-summary.html)

## Interface IReportWizardEventListener

@OpenApiAllpublic interfaceIReportWizardEventListener

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[afterGenerated](#afterGenerated(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Method is called after report is generated and show success message
`void`
`[beforeGenerating](#beforeGenerating(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Method is called before report execution
`void`
`[beforeInitialReportTask](#beforeInitialReportTask(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean))(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)`
Method is called before initial generate task

============ METHOD DETAIL ========== 
Method Details
afterGenerated
void afterGenerated([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Method is called after report is generated and show success message
beforeGenerating
void beforeGenerating(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
Method is called before report execution
beforeInitialReportTask
void beforeInitialReportTask(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)
Method is called before initial generate task

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport</a></div>
<h1 class="title" title="Interface IReportWizardEventListener">Interface IReportWizardEventListener</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IReportWizardEventListener</span></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#afterGenerated(java.io.File)">afterGenerated</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called after report is generated and show success message</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#beforeGenerating(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">beforeGenerating</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called before report execution</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#beforeInitialReportTask(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">beforeInitialReportTask</a><wbr/>(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method is called before initial generate task</div>
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
<section class="detail" id="afterGenerated(java.io.File)">
<h3>afterGenerated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">afterGenerated</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Method is called after report is generated and show success message</div>
</section>
</li>
<li>
<section class="detail" id="beforeGenerating(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>beforeGenerating</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">beforeGenerating</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
<div class="block">Method is called before report execution</div>
</section>
</li>
<li>
<section class="detail" id="beforeInitialReportTask(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean)">
<h3>beforeInitialReportTask</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">beforeInitialReportTask</span><wbr/><span class="parameters">(com.nomagic.magicdraw.magicreport.ui.bean.TemplateBean templateBean)</span></div>
<div class="block">Method is called before initial generate task</div>
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
