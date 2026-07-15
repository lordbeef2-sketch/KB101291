# JAVA OPENAPI: SimulationExecutionListener (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/simulation/execution/SimulationExecutionListener.html
- source_path: `com/nomagic/magicdraw/simulation/execution/SimulationExecutionListener.html`
- source_sha256: `69f10876321b94c04380a0e131b5a8e76db7c65b0a5d963d0f43976b474d6ea1`
- captured_utc: `2026-07-14T16:45:42.625568+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.execution](package-summary.html)

## Class SimulationExecutionListener

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener

@OpenApiAllpublic abstract classSimulationExecutionListener
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
The listener class for receiving execution events.
 Create the custom class that extends this class to capturing execution events.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimulationExecutionListener](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[beforeContextInitialized](#beforeContextInitialized(com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecution](SimulationExecution.html) execution)`
Event fired before context of `execution` is initialized.
`void`
`[beforeObjectDestroyed](#beforeObjectDestroyed(com.nomagic.magicdraw.simulation.fuml.classes.Object_))([Object_](../fuml/classes/Object_.html) object)`
Event occurred before object destroyed.
`void`
`[behaviorCalled](#behaviorCalled(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_,boolean))([Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ParameterValue](../fuml/behaviors/ParameterValue.html)> parameterValues,
 [Object_](../fuml/classes/Object_.html) caller,
 [Object_](../fuml/classes/Object_.html) target,
 boolean isSynchronous)`
Event for behavior called.
`void`
`[busyStatusChange](#busyStatusChange(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.Object,java.lang.Object))([StructuredValue](../fuml/classes/StructuredValue.html) context,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue)`
Event for busy status change.
`void`
`[configLoaded](#configLoaded(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.SimulationExecution))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) config,
 [SimulationExecution](SimulationExecution.html) execution)`
Custom additional configuration values can be read here.
`void`
`[contextInitialized](#contextInitialized(com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecution](SimulationExecution.html) execution)`
Event fired after context of `execution` is initialized.
`void`
`[elementActivated](#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values)`
Deprecated.
override [`elementActivated(Element, Collection, ActivationContext)`](#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)) which additionally provides context fUML Object, in which the
 element activation has occurred.
`void`
`[elementActivated](#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values,
 [ActivationContext](../context/ActivationContext.html) context)`
Event for element activated.
`void`
`[elementDeactivated](#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values)`
Deprecated.
override [`elementDeactivated(Element, Collection, ActivationContext)`](#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)) which additionally provides context fUML Object, in which the
 element activation has occurred.
`void`
`[elementDeactivated](#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values,
 [ActivationContext](../context/ActivationContext.html) context)`
Event for element deactivated.
`void`
`[eventTriggered](#eventTriggered(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance))([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal)`
Event for signal event triggered.
`void`
`[executionStarted](#executionStarted(com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecution](SimulationExecution.html) execution)`
Event for execution started.
`void`
`[executionTerminated](#executionTerminated(com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecution](SimulationExecution.html) execution)`
Event for execution terminated.
`void`
`[objectCreated](#objectCreated(com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_))([Object_](../fuml/classes/Object_.html) sender,
 [Object_](../fuml/classes/Object_.html) object)`
Event for object created.
`void`
`[objectStateActivated](#objectStateActivated(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State))([StructuredValue](../fuml/classes/StructuredValue.html) context,
 [State](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) newState)`
Event when state of runtime object activated.
`void`
`[operationCalled](#operationCalled(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_,boolean))([Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ParameterValue](../fuml/behaviors/ParameterValue.html)> parameterValues,
 [Object_](../fuml/classes/Object_.html) caller,
 [Object_](../fuml/classes/Object_.html) target,
 boolean isSynchronous)`
Event for operation called.
`void`
`[valueChange](#valueChange(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue,java.lang.Object,java.lang.Object))([StructuredValue](../fuml/classes/StructuredValue.html) context,
 [FeatureValue](../fuml/classes/FeatureValue.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue)`
Event for value change.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationExecutionListener
public SimulationExecutionListener()
 ============ METHOD DETAIL ========== 
Method Details
configLoaded
public void configLoaded([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) config,
 [SimulationExecution](SimulationExecution.html) execution)
Custom additional configuration values can be read here.
Parameters:
`config` - the configuration element of the running execution.
`execution` - simulation execution
executionStarted
public void executionStarted([SimulationExecution](SimulationExecution.html) execution)
Event for execution started.
Parameters:
`execution` - the started execution
eventTriggered
public void eventTriggered([SignalInstance](../fuml/behaviors/communications/SignalInstance.html) signal)
Event for signal event triggered.
Parameters:
`signal` - the triggered signal
operationCalled
public void operationCalled([Operation](../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html) operation,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ParameterValue](../fuml/behaviors/ParameterValue.html)> parameterValues,
 [Object_](../fuml/classes/Object_.html) caller,
 [Object_](../fuml/classes/Object_.html) target,
 boolean isSynchronous)
Event for operation called.
Parameters:
`operation` - the called operation
`parameterValues` - parameters
`caller` - caller
`target` - target
`isSynchronous` - isSynchronous
behaviorCalled
public void behaviorCalled([Behavior](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) behavior,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ParameterValue](../fuml/behaviors/ParameterValue.html)> parameterValues,
 [Object_](../fuml/classes/Object_.html) caller,
 [Object_](../fuml/classes/Object_.html) target,
 boolean isSynchronous)
