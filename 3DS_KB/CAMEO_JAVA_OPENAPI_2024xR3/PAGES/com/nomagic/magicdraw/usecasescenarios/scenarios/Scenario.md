# JAVA OPENAPI: Scenario (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/usecasescenarios/scenarios/Scenario.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/Scenario.html`
- source_sha256: `f38cd59a1efd05c10439bd56c1faa4efc3f0d818f3c3b97dbf57a03c50ccc1ee`
- captured_utc: `2026-07-14T16:56:07.934598+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface Scenario

All Superinterfaces:
`[ScenarioNode](ScenarioNode.html)`

@OpenApiAllpublic interfaceScenarioextends [ScenarioNode](ScenarioNode.html)

Represents a use case flow scenario.
Contains methods for manipulating it. Use [`ScenarioManager`](ScenarioManager.html) for scenario utility methods.

See Also:
[`ScenarioManager`](ScenarioManager.html)
[`ScenarioFactory`](ScenarioFactory.html)
[`AlternativeCondition`](AlternativeCondition.html)
[`ExceptionType`](ExceptionType.html)
[`FlowStep`](FlowStep.html)
[`ScenarioNode`](ScenarioNode.html)
[`ScenarioNodeEnd`](ScenarioNodeEnd.html)
[`ScenarioNodeStart`](ScenarioNodeStart.html)
[`ScenarioReadResult`](ScenarioReadResult.html)
[`ScenarioRepresentationTextProvider`](ScenarioRepresentationTextProvider.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SCENARIO_CHANGE_EVENT](#SCENARIO_CHANGE_EVENT)`
Event for indicating scenario change.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[AlternativeCondition](AlternativeCondition.html)`
`[addAlternativeCondition](#addAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([FlowStep](FlowStep.html) flowStep)`
Adds alternative condition to the flow step.
`[AlternativeCondition](AlternativeCondition.html)`
`[addAlternativeCondition](#addAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition))([FlowStep](FlowStep.html) flowStep,
 [AlternativeCondition](AlternativeCondition.html) addAfter)`
Adds alternative condition.
`[FlowStep](FlowStep.html)`
`[addAlternativeFlowStep](#addAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition))([AlternativeCondition](AlternativeCondition.html) alternativeCondition)`
Adds alternative flow step.
`[FlowStep](FlowStep.html)`
`[addAlternativeFlowStep](#addAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition,com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([AlternativeCondition](AlternativeCondition.html) alternativeCondition,
 [FlowStep](FlowStep.html) addAfter)`
Adds alternative flow step.
`[FlowStep](FlowStep.html)`
`[addExceptionalFlowStep](#addExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType))([ExceptionType](ExceptionType.html) exceptionType)`
Adds exceptional flow step.
`[FlowStep](FlowStep.html)`
`[addExceptionalFlowStep](#addExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType,com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([ExceptionType](ExceptionType.html) exceptionType,
 [FlowStep](FlowStep.html) addAfter)`
Adds exceptional flow step.
`[ExceptionType](ExceptionType.html)`
`[addExceptionType](#addExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([FlowStep](FlowStep.html) flowStep)`
Adds exception type.
`[ExceptionType](ExceptionType.html)`
`[addExceptionType](#addExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType))([FlowStep](FlowStep.html) flowStep,
 [ExceptionType](ExceptionType.html) exceptionType)`
Adds exception type.
`[FlowStep](FlowStep.html)`
`[addFlowStep](#addFlowStep())()`
Adds a flow step to the scenario.
`[FlowStep](FlowStep.html)`
`[addFlowStep](#addFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([FlowStep](FlowStep.html) addAfter)`
Adds a flow step after a given flow step.
`void`
`[addPropertyChangeListener](#addPropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Adds a property change listener to this scenario.
`[FlowStep](FlowStep.html)`
`[addUseCaseStep](#addUseCaseStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([FlowStep](FlowStep.html) addAfter,
 [UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Adds a flow step which references another use case.
`[FlowStep](FlowStep.html)`
`[addUseCaseStep](#addUseCaseStep(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Adds a flow step which references another use case.
`[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html)`
`[getActivity](#getActivity())()`
Gets activity in which use case is represented.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElements](#getElements())()`
Gets all elements which represent scenario.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)>`
`[getFlowSteps](#getFlowSteps())()`
Gets scenario flow steps.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html)>`
`[getReferencedScenarioUseCases](#getReferencedScenarioUseCases())()`
Gets scenario use cases which are referenced by this scenario.
`[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html)`
`[getScenarioDiagram](#getScenarioDiagram(boolean))(boolean createIfNotExists)`
Gets diagram which represents scenario.
`[ScenarioNodeStart](ScenarioNodeStart.html)`
`[getScenarioEnd](#getScenarioEnd())()`
Gets scenario node which ends scenario.
`[ScenarioReadResult](ScenarioReadResult.html)`
`[getScenarioReadResult](#getScenarioReadResult())()`
Gets errors of the last scenario reading.
`[ScenarioRepresentationTextProvider](ScenarioRepresentationTextProvider.html)`
`[getScenarioRepresentationTextProvider](#getScenarioRepresentationTextProvider())()`
Gets scenario GUI text provider.
`[ScenarioNodeStart](ScenarioNodeStart.html)`
`[getScenarioStart](#getScenarioStart())()`
Gets scenario node which starts scenario.
`[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html)`
`[getUseCase](#getUseCase())()`
Gets use case which represents scenario.
`boolean`
`[isEditable](#isEditable())()`
Indicates if permissions allow to edit scenario.
`void`
`[prepareModelBeforeDisplay](#prepareModelBeforeDisplay())()`
Performs necessary model preparations before displaying the scenario.
`void`
`[readScenario](#readScenario())()`
Reads scenario from the current scenario use case.
`void`
`[readScenario](#readScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Reads scenario from a given use case.
`void`
`[removeAlternativeCondition](#removeAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition))([AlternativeCondition](AlternativeCondition.html) condition)`
Removes alternative condition.
`void`
`[removeAlternativeFlowStep](#removeAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([FlowStep](FlowStep.html) alternativeFlowStep)`
Removes alternative flow step.
`void`
`[removeExceptionalFlowStep](#removeExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([FlowStep](FlowStep.html) exceptionalFlowStep)`
Removes exceptional flow step.
`void`
`[removeExceptionType](#removeExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType))([FlowStep](FlowStep.html) flowStep,
 [ExceptionType](ExceptionType.html) exceptionType)`
Removes exception type.
`void`
`[removeFlowStep](#removeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep))([FlowStep](FlowStep.html) flowStep)`
Removes flow step.
`void`
`[removePropertyChangeListener](#removePropertyChangeListener(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Removes listener from scenario listeners.
`void`
`[swapScenarioNodes](#swapScenarioNodes(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode,com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode))([ScenarioNode](ScenarioNode.html) node1,
 [ScenarioNode](ScenarioNode.html) node2)`
Swaps scenario nodes.
Methods inherited from interface com.nomagic.magicdraw.usecasescenarios.scenarios.[ScenarioNode](ScenarioNode.html)
`[belongsToIncludedExtending](ScenarioNode.html#belongsToIncludedExtending()), [getElement](ScenarioNode.html#getElement()), [getEnd](ScenarioNode.html#getEnd()), [getHumanType](ScenarioNode.html#getHumanType()), [getName](ScenarioNode.html#getName()), [getParent](ScenarioNode.html#getParent()), [getParentContainer](ScenarioNode.html#getParentContainer()), [getStart](ScenarioNode.html#getStart()), [setName](ScenarioNode.html#setName(java.lang.String))`

============ FIELD DETAIL =========== 
Field Details
SCENARIO_CHANGE_EVENT
static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SCENARIO_CHANGE_EVENT
Event for indicating scenario change.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.usecasescenarios.scenarios.Scenario.SCENARIO_CHANGE_EVENT)
 ============ METHOD DETAIL ========== 
Method Details
addFlowStep
[FlowStep](FlowStep.html) addFlowStep()
Adds a flow step to the scenario.
Returns:
added scenario.
addFlowStep
[FlowStep](FlowStep.html) addFlowStep([FlowStep](FlowStep.html) addAfter)
Adds a flow step after a given flow step.
Parameters:
`addAfter` - flow step after which to add a flow step.
Returns:
added flow step.
addUseCaseStep
[FlowStep](FlowStep.html) addUseCaseStep([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Adds a flow step which references another use case.
Parameters:
`useCase` - use case to add.
Returns:
created flow step.
addUseCaseStep
[FlowStep](FlowStep.html) addUseCaseStep([FlowStep](FlowStep.html) addAfter,
 [UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Adds a flow step which references another use case.
Parameters:
`addAfter` - flow step after which to add.
`useCase` - use case to add.
Returns:
added step
addExceptionType
[ExceptionType](ExceptionType.html) addExceptionType([FlowStep](FlowStep.html) flowStep)
Adds exception type.
Parameters:
`flowStep` - flow set to which exception type should be added.
Returns:
added exception type.
addExceptionType
[ExceptionType](ExceptionType.html) addExceptionType([FlowStep](FlowStep.html) flowStep,
 [ExceptionType](ExceptionType.html) exceptionType)
Adds exception type.
Parameters:
`flowStep` - flow step to which to add.
`exceptionType` - exception type to add.
Returns:
added exception type.
addExceptionalFlowStep
[FlowStep](FlowStep.html) addExceptionalFlowStep([ExceptionType](ExceptionType.html) exceptionType,
 [FlowStep](FlowStep.html) addAfter)
Adds exceptional flow step.
Parameters:
`exceptionType` - exception type to which step should be added.
`addAfter` - flow step after which to add.
Returns:
added exceptional flow step.
addExceptionalFlowStep
[FlowStep](FlowStep.html) addExceptionalFlowStep([ExceptionType](ExceptionType.html) exceptionType)
Adds exceptional flow step.
Parameters:
`exceptionType` - exception type to which to add exceptional flow step.
Returns:
added exceptional flow step.
removeFlowStep
void removeFlowStep([FlowStep](FlowStep.html) flowStep)
Removes flow step.
Parameters:
`flowStep` - flow step to remove.
swapScenarioNodes
void swapScenarioNodes([ScenarioNode](ScenarioNode.html) node1,
 [ScenarioNode](ScenarioNode.html) node2)
Swaps scenario nodes.
Parameters:
`node1` - first node to swap.
`node2` - second node to swap.
getFlowSteps
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FlowStep](FlowStep.html)> getFlowSteps()
Gets scenario flow steps.
Returns:
scenario flow steps.
addAlternativeCondition
[AlternativeCondition](AlternativeCondition.html) addAlternativeCondition([FlowStep](FlowStep.html) flowStep)
Adds alternative condition to the flow step.
Parameters:
`flowStep` - flow step to which to add alternative condition.
Returns:
created alternative condition.
removeAlternativeCondition
void removeAlternativeCondition([AlternativeCondition](AlternativeCondition.html) condition)
Removes alternative condition.
Parameters:
`condition` - alternative condition to remove.
removeExceptionType
void removeExceptionType([FlowStep](FlowStep.html) flowStep,
 [ExceptionType](ExceptionType.html) exceptionType)
Removes exception type.
Parameters:
`flowStep` - flow step from which to remove exception type.
`exceptionType` - exception type to remove.
removeExceptionalFlowStep
void removeExceptionalFlowStep([FlowStep](FlowStep.html) exceptionalFlowStep)
Removes exceptional flow step.
Parameters:
`exceptionalFlowStep` - exceptional flow step to remove.
removeAlternativeFlowStep
void removeAlternativeFlowStep([FlowStep](FlowStep.html) alternativeFlowStep)
Removes alternative flow step.
Parameters:
`alternativeFlowStep` - alternative flow step to remove.
addAlternativeCondition
[AlternativeCondition](AlternativeCondition.html) addAlternativeCondition([FlowStep](FlowStep.html) flowStep,
 [AlternativeCondition](AlternativeCondition.html) addAfter)
Adds alternative condition.
Parameters:
`flowStep` - flow step to which to add alternative condition.
`addAfter` - condition after which to add.
Returns:
created alternative condition.
addAlternativeFlowStep
[FlowStep](FlowStep.html) addAlternativeFlowStep([AlternativeCondition](AlternativeCondition.html) alternativeCondition)
Adds alternative flow step.
Parameters:
`alternativeCondition` - condition to which to add.
Returns:
created flow step.
addAlternativeFlowStep
[FlowStep](FlowStep.html) addAlternativeFlowStep([AlternativeCondition](AlternativeCondition.html) alternativeCondition,
 [FlowStep](FlowStep.html) addAfter)
Adds alternative flow step.
Parameters:
`alternativeCondition` - condition to which to add.
`addAfter` - flow step after which to add.
Returns:
added alternative flow step.
getActivity
[Activity](../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html) getActivity()
Gets activity in which use case is represented.
Returns:
activity in which steps are represented.
getUseCase
[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) getUseCase()
Gets use case which represents scenario.
Returns:
use case which represents scenario.
getElements
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElements()
Gets all elements which represent scenario.
Returns:
all elements which represent scenario.
getScenarioDiagram
[Diagram](../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) getScenarioDiagram(boolean createIfNotExists)
Gets diagram which represents scenario.
Parameters:
`createIfNotExists` - flag which forces diagram creation.
Returns:
gets diagram which represents scenario or null if it did not exist or was not created.
readScenario
void readScenario([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Reads scenario from a given use case.
Parameters:
`useCase` - use case from which to read.
readScenario
void readScenario()
Reads scenario from the current scenario use case.
addPropertyChangeListener
void addPropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Adds a property change listener to this scenario.
 Listeners are notified about changes in the scenario.
Parameters:
`listener` - listener to add.
removePropertyChangeListener
void removePropertyChangeListener([PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Removes listener from scenario listeners.
Parameters:
`listener` - listener to remove.
getScenarioStart
[ScenarioNodeStart](ScenarioNodeStart.html) getScenarioStart()
Gets scenario node which starts scenario.
Returns:
scenario node which starts scenario.
getScenarioEnd
[ScenarioNodeStart](ScenarioNodeStart.html) getScenarioEnd()
Gets scenario node which ends scenario.
Returns:
scenario node which ends scenario.
isEditable
boolean isEditable()
Indicates if permissions allow to edit scenario.
Specified by:
`[isEditable](ScenarioNode.html#isEditable())` in interface `[ScenarioNode](ScenarioNode.html)`
Returns:
true if scenario is editable, false otherwise.
getScenarioReadResult
[ScenarioReadResult](ScenarioReadResult.html) getScenarioReadResult()
Gets errors of the last scenario reading.
Returns:
scenario read result.
getReferencedScenarioUseCases
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html)> getReferencedScenarioUseCases()
Gets scenario use cases which are referenced by this scenario.
Returns:
scenario use cases which are referenced by this scenario.
prepareModelBeforeDisplay
void prepareModelBeforeDisplay()
Performs necessary model preparations before displaying the scenario.
getScenarioRepresentationTextProvider
[ScenarioRepresentationTextProvider](ScenarioRepresentationTextProvider.html) getScenarioRepresentationTextProvider()
Gets scenario GUI text provider.
Returns:
scenario GUI text provider.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface Scenario">Interface Scenario</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Scenario</span><span class="extends-implements">
extends <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></span></div>
<div class="block"><p>Represents a use case flow scenario.<p></p>
<p>Contains methods for manipulating it. Use <a href="ScenarioManager.html" title="class in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioManager</code></a> for scenario utility methods.<p></p></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="ScenarioManager.html" title="class in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioManager</code></a></li>
<li><a href="ScenarioFactory.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioFactory</code></a></li>
<li><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>AlternativeCondition</code></a></li>
<li><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ExceptionType</code></a></li>
<li><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>FlowStep</code></a></li>
<li><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioNode</code></a></li>
<li><a href="ScenarioNodeEnd.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioNodeEnd</code></a></li>
<li><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioNodeStart</code></a></li>
<li><a href="ScenarioReadResult.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioReadResult</code></a></li>
<li><a href="ScenarioRepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioRepresentationTextProvider</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SCENARIO_CHANGE_EVENT">SCENARIO_CHANGE_EVENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Event for indicating scenario change.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">addAlternativeCondition</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds alternative condition to the flow step.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition)">addAlternativeCondition</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep,
 <a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> addAfter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds alternative condition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition)">addAlternativeFlowStep</a><wbr/>(<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> alternativeCondition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds alternative flow step.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition,com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">addAlternativeFlowStep</a><wbr/>(<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> alternativeCondition,
 <a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds alternative flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType)">addExceptionalFlowStep</a><wbr/>(<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds exceptional flow step.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType,com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">addExceptionalFlowStep</a><wbr/>(<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType,
 <a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds exceptional flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">addExceptionType</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds exception type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType)">addExceptionType</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep,
 <a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds exception type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addFlowStep()">addFlowStep</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a flow step to the scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">addFlowStep</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a flow step after a given flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addPropertyChangeListener(java.beans.PropertyChangeListener)">addPropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a property change listener to this scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addUseCaseStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">addUseCaseStep</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter,
 <a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a flow step which references another use case.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addUseCaseStep(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">addUseCaseStep</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds a flow step which references another use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getActivity()">getActivity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets activity in which use case is represented.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElements()">getElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets all elements which represent scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFlowSteps()">getFlowSteps</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario flow steps.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getReferencedScenarioUseCases()">getReferencedScenarioUseCases</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario use cases which are referenced by this scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScenarioDiagram(boolean)">getScenarioDiagram</a><wbr/>(boolean createIfNotExists)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets diagram which represents scenario.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScenarioEnd()">getScenarioEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario node which ends scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioReadResult.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioReadResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScenarioReadResult()">getScenarioReadResult</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets errors of the last scenario reading.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioRepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioRepresentationTextProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScenarioRepresentationTextProvider()">getScenarioRepresentationTextProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario GUI text provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getScenarioStart()">getScenarioStart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario node which starts scenario.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUseCase()">getUseCase</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets use case which represents scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if permissions allow to edit scenario.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#prepareModelBeforeDisplay()">prepareModelBeforeDisplay</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs necessary model preparations before displaying the scenario.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#readScenario()">readScenario</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reads scenario from the current scenario use case.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#readScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">readScenario</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Reads scenario from a given use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition)">removeAlternativeCondition</a><wbr/>(<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> condition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes alternative condition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">removeAlternativeFlowStep</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> alternativeFlowStep)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes alternative flow step.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">removeExceptionalFlowStep</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> exceptionalFlowStep)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes exceptional flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType)">removeExceptionType</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep,
 <a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes exception type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">removeFlowStep</a><wbr/>(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes flow step.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removePropertyChangeListener(java.beans.PropertyChangeListener)">removePropertyChangeListener</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes listener from scenario listeners.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#swapScenarioNodes(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode,com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode)">swapScenarioNodes</a><wbr/>(<a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a> node1,
 <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a> node2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Swaps scenario nodes.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode">Methods inherited from interface com.nomagic.magicdraw.usecasescenarios.scenarios.<a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></h3>
<code><a href="ScenarioNode.html#belongsToIncludedExtending()">belongsToIncludedExtending</a>, <a href="ScenarioNode.html#getElement()">getElement</a>, <a href="ScenarioNode.html#getEnd()">getEnd</a>, <a href="ScenarioNode.html#getHumanType()">getHumanType</a>, <a href="ScenarioNode.html#getName()">getName</a>, <a href="ScenarioNode.html#getParent()">getParent</a>, <a href="ScenarioNode.html#getParentContainer()">getParentContainer</a>, <a href="ScenarioNode.html#getStart()">getStart</a>, <a href="ScenarioNode.html#setName(java.lang.String)">setName</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="SCENARIO_CHANGE_EVENT">
<h3>SCENARIO_CHANGE_EVENT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SCENARIO_CHANGE_EVENT</span></div>
<div class="block">Event for indicating scenario change.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.usecasescenarios.scenarios.Scenario.SCENARIO_CHANGE_EVENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="addFlowStep()">
<h3>addFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addFlowStep</span>()</div>
<div class="block">Adds a flow step to the scenario.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>added scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>addFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addFlowStep</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter)</span></div>
<div class="block">Adds a flow step after a given flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addAfter</code> - flow step after which to add a flow step.</dd>
<dt>Returns:</dt>
<dd>added flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addUseCaseStep(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>addUseCaseStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addUseCaseStep</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Adds a flow step which references another use case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - use case to add.</dd>
<dt>Returns:</dt>
<dd>created flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addUseCaseStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>addUseCaseStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addUseCaseStep</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter,
 <a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Adds a flow step which references another use case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addAfter</code> - flow step after which to add.</dd>
<dd><code>useCase</code> - use case to add.</dd>
<dt>Returns:</dt>
<dd>added step</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>addExceptionType</h3>
<div class="member-signature"><span class="return-type"><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></span> <span class="element-name">addExceptionType</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep)</span></div>
<div class="block">Adds exception type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flowStep</code> - flow set to which exception type should be added.</dd>
<dt>Returns:</dt>
<dd>added exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType)">
<h3>addExceptionType</h3>
<div class="member-signature"><span class="return-type"><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></span> <span class="element-name">addExceptionType</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep,
 <a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType)</span></div>
<div class="block">Adds exception type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flowStep</code> - flow step to which to add.</dd>
<dd><code>exceptionType</code> - exception type to add.</dd>
<dt>Returns:</dt>
<dd>added exception type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType,com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>addExceptionalFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addExceptionalFlowStep</span><wbr/><span class="parameters">(<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType,
 <a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter)</span></div>
<div class="block">Adds exceptional flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exceptionType</code> - exception type to which step should be added.</dd>
<dd><code>addAfter</code> - flow step after which to add.</dd>
<dt>Returns:</dt>
<dd>added exceptional flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType)">
<h3>addExceptionalFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addExceptionalFlowStep</span><wbr/><span class="parameters">(<a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType)</span></div>
<div class="block">Adds exceptional flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exceptionType</code> - exception type to which to add exceptional flow step.</dd>
<dt>Returns:</dt>
<dd>added exceptional flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>removeFlowStep</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeFlowStep</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep)</span></div>
<div class="block">Removes flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flowStep</code> - flow step to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="swapScenarioNodes(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode,com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioNode)">
<h3>swapScenarioNodes</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">swapScenarioNodes</span><wbr/><span class="parameters">(<a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a> node1,
 <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a> node2)</span></div>
<div class="block">Swaps scenario nodes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node1</code> - first node to swap.</dd>
<dd><code>node2</code> - second node to swap.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFlowSteps()">
<h3>getFlowSteps</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a>&gt;</span> <span class="element-name">getFlowSteps</span>()</div>
<div class="block">Gets scenario flow steps.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario flow steps.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>addAlternativeCondition</h3>
<div class="member-signature"><span class="return-type"><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></span> <span class="element-name">addAlternativeCondition</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep)</span></div>
<div class="block">Adds alternative condition to the flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flowStep</code> - flow step to which to add alternative condition.</dd>
<dt>Returns:</dt>
<dd>created alternative condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition)">
<h3>removeAlternativeCondition</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeAlternativeCondition</span><wbr/><span class="parameters">(<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> condition)</span></div>
<div class="block">Removes alternative condition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>condition</code> - alternative condition to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExceptionType(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.ExceptionType)">
<h3>removeExceptionType</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeExceptionType</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep,
 <a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a> exceptionType)</span></div>
<div class="block">Removes exception type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flowStep</code> - flow step from which to remove exception type.</dd>
<dd><code>exceptionType</code> - exception type to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExceptionalFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>removeExceptionalFlowStep</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeExceptionalFlowStep</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> exceptionalFlowStep)</span></div>
<div class="block">Removes exceptional flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>exceptionalFlowStep</code> - exceptional flow step to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>removeAlternativeFlowStep</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeAlternativeFlowStep</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> alternativeFlowStep)</span></div>
<div class="block">Removes alternative flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>alternativeFlowStep</code> - alternative flow step to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAlternativeCondition(com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep,com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition)">
<h3>addAlternativeCondition</h3>
<div class="member-signature"><span class="return-type"><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></span> <span class="element-name">addAlternativeCondition</span><wbr/><span class="parameters">(<a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> flowStep,
 <a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> addAfter)</span></div>
<div class="block">Adds alternative condition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flowStep</code> - flow step to which to add alternative condition.</dd>
<dd><code>addAfter</code> - condition after which to add.</dd>
<dt>Returns:</dt>
<dd>created alternative condition.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition)">
<h3>addAlternativeFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addAlternativeFlowStep</span><wbr/><span class="parameters">(<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> alternativeCondition)</span></div>
<div class="block">Adds alternative flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>alternativeCondition</code> - condition to which to  add.</dd>
<dt>Returns:</dt>
<dd>created flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAlternativeFlowStep(com.nomagic.magicdraw.usecasescenarios.scenarios.AlternativeCondition,com.nomagic.magicdraw.usecasescenarios.scenarios.FlowStep)">
<h3>addAlternativeFlowStep</h3>
<div class="member-signature"><span class="return-type"><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></span> <span class="element-name">addAlternativeFlowStep</span><wbr/><span class="parameters">(<a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a> alternativeCondition,
 <a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a> addAfter)</span></div>
