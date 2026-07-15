# JAVA OPENAPI: SimulationSession (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/execution/session/SimulationSession.html
- source_path: `com/nomagic/magicdraw/simulation/execution/session/SimulationSession.html`
- source_sha256: `9972da609b5f10ad7051ebe21810cbb099e61ba1ce8796b0dba8c6ed3ba7881d`
- captured_utc: `2026-07-14T16:58:02.676588+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.execution.session](package-summary.html)

## Class SimulationSession

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.execution.session.SimulationSession

@OpenApiAllpublic abstract classSimulationSession
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
The SimulationSession class.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[element](#element)`
The execution element.
`protected [ExecutionEngine](../../engine/ExecutionEngine.html)`
`[engine](#engine)`
The execution engine.
`protected [SimulationExecution](../SimulationExecution.html)`
`[execution](#execution)`
Execution that this session is part of.
`protected [AtomicBoolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html)`
`[isClosed](#isClosed)`
The is closed flag.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[SimulationSession](#%3Cinit%3E(boolean))(boolean isMainSession)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Return the execution element.
`[ExecutionEngine](../../engine/ExecutionEngine.html)`
`[getEngine](#getEngine())()`
Return the execution engine.
`[SimulationExecution](../SimulationExecution.html)`
`[getExecution](#getExecution())()`
Gets the execution of this SimulationSession.
`abstract [SimulationSession](SimulationSession.html)`
`[getParent](#getParent())()`

`boolean`
`[isClosed](#isClosed())()`

`abstract boolean`
`[isClosingOrClosed](#isClosingOrClosed())()`

`boolean`
`[isMainSession](#isMainSession())()`

`void`
`[setElement](#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Set the execution element.
`void`
`[setEngine](#setEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngine))([ExecutionEngine](../../engine/ExecutionEngine.html) engine)`
Set the execution engine.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
element
protected [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element
The execution element.
engine
protected [ExecutionEngine](../../engine/ExecutionEngine.html) engine
The execution engine.
execution
protected [SimulationExecution](../SimulationExecution.html) execution
Execution that this session is part of. [`SimulationExecution`](../SimulationExecution.html) may have multiple sessions
isClosed
protected [AtomicBoolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html) isClosed
The is closed flag. Session is closed when terminated on has run to completion
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationSession
protected SimulationSession(boolean isMainSession)
 ============ METHOD DETAIL ========== 
Method Details
getElement
public [Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Return the execution element.
Returns:
the execution element
setElement
public void setElement([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Set the execution element.
Parameters:
`element` - the element to set
getEngine
public [ExecutionEngine](../../engine/ExecutionEngine.html) getEngine()
Return the execution engine.
Returns:
the execution engine
setEngine
public void setEngine([ExecutionEngine](../../engine/ExecutionEngine.html) engine)
Set the execution engine.
Parameters:
`engine` - the engine to set
getExecution
public [SimulationExecution](../SimulationExecution.html) getExecution()
Gets the execution of this SimulationSession.
Returns:
the execution of this SimulationSession
isClosed
public boolean isClosed()
Returns:
true whether the simulation session is closed/terminated or not.
isClosingOrClosed
public abstract boolean isClosingOrClosed()
Returns:
true whether the simulation is currently closing or is already closed
getParent
@CheckForNullpublic abstract [SimulationSession](SimulationSession.html) getParent()
isMainSession
public boolean isMainSession()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.execution.session</a></div>
<h1 class="title" title="Class SimulationSession">Class SimulationSession</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.execution.session.SimulationSession</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">SimulationSession</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The SimulationSession class.</div>
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
<div class="col-first even-row-color"><code>protected <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#element">element</a></code></div>
<div class="col-last even-row-color">
<div class="block">The execution element.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a href="../../engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#engine">engine</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The execution engine.</div>
</div>
<div class="col-first even-row-color"><code>protected <a href="../SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#execution">execution</a></code></div>
<div class="col-last even-row-color">
<div class="block">Execution that this session is part of.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html" title="class or interface in java.util.concurrent.atomic">AtomicBoolean</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isClosed">isClosed</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The is closed flag.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean)">SimulationSession</a><wbr/>(boolean isMainSession)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the execution element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEngine()">getEngine</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the execution engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecution()">getExecution</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the execution of this SimulationSession.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isClosed()">isClosed</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isClosingOrClosed()">isClosingOrClosed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMainSession()">isMainSession</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setElement</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the execution element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngine)">setEngine</a><wbr/>(<a href="../../engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a> engine)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the execution engine.</div>
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
<section class="detail" id="element">
<h3>element</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">element</span></div>
<div class="block">The execution element.</div>
</section>
</li>
<li>
<section class="detail" id="engine">
<h3>engine</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a></span> <span class="element-name">engine</span></div>
<div class="block">The execution engine.</div>
</section>
</li>
<li>
<section class="detail" id="execution">
<h3>execution</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a></span> <span class="element-name">execution</span></div>
<div class="block">Execution that this session is part of. <a href="../SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution"><code>SimulationExecution</code></a> may have multiple sessions</div>
</section>
</li>
<li>
<section class="detail" id="isClosed">
<h3>isClosed</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html" title="class or interface in java.util.concurrent.atomic">AtomicBoolean</a></span> <span class="element-name">isClosed</span></div>
<div class="block">The is closed flag. Session is closed when terminated on has run to completion</div>
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
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>SimulationSession</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">SimulationSession</span><wbr/><span class="parameters">(boolean isMainSession)</span></div>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Return the execution element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the execution element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setElement</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setElement</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Set the execution element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEngine()">
<h3>getEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a></span> <span class="element-name">getEngine</span>()</div>
<div class="block">Return the execution engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the execution engine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEngine(com.nomagic.magicdraw.simulation.engine.ExecutionEngine)">
<h3>setEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEngine</span><wbr/><span class="parameters">(<a href="../../engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a> engine)</span></div>
<div class="block">Set the execution engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - the engine to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExecution()">
<h3>getExecution</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a></span> <span class="element-name">getExecution</span>()</div>
<div class="block">Gets the execution of this SimulationSession.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the execution of this SimulationSession</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isClosed()">
<h3>isClosed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isClosed</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true whether the simulation session is closed/terminated or not.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isClosingOrClosed()">
<h3>isClosingOrClosed</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">boolean</span> <span class="element-name">isClosingOrClosed</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true whether the simulation is currently closing or is already closed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public abstract</span> <span class="return-type"><a href="SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getParent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isMainSession()">
<h3>isMainSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMainSession</span>()</div>
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
