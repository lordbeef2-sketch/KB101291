# JAVA OPENAPI: PrimitiveValueConverter (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml2/datatypes/PrimitiveValueConverter.html
- source_path: `com/nomagic/magicdraw/uml2/datatypes/PrimitiveValueConverter.html`
- source_sha256: `8b272ebfedbb11ef177763c6793a1af313ef4e8f541e1cee92cf487d0607be7f`
- captured_utc: `2026-07-14T16:55:58.730494+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.datatypes](package-summary.html)

## Class PrimitiveValueConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml2.datatypes.PrimitiveValueConverter

public classPrimitiveValueConverter
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Converts value to specific primitive type.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PrimitiveValueConverter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[adjustDecimalSeparatorToSystem](#adjustDecimalSeparatorToSystem(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) number)`

`static [DecimalFormatSymbols](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html)`
`[getDecimalFormatSymbols](#getDecimalFormatSymbols())()`
Gets [`DecimalFormatSymbols`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html) of OS.
`static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[toBoolean](#toBoolean(java.lang.Object,java.lang.Boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) defaultValue)`

`static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[toBoolean](#toBoolean(java.lang.Object,java.lang.Boolean,java.util.function.Function))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) defaultValue,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> converter)`

`static [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html)`
`[toFloat](#toFloat(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`static [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html)`
`[toFloat](#toFloat(java.lang.Object,java.lang.Float))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) defaultValue)`

`static [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`
`[toInteger](#toInteger(java.lang.Object,java.lang.Integer))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) defaultValue)`

`static [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html)`
`[toNumber](#toNumber(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`static [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html)`
`[toNumber](#toNumber(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)`

`static [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`
`[toReal](#toReal(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`static [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`
`[toReal](#toReal(java.lang.Object,java.lang.Double))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) defaultValue)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PrimitiveValueConverter
public PrimitiveValueConverter()
 ============ METHOD DETAIL ========== 
Method Details
toBoolean
@CheckForNullpublic static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) toBoolean(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) defaultValue)
toBoolean
@CheckForNullpublic static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) toBoolean(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) defaultValue,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html),[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> converter)
toReal
@CheckForNullpublic static [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) toReal([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
toReal
@CheckForNullpublic static [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) toReal(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) defaultValue)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
toFloat
public static [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) toFloat([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
toFloat
@CheckForNullpublic static [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) toFloat(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Float](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html) defaultValue)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
toInteger
@CheckForNullpublic static [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) toInteger(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) defaultValue)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
toNumber
@CheckForNullpublic static [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) toNumber([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value,
 @CheckForNull
 [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type)
toNumber
public static [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html) toNumber([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)`
adjustDecimalSeparatorToSystem
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) adjustDecimalSeparatorToSystem([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) number)
getDecimalFormatSymbols
public static [DecimalFormatSymbols](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html) getDecimalFormatSymbols()
Gets [`DecimalFormatSymbols`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html) of OS. [`DecimalFormatSymbols`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html) is get on separate process because HOST locale provider
 should be used to get OS specific data, but the tool uses different one.
Returns:
OS DecimalFormatSymbols configuration.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.datatypes</a></div>
<h1 class="title" title="Class PrimitiveValueConverter">Class PrimitiveValueConverter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml2.datatypes.PrimitiveValueConverter</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">PrimitiveValueConverter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Converts value to specific primitive type.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PrimitiveValueConverter</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#adjustDecimalSeparatorToSystem(java.lang.String)">adjustDecimalSeparatorToSystem</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> number)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html" title="class or interface in java.text">DecimalFormatSymbols</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDecimalFormatSymbols()">getDecimalFormatSymbols</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html" title="class or interface in java.text"><code>DecimalFormatSymbols</code></a> of OS.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toBoolean(java.lang.Object,java.lang.Boolean)">toBoolean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> defaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toBoolean(java.lang.Object,java.lang.Boolean,java.util.function.Function)">toBoolean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> defaultValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; converter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toFloat(java.lang.Object)">toFloat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toFloat(java.lang.Object,java.lang.Float)">toFloat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a> defaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toInteger(java.lang.Object,java.lang.Integer)">toInteger</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> defaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toNumber(java.lang.Object)">toNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toNumber(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">toNumber</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toReal(java.lang.Object)">toReal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toReal(java.lang.Object,java.lang.Double)">toReal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> defaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>PrimitiveValueConverter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PrimitiveValueConverter</span>()</div>
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
<section class="detail" id="toBoolean(java.lang.Object,java.lang.Boolean)">
<h3>toBoolean</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">toBoolean</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> defaultValue)</span></div>
</section>
</li>
<li>
<section class="detail" id="toBoolean(java.lang.Object,java.lang.Boolean,java.util.function.Function)">
<h3>toBoolean</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">toBoolean</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a> defaultValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; converter)</span></div>
</section>
</li>
<li>
<section class="detail" id="toReal(java.lang.Object)">
<h3>toReal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">toReal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toReal(java.lang.Object,java.lang.Double)">
<h3>toReal</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">toReal</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> defaultValue)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toFloat(java.lang.Object)">
<h3>toFloat</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span class="element-name">toFloat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toFloat(java.lang.Object,java.lang.Float)">
<h3>toFloat</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a></span> <span class="element-name">toFloat</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" title="class or interface in java.lang">Float</a> defaultValue)</span>
                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toInteger(java.lang.Object,java.lang.Integer)">
<h3>toInteger</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">toInteger</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> defaultValue)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toNumber(java.lang.Object,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type)">
<h3>toNumber</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a></span> <span class="element-name">toNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type)</span></div>
</section>
</li>
<li>
<section class="detail" id="toNumber(java.lang.Object)">
<h3>toNumber</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a></span> <span class="element-name">toNumber</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="adjustDecimalSeparatorToSystem(java.lang.String)">
<h3>adjustDecimalSeparatorToSystem</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">adjustDecimalSeparatorToSystem</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> number)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDecimalFormatSymbols()">
<h3>getDecimalFormatSymbols</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html" title="class or interface in java.text">DecimalFormatSymbols</a></span> <span class="element-name">getDecimalFormatSymbols</span>()</div>
<div class="block">Gets <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html" title="class or interface in java.text"><code>DecimalFormatSymbols</code></a> of OS. <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DecimalFormatSymbols.html" title="class or interface in java.text"><code>DecimalFormatSymbols</code></a> is get on separate process because HOST locale provider
 should be used to get OS specific data, but the tool uses different one.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>OS DecimalFormatSymbols configuration.</dd>
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