<div class="block">Adds alternative flow step.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>alternativeCondition</code> - condition to which to add.</dd>
<dd><code>addAfter</code> - flow step after which to add.</dd>
<dt>Returns:</dt>
<dd>added alternative flow step.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActivity()">
<h3>getActivity</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/activities/mdfundamentalactivities/Activity.html" title="interface in com.nomagic.uml2.ext.magicdraw.activities.mdfundamentalactivities">Activity</a></span> <span class="element-name">getActivity</span>()</div>
<div class="block">Gets activity in which use case is represented.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>activity in which steps are represented.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUseCase()">
<h3>getUseCase</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a></span> <span class="element-name">getUseCase</span>()</div>
<div class="block">Gets use case which represents scenario.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>use case which represents scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElements()">
<h3>getElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElements</span>()</div>
<div class="block">Gets all elements which represent scenario.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all elements which represent scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScenarioDiagram(boolean)">
<h3>getScenarioDiagram</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a></span> <span class="element-name">getScenarioDiagram</span><wbr/><span class="parameters">(boolean createIfNotExists)</span></div>
<div class="block">Gets diagram which represents scenario.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>createIfNotExists</code> - flag which forces diagram creation.</dd>
<dt>Returns:</dt>
<dd>gets diagram which represents scenario or null if it did not exist or was not created.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>readScenario</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">readScenario</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Reads scenario from a given use case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - use case from which to read.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="readScenario()">
<h3>readScenario</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">readScenario</span>()</div>
<div class="block">Reads scenario from the current scenario use case.</div>
</section>
</li>
<li>
<section class="detail" id="addPropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>addPropertyChangeListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addPropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Adds a property change listener to this scenario.
 Listeners are notified about changes in the scenario.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removePropertyChangeListener(java.beans.PropertyChangeListener)">
