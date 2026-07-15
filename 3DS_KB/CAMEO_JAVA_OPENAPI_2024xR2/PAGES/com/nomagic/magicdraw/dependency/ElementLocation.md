# JAVA OPENAPI: ElementLocation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/dependency/ElementLocation.html
- source_path: `com/nomagic/magicdraw/dependency/ElementLocation.html`
- source_sha256: `e2ab09460c72bdeb25b05b5116959c6ecd769da3b62098d07b39ce563c7bfa24`
- captured_utc: `2026-07-14T16:55:12.629979+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependency](package-summary.html)

## Interface ElementLocation

@OpenApiAllpublic interfaceElementLocation

Represents a location (module or project) of an element.

Version:
1.0

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`com.nomagic.ci.persistence.IAttachedProject`
`[getAttachedProject](#getAttachedProject())()`
Returns module descriptor or null if an element is from project.
`[Project](../core/Project.html)`
`[getProject](#getProject())()`
Returns project or null if an element is from module.
`boolean`
`[isProject](#isProject())()`
Returns true if the element location is project, otherwise - element location is module.

============ METHOD DETAIL ========== 
Method Details
getAttachedProject
com.nomagic.ci.persistence.IAttachedProject getAttachedProject()
Returns module descriptor or null if an element is from project.
Returns:
module descriptor.
getProject
[Project](../core/Project.html) getProject()
Returns project or null if an element is from module.
Returns:
project.
isProject
boolean isProject()
Returns true if the element location is project, otherwise - element location is module.
Returns:
true if the element location is project.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependency</a></div>
<h1 class="title" title="Interface ElementLocation">Interface ElementLocation</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementLocation</span></div>
<div class="block">Represents a location (module or project) of an element.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.ci.persistence.IAttachedProject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAttachedProject()">getAttachedProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns module descriptor or null if an element is from project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns project or null if an element is from module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isProject()">isProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns true if the element location is project, otherwise - element location is module.</div>
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
<section class="detail" id="getAttachedProject()">
<h3>getAttachedProject</h3>
<div class="member-signature"><span class="return-type">com.nomagic.ci.persistence.IAttachedProject</span> <span class="element-name">getAttachedProject</span>()</div>
<div class="block">Returns module descriptor or null if an element is from project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>module descriptor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns project or null if an element is from module.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isProject()">
<h3>isProject</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isProject</span>()</div>
<div class="block">Returns true if the element location is project, otherwise - element location is module.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the element location is project.</dd>
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
