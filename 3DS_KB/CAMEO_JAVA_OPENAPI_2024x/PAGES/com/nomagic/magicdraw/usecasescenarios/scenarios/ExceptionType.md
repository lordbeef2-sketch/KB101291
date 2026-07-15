# JAVA OPENAPI: ExceptionType (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/usecasescenarios/scenarios/ExceptionType.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/ExceptionType.html`
- source_sha256: `c1be0db07b9080095276e488516559e7e3771cb39f89e2db8f5d19ee20050d95`
- captured_utc: `2026-07-14T16:52:32.250152+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface ExceptionType

All Superinterfaces:
`[ScenarioNode](ScenarioNode.html)`

@OpenApiAllpublic interfaceExceptionTypeextends [ScenarioNode](ScenarioNode.html)

Exception type of flow scenario.

See Also:
[`ScenarioManager`](ScenarioManager.html)
[`ScenarioFactory`](ScenarioFactory.html)
[`Scenario`](Scenario.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html)`
`[getClazz](#getClazz())()`
Gets class which represents exception type.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)>`
`[getExceptionalFlowSteps](#getExceptionalFlowSteps())()`
Get exceptional flow steps of exception type.
`[ExceptionHandler](../../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html)`
`[getExceptionHandler](#getExceptionHandler())()`
Gets exception type handler.
`[InputPin](../../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html)`
`[getInputPin](#getInputPin())()`
Gets input pin of exception type.
`[FlowStep](FlowStep.html)`
`[getParentFlowStep](#getParentFlowStep())()`
Gets exception type parent flow step.
`[StructuredActivityNode](../../../uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html)`
`[getStructuredActivityNode](#getStructuredActivityNode())()`
Gets structured node which represents this exception type.
Methods inherited from interface com.nomagic.magicdraw.usecasescenarios.scenarios.[ScenarioNode](ScenarioNode.html)
`[belongsToIncludedExtending](ScenarioNode.html#belongsToIncludedExtending()), [getElement](ScenarioNode.html#getElement()), [getEnd](ScenarioNode.html#getEnd()), [getHumanType](ScenarioNode.html#getHumanType()), [getName](ScenarioNode.html#getName()), [getParent](ScenarioNode.html#getParent()), [getParentContainer](ScenarioNode.html#getParentContainer()), [getStart](ScenarioNode.html#getStart()), [isEditable](ScenarioNode.html#isEditable()), [setName](ScenarioNode.html#setName(java.lang.String))`

============ METHOD DETAIL ========== 
Method Details
getStructuredActivityNode
[StructuredActivityNode](../../../uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html) getStructuredActivityNode()
Gets structured node which represents this exception type.
Returns:
structured node which represents this exception type.
getInputPin
[InputPin](../../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html) getInputPin()
Gets input pin of exception type.
Returns:
input pin of exception type.
getParentFlowStep
[FlowStep](FlowStep.html) getParentFlowStep()
Gets exception type parent flow step.
Returns:
exception type parent flow step.
getExceptionalFlowSteps
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)> getExceptionalFlowSteps()
Get exceptional flow steps of exception type.
Returns:
exceptional flow steps of exception type.
getClazz
[Class](../../../uml2/ext/magicdraw/classes/mdkernel/Class.html) getClazz()
Gets class which represents exception type.
Returns:
class which represents exception type.
getExceptionHandler
[ExceptionHandler](../../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html) getExceptionHandler()
Gets exception type handler.
Returns:
exception type handler.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface ExceptionType">Interface ExceptionType</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ExceptionType</span><span class="extends-implements">
extends <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></span></div>
<div class="block">Exception type of flow scenario.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ScenarioManager.html" title="class in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioManager</code></a></li>
<li><a href="ScenarioFactory.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioFactory</code></a></li>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClazz()">getClazz</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets class which represents exception type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExceptionalFlowSteps()">getExceptionalFlowSteps</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get exceptional flow steps of exception type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExceptionHandler()">getExceptionHandler</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets exception type handler.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInputPin()">getInputPin</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets input pin of exception type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentFlowStep()">getParentFlowStep</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets exception type parent flow step.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStructuredActivityNode()">getStructuredActivityNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets structured node which represents this exception type.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode">Methods inherited from interface com.nomagic.magicdraw.usecasescenarios.scenarios.<a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></h3>
<code><a href="ScenarioNode.html#belongsToIncludedExtending()">belongsToIncludedExtending</a>, <a href="ScenarioNode.html#getElement()">getElement</a>, <a href="ScenarioNode.html#getEnd()">getEnd</a>, <a href="ScenarioNode.html#getHumanType()">getHumanType</a>, <a href="ScenarioNode.html#getName()">getName</a>, <a href="ScenarioNode.html#getParent()">getParent</a>, <a href="ScenarioNode.html#getParentContainer()">getParentContainer</a>, <a href="ScenarioNode.html#getStart()">getStart</a>, <a href="ScenarioNode.html#isEditable()">isEditable</a>, <a href="ScenarioNode.html#setName(java.lang.String)">setName</a></code></div>
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
<section class="detail" id="getStructuredActivityNode()">
<h3>getStructuredActivityNode</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdstructuredactivities/StructuredActivityNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdstructuredactivities">StructuredActivityNode</a></span> <span class="element-name">getStructuredActivityNode</span>()</div>
<div class="block">Gets structured node which represents this exception type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>structured node which represents this exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInputPin()">
<h3>getInputPin</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/InputPin.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">InputPin</a></span> <span class="element-name">getInputPin</span>()</div>
<div class="block">Gets input pin of exception type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>input pin of exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentFlowStep()">
<h3>getParentFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">getParentFlowStep</span>()</div>
<div class="block">Gets exception type parent flow step.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>exception type parent flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExceptionalFlowSteps()">
<h3>getExceptionalFlowSteps</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getExceptionalFlowSteps</span>()</div>
<div class="block">Get exceptional flow steps of exception type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>exceptional flow steps of exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClazz()">
<h3>getClazz</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Class.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Class</a></span> <span class="element-name">getClazz</span>()</div>
<div class="block">Gets class which represents exception type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class which represents exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExceptionHandler()">
<h3>getExceptionHandler</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdextrastructuredactivities/ExceptionHandler.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdextrastructuredactivities">ExceptionHandler</a></span> <span class="element-name">getExceptionHandler</span>()</div>
<div class="block">Gets exception type handler.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>exception type handler.</dd>
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
