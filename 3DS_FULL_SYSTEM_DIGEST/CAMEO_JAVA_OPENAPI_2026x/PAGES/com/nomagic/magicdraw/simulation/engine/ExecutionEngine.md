# JAVA OPENAPI: ExecutionEngine (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/engine/ExecutionEngine.html
- source_path: `com/nomagic/magicdraw/simulation/engine/ExecutionEngine.html`
- source_sha256: `d9842afe5bcda1f04b5524c6e3be91af3033d52ca26acb2145b1f18e9078ed57`
- captured_utc: `2026-07-14T16:58:02.443585+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.engine](package-summary.html)

## Class ExecutionEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.engine.ExecutionEngine

@OpenApipublic abstract classExecutionEngine
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
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
`[activateElement](#activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> c)`
Activate the element, it delegates to all storing engine listener.
`void`
`[addEngineListener](#addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener))([EngineListener](EngineListener.html) listener)`
Add the specified engine listener to the storing engine listener list.
`void`
`[deactivateElement](#deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> c)`
Deactivate the element, it delegates to all storing engine listener.
`abstract void`
`[execute](#execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Engine execution.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getActiveElements](#getActiveElements())()`
Gets active elements.
`[ExecutionEngineDescriptor](ExecutionEngineDescriptor.html)`
`[getEngineDescriptor](#getEngineDescriptor())()`
ExecutionEngineDescriptor getter.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EngineListener](EngineListener.html)>`
`[getEngineListeners](#getEngineListeners())()`
Get the engine listener list.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getLastVisitedElement](#getLastVisitedElement())()`
Gets last visited element - element that was activated last and is already deactivated
`abstract void`
`[init](#init(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Engine initialization.
`abstract void`
`[onClose](#onClose())()`
Engine onClose.
`void`
`[removeEngineListener](#removeEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener))([EngineListener](EngineListener.html) listener)`
Remove the specified engine listener from the storing engine listener list.
`void`
`[triggerEvent](#triggerEvent(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) event)`
Trigger the specified event, it delegates to all storing engine listener.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
session
@OpenApiprotected [SimulationSession](../execution/session/SimulationSession.html) session
a reference to the running session of this engine.
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
addEngineListener
@OpenApipublic void addEngineListener([EngineListener](EngineListener.html) listener)
Add the specified engine listener to the storing engine listener list.
Parameters:
`listener` - the specified engine listener
removeEngineListener
@OpenApipublic void removeEngineListener([EngineListener](EngineListener.html) listener)
Remove the specified engine listener from the storing engine listener list.
Parameters:
`listener` - the specified engine listener
getEngineListeners
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[EngineListener](EngineListener.html)> getEngineListeners()
Get the engine listener list.
Returns:
the engine listener list.
activateElement
@OpenApipublic void activateElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> c)
Activate the element, it delegates to all storing engine listener.
Parameters:
`element` - the specified element
`c` - the passing values
deactivateElement
@OpenApipublic void deactivateElement([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<?> c)
Deactivate the element, it delegates to all storing engine listener.
Parameters:
`element` - the specified element
`c` - the passing values
triggerEvent
@OpenApipublic void triggerEvent([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) event)
Trigger the specified event, it delegates to all storing engine listener.
Parameters:
`event` - the specified event
getActiveElements
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getActiveElements()
Gets active elements.
Returns:
Active elements
getLastVisitedElement
@OpenApi
@CheckForNullpublic [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getLastVisitedElement()
Gets last visited element - element that was activated last and is already deactivated
Returns:
Last visited element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.engine</a></div>
<h1 class="title" title="Class ExecutionEngine">Class ExecutionEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.engine.ExecutionEngine</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">ExecutionEngine</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-first even-row-color"><code>protected <a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#session">session</a></code></div>
<div class="col-last even-row-color">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">activateElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Activate the element, it delegates to all storing engine listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener)">addEngineListener</a><wbr/>(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the specified engine listener to the storing engine listener list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">deactivateElement</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Deactivate the element, it delegates to all storing engine listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#execute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">execute</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Engine execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getActiveElements()">getActiveElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets active elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEngineDescriptor()">getEngineDescriptor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">ExecutionEngineDescriptor getter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEngineListeners()">getEngineListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the engine listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastVisitedElement()">getLastVisitedElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets last visited element - element that was activated last and is already deactivated</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#init(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">init</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Engine initialization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onClose()">onClose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Engine onClose.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeEngineListener(com.nomagic.magicdraw.simulation.engine.EngineListener)">removeEngineListener</a><wbr/>(<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove the specified engine listener from the storing engine listener list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#triggerEvent(java.lang.String)">triggerEvent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Trigger the specified event, it delegates to all storing engine listener.</div>
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
<section class="detail" id="getEngineListeners()">
<h3>getEngineListeners</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EngineListener.html" title="interface in com.nomagic.magicdraw.simulation.engine">EngineListener</a>&gt;</span> <span class="element-name">getEngineListeners</span>()</div>
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
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</span></div>
<div class="block">Activate the element, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
<dd><code>c</code> - the passing values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deactivateElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>deactivateElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deactivateElement</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; c)</span></div>
<div class="block">Deactivate the element, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the specified element</dd>
<dd><code>c</code> - the passing values</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="triggerEvent(java.lang.String)">
<h3>triggerEvent</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">triggerEvent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> event)</span></div>
<div class="block">Trigger the specified event, it delegates to all storing engine listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>event</code> - the specified event</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getActiveElements()">
<h3>getActiveElements</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getActiveElements</span>()</div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
