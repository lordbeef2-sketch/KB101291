# JAVA OPENAPI: ExecutionEngine (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/simulation/engine/ExecutionEngine.html
- source_path: `com/nomagic/magicdraw/simulation/engine/ExecutionEngine.html`
- source_sha256: `22621454911a919ce959dca25ce1d48c33668d2d8a95b29c0a383333cf5f3887`
- captured_utc: `2026-07-14T16:55:34.431223+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.engine](package-summary.html)

## Class ExecutionEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.engine.ExecutionEngine

@OpenApipublic abstract classExecutionEngine
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Allows executing [`Behavior`](../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html) in a customized
 way during simulation execution. Currently, supports overriding execution behavior of :
 - StateMachine
 - Interaction
 - Activity, unless the Activity is the target of the simulation execution itself
 Note: Simulation execution target is always executed with the default fUML ExecutionEngine to initialize the fUML runtime values

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.simulation.engine.InternalEngineListener>`
`[internalListeners](#internalListeners)`

`protected [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html)`
`[isClosed](#isClosed)`
if this flag is true, it tells that the engine is already closed.
`protected [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html)`
`[isInterrupted](#isInterrupted)`
if this flag is true, it tells that the engine is interrupted and it is closing.
`protected [SimulationSession](../execution/session/SimulationSession.html)`
`[session](#session)`
a reference to the running session of this engine.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ExecutionEngine](#%3Cinit%3E(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor))([ExecutionEngineDescriptor](ExecutionEngineDescriptor.html) engineDescriptor)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[activateElement](#activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.data.ActivationInfo))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)`
Activate the element, it delegates to all storing engine listener.
`void`
`[activateElement](#activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> c)`
Activate the element, it delegates to all storing engine listener.
`void`
`[addEngineListener](#addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener))([EngineListener](EngineListener.html) listener)`
Add the specified engine listener to the storing engine listener list.
`void`
`[addEngineListener](#addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener,int))([EngineListener](EngineListener.html) listener,
 int index)`
Add the specified engine listener to the storing engine listener list with specified position.
`void`
`[addInternalEngineListener](#addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener))(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)`
Add the specified internal engine listener to the storing engine listener list.
`void`
`[addInternalEngineListener](#addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener,int))(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener,
 int index)`
Add the specified internal engine listener to the storing internal engine listener list with specified position.
`void`
`[deactivateElement](#deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.data.ActivationInfo))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)`
Deactivate the element, it delegates to all storing engine listener.
`void`
`[deactivateElement](#deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> c)`
Deactivate the element, it delegates to all storing engine listener.
`void`
`[destroyObject](#destroyObject())()`
Destroys object.
`abstract void`
`[execute](#execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Engine execution.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getActiveElements](#getActiveElements())()`
Gets active elements.
`com.nomagic.magicdraw.simulation.engine.EngineAnimationController`
`[getAnimationController](#getAnimationController())()`

`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)>`
`[getAvailableSignals](#getAvailableSignals())()`
Returns all available signals at current state.
`[ExecutionEngineDescriptor](ExecutionEngineDescriptor.html)`
`[getEngineDescriptor](#getEngineDescriptor())()`
ExecutionEngineDescriptor getter.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[EngineListener](EngineListener.html)>`
`[getEngineListeners](#getEngineListeners())()`
Get the engine listener list.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.simulation.engine.InternalEngineListener>`
`[getInternalEngineListeners](#getInternalEngineListeners())()`
Get the engine listener list.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getLastVisitedElement](#getLastVisitedElement())()`
Gets last visited element - element that was activated last and is already deactivated
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getNormativeValues](#getNormativeValues(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)`
Get the normative values collection from the specified value collection.
`[SimulationSession](../execution/session/SimulationSession.html)`
`[getSession](#getSession())()`
`Session` getter.
`com.nomagic.magicdraw.simulation.engine.ExecutionStatus`
`[getStatus](#getStatus())()`
Get the execution status.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getValuesAsString](#getValuesAsString(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)`
Get the string of the given collection.
`abstract void`
`[init](#init(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Engine initialization.
`final void`
`[internalExecute](#internalExecute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Engine internal execution.
`final void`
`[internalInit](#internalInit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Engine internal initialization.
`final void`
`[internalOnClose](#internalOnClose())()`
Engine internal onClose.
`void`
`[interrupt](#interrupt())()`
Interrupt this engine.
`boolean`
`[isClosed](#isClosed())()`

`boolean`
`[isClosing](#isClosing())()`

`boolean`
`[isExecutionFinished](#isExecutionFinished())()`
Get executionFinished.
`boolean`
`[isInterrupted](#isInterrupted())()`
return boolean value of isInterrupted.
`abstract void`
`[onClose](#onClose())()`
Engine onClose.
`void`
`[removeEngineListener](#removeEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener))([EngineListener](EngineListener.html) listener)`
Remove the specified engine listener from the storing engine listener list.
`void`
`[removeInternalEngineListener](#removeInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener))(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)`
Remove the specified internal engine listener from the storing internal engine listener list.
`void`
`[runWhenExecutionFinished](#runWhenExecutionFinished(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)`
Thread safe way to ensure that runnable will be called exactly once when engine has finished execution
`void`
`[setSession](#setSession(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](../execution/session/SimulationSession.html) session)`
`Session` setter.
`void`
`[setStatus](#setStatus(com.nomagic.magicdraw.simulation.engine.ExecutionStatus))(com.nomagic.magicdraw.simulation.engine.ExecutionStatus status)`
Set status.
`void`
`[triggerEvent](#triggerEvent(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) event)`
Trigger the specified event, it delegates to all storing engine listener.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
session
@OpenApiprotected [SimulationSession](../execution/session/SimulationSession.html) session
a reference to the running session of this engine.
isInterrupted
protected [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html) isInterrupted
if this flag is true, it tells that the engine is interrupted and it is closing.
 this flag is used to checked in internalOnClose().
isClosed
protected [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html) isClosed
if this flag is true, it tells that the engine is already closed.
 all onClose tasks have been done.
internalListeners
protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.simulation.engine.InternalEngineListener> internalListeners
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ExecutionEngine
@OpenApipublic ExecutionEngine([ExecutionEngineDescriptor](ExecutionEngineDescriptor.html) engineDescriptor)
Constructor.
Parameters:
`engineDescriptor` - the given engine's descriptor.
 ============ METHOD DETAIL ========== 
Method Details
getEngineDescriptor
@OpenApipublic [ExecutionEngineDescriptor](ExecutionEngineDescriptor.html) getEngineDescriptor()
ExecutionEngineDescriptor getter.
Returns:
ExecutionEngineDescriptor
getAnimationController
public com.nomagic.magicdraw.simulation.engine.EngineAnimationController getAnimationController()
init
@OpenApipublic abstract void init([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Engine initialization.
Parameters:
`element` - the given element
execute
@OpenApipublic abstract void execute([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Engine execution.
Parameters:
`element` - the given element
onClose
@OpenApipublic abstract void onClose()
Engine onClose.
internalInit
public final void internalInit([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Engine internal initialization.
Parameters:
`element` - the specified element
internalExecute
public final void internalExecute([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Engine internal execution.
Parameters:
`element` - the specified element
internalOnClose
public final void internalOnClose()
Engine internal onClose.
isClosing
public boolean isClosing()
isClosed
public boolean isClosed()
destroyObject
public void destroyObject()
Destroys object.
addEngineListener
@OpenApipublic void addEngineListener([EngineListener](EngineListener.html) listener)
Add the specified engine listener to the storing engine listener list.
Parameters:
`listener` - the specified engine listener
addEngineListener
public void addEngineListener([EngineListener](EngineListener.html) listener,
 int index)
Add the specified engine listener to the storing engine listener list with specified position.
Parameters:
`listener` - the specified engine listener
`index` - the index to add
removeEngineListener
@OpenApipublic void removeEngineListener([EngineListener](EngineListener.html) listener)
Remove the specified engine listener from the storing engine listener list.
Parameters:
`listener` - the specified engine listener
addInternalEngineListener
public void addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)
Add the specified internal engine listener to the storing engine listener list.
Parameters:
`listener` - the specified internal engine listener
addInternalEngineListener
public void addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener,
 int index)
Add the specified internal engine listener to the storing internal engine listener list with specified position.
Parameters:
`listener` - the specified internal engine listener
`index` - the index to add
removeInternalEngineListener
public void removeInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)
Remove the specified internal engine listener from the storing internal engine listener list.
Parameters:
`listener` - the specified internal engine listener
getEngineListeners
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[EngineListener](EngineListener.html)> getEngineListeners()
Get the engine listener list.
Returns:
the engine listener list.
getInternalEngineListeners
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.simulation.engine.InternalEngineListener> getInternalEngineListeners()
Get the engine listener list.
Returns:
the engine listener list.
activateElement
@OpenApipublic void activateElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> c)
Activate the element, it delegates to all storing engine listener.
Parameters:
`element` - the specified element
`c` - the passing values
activateElement
public void activateElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)
Activate the element, it delegates to all storing engine listener.
Parameters:
`element` - the specified element
`info` - ActivationInfo
deactivateElement
@OpenApipublic void deactivateElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> c)
Deactivate the element, it delegates to all storing engine listener.
Parameters:
`element` - the specified element
`c` - the passing values
deactivateElement
public void deactivateElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)
Deactivate the element, it delegates to all storing engine listener.
Parameters:
`element` - the specified element
`info` - ActivationInfo
triggerEvent
@OpenApipublic void triggerEvent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) event)
Trigger the specified event, it delegates to all storing engine listener.
Parameters:
`event` - the specified event
getAvailableSignals
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Signal](../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)> getAvailableSignals()
Returns all available signals at current state. For the state machine, available signals can
 change current state to another state. 

 

 Default implementation returns an empty Set.
Returns:
the available signals at current state.
getValuesAsString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getValuesAsString(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)
Get the string of the given collection.
Parameters:
`values` - the specified collection
Returns:
the string value
getNormativeValues
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getNormativeValues([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)
Get the normative values collection from the specified value collection.
Parameters:
`values` - the specified value collection.
Returns:
the normative values collection
getStatus
public com.nomagic.magicdraw.simulation.engine.ExecutionStatus getStatus()
Get the execution status.
Returns:
the execution status
setSession
public void setSession([SimulationSession](../execution/session/SimulationSession.html) session)
`Session` setter.
Parameters:
`session` - the specified session
getSession
public [SimulationSession](../execution/session/SimulationSession.html) getSession()
`Session` getter.
Returns:
`Session`
setStatus
public void setStatus(com.nomagic.magicdraw.simulation.engine.ExecutionStatus status)
Set status.
Parameters:
`status` - the specified status
getActiveElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getActiveElements()
Gets active elements.
Returns:
Active elements
getLastVisitedElement
@OpenApi
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getLastVisitedElement()
Gets last visited element - element that was activated last and is already deactivated
Returns:
Last visited element
interrupt
public void interrupt()
Interrupt this engine.
isInterrupted
public boolean isInterrupted()
return boolean value of isInterrupted.
Returns:
boolean value of isInterrupted.
isExecutionFinished
public boolean isExecutionFinished()
Get executionFinished.
Returns:
executionFinished
runWhenExecutionFinished
public void runWhenExecutionFinished([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)
Thread safe way to ensure that runnable will be called exactly once when engine has finished execution

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.engine</a></div>
<h1 class="title" title="Class ExecutionEngine">Class ExecutionEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.engine.ExecutionEngine</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ExecutionEngine</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Allows executing <a href="../../../uml2/ext/magicdraw/commonbehaviors/mdbasicbehaviors/Behavior.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdbasicbehaviors"><code>Behavior</code></a> in a customized
 way during simulation execution. Currently, supports overriding execution behavior of :
 - StateMachine
 - Interaction
 - Activity, unless the Activity is the target of the simulation execution itself
 Note: Simulation execution target is always executed with the default fUML ExecutionEngine to initialize the fUML runtime values</div>
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
<div class="col-first even-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.simulation.engine.InternalEngineListener&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#internalListeners">internalListeners</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html" title="class or interface in java.util.concurrent.atomic">AtomicBoolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isClosed">isClosed</a></code></div>
<div class="col-last odd-row-color">
<div class="block">if this flag is true, it tells that the engine is already closed.</div>
</div>
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html" title="class or interface in java.util.concurrent.atomic">AtomicBoolean</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isInterrupted">isInterrupted</a></code></div>
<div class="col-last even-row-color">
<div class="block">if this flag is true, it tells that the engine is interrupted and it is closing.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#session">session</a></code></div>
<div class="col-last odd-row-color">
<div class="block">a reference to the running session of this engine.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor)">ExecutionEngine</a><wbr/>(<a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a> engineDescriptor)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.data.ActivationInfo)">activateElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Activate the element, it delegates to all storing engine listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">activateElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Activate the element, it delegates to all storing engine listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener)">addEngineListener</a><wbr/>(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the specified engine listener to the storing engine listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener,int)">addEngineListener</a><wbr/>(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the specified engine listener to the storing engine listener list with specified position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener)">addInternalEngineListener</a><wbr/>(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the specified internal engine listener to the storing engine listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener,int)">addInternalEngineListener</a><wbr/>(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the specified internal engine listener to the storing internal engine listener list with specified position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.data.ActivationInfo)">deactivateElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Deactivate the element, it delegates to all storing engine listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">deactivateElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Deactivate the element, it delegates to all storing engine listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroyObject()">destroyObject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Destroys object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">execute</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Engine execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveElements()">getActiveElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets active elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.simulation.engine.EngineAnimationController</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnimationController()">getAnimationController</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAvailableSignals()">getAvailableSignals</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns all available signals at current state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEngineDescriptor()">getEngineDescriptor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">ExecutionEngineDescriptor getter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEngineListeners()">getEngineListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the engine listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.simulation.engine.InternalEngineListener&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInternalEngineListeners()">getInternalEngineListeners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the engine listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastVisitedElement()">getLastVisitedElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets last visited element - element that was activated last and is already deactivated</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNormativeValues(java.util.Collection)">getNormativeValues</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the normative values collection from the specified value collection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSession()">getSession</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block"><code>Session</code> getter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.simulation.engine.ExecutionStatus</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStatus()">getStatus</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the execution status.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getValuesAsString(java.util.Collection)">getValuesAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the string of the given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">init</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Engine initialization.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalExecute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">internalExecute</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Engine internal execution.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalInit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">internalInit</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Engine internal initialization.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#internalOnClose()">internalOnClose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Engine internal onClose.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#interrupt()">interrupt</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Interrupt this engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isClosed()">isClosed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isClosing()">isClosing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExecutionFinished()">isExecutionFinished</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get executionFinished.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInterrupted()">isInterrupted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">return boolean value of isInterrupted.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onClose()">onClose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Engine onClose.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener)">removeEngineListener</a><wbr/>(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove the specified engine listener from the storing engine listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener)">removeInternalEngineListener</a><wbr/>(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove the specified internal engine listener from the storing internal engine listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#runWhenExecutionFinished(java.lang.Runnable)">runWhenExecutionFinished</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Thread safe way to ensure that runnable will be called exactly once when engine has finished execution</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSession(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">setSession</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block"><code>Session</code> setter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStatus(com.nomagic.magicdraw.simulation.engine.ExecutionStatus)">setStatus</a><wbr/>(com.nomagic.magicdraw.simulation.engine.ExecutionStatus status)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set status.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#triggerEvent(java.lang.String)">triggerEvent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> event)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Trigger the specified event, it delegates to all storing engine listener.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="session">
<h3>session</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">protected</span> <span class="return-type"><a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">session</span></div>
<div class="block">a reference to the running session of this engine.</div>
</section>
</li>
<li>
<section class="detail" id="isInterrupted">
<h3>isInterrupted</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html" title="class or interface in java.util.concurrent.atomic">AtomicBoolean</a></span> <span class="element-name">isInterrupted</span></div>
<div class="block">if this flag is true, it tells that the engine is interrupted and it is closing.
 this flag is used to checked in internalOnClose().</div>
</section>
</li>
<li>
<section class="detail" id="isClosed">
<h3>isClosed</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html" title="class or interface in java.util.concurrent.atomic">AtomicBoolean</a></span> <span class="element-name">isClosed</span></div>
<div class="block">if this flag is true, it tells that the engine is already closed.
 all onClose tasks have been done.</div>
</section>
</li>
<li>
<section class="detail" id="internalListeners">
<h3>internalListeners</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.simulation.engine.InternalEngineListener&gt;</span> <span class="element-name">internalListeners</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor)">
<h3>ExecutionEngine</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">ExecutionEngine</span><wbr/><span class="parameters">(<a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a> engineDescriptor)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engineDescriptor</code> - the given engine's descriptor.</dd>
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
<section class="detail" id="getEngineDescriptor()">
<h3>getEngineDescriptor</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></span> <span class="element-name">getEngineDescriptor</span>()</div>
<div class="block">ExecutionEngineDescriptor getter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ExecutionEngineDescriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnimationController()">
<h3>getAnimationController</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.simulation.engine.EngineAnimationController</span> <span class="element-name">getAnimationController</span>()</div>
</section>
</li>
<li>
<section class="detail" id="init(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>init</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Engine initialization.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>execute</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Engine execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onClose()">
<h3>onClose</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract</span> <span class="return-type">void</span> <span class="element-name">onClose</span>()</div>
<div class="block">Engine onClose.</div>
</section>
</li>
<li>
<section class="detail" id="internalInit(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>internalInit</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">internalInit</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Engine internal initialization.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalExecute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>internalExecute</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">internalExecute</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Engine internal execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internalOnClose()">
<h3>internalOnClose</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">void</span> <span class="element-name">internalOnClose</span>()</div>
<div class="block">Engine internal onClose.</div>
</section>
</li>
<li>
<section class="detail" id="isClosing()">
<h3>isClosing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isClosing</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isClosed()">
<h3>isClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isClosed</span>()</div>
</section>
</li>
<li>
<section class="detail" id="destroyObject()">
<h3>destroyObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroyObject</span>()</div>
<div class="block">Destroys object.</div>
</section>
</li>
<li>
<section class="detail" id="addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener)">
<h3>addEngineListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEngineListener</span><wbr/><span class="parameters">(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener)</span></div>
<div class="block">Add the specified engine listener to the storing engine listener list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified engine listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener,int)">
<h3>addEngineListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEngineListener</span><wbr/><span class="parameters">(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener,
 int index)</span></div>
<div class="block">Add the specified engine listener to the storing engine listener list with specified position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified engine listener</dd>
<dd><code>index</code> - the index to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener)">
<h3>removeEngineListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeEngineListener</span><wbr/><span class="parameters">(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener)</span></div>
<div class="block">Remove the specified engine listener from the storing engine listener list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified engine listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener)">
<h3>addInternalEngineListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInternalEngineListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)</span></div>
<div class="block">Add the specified internal engine listener to the storing engine listener list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified internal engine listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener,int)">
<h3>addInternalEngineListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInternalEngineListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener,
 int index)</span></div>
