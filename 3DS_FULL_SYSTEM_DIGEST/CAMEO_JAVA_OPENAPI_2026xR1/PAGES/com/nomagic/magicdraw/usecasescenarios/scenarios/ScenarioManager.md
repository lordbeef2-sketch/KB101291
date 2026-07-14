# JAVA OPENAPI: ScenarioManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioManager.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioManager.html`
- source_sha256: `5a9f80d32d733fb6e963a59f7a80c90998b1d8ea2463cb3b6616a0afc0fccbc3`
- captured_utc: `2026-07-14T16:46:10.506941+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Class ScenarioManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioManager

@OpenApiAllpublic classScenarioManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Scenario can be manipulated from Open API.
 The [`Scenario`](Scenario.html) class represents a use case scenario. It contains methods for manipulating it.
The [`ScenarioManager`](ScenarioManager.html) class contains utility methods for creating and manipulating scenarios.
The scenario management calls should be wrapped with the session management calls.
 See an example of how to create the use case scenario with the basic, alternative, and exceptional flows.
 Scenario can be opened in a diagram.

````java
// Scenario manipulation should be wrapped with the session management calls.
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Create scenario");

 // Creates a use case scenario.
 Scenario scenario = ScenarioManager.createScenario(useCase);
 // Sets the scenario name.
 scenario.setName("Extract money from ATM.");

 // Adds a basic flow step.
 FlowStep flowStep1 = scenario.addFlowStep();
 // Sets a name for the basic flow step.
 flowStep1.setName("Insert card");

 FlowStep flowStep2 = scenario.addFlowStep();
 flowStep2.setName("Enter pin");

 FlowStep flowStep3 = scenario.addFlowStep();
 flowStep3.setName("Good bye");

 // Adds an alternative condition for the basic flow step.
 AlternativeCondition condition = scenario.addAlternativeCondition(flowStep2);
 // Sets a condition guard.
 condition.setIfCondition("Pin correct");

 // Sets a name for the alternative flow step.
 FlowStep flowStep = condition.getAlternativeFlowSteps().get(0);
 flowStep.setName("Extract money");
 // Adds an exception type to the basic flow step.
 ExceptionType exceptionType = scenario.addExceptionType(flowStep2);

 // Sets a name for the exception type.
 exceptionType.setName("Card expired");
 // Sets a name for the exceptional flow step.
 FlowStep exceptionalFlowStep = exceptionType.getExceptionalFlowSteps().get(0);
 exceptionalFlowStep.setName("Inform customer about expired card");
 sessionManager.closeSession();

 // Opens and layouts the scenario diagram.
 ScenarioManager.displayScenario(scenario, true, true, "Open ATM Scenario");
````

For more information about the use case scenario, see the "Use Case Scenario" section in the "MagicDraw UserManual.pdf".

See Also:
[`Scenario`](Scenario.html)
[`ScenarioFactory`](ScenarioFactory.html)
[`AlternativeCondition`](AlternativeCondition.html)
[`ExceptionType`](ExceptionType.html)
[`FlowStep`](FlowStep.html)
[`ScenarioNode`](ScenarioNode.html)
[`ScenarioNodeEnd`](ScenarioNodeEnd.html)
[`ScenarioNodeStart`](ScenarioNodeStart.html)
[`ScenarioReadResult`](ScenarioReadResult.html)
[`ScenarioRepresentationTextProvider`](ScenarioRepresentationTextProvider.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ScenarioManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Scenario](Scenario.html)`
`[createScenario](#createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase))([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)`
Creates and initializes scenario for a given use case.
`static void`
`[displayScenario](#displayScenario(com.nomagic.magicdraw.usecasescenarios.scenarios.Scenario,boolean,boolean,java.lang.String))([Scenario](Scenario.html) scenario,
 boolean openDiagram,
 boolean layout,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName)`
Displays scenario on the diagram.
`static void`
`[setScenarioFactory](#setScenarioFactory(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioFactory))([ScenarioFactory](ScenarioFactory.html) scenarioFactory)`
Sets scenario factory with which to create scenarios.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ScenarioManager
public ScenarioManager()
 ============ METHOD DETAIL ========== 
Method Details
createScenario
public static [Scenario](Scenario.html) createScenario([UseCase](../../../uml2/ext/magicdraw/mdusecases/UseCase.html) useCase)
Creates and initializes scenario for a given use case.
Parameters:
`useCase` - use case for which to create scenario.
Returns:
created scenario.
setScenarioFactory
public static void setScenarioFactory([ScenarioFactory](ScenarioFactory.html) scenarioFactory)
Sets scenario factory with which to create scenarios.
 By setting another scenario factory it is possible to create custom scenarios.
Parameters:
`scenarioFactory` - scenario factory with which to create scenarios.
displayScenario
public static void displayScenario([Scenario](Scenario.html) scenario,
 boolean openDiagram,
 boolean layout,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName)
Displays scenario on the diagram.
 Performs necessary preparations and creates scenario symbols on the diagram.
 Creates its own session, all sessions should be closed before invoking this method.
 A session name can be passed.
