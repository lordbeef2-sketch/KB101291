# JAVA OPENAPI: StartupParticipant (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/core/StartupParticipant.html
- source_path: `com/nomagic/magicdraw/core/StartupParticipant.html`
- source_sha256: `cda7664e79d57b405c1298fa7c185fcd1eb5d234e432fcf9fc454d656bd382f7`
- captured_utc: `2026-07-14T16:57:51.809467+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core](package-summary.html)

## Interface StartupParticipant

@OpenApiAllpublic interfaceStartupParticipant
The startup participant for MagicDraw application starting. 

 StartupParticipant methods will be called during application startup steps.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[afterMainWindow](#afterMainWindow())()`
Is called after main application window creation
`void`
`[beforeMainWindow](#beforeMainWindow())()`
Is called before creating main application window.

============ METHOD DETAIL ========== 
Method Details
beforeMainWindow
void beforeMainWindow()
Is called before creating main application window.
 Application environment already set up.
afterMainWindow
void afterMainWindow()
Is called after main application window creation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core</a></div>
<h1 class="title" title="Interface StartupParticipant">Interface StartupParticipant</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">StartupParticipant</span></div>
<div class="block">The startup participant for MagicDraw application starting. <br/>
 StartupParticipant methods will be called during application startup steps.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#afterMainWindow()">afterMainWindow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Is called after main application window creation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#beforeMainWindow()">beforeMainWindow</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Is called before creating main application window.</div>
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
<section class="detail" id="beforeMainWindow()">
<h3>beforeMainWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">beforeMainWindow</span>()</div>
<div class="block">Is called before creating main application window.
 Application environment already set up.</div>
</section>
</li>
<li>
<section class="detail" id="afterMainWindow()">
<h3>afterMainWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">afterMainWindow</span>()</div>
<div class="block">Is called after main application window creation</div>
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
