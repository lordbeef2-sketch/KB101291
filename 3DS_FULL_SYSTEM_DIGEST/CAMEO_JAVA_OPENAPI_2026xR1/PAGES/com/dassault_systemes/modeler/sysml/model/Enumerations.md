# JAVA OPENAPI: Enumerations (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Enumerations.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Enumerations.html`
- source_sha256: `a719e90e57c5408f5b8cb04f9bf465adda6f750f95860c6d8f937a413d80b2ce`
- captured_utc: `2026-07-14T16:45:02.333034+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Enumerations

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Enumerations

@OpenApiAllpublic classEnumerations
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for identifying enumeration usages and definitions, and
 [`EnumerationUsage`](sysml/EnumerationUsage.html), [`EnumerationDefinition`](sysml/EnumerationDefinition.html), and their associated
 memberships.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Enumerations](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[isEnumerationDefinition](#isEnumerationDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents an [`EnumerationDefinition`](sysml/EnumerationDefinition.html).
`static boolean`
`[isEnumerationUsage](#isEnumerationUsage(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents an [`EnumerationUsage`](sysml/EnumerationUsage.html).
`static boolean`
`[isEnumerationUsageOrDefinition](#isEnumerationUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents either an
 [`EnumerationUsage`](sysml/EnumerationUsage.html) or an [`EnumerationDefinition`](sysml/EnumerationDefinition.html).
`static void`
`[setEnumerationFeatureValue](#setEnumerationFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage))([FeatureReferenceExpression](../../kerml/model/kerml/FeatureReferenceExpression.html) expression,
 [EnumerationUsage](sysml/EnumerationUsage.html) usage)`
Sets attribute's FeatureValue with EnumerationUsage as value.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Enumerations
public Enumerations()
 ============ METHOD DETAIL ========== 
Method Details
isEnumerationUsageOrDefinition
public static boolean isEnumerationUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents either an
 [`EnumerationUsage`](sysml/EnumerationUsage.html) or an [`EnumerationDefinition`](sysml/EnumerationDefinition.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is an enumeration usage or definition
isEnumerationUsage
public static boolean isEnumerationUsage(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents an [`EnumerationUsage`](sysml/EnumerationUsage.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is an enumeration usage
isEnumerationDefinition
public static boolean isEnumerationDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents an [`EnumerationDefinition`](sysml/EnumerationDefinition.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is an enumeration definition
setEnumerationFeatureValue
public static void setEnumerationFeatureValue([FeatureReferenceExpression](../../kerml/model/kerml/FeatureReferenceExpression.html) expression,
 [EnumerationUsage](sysml/EnumerationUsage.html) usage)
Sets attribute's FeatureValue with EnumerationUsage as value.
 Finds an existing or creates a new membership that connects the FeatureReferenceExpression and EnumerationUsage.
Parameters:
`expression` - feature value expression, see [`FeatureValues.getValueExpression(Feature)`](../../kerml/model/FeatureValues.html#getValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature))
`usage` - enumeration usage to set for expression

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Enumerations">Class Enumerations</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Enumerations</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Enumerations</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for identifying enumeration usages and definitions, and
 <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a>, <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>, and their associated
 memberships.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Enumerations</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnumerationDefinition(org.eclipse.emf.ecore.EClass)">isEnumerationDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents an <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnumerationUsage(org.eclipse.emf.ecore.EClass)">isEnumerationUsage</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents an <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnumerationUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isEnumerationUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents either an
 <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a> or an <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnumerationFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage)">setEnumerationFeatureValue</a><wbr/>(<a href="../../kerml/model/kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a> usage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets attribute's FeatureValue with EnumerationUsage as value.</div>
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
<h3>Enumerations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Enumerations</span>()</div>
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
<section class="detail" id="isEnumerationUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isEnumerationUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEnumerationUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents either an
 <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a> or an <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is an enumeration usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnumerationUsage(org.eclipse.emf.ecore.EClass)">
<h3>isEnumerationUsage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEnumerationUsage</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents an <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationUsage</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is an enumeration usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnumerationDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isEnumerationDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEnumerationDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents an <a href="sysml/EnumerationDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>EnumerationDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is an enumeration definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnumerationFeatureValue(com.dassault_systemes.modeler.kerml.model.kerml.FeatureReferenceExpression,com.dassault_systemes.modeler.sysml.model.sysml.EnumerationUsage)">
<h3>setEnumerationFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setEnumerationFeatureValue</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/FeatureReferenceExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureReferenceExpression</a> expression,
 <a href="sysml/EnumerationUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">EnumerationUsage</a> usage)</span></div>
<div class="block">Sets attribute's FeatureValue with EnumerationUsage as value.
 Finds an existing or creates a new membership that connects the FeatureReferenceExpression and EnumerationUsage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - feature value expression, see <a href="../../kerml/model/FeatureValues.html#getValueExpression(com.dassault_systemes.modeler.kerml.model.kerml.Feature)"><code>FeatureValues.getValueExpression(Feature)</code></a></dd>
<dd><code>usage</code> - enumeration usage to set for expression</dd>
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
