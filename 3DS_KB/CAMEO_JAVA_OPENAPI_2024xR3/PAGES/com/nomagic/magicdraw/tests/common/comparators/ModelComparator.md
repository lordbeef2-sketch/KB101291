# JAVA OPENAPI: ModelComparator (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/tests/common/comparators/ModelComparator.html
- source_path: `com/nomagic/magicdraw/tests/common/comparators/ModelComparator.html`
- source_sha256: `15bdfa8c0d8085305e3f5c9ac36025ababb16e2eaffb27ed745920808d6ecfb2`
- captured_utc: `2026-07-14T16:55:39.139276+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests.common.comparators](package-summary.html)

## Interface ModelComparator

@OpenApiAllpublic interfaceModelComparator
Base interface for model comparing used by ProjectsComparator.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addFilter](#addFilter(com.nomagic.magicdraw.tests.common.comparators.ModelComparatorFilter))([ModelComparatorFilter](ModelComparatorFilter.html) filter)`
Adds filter for skipping unnecessary model elements during models comparison.
`boolean`
`[compareModels](#compareModels(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) p1,
 [Project](../../../core/Project.html) p2)`
Check if models of two given MagicDraw projects are equals.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiffInfo](#getDiffInfo())()`
Textual information about differences found in compared projects.

============ METHOD DETAIL ========== 
Method Details
compareModels
boolean compareModels([Project](../../../core/Project.html) p1,
 [Project](../../../core/Project.html) p2)
Check if models of two given MagicDraw projects are equals.
Parameters:
`p1` - first MagicDraw project
`p2` - second MagicDraw project
Returns:
true if models of compared projects are equals
getDiffInfo
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiffInfo()
Textual information about differences found in compared projects.
Returns:
String representing differences found in compared projects
addFilter
void addFilter([ModelComparatorFilter](ModelComparatorFilter.html) filter)
Adds filter for skipping unnecessary model elements during models comparison.
Parameters:
`filter` - model element filter to add

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests.common.comparators</a></div>
<h1 class="title" title="Interface ModelComparator">Interface ModelComparator</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelComparator</span></div>
<div class="block">Base interface for model comparing used by ProjectsComparator.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addFilter(com.nomagic.magicdraw.tests.common.comparators.ModelComparatorFilter)">addFilter</a><wbr/>(<a href="ModelComparatorFilter.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">ModelComparatorFilter</a> filter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds filter for skipping unnecessary model elements during models comparison.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#compareModels(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">compareModels</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> p1,
 <a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> p2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if models of two given MagicDraw projects are equals.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDiffInfo()">getDiffInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Textual information about differences found in compared projects.</div>
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
<section class="detail" id="compareModels(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">
<h3>compareModels</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">compareModels</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> p1,
 <a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> p2)</span></div>
<div class="block">Check if models of two given MagicDraw projects are equals.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>p1</code> - first MagicDraw project</dd>
<dd><code>p2</code> - second MagicDraw project</dd>
<dt>Returns:</dt>
<dd>true if models of compared projects are equals</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiffInfo()">
<h3>getDiffInfo</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiffInfo</span>()</div>
<div class="block">Textual information about differences found in compared projects.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String representing differences found in compared projects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFilter(com.nomagic.magicdraw.tests.common.comparators.ModelComparatorFilter)">
<h3>addFilter</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addFilter</span><wbr/><span class="parameters">(<a href="ModelComparatorFilter.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">ModelComparatorFilter</a> filter)</span></div>
<div class="block">Adds filter for skipping unnecessary model elements during models comparison.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - model element filter to add</dd>
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