Event for behavior called.
Parameters:
`behavior` - the called behavior
`parameterValues` - parameters
`caller` - caller
`target` - target
`isSynchronous` - isSynchronous
objectCreated
public void objectCreated([Object_](../fuml/classes/Object_.html) sender,
 [Object_](../fuml/classes/Object_.html) object)
Event for object created.
Parameters:
`sender` - sender
`object` - the created `Object_`
executionTerminated
public void executionTerminated([SimulationExecution](SimulationExecution.html) execution)
Event for execution terminated.
Parameters:
`execution` - the terminated execution
elementActivated
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void elementActivated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values)
Deprecated.
override [`elementActivated(Element, Collection, ActivationContext)`](#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)) which additionally provides context fUML Object, in which the
 element activation has occurred.
elementDeactivated
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void elementDeactivated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values)
Deprecated.
override [`elementDeactivated(Element, Collection, ActivationContext)`](#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)) which additionally provides context fUML Object, in which the
 element activation has occurred.
elementActivated
public void elementActivated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values,
 [ActivationContext](../context/ActivationContext.html) context)
Event for element activated.
Parameters:
`element` - the activated element
`values` - values
`context` - provides information about enclosing Object_ in which activation has occurred
elementDeactivated
public void elementDeactivated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> values,
 [ActivationContext](../context/ActivationContext.html) context)
Event for element deactivated.
Parameters:
`element` - the deactivated element
`values` - values
`context` - provides information about enclosing Object_ in which deactivation has occurred
valueChange
public void valueChange([StructuredValue](../fuml/classes/StructuredValue.html) context,
 [FeatureValue](../fuml/classes/FeatureValue.html) feature,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue)
Event for value change.
Parameters:
`context` - the owner of feature.
`feature` - the FeatureValue that the value was changed.
`oldValue` - the old value.
`newValue` - the new value.
busyStatusChange
public void busyStatusChange([StructuredValue](../fuml/classes/StructuredValue.html) context,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue)
Event for busy status change.
Parameters:
`context` - the owner of feature.
`oldValue` - the old value.
`newValue` - the new value.
objectStateActivated
public void objectStateActivated([StructuredValue](../fuml/classes/StructuredValue.html) context,
 [State](../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html) newState)
