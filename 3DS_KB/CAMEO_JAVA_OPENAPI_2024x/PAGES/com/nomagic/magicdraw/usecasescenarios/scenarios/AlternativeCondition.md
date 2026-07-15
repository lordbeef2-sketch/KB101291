# JAVA OPENAPI: AlternativeCondition (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/usecasescenarios/scenarios/AlternativeCondition.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/AlternativeCondition.html`
- source_sha256: `9b3610cb708ba0868ea99f228d9fd851b0936119aa8f409f2dc76775b2a9423a`
- captured_utc: `2026-07-14T16:52:25.623059+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface AlternativeCondition

All Superinterfaces:
`[ScenarioNode](ScenarioNode.html)`

@OpenApiAllpublic interfaceAlternativeConditionextends [ScenarioNode](ScenarioNode.html)

Represents alternative condition in the scenario flow.

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
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)>`
`[getAlternativeFlowSteps](#getAlternativeFlowSteps())()`
Gets condition alternative flow steps.
`[DecisionNode](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html)`
`[getDecisionNode](#getDecisionNode())()`
Gets condition decision node.
`[ControlFlow](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html)`
`[getElseFlow](#getElseFlow())()`
Gets condition "else" flow.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getIfCondition](#getIfCondition())()`
Gets "if" text of condition.
`[ControlFlow](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html)`
`[getIfFlow](#getIfFlow())()`
Gets condition "if" flow.
`[MergeNode](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/MergeNode.html)`
`[getMergeNode](#getMergeNode())()`
Gets condition merge node.
`[FlowStep](FlowStep.html)`
`[getParentFlowStep](#getParentFlowStep())()`
Gets flow step to which alternative condition belongs.
`void`
`[setIfCondition](#setIfCondition(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Sets "if" text of condition.
Methods inherited from interface com.nomagic.magicdraw.usecasescenarios.scenarios.[ScenarioNode](ScenarioNode.html)
`[belongsToIncludedExtending](ScenarioNode.html#belongsToIncludedExtending()), [getElement](ScenarioNode.html#getElement()), [getEnd](ScenarioNode.html#getEnd()), [getHumanType](ScenarioNode.html#getHumanType()), [getName](ScenarioNode.html#getName()), [getParent](ScenarioNode.html#getParent()), [getParentContainer](ScenarioNode.html#getParentContainer()), [getStart](ScenarioNode.html#getStart()), [isEditable](ScenarioNode.html#isEditable()), [setName](ScenarioNode.html#setName(java.lang.String))`

============ METHOD DETAIL ========== 
Method Details
getDecisionNode
[DecisionNode](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html) getDecisionNode()
Gets condition decision node.
Returns:
condition decision node.
getMergeNode
[MergeNode](../../../uml2/ext/magicdraw/activities/mdintermediateactivities/MergeNode.html) getMergeNode()
Gets condition merge node.
Returns:
condition merge node.
getAlternativeFlowSteps
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)> getAlternativeFlowSteps()
Gets condition alternative flow steps.
Returns:
alternative flow steps of condition.
getIfFlow
[ControlFlow](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html) getIfFlow()
Gets condition "if" flow.
Returns:
"if" flow of condition.
getElseFlow
[ControlFlow](../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html) getElseFlow()
Gets condition "else" flow.
Returns:
condition "else" flow.
getIfCondition
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getIfCondition()
Gets "if" text of condition.
Returns:
"if" text of condition.
setIfCondition
void setIfCondition([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Sets "if" text of condition.
Parameters:
`value` - "if" text of condition.
getParentFlowStep
[FlowStep](FlowStep.html) getParentFlowStep()
Gets flow step to which alternative condition belongs.
Returns:
flow step to which alternative condition belongs.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface AlternativeCondition">Interface AlternativeCondition</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AlternativeCondition</span><span class="extends-implements">
extends <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></span></div>
<div class="block">Represents alternative condition in the scenario flow.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAlternativeFlowSteps()">getAlternativeFlowSteps</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets condition alternative flow steps.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDecisionNode()">getDecisionNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets condition decision node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElseFlow()">getElseFlow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets condition "else" flow.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIfCondition()">getIfCondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets "if" text of condition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIfFlow()">getIfFlow</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets condition "if" flow.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMergeNode()">getMergeNode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets condition merge node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentFlowStep()">getParentFlowStep</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step to which alternative condition belongs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIfCondition(java.lang.String)">setIfCondition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets "if" text of condition.</div>
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
<section class="detail" id="getDecisionNode()">
<h3>getDecisionNode</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/DecisionNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">DecisionNode</a></span> <span class="element-name">getDecisionNode</span>()</div>
<div class="block">Gets condition decision node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>condition decision node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMergeNode()">
<h3>getMergeNode</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdintermediateactivities/MergeNode.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdintermediateactivities">MergeNode</a></span> <span class="element-name">getMergeNode</span>()</div>
<div class="block">Gets condition merge node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>condition merge node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAlternativeFlowSteps()">
<h3>getAlternativeFlowSteps</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getAlternativeFlowSteps</span>()</div>
<div class="block">Gets condition alternative flow steps.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>alternative flow steps of condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIfFlow()">
<h3>getIfFlow</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></span> <span class="element-name">getIfFlow</span>()</div>
<div class="block">Gets condition "if" flow.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>"if" flow of condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElseFlow()">
<h3>getElseFlow</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdbasicactivities/ControlFlow.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdbasicactivities">ControlFlow</a></span> <span class="element-name">getElseFlow</span>()</div>
<div class="block">Gets condition "else" flow.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>condition "else" flow.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIfCondition()">
<h3>getIfCondition</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIfCondition</span>()</div>
<div class="block">Gets "if" text of condition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>"if" text of condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIfCondition(java.lang.String)">
<h3>setIfCondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setIfCondition</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Sets "if" text of condition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - "if" text of condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentFlowStep()">
<h3>getParentFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">getParentFlowStep</span>()</div>
<div class="block">Gets flow step to which alternative condition belongs.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step to which alternative condition belongs.</dd>
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
