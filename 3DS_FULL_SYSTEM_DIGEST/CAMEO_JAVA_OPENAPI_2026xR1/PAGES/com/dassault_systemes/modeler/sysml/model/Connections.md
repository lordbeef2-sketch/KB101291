# JAVA OPENAPI: Connections (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Connections.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Connections.html`
- source_sha256: `b5fc3389b2ed7a38a0e5716d8616e6fc76e2f30e4abaa80003d017bbd7b4ffdd`
- captured_utc: `2026-07-14T16:45:02.288033+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Connections

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Connections

@OpenApiAllpublic classConnections
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for identifying connection- and connector-related types and
 for determining connector arity semantics.
 These helpers centralize common checks involving [`ConnectionUsage`](sysml/ConnectionUsage.html),
 [`ConnectionDefinition`](sysml/ConnectionDefinition.html), [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html), and connector
 multiplicity semantics such as binary vs. n-ary connectors.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Connections](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[isAlwaysBinary](#isAlwaysBinary(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](../../kerml/model/kerml/Connector.html) connector)`
Returns whether the connector is always binary by definition.
`static boolean`
`[isConnectionDefinition](#isConnectionDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
`static boolean`
`[isConnectionUsageOrDefinition](#isConnectionUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is a [`ConnectionUsage`](sysml/ConnectionUsage.html) or
 [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
`static boolean`
`[isConnectorAsUsage](#isConnectorAsUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html).
`static boolean`
`[isConnectorAsUsageOrConnectionDefinition](#isConnectorAsUsageOrConnectionDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents either a
 [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html) or a [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
`static boolean`
`[isSemanticallyNary](#isSemanticallyNary(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](../../kerml/model/kerml/Connector.html) connector)`
Returns whether the given connector is semantically n-ary.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Connections
public Connections()
 ============ METHOD DETAIL ========== 
Method Details
isConnectionUsageOrDefinition
public static boolean isConnectionUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is a [`ConnectionUsage`](sysml/ConnectionUsage.html) or
 [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is a connection usage or definition
isConnectorAsUsageOrConnectionDefinition
public static boolean isConnectorAsUsageOrConnectionDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents either a
 [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html) or a [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a connector-as-usage or connection definition
isConnectorAsUsage
public static boolean isConnectorAsUsage(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a [`ConnectorAsUsage`](sysml/ConnectorAsUsage.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a connector-as-usage
isConnectionDefinition
public static boolean isConnectionDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a [`ConnectionDefinition`](sysml/ConnectionDefinition.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a connection definition
isSemanticallyNary
public static boolean isSemanticallyNary([Connector](../../kerml/model/kerml/Connector.html) connector)
Returns whether the given connector is semantically n-ary.
 A connector is considered n-ary when it is not restricted to always
 being binary and its end features indicate n-ary structure.
Parameters:
`connector` - the connector to test
Returns:
`true` if the connector is semantically n-ary
isAlwaysBinary
public static boolean isAlwaysBinary([Connector](../../kerml/model/kerml/Connector.html) connector)
Returns whether the connector is always binary by definition.
 Certain connector types—such as [`AllocationUsage`](sysml/AllocationUsage.html), [`Flow`](../../kerml/model/kerml/Flow.html),
 [`Succession`](../../kerml/model/kerml/Succession.html), and [`BindingConnector`](../../kerml/model/kerml/BindingConnector.html)—are inherently binary
 regardless of their end feature structure.
Parameters:
`connector` - the connector to test
Returns:
`true` if the connector is always binary

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Connections">Class Connections</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Connections</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Connections</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for identifying connection- and connector-related types and
 for determining connector arity semantics.
 <p>
 These helpers centralize common checks involving <a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionUsage</code></a>,
 <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>, <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a>, and connector
 multiplicity semantics such as binary vs. n-ary connectors.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Connections</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlwaysBinary(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">isAlwaysBinary</a><wbr/>(<a href="../../kerml/model/kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the connector is always binary by definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectionDefinition(org.eclipse.emf.ecore.EClass)">isConnectionDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectionUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isConnectionUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is a <a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionUsage</code></a> or
 <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectorAsUsage(org.eclipse.emf.ecore.EClass)">isConnectorAsUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectorAsUsageOrConnectionDefinition(org.eclipse.emf.ecore.EClass)">isConnectorAsUsageOrConnectionDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents either a
 <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a> or a <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemanticallyNary(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">isSemanticallyNary</a><wbr/>(<a href="../../kerml/model/kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given connector is semantically n-ary.</div>
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
<h3>Connections</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Connections</span>()</div>
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
<section class="detail" id="isConnectionUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isConnectionUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConnectionUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is a <a href="sysml/ConnectionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionUsage</code></a> or
 <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a connection usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnectorAsUsageOrConnectionDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isConnectorAsUsageOrConnectionDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConnectorAsUsageOrConnectionDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents either a
 <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a> or a <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a connector-as-usage or connection definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnectorAsUsage(org.eclipse.emf.ecore.EClass)">
<h3>isConnectorAsUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConnectorAsUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a <a href="sysml/ConnectorAsUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectorAsUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a connector-as-usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnectionDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isConnectionDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConnectionDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a <a href="sysml/ConnectionDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConnectionDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a connection definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemanticallyNary(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>isSemanticallyNary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSemanticallyNary</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns whether the given connector is semantically n-ary.
 A connector is considered n-ary when it is not restricted to always
 being binary and its end features indicate n-ary structure.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the connector is semantically n-ary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAlwaysBinary(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>isAlwaysBinary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAlwaysBinary</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns whether the connector is always binary by definition.
 <p>
 Certain connector types—such as <a href="sysml/AllocationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AllocationUsage</code></a>, <a href="../../kerml/model/kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Flow</code></a>,
 <a href="../../kerml/model/kerml/Succession.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Succession</code></a>, and <a href="../../kerml/model/kerml/BindingConnector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>BindingConnector</code></a>—are inherently binary
 regardless of their end feature structure.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the connector is always binary</dd>
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