Event when state of runtime object activated.
Parameters:
`context` - the runtime value
`newState` - the old state
beforeObjectDestroyed
public void beforeObjectDestroyed([Object_](../fuml/classes/Object_.html) object)
Event occurred before object destroyed.
Parameters:
`object` - Being destroyed object
beforeContextInitialized
public void beforeContextInitialized([SimulationExecution](SimulationExecution.html) execution)
Event fired before context of `execution` is initialized.
Parameters:
`execution` - Simulation execution
contextInitialized
public void contextInitialized([SimulationExecution](SimulationExecution.html) execution)
Event fired after context of `execution` is initialized.
Parameters:
`execution` - Simulation execution

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.execution</a></div>
<h1 class="title" title="Class SimulationExecutionListener">Class SimulationExecutionListener</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">SimulationExecutionListener</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The listener class for receiving execution events.
 <p>
 Create the custom class that extends this class to capturing execution events.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimulationExecutionListener</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeContextInitialized(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">beforeContextInitialized</a><wbr/>(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event fired before context of <code>execution</code> is initialized.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeObjectDestroyed(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">beforeObjectDestroyed</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event occurred before object destroyed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#behaviorCalled(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_,boolean)">behaviorCalled</a><wbr/>(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../fuml/behaviors/ParameterValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">ParameterValue</a>&gt; parameterValues,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> caller,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 boolean isSynchronous)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for behavior called.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#busyStatusChange(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.Object,java.lang.Object)">busyStatusChange</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for busy status change.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#configLoaded(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.SimulationExecution)">configLoaded</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> config,
 <a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Custom additional configuration values can be read here.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#contextInitialized(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">contextInitialized</a><wbr/>(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event fired after context of <code>execution</code> is initialized.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">elementActivated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">override <a href="#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)"><code>elementActivated(Element, Collection, ActivationContext)</code></a> which additionally provides context fUML Object, in which the
             element activation has occurred.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)">elementActivated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values,
 <a href="../context/ActivationContext.html" title="interface in com.nomagic.magicdraw.simulation.context">ActivationContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for element activated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">elementDeactivated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">override <a href="#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)"><code>elementDeactivated(Element, Collection, ActivationContext)</code></a> which additionally provides context fUML Object, in which the
             element activation has occurred.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)">elementDeactivated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values,
 <a href="../context/ActivationContext.html" title="interface in com.nomagic.magicdraw.simulation.context">ActivationContext</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for element deactivated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eventTriggered(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance)">eventTriggered</a><wbr/>(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for signal event triggered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executionStarted(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">executionStarted</a><wbr/>(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for execution started.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executionTerminated(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">executionTerminated</a><wbr/>(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for execution terminated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#objectCreated(com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">objectCreated</a><wbr/>(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> sender,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for object created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#objectStateActivated(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">objectStateActivated</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> context,
 <a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> newState)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event when state of runtime object activated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#operationCalled(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_,boolean)">operationCalled</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../fuml/behaviors/ParameterValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">ParameterValue</a>&gt; parameterValues,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> caller,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 boolean isSynchronous)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for operation called.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#valueChange(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue,java.lang.Object,java.lang.Object)">valueChange</a><wbr/>(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> context,
 <a href="../fuml/classes/FeatureValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">FeatureValue</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Event for value change.</div>
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
<h3>SimulationExecutionListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimulationExecutionListener</span>()</div>
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
<section class="detail" id="configLoaded(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>configLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">configLoaded</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> config,
 <a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Custom additional configuration values can be read here.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>config</code> - the configuration element of the running execution.</dd>
<dd><code>execution</code> - simulation execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executionStarted(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>executionStarted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">executionStarted</span><wbr/><span class="parameters">(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Event for execution started.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - the started execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eventTriggered(com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance)">
<h3>eventTriggered</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">eventTriggered</span><wbr/><span class="parameters">(<a href="../fuml/behaviors/communications/SignalInstance.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors.communications">SignalInstance</a> signal)</span></div>
<div class="block">Event for signal event triggered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>signal</code> - the triggered signal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="operationCalled(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_,boolean)">
<h3>operationCalled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">operationCalled</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../fuml/behaviors/ParameterValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">ParameterValue</a>&gt; parameterValues,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> caller,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 boolean isSynchronous)</span></div>
<div class="block">Event for operation called.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - the called operation</dd>
<dd><code>parameterValues</code> - parameters</dd>
<dd><code>caller</code> - caller</dd>
<dd><code>target</code> - target</dd>
<dd><code>isSynchronous</code> - isSynchronous</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="behaviorCalled(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors.Behavior,java.util.List,com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_,boolean)">
<h3>behaviorCalled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">behaviorCalled</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors">Behavior</a> behavior,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../fuml/behaviors/ParameterValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">ParameterValue</a>&gt; parameterValues,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> caller,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> target,
 boolean isSynchronous)</span></div>
<div class="block">Event for behavior called.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>behavior</code> - the called behavior</dd>
<dd><code>parameterValues</code> - parameters</dd>
<dd><code>caller</code> - caller</dd>
<dd><code>target</code> - target</dd>
<dd><code>isSynchronous</code> - isSynchronous</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="objectCreated(com.nomagic.magicdraw.simulation.fuml.classes.Object_,com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>objectCreated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">objectCreated</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> sender,
 <a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</span></div>
<div class="block">Event for object created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sender</code> - sender</dd>
<dd><code>object</code> - the created <code>Object_</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executionTerminated(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>executionTerminated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">executionTerminated</span><wbr/><span class="parameters">(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Event for execution terminated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - the terminated execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>elementActivated</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">elementActivated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">override <a href="#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)"><code>elementActivated(Element, Collection, ActivationContext)</code></a> which additionally provides context fUML Object, in which the
             element activation has occurred.</div>
</div>
</section>
</li>
<li>
<section class="detail" id="elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>elementDeactivated</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">elementDeactivated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">override <a href="#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)"><code>elementDeactivated(Element, Collection, ActivationContext)</code></a> which additionally provides context fUML Object, in which the
             element activation has occurred.</div>
</div>
</section>
</li>
<li>
<section class="detail" id="elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)">
<h3>elementActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">elementActivated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values,
 <a href="../context/ActivationContext.html" title="interface in com.nomagic.magicdraw.simulation.context">ActivationContext</a> context)</span></div>
<div class="block">Event for element activated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the activated element</dd>
<dd><code>values</code> - values</dd>
<dd><code>context</code> - provides information about enclosing Object_ in which activation has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection,com.nomagic.magicdraw.simulation.context.ActivationContext)">
<h3>elementDeactivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">elementDeactivated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values,
 <a href="../context/ActivationContext.html" title="interface in com.nomagic.magicdraw.simulation.context">ActivationContext</a> context)</span></div>
