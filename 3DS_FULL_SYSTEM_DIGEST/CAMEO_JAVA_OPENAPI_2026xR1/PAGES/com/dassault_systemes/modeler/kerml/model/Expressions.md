# JAVA OPENAPI: Expressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Expressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Expressions.html`
- source_sha256: `7c499ed67255d717a1294efab3915e1014ad9ef4311737cdbc14d6d45e395dc7`
- captured_utc: `2026-07-14T16:44:47.448835+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Expressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Expressions

@OpenApiAllpublic classExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Expression`](kerml/Expression.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Expressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Expression](kerml/Expression.html)`
`[getOwnedResultExpressionOf](#getOwnedResultExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the owned result expression of the given type, if defined
 directly on the type through a [`ResultExpressionMembership`](kerml/ResultExpressionMembership.html).
`static [Feature](kerml/Feature.html)`
`[getResult](#getResult(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the result feature of the given type, if it is an expression
 or a function.
`static [Expression](kerml/Expression.html)`
`[getResultExpressionOf](#getResultExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the result expression of the given type, if defined through
 a [`ResultExpressionMembership`](kerml/ResultExpressionMembership.html).
`static [Expression](kerml/Expression.html)`
`[getResultExpressionOrResultValueExpressionOf](#getResultExpressionOrResultValueExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the result expression of the given type, or if none exists,
 returns the value expression of the result feature.
`static boolean`
`[isBooleanFunctionFromDataFunctions](#isBooleanFunctionFromDataFunctions(com.dassault_systemes.modeler.kerml.model.kerml.Function))([Function](kerml/Function.html) function)`
Checks whether the given function is one of the functions
 defined in the standard [`DataFunctionsLibrary`](../libraries/standard/DataFunctionsLibrary.html).
`static boolean`
`[isExpressionOrFunction](#isExpressionOrFunction(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the given element is an expression or a function.
`static boolean`
`[isExpressionOrFunction](#isExpressionOrFunction(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents an expression or a function.
`static boolean`
`[isPureExpression](#isPureExpression(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Determines whether the given EClass represents a pure expression.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Expressions
public Expressions()
 ============ METHOD DETAIL ========== 
Method Details
getResultExpressionOf
@CheckForNullpublic static [Expression](kerml/Expression.html) getResultExpressionOf([Type](kerml/Type.html) type)
Returns the result expression of the given type, if defined through
 a [`ResultExpressionMembership`](kerml/ResultExpressionMembership.html).
Parameters:
`type` - the type
Returns:
result expression, or null
getOwnedResultExpressionOf
@CheckForNullpublic static [Expression](kerml/Expression.html) getOwnedResultExpressionOf([Type](kerml/Type.html) type)
Returns the owned result expression of the given type, if defined
 directly on the type through a [`ResultExpressionMembership`](kerml/ResultExpressionMembership.html).
Parameters:
`type` - the type
Returns:
owned result expression, or null
isPureExpression
public static boolean isPureExpression(org.eclipse.emf.ecore.EClass eClass)
Determines whether the given EClass represents a pure expression.
 A pure expression is an [`Expression`](kerml/Expression.html) whose purity is confirmed
 by `ExpressionPurityProvider`, if available.
Parameters:
`eClass` - the class to check
Returns:
true if the class represents a pure expression
isExpressionOrFunction
public static boolean isExpressionOrFunction(@CheckForNull
 [Element](kerml/Element.html) element)
Checks whether the given element is an expression or a function.
Parameters:
`element` - the element to check
Returns:
true if the element is an expression or function
isExpressionOrFunction
public static boolean isExpressionOrFunction(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents an expression or a function.
Parameters:
`eClass` - the class to check
Returns:
true if the class is an expression or function
getResult
@CheckForNullpublic static [Feature](kerml/Feature.html) getResult([Type](kerml/Type.html) type)
Returns the result feature of the given type, if it is an expression
 or a function.
Parameters:
`type` - the type
Returns:
result feature, or null
getResultExpressionOrResultValueExpressionOf
@CheckForNullpublic static [Expression](kerml/Expression.html) getResultExpressionOrResultValueExpressionOf([Type](kerml/Type.html) type)
Returns the result expression of the given type, or if none exists,
 returns the value expression of the result feature.
Parameters:
`type` - the type
Returns:
result expression or result value expression, or null
isBooleanFunctionFromDataFunctions
public static boolean isBooleanFunctionFromDataFunctions([Function](kerml/Function.html) function)
Checks whether the given function is one of the functions
 defined in the standard [`DataFunctionsLibrary`](../libraries/standard/DataFunctionsLibrary.html).
Parameters:
`function` - the function to check
Returns:
true if the function is a standard boolean function

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Expressions">Class Expressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Expressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Expressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Expressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedResultExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedResultExpressionOf</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned result expression of the given type, if defined
 directly on the type through a <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ResultExpressionMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResult(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getResult</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the result feature of the given type, if it is an expression
 or a function.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResultExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getResultExpressionOf</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the result expression of the given type, if defined through
 a <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ResultExpressionMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getResultExpressionOrResultValueExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getResultExpressionOrResultValueExpressionOf</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the result expression of the given type, or if none exists,
 returns the value expression of the result feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isBooleanFunctionFromDataFunctions(com.dassault_systemes.modeler.kerml.model.kerml.Function)">isBooleanFunctionFromDataFunctions</a><wbr/>(<a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a> function)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given function is one of the functions
 defined in the standard <a href="../libraries/standard/DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard"><code>DataFunctionsLibrary</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExpressionOrFunction(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isExpressionOrFunction</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given element is an expression or a function.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isExpressionOrFunction(org.eclipse.emf.ecore.EClass)">isExpressionOrFunction</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents an expression or a function.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPureExpression(org.eclipse.emf.ecore.EClass)">isPureExpression</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines whether the given EClass represents a pure expression.</div>
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
<h3>Expressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Expressions</span>()</div>
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
<section class="detail" id="getResultExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getResultExpressionOf</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getResultExpressionOf</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the result expression of the given type, if defined through
 a <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ResultExpressionMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>result expression, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedResultExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedResultExpressionOf</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOwnedResultExpressionOf</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the owned result expression of the given type, if defined
 directly on the type through a <a href="kerml/ResultExpressionMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>ResultExpressionMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>owned result expression, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPureExpression(org.eclipse.emf.ecore.EClass)">
<h3>isPureExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPureExpression</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Determines whether the given EClass represents a pure expression.
 A pure expression is an <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> whose purity is confirmed
 by <code>ExpressionPurityProvider</code>, if available.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class represents a pure expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExpressionOrFunction(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isExpressionOrFunction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExpressionOrFunction</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the given element is an expression or a function.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is an expression or function</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isExpressionOrFunction(org.eclipse.emf.ecore.EClass)">
<h3>isExpressionOrFunction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isExpressionOrFunction</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents an expression or a function.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is an expression or function</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResult(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getResult</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getResult</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the result feature of the given type, if it is an expression
 or a function.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>result feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResultExpressionOrResultValueExpressionOf(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getResultExpressionOrResultValueExpressionOf</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getResultExpressionOrResultValueExpressionOf</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the result expression of the given type, or if none exists,
 returns the value expression of the result feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>result expression or result value expression, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isBooleanFunctionFromDataFunctions(com.dassault_systemes.modeler.kerml.model.kerml.Function)">
<h3>isBooleanFunctionFromDataFunctions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isBooleanFunctionFromDataFunctions</span><wbr/><span class="parameters">(<a href="kerml/Function.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Function</a> function)</span></div>
<div class="block">Checks whether the given function is one of the functions
 defined in the standard <a href="../libraries/standard/DataFunctionsLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries.standard"><code>DataFunctionsLibrary</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>function</code> - the function to check</dd>
<dt>Returns:</dt>
<dd>true if the function is a standard boolean function</dd>
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
