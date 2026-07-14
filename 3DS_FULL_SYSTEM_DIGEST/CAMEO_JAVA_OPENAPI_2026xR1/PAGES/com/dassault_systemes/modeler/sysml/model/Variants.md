# JAVA OPENAPI: Variants (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Variants.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Variants.html`
- source_sha256: `46f25e3a1b60a32a3f15949ddb0d43964b180a2d591d3fc3d9cda4b59f47cce8`
- captured_utc: `2026-07-14T16:45:02.739038+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Variants

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Variants

@OpenApiAllpublic classVariants
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for working with Variants

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Variants](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Type](../../kerml/model/kerml/Type.html)`
`[getOwningVariation](#getOwningVariation(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership))([OwningMembership](../../kerml/model/kerml/OwningMembership.html) membership)`
Returns the type that owns the given variation membership.
`static [Type](../../kerml/model/kerml/Type.html)`
`[getOwningVariation](#getOwningVariation(com.dassault_systemes.modeler.sysml.model.sysml.Usage))([Usage](sysml/Usage.html) usage)`
Returns the type that owns the variation membership of the given usage,
 if any.
`static boolean`
`[isVariation](#isVariation(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Checks whether the given type represents a variation.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Variants
public Variants()
 ============ METHOD DETAIL ========== 
Method Details
isVariation
public static boolean isVariation([Type](../../kerml/model/kerml/Type.html) type)
Checks whether the given type represents a variation.
 A type is considered a variation if it is a [`Usage`](sysml/Usage.html) or
 [`Definition`](sysml/Definition.html) whose `isVariation` flag is set.
Parameters:
`type` - the type to check
Returns:
true if the type is a variation
getOwningVariation
@CheckForNullpublic static [Type](../../kerml/model/kerml/Type.html) getOwningVariation([Usage](sysml/Usage.html) usage)
Returns the type that owns the variation membership of the given usage,
 if any.
Parameters:
`usage` - the usage whose owning variation is requested
Returns:
owning variation type, or null if none exists
getOwningVariation
@CheckForNullpublic static [Type](../../kerml/model/kerml/Type.html) getOwningVariation(@CheckForNull
 [OwningMembership](../../kerml/model/kerml/OwningMembership.html) membership)
Returns the type that owns the given variation membership.
 A variation is owned when the membership is a [`VariantMembership`](sysml/VariantMembership.html)
 whose owning namespace is a [`Type`](../../kerml/model/kerml/Type.html).
Parameters:
`membership` - the owning membership
Returns:
owning variation type, or null if none exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Variants">Class Variants</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Variants</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Variants</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for working with Variants</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Variants</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwningVariation(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">getOwningVariation</a><wbr/>(<a href="../../kerml/model/kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the type that owns the given variation membership.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwningVariation(com.dassault_systemes.modeler.sysml.model.sysml.Usage)">getOwningVariation</a><wbr/>(<a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a> usage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the type that owns the variation membership of the given usage,
 if any.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isVariation(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isVariation</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given type represents a variation.</div>
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
<h3>Variants</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Variants</span>()</div>
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
<section class="detail" id="isVariation(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isVariation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isVariation</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Checks whether the given type represents a variation.
 A type is considered a variation if it is a <a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Usage</code></a> or
 <a href="sysml/Definition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>Definition</code></a> whose <code>isVariation</code> flag is set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to check</dd>
<dt>Returns:</dt>
<dd>true if the type is a variation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningVariation(com.dassault_systemes.modeler.sysml.model.sysml.Usage)">
<h3>getOwningVariation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getOwningVariation</span><wbr/><span class="parameters">(<a href="sysml/Usage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">Usage</a> usage)</span></div>
<div class="block">Returns the type that owns the variation membership of the given usage,
 if any.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usage</code> - the usage whose owning variation is requested</dd>
<dt>Returns:</dt>
<dd>owning variation type, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwningVariation(com.dassault_systemes.modeler.kerml.model.kerml.OwningMembership)">
<h3>getOwningVariation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getOwningVariation</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a> membership)</span></div>
<div class="block">Returns the type that owns the given variation membership.
 A variation is owned when the membership is a <a href="sysml/VariantMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>VariantMembership</code></a>
 whose owning namespace is a <a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Type</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the owning membership</dd>
<dt>Returns:</dt>
<dd>owning variation type, or null if none exists</dd>
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