<div class="block">Add the specified internal engine listener to the storing internal engine listener list with specified position.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified internal engine listener</dd>
<dd><code>index</code> - the index to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeInternalEngineListener(com.nomagic.magicdraw.simulation.engine.InternalEngineListener)">
<h3>removeInternalEngineListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeInternalEngineListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.simulation.engine.InternalEngineListener listener)</span></div>
<div class="block">Remove the specified internal engine listener from the storing internal engine listener list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified internal engine listener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEngineListeners()">
<h3>getEngineListeners</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a>&gt;</span> <span class="element-name">getEngineListeners</span>()</div>
<div class="block">Get the engine listener list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the engine listener list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInternalEngineListeners()">
<h3>getInternalEngineListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.simulation.engine.InternalEngineListener&gt;</span> <span class="element-name">getInternalEngineListeners</span>()</div>
<div class="block">Get the engine listener list.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the engine listener list.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>activateElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activateElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</span></div>
<div class="block">Activate the element, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
<dd><code>c</code> - the passing values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.data.ActivationInfo)">
<h3>activateElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activateElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)</span></div>
<div class="block">Activate the element, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
<dd><code>info</code> - ActivationInfo</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>deactivateElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deactivateElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</span></div>
<div class="block">Deactivate the element, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
<dd><code>c</code> - the passing values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.magicdraw.simulation.execution.data.ActivationInfo)">
<h3>deactivateElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deactivateElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 com.nomagic.magicdraw.simulation.execution.data.ActivationInfo info)</span></div>
<div class="block">Deactivate the element, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
<dd><code>info</code> - ActivationInfo</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="triggerEvent(java.lang.String)">
<h3>triggerEvent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">triggerEvent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> event)</span></div>
<div class="block">Trigger the specified event, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - the specified event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAvailableSignals()">
<h3>getAvailableSignals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</span> <span class="element-name">getAvailableSignals</span>()</div>
<div class="block">Returns all available signals at current state. For the state machine, available signals can
 change current state to another state.<br/>
