# JAVA OPENAPI: Exposes (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Exposes.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Exposes.html`
- source_sha256: `2e5bf13b4674059329323d2ae520bb1b4142fb10fcb5ff35e461a5e77f0201c2`
- captured_utc: `2026-07-14T16:45:02.352032+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Exposes

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Exposes

@OpenApiAllpublic classExposes
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for retrieving [`Expose`](sysml/Expose.html) imports owned by a [`Namespace`](../../kerml/model/kerml/Namespace.html).
 An `Expose` is a specialized form of import. These helpers provide
 convenient access to all expose imports owned directly by a namespace.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Exposes](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expose](sysml/Expose.html)>`
`[getOwnedExpose](#getOwnedExpose(com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Namespace](../../kerml/model/kerml/Namespace.html) namespace)`
Returns a list of all [`Expose`](sysml/Expose.html) imports owned by the given namespace.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Expose](sysml/Expose.html)>`
`[streamOfOwnedExpose](#streamOfOwnedExpose(com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Namespace](../../kerml/model/kerml/Namespace.html) namespace)`
Returns a stream of all [`Expose`](sysml/Expose.html) imports owned by the given namespace.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Exposes
public Exposes()
 ============ METHOD DETAIL ========== 
Method Details
streamOfOwnedExpose
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Expose](sysml/Expose.html)> streamOfOwnedExpose([Namespace](../../kerml/model/kerml/Namespace.html) namespace)
Returns a stream of all [`Expose`](sysml/Expose.html) imports owned by the given namespace.
Parameters:
`namespace` - the namespace whose expose imports are requested
Returns:
a stream of owned expose imports
getOwnedExpose
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expose](sysml/Expose.html)> getOwnedExpose([Namespace](../../kerml/model/kerml/Namespace.html) namespace)
Returns a list of all [`Expose`](sysml/Expose.html) imports owned by the given namespace.
Parameters:
`namespace` - the namespace whose expose imports are requested
Returns:
a list of owned expose imports

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Exposes">Class Exposes</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Exposes</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Exposes</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for retrieving <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a> imports owned by a <a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Namespace</code></a>.
 <p>
 An <code>Expose</code> is a specialized form of import. These helpers provide
 convenient access to all expose imports owned directly by a namespace.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Exposes</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedExpose(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">getOwnedExpose</a><wbr/>(<a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a list of all <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a> imports owned by the given namespace.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfOwnedExpose(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">streamOfOwnedExpose</a><wbr/>(<a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of all <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a> imports owned by the given namespace.</div>
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
<h3>Exposes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Exposes</span>()</div>
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
<section class="detail" id="streamOfOwnedExpose(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>streamOfOwnedExpose</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a>&gt;</span> <span class="element-name">streamOfOwnedExpose</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</span></div>
<div class="block">Returns a stream of all <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a> imports owned by the given namespace.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>namespace</code> - the namespace whose expose imports are requested</dd>
<dt>Returns:</dt>
<dd>a stream of owned expose imports</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedExpose(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>getOwnedExpose</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Expose</a>&gt;</span> <span class="element-name">getOwnedExpose</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace)</span></div>
<div class="block">Returns a list of all <a href="sysml/Expose.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Expose</code></a> imports owned by the given namespace.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>namespace</code> - the namespace whose expose imports are requested</dd>
<dt>Returns:</dt>
<dd>a list of owned expose imports</dd>
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
