# JAVA OPENAPI: SequenceExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/SequenceExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/SequenceExpressions.html`
- source_sha256: `86578ab633975aa87fe077371040c485c5d46afa5dcb3d641e6bb594cf8756ec`
- captured_utc: `2026-07-14T16:44:48.258846+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class SequenceExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.SequenceExpressions

@OpenApiAllpublic classSequenceExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COMMA_OPERATOR](#COMMA_OPERATOR)`
Operator symbol for sequencing expressions using the comma operator.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SequenceExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addElementToSequence](#addElementToSequence(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Function))([Feature](kerml/Feature.html) sequenceFeature,
 [Element](kerml/Element.html) addedElement,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Element](kerml/Element.html),[Expression](kerml/Expression.html)> expressionFactory)`
Adds the element to the sequence using the ',' operator.
`static [OperatorExpression](kerml/OperatorExpression.html)`
`[createCommaOperatorExpression](#createCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression...))([Expression](kerml/Expression.html)... expressions)`
Creates a comma operator expression from the given list of expressions.
`static [OperatorExpression](kerml/OperatorExpression.html)`
`[createCommaOperatorExpression](#createCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,com.dassault_systemes.modeler.kerml.model.kerml.Expression))([Expression](kerml/Expression.html) first,
 [Expression](kerml/Expression.html) second)`
Creates a comma operator expression combining two expressions.
`static [OperatorExpression](kerml/OperatorExpression.html)`
`[createCommaOperatorExpression](#createCommaOperatorExpression(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier)`
Creates a new comma operator expression with two input parameters.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expression](kerml/Expression.html)>`
`[getValue](#getValue(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression))([OperatorExpression](kerml/OperatorExpression.html) topExpression)`
Extracts all non-operator expressions from a comma operator expression tree.
`static boolean`
`[isCommaOperatorExpression](#isCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression))([Expression](kerml/Expression.html) expression)`
Checks whether the given expression is a comma operator expression.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
COMMA_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COMMA_OPERATOR
Operator symbol for sequencing expressions using the comma operator.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.SequenceExpressions.COMMA_OPERATOR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SequenceExpressions
public SequenceExpressions()
 ============ METHOD DETAIL ========== 
Method Details
addElementToSequence
public static void addElementToSequence([Feature](kerml/Feature.html) sequenceFeature,
 [Element](kerml/Element.html) addedElement,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Element](kerml/Element.html),[Expression](kerml/Expression.html)> expressionFactory)
Adds the element to the sequence using the ',' operator. 

 

 For example, if the passed sequence feature is the following:
 `(requirement1.metadata, requirement2.metadata)` 

 and the element parameter
 `requirement3` is passed along with [`MetadataAccessExpressions.createMetadataAccessExpression(Element)`](MetadataAccessExpressions.html#createMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.Element))
 factory, it will result in the following sequence:
 `(requirement1.metadata, requirement2.metadata, requirement3.metadata)`
Parameters:
`sequenceFeature` - root feature of the sequence
`addedElement` - element, which will be added to the sequence
getValue
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expression](kerml/Expression.html)> getValue([OperatorExpression](kerml/OperatorExpression.html) topExpression)
Extracts all non-operator expressions from a comma operator expression tree.
Parameters:
`topExpression` - the root operator expression
Returns:
list of contained expressions in sequence order
isCommaOperatorExpression
public static boolean isCommaOperatorExpression(@CheckForNull
 [Expression](kerml/Expression.html) expression)