Parameters:
`scenario` - scenario to display.
`openDiagram` - indicates whether scenario diagram should be opened.
`layout` - indicates whether scenario diagram should be layouted.
`sessionName` - name of the session to use in undo/redo history.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Class ScenarioManager">Class ScenarioManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ScenarioManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Scenario can be manipulated from Open API.
 <ul>
<li>The <a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>Scenario</code></a> class represents a use case scenario. It contains methods for manipulating it.</li>
<li>The <a href="ScenarioManager.html" title="class in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>ScenarioManager</code></a> class contains utility methods for creating and manipulating scenarios.</li>
<li>The scenario management calls should be wrapped with the session management calls.</li>
</ul>
 See an example of how to create the use case scenario with the basic, alternative, and exceptional flows.
 Scenario can be opened in a diagram.
 </p>
<pre>

 // Scenario manipulation should be wrapped with the session management calls.
 SessionManager sessionManager = SessionManager.getInstance();
 sessionManager.createSession("Create scenario");

 // Creates a use case scenario.
 Scenario scenario = ScenarioManager.createScenario(useCase);
 // Sets the scenario name.
 scenario.setName("Extract money from ATM.");

 // Adds a basic flow step.
 FlowStep flowStep1 = scenario.addFlowStep();
 // Sets a name for the basic flow step.
 flowStep1.setName("Insert card");

 FlowStep flowStep2 = scenario.addFlowStep();
 flowStep2.setName("Enter pin");

 FlowStep flowStep3 = scenario.addFlowStep();
 flowStep3.setName("Good bye");

 // Adds an alternative condition for the basic flow step.
 AlternativeCondition condition = scenario.addAlternativeCondition(flowStep2);
 // Sets a condition guard.
 condition.setIfCondition("Pin correct");

 // Sets a name for the alternative flow step.
 FlowStep flowStep = condition.getAlternativeFlowSteps().get(0);
 flowStep.setName("Extract money");
 // Adds an exception type to the basic flow step.
 ExceptionType exceptionType = scenario.addExceptionType(flowStep2);

 // Sets a name for the exception type.
 exceptionType.setName("Card expired");
 // Sets a name for the exceptional flow step.
 FlowStep exceptionalFlowStep = exceptionType.getExceptionalFlowSteps().get(0);
 exceptionalFlowStep.setName("Inform customer about expired card");
 sessionManager.closeSession();

 // Opens and layouts the scenario diagram.
 ScenarioManager.displayScenario(scenario, true, true, "Open ATM Scenario");
 </pre>
<p></p>
<p>For more information about the use case scenario, see the "Use Case Scenario" section in the "MagicDraw UserManual.pdf".</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios"><code>Scenario</code></a></li>
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
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ScenarioManager</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">createScenario</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates and initializes scenario for a given use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#displayScenario(com.nomagic.magicdraw.usecasescenarios.scenarios.Scenario,boolean,boolean,java.lang.String)">displayScenario</a><wbr/>(<a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a> scenario,
 boolean openDiagram,
 boolean layout,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Displays scenario on the diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setScenarioFactory(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioFactory)">setScenarioFactory</a><wbr/>(<a href="ScenarioFactory.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioFactory</a> scenarioFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets scenario factory with which to create scenarios.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ScenarioManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScenarioManager</span>()</div>
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
<section class="detail" id="createScenario(com.nomagic.uml2.ext.magicdraw.mdusecases.UseCase)">
<h3>createScenario</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></span> <span class="element-name">createScenario</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdusecases/UseCase.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdusecases">UseCase</a> useCase)</span></div>
<div class="block">Creates and initializes scenario for a given use case.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>useCase</code> - use case for which to create scenario.</dd>
<dt>Returns:</dt>
<dd>created scenario.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setScenarioFactory(com.nomagic.magicdraw.usecasescenarios.scenarios.ScenarioFactory)">
<h3>setScenarioFactory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setScenarioFactory</span><wbr/><span class="parameters">(<a href="ScenarioFactory.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioFactory</a> scenarioFactory)</span></div>
<div class="block">Sets scenario factory with which to create scenarios.
 By setting another scenario factory it is possible to create custom scenarios.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scenarioFactory</code> - scenario factory with which to create scenarios.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="displayScenario(com.nomagic.magicdraw.usecasescenarios.scenarios.Scenario,boolean,boolean,java.lang.String)">
<h3>displayScenario</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">displayScenario</span><wbr/><span class="parameters">(<a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a> scenario,
 boolean openDiagram,
 boolean layout,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName)</span></div>
<div class="block">Displays scenario on the diagram.
 Performs necessary preparations and creates scenario symbols on the diagram.
 Creates its own session, all sessions should be closed before invoking this method.
 A session name can be passed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scenario</code> - scenario to display.</dd>
<dd><code>openDiagram</code> - indicates whether scenario diagram should be opened.</dd>
<dd><code>layout</code> - indicates whether scenario diagram should be layouted.</dd>
<dd><code>sessionName</code> - name of the session to use in undo/redo history.</dd>
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
