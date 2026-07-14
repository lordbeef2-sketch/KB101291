# JAVA OPENAPI: MathTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/MathTool.html
- source_path: `com/nomagic/reportwizard/tools/MathTool.html`
- source_sha256: `1b191ca30be3bb4aa0ed80af29ddc1fff1b02512a9d61fcdf0338a03c36036f9`
- captured_utc: `2026-07-14T16:58:39.742310+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools](package-summary.html)

## Class MathTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../magicreport/engine/Tool.html)
com.nomagic.reportwizard.tools.MathTool

All Implemented Interfaces:
`[ITool](../../magicreport/engine/ITool.html)`, `[IVariable](../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classMathTool
extends [Tool](../../magicreport/engine/Tool.html)

Provide basic numeric operations for report.

Since:
Jun 6, 2008
See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.reportwizard.tools.MathTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[context](../../magicreport/engine/Tool.html#context), [properties](../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[VOID](../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MathTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static double`
`[abs](#abs(double))(double a)`
Returns the absolute value of an `double` value.
`static int`
`[abs](#abs(int))(int a)`
Returns the absolute value of an `int` value.
`static double`
`[ceil](#ceil(double))(double a)`
Returns the smallest (closest to negative infinity) `double` value that is greater than or equal
 to the argument and is equal to a mathematical integer.
`static double`
`[floor](#floor(double))(double a)`
Returns the largest (closest to positive infinity) `double` value that is less than or equal to
 the argument and is equal to a mathematical integer.
`static double`
`[max](#max(double,double))(double a,
 double b)`
Returns the greater of two `double` values.
`static int`
`[max](#max(int,int))(int a,
 int b)`
Returns the greater of two `int` values.
`static double`
`[min](#min(double,double))(double a,
 double b)`
Returns the smaller of two `double` values.
`static int`
`[min](#min(int,int))(int a,
 int b)`
Returns the smaller of two `int` values.
`static long`
`[round](#round(double))(double a)`
Returns the closest `long` to the argument.
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[clone](../../magicreport/engine/Tool.html#clone()), [getContext](../../magicreport/engine/Tool.html#getContext()), [getProperties](../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[clearTool](../../magicreport/engine/ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MathTool
public MathTool()
 ============ METHOD DETAIL ========== 
Method Details
abs
public static int abs(int a)
Returns the absolute value of an `int` value. If the argument is not negative, the argument is
 returned. If the argument is negative, the negation of the argument is returned.
Parameters:
`a` - the argument whose absolute value is to be determined
Returns:
the absolute value of the argument.
abs
public static double abs(double a)
Returns the absolute value of an `double` value. If the argument is not negative, the argument is
 returned. If the argument is negative, the negation of the argument is returned.
Parameters:
`a` - the argument whose absolute value is to be determined
Returns:
the absolute value of the argument.
ceil
public static double ceil(double a)
Returns the smallest (closest to negative infinity) `double` value that is greater than or equal
 to the argument and is equal to a mathematical integer. Special cases:
 If the argument value is already equal to a mathematical integer, then the result is the same as the
 argument.
 If the argument is NaN or an infinity or positive zero or negative zero, then the result is the same as
 the argument.
 If the argument value is less than zero but greater than -1.0, then the result is negative zero.
Parameters:
`a` - a value.
Returns:
the smallest (closest to negative infinity) floating-point value that is greater than or equal to
 the argument and is equal to a mathematical integer.
floor
public static double floor(double a)
Returns the largest (closest to positive infinity) `double` value that is less than or equal to
 the argument and is equal to a mathematical integer. Special cases:
 If the argument value is already equal to a mathematical integer, then the result is the same as the
 argument.
 If the argument is NaN or an infinity or positive zero or negative zero, then the result is the same as
 the argument.
Parameters:
`a` - a value.
Returns:
the largest (closest to positive infinity) floating-point value that less than or equal to the
 argument and is equal to a mathematical integer.
max
public static int max(int a,
 int b)
Returns the greater of two `int` values. If the arguments have the same value, the result is that
 same value.
Parameters:
`a` - an argument.
`b` - another argument.
Returns:
the larger of `a` and `b`.
max
public static double max(double a,
 double b)
Returns the greater of two `double` values. If the arguments have the same value, the result is
 that same value.
Parameters:
`a` - an argument.
`b` - another argument.
Returns:
the larger of `a` and `b`.
min
public static int min(int a,
 int b)
Returns the smaller of two `int` values. If the arguments have the same value, the result is that
 same value.
Parameters:
`a` - an argument.
`b` - another argument.
Returns:
the smaller of `a` and `b`.
min
public static double min(double a,
 double b)
Returns the smaller of two `double` values. If the arguments have the same value, the result is
 that same value.
Parameters:
`a` - an argument.
`b` - another argument.
Returns:
the smaller of `a` and `b`.
round
public static long round(double a)
Returns the closest `long` to the argument. The result is rounded to an integer by adding 1/2,
 taking the floor of the result, and casting the result to type `long`.
Parameters:
`a` - a floating-point value to be rounded to a `long`.
Returns:
the value of the argument rounded to the nearest `long` value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools</a></div>
<h1 class="title" title="Class MathTool">Class MathTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.MathTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MathTool</span>
<span class="extends-implements">extends <a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">Provide basic numeric operations for report.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 6, 2008</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.reportwizard.tools.MathTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#context">context</a>, <a href="../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MathTool</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#abs(double)">abs</a><wbr/>(double a)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the absolute value of an <code>double</code> value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#abs(int)">abs</a><wbr/>(int a)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the absolute value of an <code>int</code> value.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ceil(double)">ceil</a><wbr/>(double a)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the smallest (closest to negative infinity) <code>double</code> value that is greater than or equal
 to the argument and is equal to a mathematical integer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#floor(double)">floor</a><wbr/>(double a)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the largest (closest to positive infinity) <code>double</code> value that is less than or equal to
 the argument and is equal to a mathematical integer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#max(double,double)">max</a><wbr/>(double a,
 double b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the greater of two <code>double</code> values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#max(int,int)">max</a><wbr/>(int a,
 int b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the greater of two <code>int</code> values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#min(double,double)">min</a><wbr/>(double a,
 double b)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the smaller of two <code>double</code> values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#min(int,int)">min</a><wbr/>(int a,
 int b)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the smaller of two <code>int</code> values.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#round(double)">round</a><wbr/>(double a)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the closest <code>long</code> to the argument.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<h3>MathTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MathTool</span>()</div>
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
<section class="detail" id="abs(int)">
<h3>abs</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">abs</span><wbr/><span class="parameters">(int a)</span></div>
<div class="block">Returns the absolute value of an <code>int</code> value. If the argument is not negative, the argument is
 returned. If the argument is negative, the negation of the argument is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - the argument whose absolute value is to be determined</dd>
<dt>Returns:</dt>
<dd>the absolute value of the argument.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="abs(double)">
<h3>abs</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">abs</span><wbr/><span class="parameters">(double a)</span></div>
<div class="block">Returns the absolute value of an <code>double</code> value. If the argument is not negative, the argument is
 returned. If the argument is negative, the negation of the argument is returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - the argument whose absolute value is to be determined</dd>
<dt>Returns:</dt>
<dd>the absolute value of the argument.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ceil(double)">
<h3>ceil</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">ceil</span><wbr/><span class="parameters">(double a)</span></div>
<div class="block">Returns the smallest (closest to negative infinity) <code>double</code> value that is greater than or equal
 to the argument and is equal to a mathematical integer. Special cases:
 <ul>
<li>If the argument value is already equal to a mathematical integer, then the result is the same as the
 argument.
 <li>If the argument is NaN or an infinity or positive zero or negative zero, then the result is the same as
 the argument.
 <li>If the argument value is less than zero but greater than -1.0, then the result is negative zero.
 </li></li></li></ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - a value.</dd>
<dt>Returns:</dt>
<dd>the smallest (closest to negative infinity) floating-point value that is greater than or equal to
         the argument and is equal to a mathematical integer.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="floor(double)">
<h3>floor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">floor</span><wbr/><span class="parameters">(double a)</span></div>
<div class="block">Returns the largest (closest to positive infinity) <code>double</code> value that is less than or equal to
 the argument and is equal to a mathematical integer. Special cases:
 <ul>
<li>If the argument value is already equal to a mathematical integer, then the result is the same as the
 argument.
 <li>If the argument is NaN or an infinity or positive zero or negative zero, then the result is the same as
 the argument.
 </li></li></ul></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - a value.</dd>
<dt>Returns:</dt>
<dd>the largest (closest to positive infinity) floating-point value that less than or equal to the
         argument and is equal to a mathematical integer.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="max(int,int)">
<h3>max</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">max</span><wbr/><span class="parameters">(int a,
 int b)</span></div>