<h3>removePropertyChangeListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removePropertyChangeListener</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="block">Removes listener from scenario listeners.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScenarioStart()">
<h3>getScenarioStart</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></span> <span class="element-name">getScenarioStart</span>()</div>
<div class="block">Gets scenario node which starts scenario.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario node which starts scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScenarioEnd()">
<h3>getScenarioEnd</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></span> <span class="element-name">getScenarioEnd</span>()</div>
<div class="block">Gets scenario node which ends scenario.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario node which ends scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block">Indicates if permissions allow to edit scenario.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ScenarioNode.html#isEditable()">isEditable</a></code> in interface <code><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></code></dd>
<dt>Returns:</dt>
<dd>true if scenario is editable, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScenarioReadResult()">
<h3>getScenarioReadResult</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioReadResult.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioReadResult</a></span> <span class="element-name">getScenarioReadResult</span>()</div>
<div class="block">Gets errors of the last scenario reading.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario read result.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferencedScenarioUseCases()">
<h3>getReferencedScenarioUseCases</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a>&gt;</span> <span class="element-name">getReferencedScenarioUseCases</span>()</div>
<div class="block">Gets scenario use cases which are referenced by this scenario.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario use cases which are referenced by this scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareModelBeforeDisplay()">
<h3>prepareModelBeforeDisplay</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">prepareModelBeforeDisplay</span>()</div>
<div class="block">Performs necessary model preparations before displaying the scenario.</div>
</section>
</li>
<li>
<section class="detail" id="getScenarioRepresentationTextProvider()">
<h3>getScenarioRepresentationTextProvider</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioRepresentationTextProvider.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioRepresentationTextProvider</a></span> <span class="element-name">getScenarioRepresentationTextProvider</span>()</div>
<div class="block">Gets scenario GUI text provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario GUI text provider.</dd>
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
