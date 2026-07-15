# JAVA OPENAPI: ProjectOptionsDifference (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/diff/ProjectOptionsDifference.html
- source_path: `com/nomagic/magicdraw/diff/ProjectOptionsDifference.html`
- source_sha256: `145ceb577a70e86ce37576ff6a87832baf76bd552027d02bb7d5acf0b54159ab`
- captured_utc: `2026-07-14T16:57:54.295495+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ProjectOptionsDifference

All Superinterfaces:
`[Difference](Difference.html)`

@OpenApiAllpublic interfaceProjectOptionsDifferenceextends [Difference](Difference.html)

Difference between project options.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Style](../properties/Style.html)`
`[getProjectOptionsModelElementsStyle](#getProjectOptionsModelElementsStyle())()`

`[Style](../properties/Style.html)`
`[getProjectOptionsStyle](#getProjectOptionsStyle())()`

`[StyleManager](../properties/StyleManager.html)`
`[getSymbolsStyle](#getSymbolsStyle())()`

============ METHOD DETAIL ========== 
Method Details
getProjectOptionsStyle
@CheckForNull[Style](../properties/Style.html) getProjectOptionsStyle()
Returns:
project options style.
See Also:
[`ProjectOptions.getStyle()`](../core/options/ProjectOptions.html#getStyle())
getProjectOptionsModelElementsStyle
@CheckForNull[Style](../properties/Style.html) getProjectOptionsModelElementsStyle()
Returns:
project options model element style
See Also:
[`ProjectOptions.getActualModelElementStyle()`](../core/options/ProjectOptions.html#getActualModelElementStyle())
getSymbolsStyle
@CheckForNull[StyleManager](../properties/StyleManager.html) getSymbolsStyle()
Returns:
symbol style in project
See Also:
`Project.getStyleManager()`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ProjectOptionsDifference">Interface ProjectOptionsDifference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectOptionsDifference</span><span class="extends-implements">
extends <a href="Difference.html" title="interface in com.nomagic.magicdraw.diff">Difference</a></span></div>
<div class="block">Difference between project options.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectOptionsModelElementsStyle()">getProjectOptionsModelElementsStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectOptionsStyle()">getProjectOptionsStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSymbolsStyle()">getSymbolsStyle</a>()</code></div>
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
<section class="detail" id="getProjectOptionsStyle()">
<h3>getProjectOptionsStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getProjectOptionsStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project options style.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../core/options/ProjectOptions.html#getStyle()"><code>ProjectOptions.getStyle()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectOptionsModelElementsStyle()">
<h3>getProjectOptionsModelElementsStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getProjectOptionsModelElementsStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project options model element style</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../core/options/ProjectOptions.html#getActualModelElementStyle()"><code>ProjectOptions.getActualModelElementStyle()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSymbolsStyle()">
<h3>getSymbolsStyle</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></span> <span class="element-name">getSymbolsStyle</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>symbol style in project</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>Project.getStyleManager()</code></li>
</ul>
</dd>
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
