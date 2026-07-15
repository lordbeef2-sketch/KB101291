# JAVA OPENAPI: MultiResourceProjectLoadConverter (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/persistence/convert/MultiResourceProjectLoadConverter.html
- source_path: `com/nomagic/magicdraw/persistence/convert/MultiResourceProjectLoadConverter.html`
- source_sha256: `ce09a4d3c38f43af22da3fc6e4f506f70603d69e916d60a77919759e2d9ea11b`
- captured_utc: `2026-07-14T16:45:38.938524+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.persistence.convert](package-summary.html)

## Interface MultiResourceProjectLoadConverter

@OpenApiAllpublic interfaceMultiResourceProjectLoadConverter
Interface for creating multi-resource/platform project converters which are invoked after project load.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static enum`
`[MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer](MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer.html)`
Converter answers for necessity to do mid-level commit.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[convertMidToFinal](#convertMidToFinal(com.nomagic.ci.persistence.IPrimaryProject))(com.nomagic.ci.persistence.IPrimaryProject primaryProject)`
Does upgrade from mid-level to final commit.
`default [MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer](MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer.html)`
`[getMidLevelCommitNeeded](#getMidLevelCommitNeeded(com.nomagic.ci.persistence.IPrimaryProject))(com.nomagic.ci.persistence.IPrimaryProject primaryProject)`
Determines if mid-level upgrade commit required.
`default boolean`
`[isMidToFinalConvertNeeded](#isMidToFinalConvertNeeded(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Is upgrade from mid-level to final upgrade commit needed? Method is used in multi-resource mode.

============ METHOD DETAIL ========== 
Method Details
getMidLevelCommitNeeded
default [MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer](MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer.html) getMidLevelCommitNeeded(com.nomagic.ci.persistence.IPrimaryProject primaryProject)
Determines if mid-level upgrade commit required. Method is used in multi-resource mode.
Parameters:
`primaryProject` - profile's project for which mid-level commit would be made
Returns:
`true` when mid-level upgrade commit is needed
isMidToFinalConvertNeeded
default boolean isMidToFinalConvertNeeded(com.nomagic.ci.persistence.IProject project)
Is upgrade from mid-level to final upgrade commit needed? Method is used in multi-resource mode.
Parameters:
`project` - profile's project because of which main project will have to be upgraded
Returns:
`true` when upgrade is needed
convertMidToFinal
default void convertMidToFinal(com.nomagic.ci.persistence.IPrimaryProject primaryProject)
Does upgrade from mid-level to final commit.
Parameters:
`primaryProject` - main project where upgrade needs to be done

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.persistence.convert</a></div>
<h1 class="title" title="Interface MultiResourceProjectLoadConverter">Interface MultiResourceProjectLoadConverter</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MultiResourceProjectLoadConverter</span></div>
<div class="block">Interface for creating multi-resource/platform project converters which are invoked after project load.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer.html" title="enum class in com.nomagic.magicdraw.persistence.convert">MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer</a></code></div>
<div class="col-last even-row-color">
<div class="block">Converter answers for necessity to do mid-level commit.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#convertMidToFinal(com.nomagic.ci.persistence.IPrimaryProject)">convertMidToFinal</a><wbr/>(com.nomagic.ci.persistence.IPrimaryProject primaryProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Does upgrade from mid-level to final commit.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer.html" title="enum class in com.nomagic.magicdraw.persistence.convert">MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getMidLevelCommitNeeded(com.nomagic.ci.persistence.IPrimaryProject)">getMidLevelCommitNeeded</a><wbr/>(com.nomagic.ci.persistence.IPrimaryProject primaryProject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Determines if mid-level upgrade commit required.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isMidToFinalConvertNeeded(com.nomagic.ci.persistence.IProject)">isMidToFinalConvertNeeded</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Is upgrade from mid-level to final upgrade commit needed? Method is used in multi-resource mode.</div>
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
<section class="detail" id="getMidLevelCommitNeeded(com.nomagic.ci.persistence.IPrimaryProject)">
<h3>getMidLevelCommitNeeded</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type"><a href="MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer.html" title="enum class in com.nomagic.magicdraw.persistence.convert">MultiResourceProjectLoadConverter.MidLevelCommitNeededAnswer</a></span> <span class="element-name">getMidLevelCommitNeeded</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IPrimaryProject primaryProject)</span></div>
<div class="block">Determines if mid-level upgrade commit required. Method is used in multi-resource mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>primaryProject</code> - profile's project for which mid-level commit would be made</dd>
<dt>Returns:</dt>
<dd><code>true</code> when mid-level upgrade commit is needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMidToFinalConvertNeeded(com.nomagic.ci.persistence.IProject)">
<h3>isMidToFinalConvertNeeded</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isMidToFinalConvertNeeded</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Is upgrade from mid-level to final upgrade commit needed? Method is used in multi-resource mode.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - profile's project because of which main project will have to be upgraded</dd>
<dt>Returns:</dt>
<dd><code>true</code> when upgrade is needed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="convertMidToFinal(com.nomagic.ci.persistence.IPrimaryProject)">
<h3>convertMidToFinal</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">convertMidToFinal</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IPrimaryProject primaryProject)</span></div>
<div class="block">Does upgrade from mid-level to final commit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>primaryProject</code> - main project where upgrade needs to be done</dd>
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