Checks whether the given expression is a comma operator expression.
Parameters:
`expression` - the expression to check
Returns:
true if the expression uses the comma operator
createCommaOperatorExpression
public static [OperatorExpression](kerml/OperatorExpression.html) createCommaOperatorExpression([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier)
Creates a new comma operator expression with two input parameters.
Parameters:
`factorySupplier` - supplier for the elements factory
Returns:
a new comma operator expression
createCommaOperatorExpression
public static [OperatorExpression](kerml/OperatorExpression.html) createCommaOperatorExpression([Expression](kerml/Expression.html) first,
 [Expression](kerml/Expression.html) second)
Creates a comma operator expression combining two expressions.
Parameters:
`first` - the first expression
`second` - the second expression
Returns:
a new comma operator expression
createCommaOperatorExpression
@CheckForNullpublic static [OperatorExpression](kerml/OperatorExpression.html) createCommaOperatorExpression([Expression](kerml/Expression.html)... expressions)
Creates a comma operator expression from the given list of expressions.
 If no expressions are provided, this method returns null.
Parameters:
`expressions` - the expressions to combine using the comma operator
Returns:
a comma operator expression combining the given expressions,
 or null if the input is empty

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class SequenceExpressions">Class SequenceExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.SequenceExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SequenceExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMMA_OPERATOR">COMMA_OPERATOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operator symbol for sequencing expressions using the comma operator.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SequenceExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addElementToSequence(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Function)">addElementToSequence</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> sequenceFeature,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> addedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>,<wbr/><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; expressionFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds the element to the sequence using the ',' operator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression...)">createCommaOperatorExpression</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>... expressions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a comma operator expression from the given list of expressions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,com.dassault_systemes.modeler.kerml.model.kerml.Expression)">createCommaOperatorExpression</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> first,
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> second)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a comma operator expression combining two expressions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommaOperatorExpression(java.util.function.Supplier)">createCommaOperatorExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new comma operator expression with two input parameters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getValue(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression)">getValue</a><wbr/>(<a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a> topExpression)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extracts all non-operator expressions from a comma operator expression tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression)">isCommaOperatorExpression</a><wbr/>(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> expression)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given expression is a comma operator expression.</div>
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
<section class="detail" id="COMMA_OPERATOR">
<h3>COMMA_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMMA_OPERATOR</span></div>
<div class="block">Operator symbol for sequencing expressions using the comma operator.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.SequenceExpressions.COMMA_OPERATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;()">
<h3>SequenceExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SequenceExpressions</span>()</div>
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
<section class="detail" id="addElementToSequence(com.dassault_systemes.modeler.kerml.model.kerml.Feature,com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Function)">
<h3>addElementToSequence</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addElementToSequence</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> sequenceFeature,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> addedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>,<wbr/><a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; expressionFactory)</span></div>
<div class="block">Adds the element to the sequence using the ',' operator. <br/>
<br/>
 For example, if the passed sequence feature is the following:
 <code>(requirement1.metadata, requirement2.metadata)</code> <br/>
 and the element parameter
 <code>requirement3</code> is passed along with <a href="MetadataAccessExpressions.html#createMetadataAccessExpression(com.dassault_systemes.modeler.kerml.model.kerml.Element)"><code>MetadataAccessExpressions.createMetadataAccessExpression(Element)</code></a>
 factory, it will result in the following sequence:
 <code>(requirement1.metadata, requirement2.metadata, requirement3.metadata)</code>
<br/></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sequenceFeature</code> - root feature of the sequence</dd>
<dd><code>addedElement</code> - element, which will be added to the sequence</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getValue(com.dassault_systemes.modeler.kerml.model.kerml.OperatorExpression)">
<h3>getValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</span> <span class="element-name">getValue</span><wbr/><span class="parameters">(<a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a> topExpression)</span></div>
<div class="block">Extracts all non-operator expressions from a comma operator expression tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>topExpression</code> - the root operator expression</dd>
<dt>Returns:</dt>
<dd>list of contained expressions in sequence order</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression)">
<h3>isCommaOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCommaOperatorExpression</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> expression)</span></div>
<div class="block">Checks whether the given expression is a comma operator expression.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expression</code> - the expression to check</dd>
<dt>Returns:</dt>
<dd>true if the expression uses the comma operator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommaOperatorExpression(java.util.function.Supplier)">
<h3>createCommaOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createCommaOperatorExpression</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier)</span></div>
<div class="block">Creates a new comma operator expression with two input parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factorySupplier</code> - supplier for the elements factory</dd>
<dt>Returns:</dt>
<dd>a new comma operator expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression,com.dassault_systemes.modeler.kerml.model.kerml.Expression)">
<h3>createCommaOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createCommaOperatorExpression</span><wbr/><span class="parameters">(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> first,
 <a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a> second)</span></div>
<div class="block">Creates a comma operator expression combining two expressions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>first</code> - the first expression</dd>
<dd><code>second</code> - the second expression</dd>
<dt>Returns:</dt>
<dd>a new comma operator expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommaOperatorExpression(com.dassault_systemes.modeler.kerml.model.kerml.Expression...)">
<h3>createCommaOperatorExpression</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createCommaOperatorExpression</span><wbr/><span class="parameters">(<a href="kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>... expressions)</span></div>
<div class="block">Creates a comma operator expression from the given list of expressions.
 If no expressions are provided, this method returns null.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>expressions</code> - the expressions to combine using the comma operator</dd>
<dt>Returns:</dt>
<dd>a comma operator expression combining the given expressions,
         or null if the input is empty</dd>
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
