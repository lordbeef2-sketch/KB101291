# JAVA OPENAPI: OperatorExpressions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/OperatorExpressions.html
- source_path: `com/dassault_systemes/modeler/kerml/model/OperatorExpressions.html`
- source_sha256: `8ed4dd8ad500f79f746c71ef0bca690a184f5b42e37b0eecca4437fcdf388b11`
- captured_utc: `2026-07-14T16:44:47.886840+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class OperatorExpressions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.OperatorExpressions

@OpenApiAllpublic classOperatorExpressions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`OperatorExpression`](kerml/OperatorExpression.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[AS_OPERATOR](#AS_OPERATOR)`
Operator symbol for type‑ascription (“as”) expressions.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COLLECT_OPERATOR](#COLLECT_OPERATOR)`
Operator symbol for the collection (map‑over) operation.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[EQUALS_OPERATOR](#EQUALS_OPERATOR)`
Operator symbol for equality comparison.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INDEX_OPERATOR](#INDEX_OPERATOR)`
Operator symbol for index access within a collection.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[L_BRACKET_OPERATOR](#L_BRACKET_OPERATOR)`
Operator symbol for bracket‑based access expressions.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SELECT_OPERATOR](#SELECT_OPERATOR)`
Operator symbol for filtering elements of a collection.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OperatorExpressions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [OperatorExpression](kerml/OperatorExpression.html)`
`[createLBRACKETOperatorExpression](#createLBRACKETOperatorExpression(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier)`
Creates an operator expression using the "[" operator.
`static [OperatorExpression](kerml/OperatorExpression.html)`
`[createOperatorExpression](#createOperatorExpression(java.util.function.Supplier,java.lang.String,int))([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) operator,
 int numberOfInputParameters)`
Creates an operator expression with the given operator and number of input parameters.
`static [OperatorExpression](kerml/OperatorExpression.html)`
`[createOperatorExpression](#createOperatorExpression(java.util.function.Supplier,java.lang.String,com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Object...))([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) operator,
 [Type](kerml/Type.html) resultType,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputParameterValues)`
Creates an operator expression with the given operator, result type,
 and input parameter values.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
COLLECT_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COLLECT_OPERATOR
Operator symbol for the collection (map‑over) operation.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.COLLECT_OPERATOR)
INDEX_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INDEX_OPERATOR
Operator symbol for index access within a collection.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.INDEX_OPERATOR)
SELECT_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SELECT_OPERATOR
Operator symbol for filtering elements of a collection.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.SELECT_OPERATOR)
L_BRACKET_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) L_BRACKET_OPERATOR
Operator symbol for bracket‑based access expressions.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.L_BRACKET_OPERATOR)
AS_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) AS_OPERATOR
Operator symbol for type‑ascription (“as”) expressions.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.AS_OPERATOR)
EQUALS_OPERATOR
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) EQUALS_OPERATOR
Operator symbol for equality comparison.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.EQUALS_OPERATOR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OperatorExpressions
public OperatorExpressions()
 ============ METHOD DETAIL ========== 
Method Details
createLBRACKETOperatorExpression
public static [OperatorExpression](kerml/OperatorExpression.html) createLBRACKETOperatorExpression([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier)
Creates an operator expression using the "[" operator.
 The expression will have exactly two input parameters.
Parameters:
`factorySupplier` - supplier providing the [`ElementsFactory`](ElementsFactory.html)
Returns:
a new operator expression using the "[" operator
createOperatorExpression
public static [OperatorExpression](kerml/OperatorExpression.html) createOperatorExpression([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) operator,
 @CheckForNull
 [Type](kerml/Type.html) resultType,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)... inputParameterValues)
Creates an operator expression with the given operator, result type,
 and input parameter values.
Parameters:
`factorySupplier` - supplier providing the [`ElementsFactory`](ElementsFactory.html)
`operator` - operator symbol
`resultType` - optional result type of the expression
`inputParameterValues` - values for the input parameters
Returns:
a new operator expression
createOperatorExpression
public static [OperatorExpression](kerml/OperatorExpression.html) createOperatorExpression([Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ElementsFactory](ElementsFactory.html)> factorySupplier,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) operator,
 int numberOfInputParameters)
