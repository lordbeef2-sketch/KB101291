# JAVA OPENAPI: ScenarioFactory (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioFactory.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioFactory.html`
- source_sha256: `3451e8a9ea2024c8df93d53a507110eac403a965f04c94894f68ef8a4665a514`
- captured_utc: `2026-07-14T16:52:19.006971+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface ScenarioFactory

@OpenApiAllpublic interfaceScenarioFactory
Knows how to construct scenarios.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Scenario](Scenario.html)`
`[createScenario](#createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Creates a scenario.
`[Scenario](Scenario.html)`
`[createScenario](#createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,boolean))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase,
 boolean createEvents)`
Creates a scenario.

============ METHOD DETAIL ========== 
Method Details
createScenario
@OpenApi[Scenario](Scenario.html) createScenario([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Creates a scenario.
Parameters:
`useCase` - use case for which to create scenario.
Returns:
created scenario.
createScenario
[Scenario](Scenario.html) createScenario([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase,
 boolean createEvents)
Creates a scenario.
Parameters:
`useCase` - use case for which to create scenario.
`createEvents` - indicates whether event propagation should be enabled for the created scenario.
Returns:
created scenario.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface ScenarioFactory">Interface ScenarioFactory</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ScenarioFactory</span></div>
<div class="block">Knows how to construct scenarios.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">createScenario</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates a scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,boolean)">createScenario</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase,
 boolean createEvents)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates a scenario.</div>
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
<section class="detail" id="createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>createScenario</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></span> <span class="element-name">createScenario</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Creates a scenario.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - use case for which to create scenario.</dd>
<dt>Returns:</dt>
<dd>created scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase,boolean)">
<h3>createScenario</h3>
<div class="member-signature"><span class="return-type"><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></span> <span class="element-name">createScenario</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase,
 boolean createEvents)</span></div>
<div class="block">Creates a scenario.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - use case for which to create scenario.</dd>
<dd><code>createEvents</code> - indicates whether event propagation should be enabled for the created scenario.</dd>
<dt>Returns:</dt>
<dd>created scenario.</dd>
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
