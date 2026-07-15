# JAVA OPENAPI: AnnotationSubsetConfigurator (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/annotation/AnnotationSubsetConfigurator.html
- source_path: `com/nomagic/magicdraw/annotation/AnnotationSubsetConfigurator.html`
- source_sha256: `2dec950dad2fb8dcf4ce33406b950a527a48b4ff2acdb281718a2158048464ed`
- captured_utc: `2026-07-14T16:55:03.264873+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation](package-summary.html)

## Interface AnnotationSubsetConfigurator

@OpenApiAllpublic interfaceAnnotationSubsetConfigurator

When registered to `AnnotationSubsetConfigurators`, can modify (restrict, append) annotation categories that are
 1) Highlighted in diagrams by drawing rectangle around symbols
 2) Marked in the diagram right-side bar (marker area)

See Also:
[`AnnotationSubset`](AnnotationSubset.html)
`AnnotationSubsetConfigurators`

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[AnnotationSubset](AnnotationSubset.html)`
`[configureHighlightAnnotationSubset](#configureHighlightAnnotationSubset(com.nomagic.magicdraw.annotation.AnnotationSubset))([AnnotationSubset](AnnotationSubset.html) highlightedAnnotations)`

`[AnnotationSubset](AnnotationSubset.html)`
`[configureMarkerAnnotationSubset](#configureMarkerAnnotationSubset(com.nomagic.magicdraw.annotation.AnnotationSubset))([AnnotationSubset](AnnotationSubset.html) markedAnnotations)`

`static [AnnotationSubset](AnnotationSubset.html)`
`[excludeCategories](#excludeCategories(com.nomagic.magicdraw.annotation.AnnotationSubset,com.nomagic.magicdraw.annotation.AnnotationCategory...))([AnnotationSubset](AnnotationSubset.html) subset,
 [AnnotationCategory](AnnotationCategory.html)... toExclude)`

============ METHOD DETAIL ========== 
Method Details
configureHighlightAnnotationSubset
[AnnotationSubset](AnnotationSubset.html) configureHighlightAnnotationSubset([AnnotationSubset](AnnotationSubset.html) highlightedAnnotations)
Returns:
different subset to be highlighted in diagrams, or the same instance if it does not change
configureMarkerAnnotationSubset
[AnnotationSubset](AnnotationSubset.html) configureMarkerAnnotationSubset([AnnotationSubset](AnnotationSubset.html) markedAnnotations)
Returns:
different subset to be highlighted in diagrams, or the same instance if it does not change
excludeCategories
static [AnnotationSubset](AnnotationSubset.html) excludeCategories([AnnotationSubset](AnnotationSubset.html) subset,
 [AnnotationCategory](AnnotationCategory.html)... toExclude)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation</a></div>
<h1 class="title" title="Interface AnnotationSubsetConfigurator">Interface AnnotationSubsetConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AnnotationSubsetConfigurator</span></div>
<div class="block">When registered to <code>AnnotationSubsetConfigurators</code>, can modify (restrict, append) annotation categories that are
 1) Highlighted in diagrams by drawing rectangle around symbols
 2) Marked in the diagram right-side bar (marker area)</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation"><code>AnnotationSubset</code></a></li>
<li><code>AnnotationSubsetConfigurators</code></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configureHighlightAnnotationSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">configureHighlightAnnotationSubset</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> highlightedAnnotations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configureMarkerAnnotationSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">configureMarkerAnnotationSubset</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> markedAnnotations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#excludeCategories(com.nomagic.magicdraw.annotation.AnnotationSubset,com.nomagic.magicdraw.annotation.AnnotationCategory...)">excludeCategories</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset,
 <a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>... toExclude)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1"> </div>
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
<section class="detail" id="configureHighlightAnnotationSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>configureHighlightAnnotationSubset</h3>
<div class="member-signature"><span class="return-type"><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></span> <span class="element-name">configureHighlightAnnotationSubset</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> highlightedAnnotations)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>different subset to be highlighted in diagrams, or the same instance if it does not change</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureMarkerAnnotationSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>configureMarkerAnnotationSubset</h3>
<div class="member-signature"><span class="return-type"><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></span> <span class="element-name">configureMarkerAnnotationSubset</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> markedAnnotations)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>different subset to be highlighted in diagrams, or the same instance if it does not change</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="excludeCategories(com.nomagic.magicdraw.annotation.AnnotationSubset,com.nomagic.magicdraw.annotation.AnnotationCategory...)">
<h3>excludeCategories</h3>
<div class="member-signature"><span class="modifiers">static</span> <span class="return-type"><a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a></span> <span class="element-name">excludeCategories</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset,
 <a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a>... toExclude)</span></div>
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
