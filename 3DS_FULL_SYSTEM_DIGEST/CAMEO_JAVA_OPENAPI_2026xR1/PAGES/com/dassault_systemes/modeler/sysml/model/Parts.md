# JAVA OPENAPI: Parts (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Parts.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Parts.html`
- source_sha256: `c5a07110e3b245b892f9f5e5fd2affb373e0aaa1ac6cd2ce6dcd921937875a2b`
- captured_utc: `2026-07-14T16:45:02.489034+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Parts

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Parts

@OpenApiAllpublic classParts
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for identifying part usages and
 part definitions, as well as retrieving owned parts from a type.

 In SysML, a part may appear either as a [`PartUsage`](sysml/PartUsage.html) or a
 [`PartDefinition`](sysml/PartDefinition.html). These helpers make it easy to detect and work
 with both forms.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Parts](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)>`
`[getOwnedPart](#getOwnedPart(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the parts owned by the given type.
`static boolean`
`[isOwningTypePartUsageOrDefinition](#isOwningTypePartUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the owning type of the given feature is a
 [`PartUsage`](sysml/PartUsage.html) or [`PartDefinition`](sysml/PartDefinition.html).
`static boolean`
`[isPartUsageOrDefinition](#isPartUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the given element is a [`PartUsage`](sysml/PartUsage.html) or
 [`PartDefinition`](sysml/PartDefinition.html).
`static boolean`
`[isPurePartDefinition](#isPurePartDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a pure part definition.
`static boolean`
`[isPurePartUsage](#isPurePartUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a pure part usage.
`static boolean`
`[isPurePartUsageOrDefinition](#isPurePartUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a pure part usage or
 pure part definition.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Parts
public Parts()
 ============ METHOD DETAIL ========== 
Method Details
isOwningTypePartUsageOrDefinition
public static boolean isOwningTypePartUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the owning type of the given feature is a
 [`PartUsage`](sysml/PartUsage.html) or [`PartDefinition`](sysml/PartDefinition.html).
Parameters:
`feature` - the feature whose owning type is checked
Returns:
true if the owning type is a part usage or definition
isPartUsageOrDefinition
public static boolean isPartUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the given element is a [`PartUsage`](sysml/PartUsage.html) or
 [`PartDefinition`](sysml/PartDefinition.html).
Parameters:
`element` - the element to check
Returns:
true if the element is a part usage or definition
getOwnedPart
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[PartUsage](sysml/PartUsage.html)> getOwnedPart([Type](../../kerml/model/kerml/Type.html) type)
Returns the parts owned by the given type. For part definitions,
 this returns the owned parts; for part usages, this returns the
 nested parts.
Parameters:
`type` - the type whose parts are requested
Returns:
list of owned or nested parts
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the type is not a part usage or definition
isPurePartUsageOrDefinition
public static boolean isPurePartUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a pure part usage or
 pure part definition. “Pure” means the EClass matches the SysML
 metaclass exactly.
Parameters:
`eClass` - the class to check
Returns:
true if the class is a pure part usage or definition
isPurePartDefinition
public static boolean isPurePartDefinition(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a pure part definition.
Parameters:
`eClass` - the class to check
Returns:
true if pure part definition
isPurePartUsage
public static boolean isPurePartUsage(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a pure part usage.
Parameters:
`eClass` - the class to check
Returns:
true if pure part usage

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Parts">Class Parts</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Parts</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Parts</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for identifying part usages and
 part definitions, as well as retrieving owned parts from a type.

 <p>In SysML, a part may appear either as a <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> or a
 <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>. These helpers make it easy to detect and work
 with both forms.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Parts</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedPart(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedPart</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the parts owned by the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypePartUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypePartUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the owning type of the given feature is a
 <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> or <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPartUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isPartUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element is a <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> or
 <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPurePartDefinition(org.eclipse.emf.ecore.EClass)">isPurePartDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a pure part definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPurePartUsage(org.eclipse.emf.ecore.EClass)">isPurePartUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a pure part usage.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPurePartUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isPurePartUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a pure part usage or
 pure part definition.</div>
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
<h3>Parts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Parts</span>()</div>
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
<section class="detail" id="isOwningTypePartUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypePartUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypePartUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the owning type of the given feature is a
 <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> or <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature whose owning type is checked</dd>
<dt>Returns:</dt>
<dd>true if the owning type is a part usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPartUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isPartUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPartUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the given element is a <a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartUsage</code></a> or
 <a href="sysml/PartDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>PartDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is a part usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedPart(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedPart</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/PartUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PartUsage</a>&gt;</span> <span class="element-name">getOwnedPart</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the parts owned by the given type. For part definitions,
 this returns the owned parts; for part usages, this returns the
 nested parts.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose parts are requested</dd>
<dt>Returns:</dt>
<dd>list of owned or nested parts</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the type is not a part usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPurePartUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isPurePartUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPurePartUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a pure part usage or
 pure part definition. “Pure” means the EClass matches the SysML
 metaclass exactly.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is a pure part usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPurePartDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isPurePartDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPurePartDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a pure part definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if pure part definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPurePartUsage(org.eclipse.emf.ecore.EClass)">
<h3>isPurePartUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPurePartUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a pure part usage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if pure part usage</dd>
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