<div class="block">Returns the greater of two <code>int</code> values. If the arguments have the same value, the result is that
 same value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - an argument.</dd>
<dd><code>b</code> - another argument.</dd>
<dt>Returns:</dt>
<dd>the larger of <code>a</code> and <code>b</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="max(double,double)">
<h3>max</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">max</span><wbr/><span class="parameters">(double a,
 double b)</span></div>
<div class="block">Returns the greater of two <code>double</code> values. If the arguments have the same value, the result is
 that same value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - an argument.</dd>
<dd><code>b</code> - another argument.</dd>
<dt>Returns:</dt>
<dd>the larger of <code>a</code> and <code>b</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="min(int,int)">
<h3>min</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">min</span><wbr/><span class="parameters">(int a,
 int b)</span></div>
<div class="block">Returns the smaller of two <code>int</code> values. If the arguments have the same value, the result is that
 same value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - an argument.</dd>
<dd><code>b</code> - another argument.</dd>
<dt>Returns:</dt>
<dd>the smaller of <code>a</code> and <code>b</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="min(double,double)">
<h3>min</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">min</span><wbr/><span class="parameters">(double a,
 double b)</span></div>
<div class="block">Returns the smaller of two <code>double</code> values. If the arguments have the same value, the result is
 that same value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - an argument.</dd>
<dd><code>b</code> - another argument.</dd>
<dt>Returns:</dt>
<dd>the smaller of <code>a</code> and <code>b</code>.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="round(double)">
<h3>round</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">long</span> <span class="element-name">round</span><wbr/><span class="parameters">(double a)</span></div>
<div class="block">Returns the closest <code>long</code> to the argument. The result is rounded to an integer by adding 1/2,
 taking the floor of the result, and casting the result to type <code>long</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>a</code> - a floating-point value to be rounded to a <code>long</code>.</dd>
<dt>Returns:</dt>
<dd>the value of the argument rounded to the nearest <code>long</code> value.</dd>
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
