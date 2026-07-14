# JAVA OPENAPI: DependencyCheckResult (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/dependency/DependencyCheckResult.html
- source_path: `com/nomagic/magicdraw/dependency/DependencyCheckResult.html`
- source_sha256: `b74163b7cbda88e2409b3bd169f134a1290e0c63dcac91782985a410ffb47dc8`
- captured_utc: `2026-07-14T16:57:52.917479+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependency](package-summary.html)

## Interface DependencyCheckResult

@OpenApiAllpublic interfaceDependencyCheckResult

Interface for getting dependency checking information.

Version:
1.0

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ElementLocationDependency](ElementLocationDependency.html)>`
`[getDependencies](#getDependencies())()`
Returns dependencies between modules and a project.
`boolean`
`[hasCyclicDependencies](#hasCyclicDependencies())()`
Returns indication whether the dependency check has found cyclic dependencies.
`boolean`
`[hasDependencies](#hasDependencies())()`
Returns indication whether the dependency check has found dependencies.

============ METHOD DETAIL ========== 
Method Details
getDependencies
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[ElementLocationDependency](ElementLocationDependency.html)> getDependencies()
Returns dependencies between modules and a project.
Returns:
dependencies.
hasCyclicDependencies
boolean hasCyclicDependencies()
Returns indication whether the dependency check has found cyclic dependencies.
Returns:
true if cyclic dependencies exist.
hasDependencies
boolean hasDependencies()
Returns indication whether the dependency check has found dependencies.
Returns:
true if dependencies exist, otherwise - false.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependency</a></div>
<h1 class="title" title="Interface DependencyCheckResult">Interface DependencyCheckResult</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DependencyCheckResult</span></div>
<div class="block">Interface for getting dependency checking information.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="ElementLocationDependency.html" title="interface in com.nomagic.magicdraw.dependency">ElementLocationDependency</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDependencies()">getDependencies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns dependencies between modules and a project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasCyclicDependencies()">hasCyclicDependencies</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns indication whether the dependency check has found cyclic dependencies.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasDependencies()">hasDependencies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns indication whether the dependency check has found dependencies.</div>
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
<section class="detail" id="getDependencies()">
<h3>getDependencies</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ElementLocationDependency.html" title="interface in com.nomagic.magicdraw.dependency">ElementLocationDependency</a>&gt;</span> <span class="element-name">getDependencies</span>()</div>
<div class="block">Returns dependencies between modules and a project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>dependencies.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasCyclicDependencies()">
<h3>hasCyclicDependencies</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasCyclicDependencies</span>()</div>
<div class="block">Returns indication whether the dependency check has found cyclic dependencies.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if cyclic dependencies exist.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasDependencies()">
<h3>hasDependencies</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasDependencies</span>()</div>
<div class="block">Returns indication whether the dependency check has found dependencies.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if dependencies exist, otherwise - false.</dd>
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
