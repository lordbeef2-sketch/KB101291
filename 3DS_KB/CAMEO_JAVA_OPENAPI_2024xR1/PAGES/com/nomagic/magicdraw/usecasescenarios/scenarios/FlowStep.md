# JAVA OPENAPI: FlowStep (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/usecasescenarios/scenarios/FlowStep.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/FlowStep.html`
- source_sha256: `6102068d99ce7e62feb1caa8b38b9984ffffbe88f804467d60a1f4d7775dab73`
- captured_utc: `2026-07-14T16:52:18.923970+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface FlowStep

All Superinterfaces:
`[ScenarioNode](ScenarioNode.html)`

@OpenApiAllpublic interfaceFlowStepextends [ScenarioNode](ScenarioNode.html)

Represents use case scenario flow step.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[belongsToExtending](#belongsToExtending())()`
Indicates if this step belongs to extending.
`boolean`
`[belongsToIncluded](#belongsToIncluded())()`
Indicates if this step belongs to included.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[AlternativeCondition](AlternativeCondition.html)>`
`[getAlternativeConditions](#getAlternativeConditions())()`
Gets flow step alternative conditions.
`[CallBehaviorAction](../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html)`
`[getCallBehaviorAction](#getCallBehaviorAction())()`
Gets call behavior action which represents this step.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExceptionType](ExceptionType.html)>`
`[getExceptionTypes](#getExceptionTypes())()`
Gets flow step exception types.
`[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html)`
`[getExtendingActivity](#getExtendingActivity())()`
Gets flow step extending activity.
`[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html)`
`[getExtendingUseCase](#getExtendingUseCase())()`
Gets flow step extending use case.
`[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html)`
`[getIncludedActivity](#getIncludedActivity())()`
Gets flow step included activity.
`[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html)`
`[getIncludedExtendingActivity](#getIncludedExtendingActivity(boolean))(boolean included)`
Gets flow step included/extending activity.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)>`
`[getIncludedExtendingFlowSteps](#getIncludedExtendingFlowSteps())()`
Gets included/extending flows steps of this flow step.
`[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html)`
`[getIncludedUseCase](#getIncludedUseCase())()`
Gets flow step included use case.
`[AlternativeCondition](AlternativeCondition.html)`
`[getParentAlternativeCondition](#getParentAlternativeCondition())()`
Gets parent alternative condition.
`[ExceptionType](ExceptionType.html)`
`[getParentExceptionType](#getParentExceptionType())()`
Gets parent exception type.
`[FlowStep](FlowStep.html)`
`[getParentFlowStep](#getParentFlowStep())()`
Gets parent flow step.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExceptionType](ExceptionType.html)>`
`[getSortedExceptionTypes](#getSortedExceptionTypes())()`
Gets sorted flow step exception types.
`boolean`
`[isAlternativeStep](#isAlternativeStep())()`
Indicates if this step is alternative flow step.
`boolean`
`[isExceptionalStep](#isExceptionalStep())()`
Indicates if this step is exceptional flow step.
`boolean`
`[isExtending](#isExtending())()`
Indicates if this step is extending.
`boolean`
`[isIncluded](#isIncluded())()`
Indicates if this step is included.
`boolean`
`[isIncludedExtending](#isIncludedExtending())()`
Indicates if this step is included/extending.
Methods inherited from interface com.nomagic.magicdraw.usecasescenarios.scenarios.[ScenarioNode](ScenarioNode.html)
`[belongsToIncludedExtending](ScenarioNode.html#belongsToIncludedExtending()), [getElement](ScenarioNode.html#getElement()), [getEnd](ScenarioNode.html#getEnd()), [getHumanType](ScenarioNode.html#getHumanType()), [getName](ScenarioNode.html#getName()), [getParent](ScenarioNode.html#getParent()), [getParentContainer](ScenarioNode.html#getParentContainer()), [getStart](ScenarioNode.html#getStart()), [isEditable](ScenarioNode.html#isEditable()), [setName](ScenarioNode.html#setName(java.lang.String))`

============ METHOD DETAIL ========== 
Method Details
getAlternativeConditions
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[AlternativeCondition](AlternativeCondition.html)> getAlternativeConditions()
Gets flow step alternative conditions.
Returns:
flow step alternative conditions.
isExceptionalStep
boolean isExceptionalStep()
Indicates if this step is exceptional flow step.
Returns:
true if this step is exceptional flow step, false otherwise.
isAlternativeStep
boolean isAlternativeStep()
Indicates if this step is alternative flow step.
Returns:
true if this step is alternative flow step, false otherwise.
getParentAlternativeCondition
[AlternativeCondition](AlternativeCondition.html) getParentAlternativeCondition()
Gets parent alternative condition.
Returns:
parent alternative condition.
getParentExceptionType
[ExceptionType](ExceptionType.html) getParentExceptionType()
Gets parent exception type.
Returns:
parent exception type.
getParentFlowStep
[FlowStep](FlowStep.html) getParentFlowStep()
Gets parent flow step.
Returns:
parent flow step.
getExceptionTypes
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExceptionType](ExceptionType.html)> getExceptionTypes()
Gets flow step exception types.
Returns:
flow step exception types.
getIncludedExtendingFlowSteps
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)> getIncludedExtendingFlowSteps()
Gets included/extending flows steps of this flow step.
Returns:
included/extending flows steps of this flow step.
isIncludedExtending
boolean isIncludedExtending()
Indicates if this step is included/extending.
Returns:
true if this step is included/extending, false otherwise.
belongsToIncluded
boolean belongsToIncluded()
Indicates if this step belongs to included.
Returns:
true if this step belongs to included, false otherwise.
belongsToExtending
boolean belongsToExtending()
Indicates if this step belongs to extending.
Returns:
true if this step belongs to extending, false otherwise.
isIncluded
boolean isIncluded()
Indicates if this step is included.
Returns:
true if this step is included, false otherwise.
isExtending
boolean isExtending()
Indicates if this step is extending.
Returns:
true if this step is extending, false otherwise.
getIncludedActivity
[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html) getIncludedActivity()
Gets flow step included activity.
Returns:
flow step included activity.
getIncludedUseCase
[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) getIncludedUseCase()
Gets flow step included use case.
Returns:
flow step included use case.
getExtendingUseCase
[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) getExtendingUseCase()
Gets flow step extending use case.
Returns:
flow step extending use case.
getExtendingActivity
[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html) getExtendingActivity()
Gets flow step extending activity.
Returns:
flow step extending activity.
getIncludedExtendingActivity
[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html) getIncludedExtendingActivity(boolean included)
Gets flow step included/extending activity.
Parameters:
`included` - true if included, false if extending.
Returns:
flow step included/extending activity if found, null otherwise.
getSortedExceptionTypes
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[ExceptionType](ExceptionType.html)> getSortedExceptionTypes()
Gets sorted flow step exception types.
Returns:
sorted flow step exception types.
getCallBehaviorAction
[CallBehaviorAction](../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html) getCallBehaviorAction()
Gets call behavior action which represents this step.
Returns:
call behavior action which represents this step.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface FlowStep">Interface FlowStep</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">FlowStep</span><span class="extends-implements">
extends <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></span></div>
<div class="block">Represents use case scenario flow step.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#belongsToExtending()">belongsToExtending</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step belongs to extending.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#belongsToIncluded()">belongsToIncluded</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step belongs to included.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAlternativeConditions()">getAlternativeConditions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step alternative conditions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCallBehaviorAction()">getCallBehaviorAction</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets call behavior action which represents this step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExceptionTypes()">getExceptionTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step exception types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtendingActivity()">getExtendingActivity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step extending activity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtendingUseCase()">getExtendingUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step extending use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIncludedActivity()">getIncludedActivity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step included activity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIncludedExtendingActivity(boolean)">getIncludedExtendingActivity</a><wbr/>(boolean included)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step included/extending activity.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIncludedExtendingFlowSteps()">getIncludedExtendingFlowSteps</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets included/extending flows steps of this flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIncludedUseCase()">getIncludedUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets flow step included use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentAlternativeCondition()">getParentAlternativeCondition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets parent alternative condition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentExceptionType()">getParentExceptionType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets parent exception type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentFlowStep()">getParentFlowStep</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets parent flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSortedExceptionTypes()">getSortedExceptionTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets sorted flow step exception types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isAlternativeStep()">isAlternativeStep</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step is alternative flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isExceptionalStep()">isExceptionalStep</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step is exceptional flow step.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isExtending()">isExtending</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step is extending.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isIncluded()">isIncluded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step is included.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isIncludedExtending()">isIncludedExtending</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if this step is included/extending.</div>
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
<section class="detail" id="getAlternativeConditions()">
<h3>getAlternativeConditions</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a>&gt;</span> <span class="element-name">getAlternativeConditions</span>()</div>
<div class="block">Gets flow step alternative conditions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step alternative conditions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExceptionalStep()">
<h3>isExceptionalStep</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isExceptionalStep</span>()</div>
<div class="block">Indicates if this step is exceptional flow step.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step is exceptional flow step, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAlternativeStep()">
<h3>isAlternativeStep</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isAlternativeStep</span>()</div>
<div class="block">Indicates if this step is alternative flow step.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step is alternative flow step, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentAlternativeCondition()">
<h3>getParentAlternativeCondition</h3>
<div class="member-signature"><span class="return-type"><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></span> <span class="element-name">getParentAlternativeCondition</span>()</div>
<div class="block">Gets parent alternative condition.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent alternative condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentExceptionType()">
<h3>getParentExceptionType</h3>
<div class="member-signature"><span class="return-type"><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></span> <span class="element-name">getParentExceptionType</span>()</div>
<div class="block">Gets parent exception type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentFlowStep()">
<h3>getParentFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">getParentFlowStep</span>()</div>
<div class="block">Gets parent flow step.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExceptionTypes()">
<h3>getExceptionTypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a>&gt;</span> <span class="element-name">getExceptionTypes</span>()</div>
<div class="block">Gets flow step exception types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step exception types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludedExtendingFlowSteps()">
<h3>getIncludedExtendingFlowSteps</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getIncludedExtendingFlowSteps</span>()</div>
<div class="block">Gets included/extending flows steps of this flow step.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>included/extending flows steps of this flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIncludedExtending()">
<h3>isIncludedExtending</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isIncludedExtending</span>()</div>
<div class="block">Indicates if this step is included/extending.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step is included/extending, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="belongsToIncluded()">
<h3>belongsToIncluded</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">belongsToIncluded</span>()</div>
<div class="block">Indicates if this step belongs to included.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step belongs to included, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="belongsToExtending()">
<h3>belongsToExtending</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">belongsToExtending</span>()</div>
<div class="block">Indicates if this step belongs to extending.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step belongs to extending, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isIncluded()">
<h3>isIncluded</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isIncluded</span>()</div>
<div class="block">Indicates if this step is included.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step is included, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExtending()">
<h3>isExtending</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isExtending</span>()</div>
<div class="block">Indicates if this step is extending.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if this step is extending, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludedActivity()">
<h3>getIncludedActivity</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">getIncludedActivity</span>()</div>
<div class="block">Gets flow step included activity.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step included activity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludedUseCase()">
<h3>getIncludedUseCase</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></span> <span class="element-name">getIncludedUseCase</span>()</div>
<div class="block">Gets flow step included use case.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step included use case.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtendingUseCase()">
<h3>getExtendingUseCase</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></span> <span class="element-name">getExtendingUseCase</span>()</div>
<div class="block">Gets flow step extending use case.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step extending use case.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtendingActivity()">
<h3>getExtendingActivity</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">getExtendingActivity</span>()</div>
<div class="block">Gets flow step extending activity.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>flow step extending activity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIncludedExtendingActivity(boolean)">
<h3>getIncludedExtendingActivity</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">getIncludedExtendingActivity</span><wbr/><span class="parameters">(boolean included)</span></div>
<div class="block">Gets flow step included/extending activity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>included</code> - true if included, false if extending.</dd>
<dt>Returns:</dt>
<dd>flow step included/extending activity if found, null otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSortedExceptionTypes()">
<h3>getSortedExceptionTypes</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a>&gt;</span> <span class="element-name">getSortedExceptionTypes</span>()</div>
<div class="block">Gets sorted flow step exception types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>sorted flow step exception types.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCallBehaviorAction()">
<h3>getCallBehaviorAction</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/actions/mdbasicactions/CallBehaviorAction.html" title="interface in com.nomagic.uml2.ext.magicdraw.actions.mdbasicactions">CallBehaviorAction</a></span> <span class="element-name">getCallBehaviorAction</span>()</div>
<div class="block">Gets call behavior action which represents this step.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>call behavior action which represents this step.</dd>
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
