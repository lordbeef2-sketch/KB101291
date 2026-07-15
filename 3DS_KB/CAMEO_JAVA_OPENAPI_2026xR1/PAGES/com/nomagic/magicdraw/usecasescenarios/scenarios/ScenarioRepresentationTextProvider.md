# JAVA OPENAPI: ScenarioRepresentationTextProvider (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioRepresentationTextProvider.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioRepresentationTextProvider.html`
- source_sha256: `bd53b996b46fb34d8bada76feadda2af72db638076542e333f15897e64a156fd`
- captured_utc: `2026-07-14T16:46:10.532941+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface ScenarioRepresentationTextProvider

@OpenApiAllpublic interfaceScenarioRepresentationTextProvider

Contains knowledge how scenario elements should be represented in GUI.
 Each scenario implementation can return its own provider to change
 GUI representation of scenario elements.

See Also:
[`Scenario`](Scenario.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRepresentationText](#getRepresentationText(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode))([ScenarioNode](ScenarioNode.html) scenarioNode)`
Gets representation text of the given scenario node.

============ METHOD DETAIL ========== 
Method Details
getRepresentationText
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRepresentationText([ScenarioNode](ScenarioNode.html) scenarioNode)
Gets representation text of the given scenario node.
Parameters:
`scenarioNode` - scenario node for which to get representation text.
Returns:
representation text of the given scenario node.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface ScenarioRepresentationTextProvider">Interface ScenarioRepresentationTextProvider</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ScenarioRepresentationTextProvider</span></div>
<div class="block">Contains knowledge how scenario elements should be represented in GUI.
 Each scenario implementation can return its own provider to change
 GUI representation of scenario elements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>Scenario</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRepresentationText(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode)">getRepresentationText</a><wbr/>(<a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a> scenarioNode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets representation text of the given scenario node.</div>
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
<section class="detail" id="getRepresentationText(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode)">
<h3>getRepresentationText</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRepresentationText</span><wbr/><span class="parameters">(<a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a> scenarioNode)</span></div>
<div class="block">Gets representation text of the given scenario node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scenarioNode</code> - scenario node for which to get representation text.</dd>
<dt>Returns:</dt>
<dd>representation text of the given scenario node.</dd>
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
