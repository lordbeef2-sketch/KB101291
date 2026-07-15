# JAVA OPENAPI: MetadataAccessExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/MetadataAccessExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/MetadataAccessExpressions.html`
- source_sha256: `b14c68eba4cfca76ec349343e4d139b0fabfff8c95080e147b0b803616300722`
- captured_utc: `2026-07-14T16:44:47.713838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class MetadataAccessExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.MetadataAccessExpressions

@OpenApiAllpublic classMetadataAccessExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`MetadataAccessExpression`](kerml/MetadataAccessExpression.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MetadataAccessExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MetadataAccessExpression](kerml/MetadataAccessExpression.html)`
`[createMetadataAccessExpression](#createMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) referencedElement)`
Creates a new metadata access expression referencing the given element.
`static [Membership](kerml/Membership.html)`
`[getReferencedElementMembership](#getReferencedElementMembership(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression))([MetadataAccessExpression](kerml/MetadataAccessExpression.html) expression)`
Returns the membership that stores the referenced element
 for the given metadata access expression.
`static void`
`[setReferencedElement](#setReferencedElement(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,com.dassault_systemes.modeler.kerml.model.kerml.Element))([MetadataAccessExpression](kerml/MetadataAccessExpression.html) expression,
 [Element](kerml/Element.html) referencedElement)`
Sets the referenced element of the given metadata access expression.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MetadataAccessExpressions
public MetadataAccessExpressions()
 ============ METHOD DETAIL ========== 
Method Details
setReferencedElement
public static void setReferencedElement([MetadataAccessExpression](kerml/MetadataAccessExpression.html) expression,
 @CheckForNull
 [Element](kerml/Element.html) referencedElement)
Sets the referenced element of the given metadata access expression.
 Creates or reuses an appropriate membership to store the reference.
Parameters:
`expression` - the metadata access expression to modify
`referencedElement` - the element to reference, or null to clear
createMetadataAccessExpression
public static [MetadataAccessExpression](kerml/MetadataAccessExpression.html) createMetadataAccessExpression([Element](kerml/Element.html) referencedElement)
Creates a new metadata access expression referencing the given element.
Parameters:
`referencedElement` - the element to reference
Returns:
a newly created metadata access expression
getReferencedElementMembership
@CheckForNullpublic static [Membership](kerml/Membership.html) getReferencedElementMembership([MetadataAccessExpression](kerml/MetadataAccessExpression.html) expression)
Returns the membership that stores the referenced element
 for the given metadata access expression.
Parameters:
`expression` - the metadata access expression
Returns:
the membership holding the referenced element, or null if none exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class MetadataAccessExpressions">Class MetadataAccessExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.MetadataAccessExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MetadataAccessExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>MetadataAccessExpression</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MetadataAccessExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.Element)">createMetadataAccessExpression</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> referencedElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new metadata access expression referencing the given element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReferencedElementMembership(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression)">getReferencedElementMembership</a><wbr/>(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the membership that stores the referenced element
 for the given metadata access expression.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferencedElement(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,com.dassault_systemes.modeler.kerml.model.kerml.Element)">setReferencedElement</a><wbr/>(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> expression,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> referencedElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referenced element of the given metadata access expression.</div>
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
<h3>MetadataAccessExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MetadataAccessExpressions</span>()</div>
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
<section class="detail" id="setReferencedElement(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setReferencedElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReferencedElement</span><wbr/><span class="parameters">(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> expression,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> referencedElement)</span></div>
<div class="block">Sets the referenced element of the given metadata access expression.
 Creates or reuses an appropriate membership to store the reference.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the metadata access expression to modify</dd>
<dd><code>referencedElement</code> - the element to reference, or null to clear</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>createMetadataAccessExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a></span> <span class="element-name">createMetadataAccessExpression</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> referencedElement)</span></div>
<div class="block">Creates a new metadata access expression referencing the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referencedElement</code> - the element to reference</dd>
<dt>Returns:</dt>
<dd>a newly created metadata access expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferencedElementMembership(com.dassault_systemes.modeler.kerml.model.kerml.MetadataAccessExpression)">
<h3>getReferencedElementMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getReferencedElementMembership</span><wbr/><span class="parameters">(<a href="kerml/MetadataAccessExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">MetadataAccessExpression</a> expression)</span></div>
<div class="block">Returns the membership that stores the referenced element
 for the given metadata access expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the metadata access expression</dd>
<dt>Returns:</dt>
<dd>the membership holding the referenced element, or null if none exists</dd>
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