<br/>
 Default implementation returns an empty Set.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the available signals at current state.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValuesAsString(java.util.Collection)">
<h3>getValuesAsString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getValuesAsString</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="block">Get the string of the given collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>values</code> - the specified collection</dd>
<dt>Returns:</dt>
<dd>the string value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNormativeValues(java.util.Collection)">
<h3>getNormativeValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNormativeValues</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="block">Get the normative values collection from the specified value collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>values</code> - the specified value collection.</dd>
<dt>Returns:</dt>
<dd>the normative values collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStatus()">
<h3>getStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.simulation.engine.ExecutionStatus</span> <span class="element-name">getStatus</span>()</div>
<div class="block">Get the execution status.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the execution status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSession(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>setSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSession</span><wbr/><span class="parameters">(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="block"><code>Session</code> setter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>session</code> - the specified session</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSession()">
<h3>getSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getSession</span>()</div>
<div class="block"><code>Session</code> getter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>Session</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStatus(com.nomagic.magicdraw.simulation.engine.ExecutionStatus)">
<h3>setStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStatus</span><wbr/><span class="parameters">(com.nomagic.magicdraw.simulation.engine.ExecutionStatus status)</span></div>
<div class="block">Set status.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>status</code> - the specified status</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveElements()">
<h3>getActiveElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getActiveElements</span>()</div>
<div class="block">Gets active elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Active elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastVisitedElement()">
<h3>getLastVisitedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getLastVisitedElement</span>()</div>
<div class="block">Gets last visited element - element that was activated last and is already deactivated</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Last visited element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="interrupt()">
<h3>interrupt</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">interrupt</span>()</div>
<div class="block">Interrupt this engine.</div>
</section>
</li>
<li>
<section class="detail" id="isInterrupted()">
<h3>isInterrupted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInterrupted</span>()</div>
<div class="block">return boolean value of isInterrupted.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>boolean value of isInterrupted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExecutionFinished()">
<h3>isExecutionFinished</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExecutionFinished</span>()</div>
<div class="block">Get executionFinished.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>executionFinished</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runWhenExecutionFinished(java.lang.Runnable)">
<h3>runWhenExecutionFinished</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">runWhenExecutionFinished</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="block">Thread safe way to ensure that runnable will be called exactly once when engine has finished execution</div>
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
