# JAVA OPENAPI: ProjectDescriptor (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/project/ProjectDescriptor.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectDescriptor.html`
- source_sha256: `ec013eb2a9311de88795658fdad6f7c54af3a8ebea934ec6f3c0516de451764b`
- captured_utc: `2026-07-14T16:45:31.401420+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Interface ProjectDescriptor

All Known Implementing Classes:
`[AbstractRemoteProjectDescriptor](AbstractRemoteProjectDescriptor.html)`, `com.nomagic.magicdraw.core.project.AProjectDescriptor`, `[EsiUtils.OfflineProjectDescriptor](../../esi/EsiUtils.OfflineProjectDescriptor.html)`

@OpenApiAllpublic interfaceProjectDescriptor

Identifier for project storage location. Descriptor is used to load/save project.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRepresentationString](#getRepresentationString())()`
Constructs human representation of project.
`[URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html)`
`[getURI](#getURI())()`
Returns project location URI.
`boolean`
`[isRemote](#isRemote())()`

============ METHOD DETAIL ========== 
Method Details
getURI
[URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) getURI()
Returns project location URI.
 Used only for persistence, not for human representation.
 This location can be used for new descriptors creating in ProjectDescriptorsFactory.
Returns:
project URI.
getRepresentationString
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRepresentationString()
Constructs human representation of project.
Returns:
project's representation as String.
isRemote
boolean isRemote()
Returns:
true if descriptor points to remote project location.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Interface ProjectDescriptor">Interface ProjectDescriptor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractRemoteProjectDescriptor.html" title="class in com.nomagic.magicdraw.core.project">AbstractRemoteProjectDescriptor</a></code>, <code>com.nomagic.magicdraw.core.project.AProjectDescriptor</code>, <code><a href="../../esi/EsiUtils.OfflineProjectDescriptor.html" title="class in com.nomagic.magicdraw.esi">EsiUtils.OfflineProjectDescriptor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectDescriptor</span></div>
<div class="block">Identifier for project storage location. Descriptor is used to load/save project.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresentationString()">getRepresentationString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Constructs human representation of project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getURI()">getURI</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns project location URI.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isRemote()">isRemote</a>()</code></div>
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
<section class="detail" id="getURI()">
<h3>getURI</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a></span> <span class="element-name">getURI</span>()</div>
<div class="block">Returns project location URI.
 Used only for persistence, not for human representation.
 This location can be used for new descriptors creating in ProjectDescriptorsFactory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project URI.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRepresentationString()">
<h3>getRepresentationString</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationString</span>()</div>
<div class="block">Constructs human representation of project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project's representation as String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemote()">
<h3>isRemote</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isRemote</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if descriptor points to remote project location.</dd>
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
