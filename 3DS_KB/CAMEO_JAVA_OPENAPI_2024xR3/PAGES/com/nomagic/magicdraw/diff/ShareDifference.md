# JAVA OPENAPI: ShareDifference (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/diff/ShareDifference.html
- source_path: `com/nomagic/magicdraw/diff/ShareDifference.html`
- source_sha256: `3f5e4208bfa1c880fbcbd2901e924d2ae0d949971d074a203477dda3e428eef1`
- captured_utc: `2026-07-14T16:55:16.570028+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ShareDifference

All Superinterfaces:
`[Difference](Difference.html)`

@OpenApiAllpublic interfaceShareDifferenceextends [Difference](Difference.html)

Shared packages difference. Shares can be added, or removed.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ModificationKind](ModificationKind.html)`
`[getModificationKind](#getModificationKind())()`

`[ModuleInfo](ModuleInfo.html)`
`[getModule](#getModule())()`
Gets the module that is used by a project.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPath](#getPath())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getSharedPackageID](#getSharedPackageID())()`
Methods inherited from interface com.nomagic.magicdraw.diff.[Difference](Difference.html)
`[accept](Difference.html#accept(com.nomagic.magicdraw.diff.DifferenceVisitor))`

============ METHOD DETAIL ========== 
Method Details
getSharedPackageID
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getSharedPackageID()
Returns:
id of shared package.
getModificationKind
[ModificationKind](ModificationKind.html) getModificationKind()
Returns:
modification kind (add/remove)
getPath
@CheckForNull[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPath()
Returns:
preferred share path or null if [`getModule()`](#getModule()) returns non-null value
getModule
@CheckForNull[ModuleInfo](ModuleInfo.html) getModule()
Gets the module that is used by a project. The method returns non-null value
 if corresponding module re-sharing state has been changed.
Returns:
module info if share difference means change module
 re-sharing state change.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ShareDifference">Interface ShareDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ShareDifference</span><span class="extends-implements">
extends <a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></span></div>
<div class="block">Shared packages difference. Shares can be added, or removed.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModificationKind()">getModificationKind</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getModule()">getModule</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the module that is used by a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPath()">getPath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSharedPackageID()">getSharedPackageID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.Difference">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></h3>
<code><a href="Difference.html#accept(com.nomagic.magicdraw.diff.DifferenceVisitor)">accept</a></code></div>
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
<section class="detail" id="getSharedPackageID()">
<h3>getSharedPackageID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getSharedPackageID</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>id of shared package.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModificationKind()">
<h3>getModificationKind</h3>
<div class="member-signature"><span class="return-type"><a href="ModificationKind.html" title="enum class in com.nomagic.magicdraw.diff">ModificationKind</a></span> <span class="element-name">getModificationKind</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>modification kind (add/remove)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPath()">
<h3>getPath</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPath</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>preferred share path or null if <a href="#getModule()"><code>getModule()</code></a> returns non-null value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getModule()">
<h3>getModule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="ModuleInfo.html" title="interface in com.nomagic.magicdraw.diff">ModuleInfo</a></span> <span class="element-name">getModule</span>()</div>
<div class="block">Gets the module that is used by a project. The method returns non-null value
 if corresponding module re-sharing state has been changed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>module info if share difference means change module
 re-sharing state change.</dd>
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
