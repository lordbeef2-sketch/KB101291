# JAVA OPENAPI: Job (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/job/Job.html
- source_path: `com/nomagic/magicdraw/job/Job.html`
- source_sha256: `9f26a0c88e91452f39be1f22409a46929a6f71c32b97522212f40cc6afe9d4fc`
- captured_utc: `2026-07-14T16:45:37.235497+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.job](package-summary.html)

## Interface Job

@OpenApiAllpublic interfaceJob

An interface for performing some work in the application.

See Also:
[`IdleJobService`](IdleJobService.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[execute](#execute(com.nomagic.task.ProgressStatus))([ProgressStatus](../../task/ProgressStatus.html) progressStatus)`
Executes the work.
`void`
`[finished](#finished())()`
Cleanup should be done here after the job is finished.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Human-readable name of the job to display to the user in GUI.
`boolean`
`[needsExecute](#needsExecute())()`
Indicates if the job needs to be executed.

============ METHOD DETAIL ========== 
Method Details
needsExecute
boolean needsExecute()
Indicates if the job needs to be executed.
 Environment or project/model conditions could be checked here.
Returns:
true if job needs to be executed, false otherwise.
execute
void execute([ProgressStatus](../../task/ProgressStatus.html) progressStatus)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Executes the work.
Parameters:
`progressStatus` - progress status to indicate work pace.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - if any error occurs
finished
void finished()
Cleanup should be done here after the job is finished.
getName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Human-readable name of the job to display to the user in GUI.
Returns:
name of the job.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.job</a></div>
<h1 class="title" title="Interface Job">Interface Job</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Job</span></div>
<div class="block">An interface for performing some work in the application.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="IdleJobService.html" title="class in com.nomagic.magicdraw.job"><code>IdleJobService</code></a></li>
</ul>
</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(com.nomagic.task.ProgressStatus)">execute</a><wbr/>(<a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Executes the work.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#finished()">finished</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Cleanup should be done here after the job is finished.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Human-readable name of the job to display to the user in GUI.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#needsExecute()">needsExecute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if the job needs to be executed.</div>
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
<section class="detail" id="needsExecute()">
<h3>needsExecute</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">needsExecute</span>()</div>
<div class="block">Indicates if the job needs to be executed.
 Environment or project/model conditions could be checked here.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if job needs to be executed, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(com.nomagic.task.ProgressStatus)">
<h3>execute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progressStatus)</span>
      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Executes the work.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>progressStatus</code> - progress status to indicate work pace.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if any error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="finished()">
<h3>finished</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">finished</span>()</div>
<div class="block">Cleanup should be done here after the job is finished.</div>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Human-readable name of the job to display to the user in GUI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the job.</dd>
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
