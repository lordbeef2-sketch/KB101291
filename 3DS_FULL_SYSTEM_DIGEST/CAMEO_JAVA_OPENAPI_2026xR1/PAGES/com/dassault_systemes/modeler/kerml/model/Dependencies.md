# JAVA OPENAPI: Dependencies (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Dependencies.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Dependencies.html`
- source_sha256: `0c5b04e846d48633a5009f89b58c9989fcd498d794691331242d4e151989e421`
- captured_utc: `2026-07-14T16:44:47.322833+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Dependencies

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Dependencies

@OpenApiAllpublic classDependencies
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Dependency`](kerml/Dependency.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Dependencies](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[isBinary](#isBinary(com.dassault_systemes.modeler.kerml.model.kerml.Dependency))([Dependency](kerml/Dependency.html) dependency)`
Checks whether the dependency is binary, meaning it has at most one client
 and at most one supplier.
`static boolean`
`[isDependency](#isDependency(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a [`Dependency`](kerml/Dependency.html).
`static boolean`
`[isNary](#isNary(com.dassault_systemes.modeler.kerml.model.kerml.Dependency))([Dependency](kerml/Dependency.html) dependency)`
Checks whether the dependency is n‑ary, meaning it has more than one client
 or more than one supplier.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Dependency](kerml/Dependency.html)>`
`[streamOfOwnedOutgoingDependencies](#streamOfOwnedOutgoingDependencies(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) context)`
Returns a stream of all outgoing dependencies owned by the given context element.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Element](kerml/Element.html)>`
`[streamOfSuppliersOfOwnedOutgoingDependencies](#streamOfSuppliersOfOwnedOutgoingDependencies(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) context)`
Returns a stream of all supplier elements of outgoing dependencies
 owned by the given context element.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Dependencies
public Dependencies()
 ============ METHOD DETAIL ========== 
Method Details
isBinary
public static boolean isBinary([Dependency](kerml/Dependency.html) dependency)
Checks whether the dependency is binary, meaning it has at most one client
 and at most one supplier.
Parameters:
`dependency` - the dependency
Returns:
true if the dependency is binary
isNary
public static boolean isNary([Dependency](kerml/Dependency.html) dependency)
Checks whether the dependency is n‑ary, meaning it has more than one client
 or more than one supplier.
Parameters:
`dependency` - the dependency
Returns:
true if the dependency is n‑ary
isDependency
public static boolean isDependency(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a [`Dependency`](kerml/Dependency.html).
Parameters:
`eClass` - the class to check
Returns:
true if the class is a dependency
streamOfSuppliersOfOwnedOutgoingDependencies
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Element](kerml/Element.html)> streamOfSuppliersOfOwnedOutgoingDependencies([Element](kerml/Element.html) context)
Returns a stream of all supplier elements of outgoing dependencies
 owned by the given context element.
Parameters:
`context` - the element whose outgoing dependencies are examined
Returns:
stream of supplier elements
streamOfOwnedOutgoingDependencies
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Dependency](kerml/Dependency.html)> streamOfOwnedOutgoingDependencies([Element](kerml/Element.html) context)
Returns a stream of all outgoing dependencies owned by the given context element.
 Outgoing dependencies are those directly contained in [`Element.getOwnedElement()`](kerml/Element.html#getOwnedElement()).
Parameters:
`context` - the element whose outgoing dependencies are examined
Returns:
stream of owned outgoing dependencies

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Dependencies">Class Dependencies</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Dependencies</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Dependencies</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Dependency</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Dependencies</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isBinary(com.dassault_systemes.modeler.kerml.model.kerml.Dependency)">isBinary</a><wbr/>(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> dependency)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the dependency is binary, meaning it has at most one client
 and at most one supplier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isDependency(org.eclipse.emf.ecore.EClass)">isDependency</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a <a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Dependency</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNary(com.dassault_systemes.modeler.kerml.model.kerml.Dependency)">isNary</a><wbr/>(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> dependency)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the dependency is n‑ary, meaning it has more than one client
 or more than one supplier.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfOwnedOutgoingDependencies(com.dassault_systemes.modeler.kerml.model.kerml.Element)">streamOfOwnedOutgoingDependencies</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of all outgoing dependencies owned by the given context element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfSuppliersOfOwnedOutgoingDependencies(com.dassault_systemes.modeler.kerml.model.kerml.Element)">streamOfSuppliersOfOwnedOutgoingDependencies</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of all supplier elements of outgoing dependencies
 owned by the given context element.</div>
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
<h3>Dependencies</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Dependencies</span>()</div>
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
<section class="detail" id="isBinary(com.dassault_systemes.modeler.kerml.model.kerml.Dependency)">
<h3>isBinary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBinary</span><wbr/><span class="parameters">(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> dependency)</span></div>
<div class="block">Checks whether the dependency is binary, meaning it has at most one client
 and at most one supplier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dependency</code> - the dependency</dd>
<dt>Returns:</dt>
<dd>true if the dependency is binary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNary(com.dassault_systemes.modeler.kerml.model.kerml.Dependency)">
<h3>isNary</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNary</span><wbr/><span class="parameters">(<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a> dependency)</span></div>
<div class="block">Checks whether the dependency is n‑ary, meaning it has more than one client
 or more than one supplier.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dependency</code> - the dependency</dd>
<dt>Returns:</dt>
<dd>true if the dependency is n‑ary</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDependency(org.eclipse.emf.ecore.EClass)">
<h3>isDependency</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDependency</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a <a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Dependency</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is a dependency</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfSuppliersOfOwnedOutgoingDependencies(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>streamOfSuppliersOfOwnedOutgoingDependencies</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="element-name">streamOfSuppliersOfOwnedOutgoingDependencies</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</span></div>
<div class="block">Returns a stream of all supplier elements of outgoing dependencies
 owned by the given context element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the element whose outgoing dependencies are examined</dd>
<dt>Returns:</dt>
<dd>stream of supplier elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfOwnedOutgoingDependencies(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>streamOfOwnedOutgoingDependencies</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Dependency.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Dependency</a>&gt;</span> <span class="element-name">streamOfOwnedOutgoingDependencies</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context)</span></div>
<div class="block">Returns a stream of all outgoing dependencies owned by the given context element.
 Outgoing dependencies are those directly contained in <a href="kerml/Element.html#getOwnedElement()"><code>Element.getOwnedElement()</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the element whose outgoing dependencies are examined</dd>
<dt>Returns:</dt>
<dd>stream of owned outgoing dependencies</dd>
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
