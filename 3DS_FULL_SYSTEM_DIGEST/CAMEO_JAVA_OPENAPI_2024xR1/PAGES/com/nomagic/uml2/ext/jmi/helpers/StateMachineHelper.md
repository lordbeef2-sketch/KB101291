# JAVA OPENAPI: StateMachineHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ext/jmi/helpers/StateMachineHelper.html
- source_path: `com/nomagic/uml2/ext/jmi/helpers/StateMachineHelper.html`
- source_sha256: `875fb036cd3a3e1a6a99bbfd6f5d3d780be7a9db83241bd5c71800696ce6db6a`
- captured_utc: `2026-07-14T16:52:37.623220+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.helpers](package-summary.html)

## Class StateMachineHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.helpers.StateMachineHelper

@OpenApiAllpublic classStateMachineHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
An utility class with utility methods operating on state machine domain elements

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StateMachineHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static void`
`[disposeEvent](#disposeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event))([Event](../../magicdraw/commonbehaviors/mdcommunications/Event.html) event)`
Disposes event if it is not used any more by other elements in the model.
`static void`
`[disposeTriggers](#disposeTriggers(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Trigger](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html)> triggers)`

`static void`
`[disposeTriggers](#disposeTriggers(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Trigger](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html)> triggers)`
Deprecated.
use [`disposeTriggers(Collection)`](#disposeTriggers(java.util.Collection))
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getClassifierForTransition](#getClassifierForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Returns the classifier as context for given transition.
`static [Event](../../magicdraw/commonbehaviors/mdcommunications/Event.html)`
`[getEventForTransition](#getEventForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Returns an event of given transition.
`static [Trigger](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html)`
`[getFirstTrigger](#getFirstTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Returns first trigger from transition
`static [Operation](../../magicdraw/classes/mdkernel/Operation.html)`
`[getOperationForTransition](#getOperationForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Returns an operation of given transition.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)>`
`[getOperationsForTransition](#getOperationsForTransition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))([Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)`
Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
`static [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[getSignalForTransition](#getSignalForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Returns a signal of given transition.
`static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html)`
`[getStateMachineContext](#getStateMachineContext(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine))([StateMachine](../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html) machine)`
Returns the context of the state machine.
`static boolean`
`[isCallEvent](#isCallEvent(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Check if event of given transition is CallEvent
`static boolean`
`[isSignalEvent](#isSignalEvent(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)`
Check if event of given transition is SignalEvent
`static void`
`[setOperationForTransition](#setOperationForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation)`
Set derived property operation for transition.
`static void`
`[setSignalForTransition](#setSignalForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal))([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal)`
Set derived property signal for transition.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StateMachineHelper
public StateMachineHelper()
 ============ METHOD DETAIL ========== 
Method Details
setOperationForTransition
public static void setOperationForTransition([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 [Operation](../../magicdraw/classes/mdkernel/Operation.html) operation)
Set derived property operation for transition. Operation is mapped to first trigger call event operation.
 If transition does not own trigger, new one is created.
 If trigger does not reference CallEvent or old even is referenced by other elements, new CallEvent is created.
Parameters:
`transition` - the given transition
`operation` - the given operation
setSignalForTransition
public static void setSignalForTransition([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition,
 [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) signal)
Set derived property signal for transition. Signal is mapped to first trigger signal event signal.
 If transition does not own trigger, new one is created.
 If trigger does not reference SignalEvent or old even is referenced by other elements, new SignalEvent is created.
Parameters:
`transition` - the given transition
`signal` - the given signal
getOperationForTransition
@CheckForNullpublic static [Operation](../../magicdraw/classes/mdkernel/Operation.html) getOperationForTransition([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Returns an operation of given transition. Operation is taken from trigger call event.
Parameters:
`transition` - the given transition
Returns:
an operation of given transition
getSignalForTransition
@CheckForNullpublic static [Signal](../../magicdraw/commonbehaviors/mdcommunications/Signal.html) getSignalForTransition([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Returns a signal of given transition. Signal is taken from trigger signal event.
Parameters:
`transition` - the given transition
Returns:
a signal of given transition
isSignalEvent
public static boolean isSignalEvent([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Check if event of given transition is SignalEvent
Parameters:
`transition` - transition
Returns:
true if event is SignalEvent
isCallEvent
public static boolean isCallEvent([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Check if event of given transition is CallEvent
Parameters:
`transition` - transition
Returns:
true if event is CallEvent
getOperationsForTransition
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Operation](../../magicdraw/classes/mdkernel/Operation.html)> getOperationsForTransition(@CheckForNull
 [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) classifier)
Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
 Current implementation uses InteractionHelper.getOperationsForCallAction(classifier)
Parameters:
`classifier` - classifier
Returns:
operations
See Also:
[`InteractionHelper.getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)`](InteractionHelper.html#getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier))
getClassifierForTransition
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getClassifierForTransition([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Returns the classifier as context for given transition. If transition is in protocol state machine,
 ProtocolStateMachine.Interface can be returned.
Parameters:
`transition` - transition
Returns:
classifier
getStateMachineContext
@CheckForNullpublic static [Classifier](../../magicdraw/classes/mdkernel/Classifier.html) getStateMachineContext([StateMachine](../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html) machine)
Returns the context of the state machine.
Parameters:
`machine` - - state machine.
Returns:
context of the state machine.
disposeTriggers
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void disposeTriggers([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Trigger](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html)> triggers)
Deprecated.
use [`disposeTriggers(Collection)`](#disposeTriggers(java.util.Collection))
Disposes given collection of triggers and referenced by them events
Parameters:
`triggers` - triggers
disposeTriggers
public static void disposeTriggers([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Trigger](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html)> triggers)
disposeEvent
public static void disposeEvent(@CheckForNull
 [Event](../../magicdraw/commonbehaviors/mdcommunications/Event.html) event)
Disposes event if it is not used any more by other elements in the model.
Parameters:
`event` - event
getEventForTransition
@CheckForNullpublic static [Event](../../magicdraw/commonbehaviors/mdcommunications/Event.html) getEventForTransition([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Returns an event of given transition. Event is taken from trigger.
Parameters:
`transition` - the given transition
Returns:
an event of given transition
getFirstTrigger
@CheckForNullpublic static [Trigger](../../magicdraw/commonbehaviors/mdcommunications/Trigger.html) getFirstTrigger([Transition](../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html) transition)
Returns first trigger from transition
Parameters:
`transition` - transition
Returns:
trigger

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.helpers</a></div>
<h1 class="title" title="Class StateMachineHelper">Class StateMachineHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.helpers.StateMachineHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StateMachineHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">An utility class with utility methods operating on state machine domain elements</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">StateMachineHelper</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">disposeEvent</a><wbr/>(<a href="../../magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disposes event if it is not used any more by other elements in the model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeTriggers(java.util.Collection)">disposeTriggers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt; triggers)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#disposeTriggers(java.util.List)">disposeTriggers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt; triggers)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#disposeTriggers(java.util.Collection)"><code>disposeTriggers(Collection)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassifierForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">getClassifierForTransition</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the classifier as context for given transition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEventForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">getEventForTransition</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an event of given transition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">getFirstTrigger</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns first trigger from transition</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">getOperationForTransition</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an operation of given transition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOperationsForTransition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">getOperationsForTransition</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignalForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">getSignalForTransition</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a signal of given transition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateMachineContext(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">getStateMachineContext</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> machine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the context of the state machine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCallEvent(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">isCallEvent</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if event of given transition is CallEvent</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSignalEvent(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">isSignalEvent</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if event of given transition is SignalEvent</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOperationForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">setOperationForTransition</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set derived property operation for transition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSignalForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">setSignalForTransition</a><wbr/>(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Set derived property signal for transition.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>StateMachineHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StateMachineHelper</span>()</div>
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
<section class="detail" id="setOperationForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation)">
<h3>setOperationForTransition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOperationForTransition</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 <a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a> operation)</span></div>
<div class="block">Set derived property operation for transition. Operation is mapped to first trigger call event operation.
 If transition does not own trigger, new one is created.
 If trigger does not reference CallEvent or old even is referenced by other elements, new CallEvent is created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - the given transition</dd>
<dd><code>operation</code> - the given operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSignalForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition,com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Signal)">
<h3>setSignalForTransition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSignalForTransition</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition,
 <a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a> signal)</span></div>
<div class="block">Set derived property signal for transition. Signal is mapped to first trigger signal event signal.
 If transition does not own trigger, new one is created.
 If trigger does not reference SignalEvent or old even is referenced by other elements, new SignalEvent is created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - the given transition</dd>
<dd><code>signal</code> - the given signal</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>getOperationForTransition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a></span> <span class="element-name">getOperationForTransition</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Returns an operation of given transition. Operation is taken from trigger call event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - the given transition</dd>
<dt>Returns:</dt>
<dd>an operation of given transition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignalForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>getSignalForTransition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">getSignalForTransition</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Returns a signal of given transition. Signal is taken from trigger signal event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - the given transition</dd>
<dt>Returns:</dt>
<dd>a signal of given transition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSignalEvent(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>isSignalEvent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSignalEvent</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Check if event of given transition is SignalEvent</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - transition</dd>
<dt>Returns:</dt>
<dd>true if event is SignalEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCallEvent(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>isCallEvent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCallEvent</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Check if event of given transition is CallEvent</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - transition</dd>
<dt>Returns:</dt>
<dd>true if event is CallEvent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOperationsForTransition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)">
<h3>getOperationsForTransition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/classes/mdkernel/Operation.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Operation</a>&gt;</span> <span class="element-name">getOperationsForTransition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a> classifier)</span></div>
<div class="block">Collects operations from given classifiers, base classifiers and provided interfaces of given classifiers.
 Current implementation uses InteractionHelper.getOperationsForCallAction(classifier)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classifier</code> - classifier</dd>
<dt>Returns:</dt>
<dd>operations</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="InteractionHelper.html#getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)"><code>InteractionHelper.getOperationsForCallAction(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassifierForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>getClassifierForTransition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getClassifierForTransition</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Returns the classifier as context for given transition. If transition is in protocol state machine,
 ProtocolStateMachine.Interface can be returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - transition</dd>
<dt>Returns:</dt>
<dd>classifier</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateMachineContext(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.StateMachine)">
<h3>getStateMachineContext</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a></span> <span class="element-name">getStateMachineContext</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/StateMachine.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">StateMachine</a> machine)</span></div>
<div class="block">Returns the context of the state machine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>machine</code> - - state machine.</dd>
<dt>Returns:</dt>
<dd>context of the state machine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeTriggers(java.util.List)">
<h3>disposeTriggers</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disposeTriggers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt; triggers)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#disposeTriggers(java.util.Collection)"><code>disposeTriggers(Collection)</code></a></div>
</div>
<div class="block">Disposes given collection of triggers and referenced by them events</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>triggers</code> - triggers</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeTriggers(java.util.Collection)">
<h3>disposeTriggers</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disposeTriggers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a>&gt; triggers)</span></div>
</section>
</li>
<li>
<section class="detail" id="disposeEvent(com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications.Event)">
<h3>disposeEvent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">disposeEvent</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a> event)</span></div>
<div class="block">Disposes event if it is not used any more by other elements in the model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEventForTransition(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>getEventForTransition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdcommunications/Event.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Event</a></span> <span class="element-name">getEventForTransition</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Returns an event of given transition. Event is taken from trigger.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - the given transition</dd>
<dt>Returns:</dt>
<dd>an event of given transition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstTrigger(com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines.Transition)">
<h3>getFirstTrigger</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../magicdraw/commonbehaviors/mdcommunications/Trigger.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Trigger</a></span> <span class="element-name">getFirstTrigger</span><wbr/><span class="parameters">(<a href="../../magicdraw/statemachines/mdbehaviorstatemachines/Transition.html" title="interface in com.nomagic.uml2.ext.magicdraw.statemachines.mdbehaviorstatemachines">Transition</a> transition)</span></div>
<div class="block">Returns first trigger from transition</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transition</code> - transition</dd>
<dt>Returns:</dt>
<dd>trigger</dd>
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
