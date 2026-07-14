# JAVA OPENAPI: ModuleInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/diff/ModuleInfo.html
- source_path: `com/nomagic/magicdraw/diff/ModuleInfo.html`
- source_sha256: `7a20a6d8bc8f4efced8d5fd0d8dbd6cb381ab464f5d8a1a3d2ce9c4dc51b29e3`
- captured_utc: `2026-07-14T16:51:17.848159+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ModuleInfo

@OpenApiAllpublic interfaceModuleInfo
Module information.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static enum`
`[ModuleInfo.ProjectType](ModuleInfo.ProjectType.html)`
Defines project type.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProjectId](#getProjectId())()`
Module project Id
`[ModuleInfo.ProjectType](ModuleInfo.ProjectType.html)`
`[getProjectType](#getProjectType())()`
Project type.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getQualifiedName](#getQualifiedName())()`
Module qualified name.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getRootIds](#getRootIds())()`
Module root ids.
`org.eclipse.emf.common.util.URI`
`[getUri](#getUri())()`
Module URI.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getVersion](#getVersion())()`
Module version.

============ METHOD DETAIL ========== 
Method Details
getUri
org.eclipse.emf.common.util.URI getUri()
Module URI.
Returns:
uri.
getQualifiedName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getQualifiedName()
Module qualified name.
Returns:
qualified name.
getVersion
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getVersion()
Module version.
Returns:
version.
getProjectId
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProjectId()
Module project Id
Returns:
project id.
getRootIds
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getRootIds()
Module root ids.
Returns:
root ids.
getProjectType
[ModuleInfo.ProjectType](ModuleInfo.ProjectType.html) getProjectType()
Project type.
Returns:
project type.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ModuleInfo">Interface ModuleInfo</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModuleInfo</span></div>
<div class="block">Module information.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ModuleInfo.ProjectType.html" title="enum class in com.nomagic.magicdraw.diff">ModuleInfo.ProjectType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines project type.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectId()">getProjectId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Module project Id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModuleInfo.ProjectType.html" title="enum class in com.nomagic.magicdraw.diff">ModuleInfo.ProjectType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectType()">getProjectType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Project type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getQualifiedName()">getQualifiedName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Module qualified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRootIds()">getRootIds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Module root ids.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.emf.common.util.URI</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUri()">getUri</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Module URI.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVersion()">getVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Module version.</div>
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
<section class="detail" id="getUri()">
<h3>getUri</h3>
<div class="member-signature"><span class="return-type">org.eclipse.emf.common.util.URI</span> <span class="element-name">getUri</span>()</div>
<div class="block">Module URI.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>uri.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getQualifiedName()">
<h3>getQualifiedName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getQualifiedName</span>()</div>
<div class="block">Module qualified name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>qualified name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion()">
<h3>getVersion</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVersion</span>()</div>
<div class="block">Module version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectId()">
<h3>getProjectId</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProjectId</span>()</div>
<div class="block">Module project Id</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootIds()">
<h3>getRootIds</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRootIds</span>()</div>
<div class="block">Module root ids.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root ids.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectType()">
<h3>getProjectType</h3>
<div class="member-signature"><span class="return-type"><a href="ModuleInfo.ProjectType.html" title="enum class in com.nomagic.magicdraw.diff">ModuleInfo.ProjectType</a></span> <span class="element-name">getProjectType</span>()</div>
<div class="block">Project type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project type.</dd>
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
