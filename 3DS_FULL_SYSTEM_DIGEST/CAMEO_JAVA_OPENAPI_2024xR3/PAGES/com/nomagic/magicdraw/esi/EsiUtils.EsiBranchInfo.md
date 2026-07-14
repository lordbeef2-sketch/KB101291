# JAVA OPENAPI: EsiUtils.EsiBranchInfo (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/esi/EsiUtils.EsiBranchInfo.html
- source_path: `com/nomagic/magicdraw/esi/EsiUtils.EsiBranchInfo.html`
- source_sha256: `6200f66171038383058ba116728db468392e68880784bc50d41fce5ce2fbbf6e`
- captured_utc: `2026-07-14T16:55:20.367068+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi](package-summary.html)

## Interface EsiUtils.EsiBranchInfo

Enclosing class:
[EsiUtils](EsiUtils.html)

public static interfaceEsiUtils.EsiBranchInfo

Branch information.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAuthor](#getAuthor())()`

`long`
`[getBranchedFrom](#getBranchedFrom())()`

`[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)`
`[getCreatedDate](#getCreatedDate())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDescription](#getDescription())()`

`[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html)`
`[getID](#getID())()`

`long`
`[getLatestRevision](#getLatestRevision())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getMetadata](#getMetadata())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`

`[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html)`
`[getResourceID](#getResourceID())()`

============ METHOD DETAIL ========== 
Method Details
getName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
getDescription
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDescription()
getAuthor
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAuthor()
getBranchedFrom
long getBranchedFrom()
getID
[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) getID()
getCreatedDate
[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getCreatedDate()
getMetadata
[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getMetadata()
getResourceID
[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) getResourceID()
getLatestRevision
long getLatestRevision()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi</a></div>
<h1 class="title" title="Interface EsiUtils.EsiBranchInfo">Interface EsiUtils.EsiBranchInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="EsiUtils.html" title="class in com.nomagic.magicdraw.esi">EsiUtils</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static interface </span><span class="element-name type-name-label">EsiUtils.EsiBranchInfo</span></div>
<div class="block">Branch information.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAuthor()">getAuthor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBranchedFrom()">getBranchedFrom</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCreatedDate()">getCreatedDate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDescription()">getDescription</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLatestRevision()">getLatestRevision</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMetadata()">getMetadata</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getResourceID()">getResourceID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDescription()">
<h3>getDescription</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDescription</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getAuthor()">
<h3>getAuthor</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAuthor</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getBranchedFrom()">
<h3>getBranchedFrom</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getBranchedFrom</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></span> <span class="element-name">getID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCreatedDate()">
<h3>getCreatedDate</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">getCreatedDate</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getMetadata</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getResourceID()">
<h3>getResourceID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></span> <span class="element-name">getResourceID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLatestRevision()">
<h3>getLatestRevision</h3>
<div class="member-signature"><span class="return-type">long</span> <span class="element-name">getLatestRevision</span>()</div>
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