Creates an operator expression with the given operator and number of input parameters.
Parameters:
`factorySupplier` - supplier providing the [`ElementsFactory`](ElementsFactory.html)
`operator` - operator symbol
`numberOfInputParameters` - number of input parameters
Returns:
a new operator expression

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class OperatorExpressions">Class OperatorExpressions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.OperatorExpressions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OperatorExpressions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OperatorExpression</code></a></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AS_OPERATOR">AS_OPERATOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operator symbol for type‑ascription (“as”) expressions.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLLECT_OPERATOR">COLLECT_OPERATOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Operator symbol for the collection (map‑over) operation.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EQUALS_OPERATOR">EQUALS_OPERATOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operator symbol for equality comparison.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INDEX_OPERATOR">INDEX_OPERATOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Operator symbol for index access within a collection.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#L_BRACKET_OPERATOR">L_BRACKET_OPERATOR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operator symbol for bracket‑based access expressions.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SELECT_OPERATOR">SELECT_OPERATOR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Operator symbol for filtering elements of a collection.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">OperatorExpressions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createLBRACKETOperatorExpression(java.util.function.Supplier)">createLBRACKETOperatorExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an operator expression using the "[" operator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperatorExpression(java.util.function.Supplier,java.lang.String,int)">createOperatorExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> operator,
 int numberOfInputParameters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an operator expression with the given operator and number of input parameters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperatorExpression(java.util.function.Supplier,java.lang.String,com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Object...)">createOperatorExpression</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> operator,
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> resultType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputParameterValues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an operator expression with the given operator, result type,
 and input parameter values.</div>
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
<section class="detail" id="COLLECT_OPERATOR">
<h3>COLLECT_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COLLECT_OPERATOR</span></div>
<div class="block">Operator symbol for the collection (map‑over) operation.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.COLLECT_OPERATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INDEX_OPERATOR">
<h3>INDEX_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INDEX_OPERATOR</span></div>
<div class="block">Operator symbol for index access within a collection.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.INDEX_OPERATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SELECT_OPERATOR">
<h3>SELECT_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SELECT_OPERATOR</span></div>
<div class="block">Operator symbol for filtering elements of a collection.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.SELECT_OPERATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="L_BRACKET_OPERATOR">
<h3>L_BRACKET_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">L_BRACKET_OPERATOR</span></div>
<div class="block">Operator symbol for bracket‑based access expressions.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.L_BRACKET_OPERATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AS_OPERATOR">
<h3>AS_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AS_OPERATOR</span></div>
<div class="block">Operator symbol for type‑ascription (“as”) expressions.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.AS_OPERATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EQUALS_OPERATOR">
<h3>EQUALS_OPERATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EQUALS_OPERATOR</span></div>
<div class="block">Operator symbol for equality comparison.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.OperatorExpressions.EQUALS_OPERATOR">Constant Field Values</a></li>
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
<h3>OperatorExpressions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OperatorExpressions</span>()</div>
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
<section class="detail" id="createLBRACKETOperatorExpression(java.util.function.Supplier)">
<h3>createLBRACKETOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createLBRACKETOperatorExpression</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier)</span></div>
<div class="block">Creates an operator expression using the "[" operator.
 The expression will have exactly two input parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factorySupplier</code> - supplier providing the <a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>ElementsFactory</code></a></dd>
<dt>Returns:</dt>
<dd>a new operator expression using the "[" operator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperatorExpression(java.util.function.Supplier,java.lang.String,com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Object...)">
<h3>createOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createOperatorExpression</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> operator,
 @CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> resultType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>... inputParameterValues)</span></div>
<div class="block">Creates an operator expression with the given operator, result type,
 and input parameter values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factorySupplier</code> - supplier providing the <a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>ElementsFactory</code></a></dd>
<dd><code>operator</code> - operator symbol</dd>
<dd><code>resultType</code> - optional result type of the expression</dd>
<dd><code>inputParameterValues</code> - values for the input parameters</dd>
<dt>Returns:</dt>
<dd>a new operator expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperatorExpression(java.util.function.Supplier,java.lang.String,int)">
<h3>createOperatorExpression</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/OperatorExpression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OperatorExpression</a></span> <span class="element-name">createOperatorExpression</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model">ElementsFactory</a>&gt; factorySupplier,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> operator,
 int numberOfInputParameters)</span></div>
<div class="block">Creates an operator expression with the given operator and number of input parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factorySupplier</code> - supplier providing the <a href="ElementsFactory.html" title="interface in com.dassault_systemes.modeler.kerml.model"><code>ElementsFactory</code></a></dd>
<dd><code>operator</code> - operator symbol</dd>
<dd><code>numberOfInputParameters</code> - number of input parameters</dd>
<dt>Returns:</dt>
<dd>a new operator expression</dd>
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