<div class="block">Event for element deactivated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the deactivated element</dd>
<dd><code>values</code> - values</dd>
<dd><code>context</code> - provides information about enclosing Object_ in which deactivation has occurred</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueChange(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.magicdraw.simulation.fuml.classes.FeatureValue,java.lang.Object,java.lang.Object)">
<h3>valueChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">valueChange</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> context,
 <a href="../fuml/classes/FeatureValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">FeatureValue</a> feature,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Event for value change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the owner of feature.</dd>
<dd><code>feature</code> - the FeatureValue that the value was changed.</dd>
<dd><code>oldValue</code> - the old value.</dd>
<dd><code>newValue</code> - the new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="busyStatusChange(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,java.lang.Object,java.lang.Object)">
<h3>busyStatusChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">busyStatusChange</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue)</span></div>
<div class="block">Event for busy status change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the owner of feature.</dd>
<dd><code>oldValue</code> - the old value.</dd>
<dd><code>newValue</code> - the new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="objectStateActivated(com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue,com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.State)">
<h3>objectStateActivated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">objectStateActivated</span><wbr/><span class="parameters">(<a href="../fuml/classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">StructuredValue</a> context,
 <a href="../../../uml2/ext/magicdraw/statemachines/mdbehaviorstatemachines/State.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">State</a> newState)</span></div>
<div class="block">Event when state of runtime object activated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the runtime value</dd>
<dd><code>newState</code> - the old state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="beforeObjectDestroyed(com.nomagic.magicdraw.simulation.fuml.classes.Object_)">
<h3>beforeObjectDestroyed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">beforeObjectDestroyed</span><wbr/><span class="parameters">(<a href="../fuml/classes/Object_.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Object_</a> object)</span></div>
<div class="block">Event occurred before object destroyed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - Being destroyed object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="beforeContextInitialized(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>beforeContextInitialized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">beforeContextInitialized</span><wbr/><span class="parameters">(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Event fired before context of <code>execution</code> is initialized.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - Simulation execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contextInitialized(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>contextInitialized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">contextInitialized</span><wbr/><span class="parameters">(<a href="SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Event fired after context of <code>execution</code> is initialized.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - Simulation execution</dd>
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
