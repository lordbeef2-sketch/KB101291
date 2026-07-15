# JAVA OPENAPI: Ports (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Ports.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Ports.html`
- source_sha256: `90dbb1ff1367526b0492feab20ef579833f5ef5a06bbc1390d096405e740c81e`
- captured_utc: `2026-07-14T16:45:02.555037+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Ports

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Ports

@OpenApiAllpublic classPorts
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for [`PortDefinition`](sysml/PortDefinition.html) or [`PortUsage`](sysml/PortUsage.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Ports](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[isOwningTypePortUsageOrDefinition](#isOwningTypePortUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the owning type of the given feature is a
 [`PortUsage`](sysml/PortUsage.html) or [`PortDefinition`](sysml/PortDefinition.html).
`static boolean`
`[isPortUsageOrDefinition](#isPortUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the given element is a [`PortUsage`](sysml/PortUsage.html) or
 [`PortDefinition`](sysml/PortDefinition.html).
`static boolean`
`[isPortUsageOrDefinition](#isPortUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a [`PortUsage`](sysml/PortUsage.html)
 or [`PortDefinition`](sysml/PortDefinition.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Ports
public Ports()
 ============ METHOD DETAIL ========== 
Method Details
isOwningTypePortUsageOrDefinition
public static boolean isOwningTypePortUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the owning type of the given feature is a
 [`PortUsage`](sysml/PortUsage.html) or [`PortDefinition`](sysml/PortDefinition.html).
Parameters:
`feature` - the feature whose owning type is checked
Returns:
true if the owning type is a port usage or definition
isPortUsageOrDefinition
public static boolean isPortUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the given element is a [`PortUsage`](sysml/PortUsage.html) or
 [`PortDefinition`](sysml/PortDefinition.html).
Parameters:
`element` - the element to check
Returns:
true if the element is a port usage or definition
isPortUsageOrDefinition
public static boolean isPortUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a [`PortUsage`](sysml/PortUsage.html)
 or [`PortDefinition`](sysml/PortDefinition.html).
Parameters:
`eClass` - the class to check
Returns:
true if the class is a port usage or definition

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Ports">Class Ports</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Ports</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Ports</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for  <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a> or <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Ports</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypePortUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypePortUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the owning type of the given feature is a
 <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a> or <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPortUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isPortUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element is a <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a> or
 <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPortUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isPortUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a>
 or <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
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
<h3>Ports</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Ports</span>()</div>
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
<section class="detail" id="isOwningTypePortUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypePortUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypePortUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the owning type of the given feature is a
 <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a> or <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature whose owning type is checked</dd>
<dt>Returns:</dt>
<dd>true if the owning type is a port usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPortUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isPortUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPortUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the given element is a <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a> or
 <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is a port usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPortUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isPortUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPortUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a <a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortUsage</code></a>
 or <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PortDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is a port usage or definition</dd>
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
