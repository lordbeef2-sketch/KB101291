# JAVA OPENAPI: MatrixSettings.Direction (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/dependencymatrix/persistence/MatrixSettings.Direction.html
- source_path: `com/nomagic/magicdraw/dependencymatrix/persistence/MatrixSettings.Direction.html`
- source_sha256: `9f179fb303a6cf9fb05e511cd76d4a8c14e94a1c33e1e52af32b65b88bcfb1c9`
- captured_utc: `2026-07-14T16:55:13.890994+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependencymatrix.persistence](package-summary.html)

## Enum Class MatrixSettings.Direction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[MatrixSettings.Direction](MatrixSettings.Direction.html)>
com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.Direction

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[MatrixSettings.Direction](MatrixSettings.Direction.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
[MatrixSettings](MatrixSettings.html)

public static enumMatrixSettings.Direction
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[MatrixSettings.Direction](MatrixSettings.Direction.html)>

Dependency filter and default edit direction setting enum

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[BOTH](#BOTH)`

`[COLUMN_TO_ROW](#COLUMN_TO_ROW)`

`[ROW_TO_COLUMN](#ROW_TO_COLUMN)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [MatrixSettings.Direction](MatrixSettings.Direction.html)`
`[getDirectionFromEnum](#getDirectionFromEnum(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) direction)`
Converts enumeration literal to enum value
`static [MatrixSettings.Direction](MatrixSettings.Direction.html)`
`[getEnum](#getEnum(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)`
finds direction by its representation type
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getType](#getType())()`
Returns representation type for this enum value
`[MatrixSettings.Direction](MatrixSettings.Direction.html)`
`[invert](#invert())()`
Gets inverted direction or the sam for BOTH.
`boolean`
`[isColumnToRowSupported](#isColumnToRowSupported())()`
Returns if column to row mode is supported - [`COLUMN_TO_ROW`](#COLUMN_TO_ROW) and [`BOTH`](#BOTH) cases.
`boolean`
`[isRowToColumnSupported](#isRowToColumnSupported())()`
Returns if row to column mode is supported - [`ROW_TO_COLUMN`](#ROW_TO_COLUMN) and [`BOTH`](#BOTH) cases.
`static [MatrixSettings.Direction](MatrixSettings.Direction.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [MatrixSettings.Direction](MatrixSettings.Direction.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
ROW_TO_COLUMN
public static final [MatrixSettings.Direction](MatrixSettings.Direction.html) ROW_TO_COLUMN
COLUMN_TO_ROW
public static final [MatrixSettings.Direction](MatrixSettings.Direction.html) COLUMN_TO_ROW
BOTH
public static final [MatrixSettings.Direction](MatrixSettings.Direction.html) BOTH
 ============ METHOD DETAIL ========== 
Method Details
values
public static [MatrixSettings.Direction](MatrixSettings.Direction.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [MatrixSettings.Direction](MatrixSettings.Direction.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Returns the enum constant of this class with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this class. (Extraneous whitespace characters are 
not permitted.)
Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if this enum class has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html)` - if the argument is null
getDirectionFromEnum
public static [MatrixSettings.Direction](MatrixSettings.Direction.html) getDirectionFromEnum(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) direction)
Converts enumeration literal to enum value
Parameters:
`direction` - enumeration literal object
Returns:
direction corresponding to enumeration literal value
getType
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getType()
Returns representation type for this enum value
Returns:
representation string
isRowToColumnSupported
public boolean isRowToColumnSupported()
Returns if row to column mode is supported - [`ROW_TO_COLUMN`](#ROW_TO_COLUMN) and [`BOTH`](#BOTH) cases.
Returns:
true if supported.
isColumnToRowSupported
public boolean isColumnToRowSupported()
Returns if column to row mode is supported - [`COLUMN_TO_ROW`](#COLUMN_TO_ROW) and [`BOTH`](#BOTH) cases.
Returns:
true if supported.
getEnum
public static [MatrixSettings.Direction](MatrixSettings.Direction.html) getEnum([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) type)
finds direction by its representation type
Parameters:
`type` - representation type
Returns:
enum value of this type
invert
public [MatrixSettings.Direction](MatrixSettings.Direction.html) invert()
Gets inverted direction or the sam for BOTH.
Returns:
inverted direction

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependencymatrix.persistence</a></div>
<h1 class="title" title="Enum Class MatrixSettings.Direction">Enum Class MatrixSettings.Direction</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.dependencymatrix.persistence.MatrixSettings.Direction</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="MatrixSettings.html" title="class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">MatrixSettings.Direction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a>&gt;</span></div>
<div class="block">Dependency filter and default edit direction setting enum</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">
<h2>Enum Constant Summary</h2>
<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#BOTH">BOTH</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#COLUMN_TO_ROW">COLUMN_TO_ROW</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#ROW_TO_COLUMN">ROW_TO_COLUMN</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirectionFromEnum(java.lang.Object)">getDirectionFromEnum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts enumeration literal to enum value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEnum(java.lang.String)">getEnum</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">finds direction by its representation type</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns representation type for this enum value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invert()">invert</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets inverted direction or the sam for BOTH.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isColumnToRowSupported()">isColumnToRowSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if column to row mode is supported - <a href="#COLUMN_TO_ROW"><code>COLUMN_TO_ROW</code></a> and <a href="#BOTH"><code>BOTH</code></a> cases.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRowToColumnSupported()">isRowToColumnSupported</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns if row to column mode is supported - <a href="#ROW_TO_COLUMN"><code>ROW_TO_COLUMN</code></a> and <a href="#BOTH"><code>BOTH</code></a> cases.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">
<h2>Enum Constant Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="ROW_TO_COLUMN">
<h3>ROW_TO_COLUMN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">ROW_TO_COLUMN</span></div>
</section>
</li>
<li>
<section class="detail" id="COLUMN_TO_ROW">
<h3>COLUMN_TO_ROW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">COLUMN_TO_ROW</span></div>
</section>
</li>
<li>
<section class="detail" id="BOTH">
<h3>BOTH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">BOTH</span></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirectionFromEnum(java.lang.Object)">
<h3>getDirectionFromEnum</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">getDirectionFromEnum</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> direction)</span></div>
<div class="block">Converts enumeration literal to enum value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>direction</code> - enumeration literal object</dd>
<dt>Returns:</dt>
<dd>direction corresponding to enumeration literal value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns representation type for this enum value</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>representation string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRowToColumnSupported()">
<h3>isRowToColumnSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRowToColumnSupported</span>()</div>
<div class="block">Returns if row to column mode is supported - <a href="#ROW_TO_COLUMN"><code>ROW_TO_COLUMN</code></a> and <a href="#BOTH"><code>BOTH</code></a> cases.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isColumnToRowSupported()">
<h3>isColumnToRowSupported</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isColumnToRowSupported</span>()</div>
<div class="block">Returns if column to row mode is supported - <a href="#COLUMN_TO_ROW"><code>COLUMN_TO_ROW</code></a> and <a href="#BOTH"><code>BOTH</code></a> cases.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if supported.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnum(java.lang.String)">
<h3>getEnum</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">getEnum</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">finds direction by its representation type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - representation type</dd>
<dt>Returns:</dt>
<dd>enum value of this type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invert()">
<h3>invert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MatrixSettings.Direction.html" title="enum class in com.nomagic.magicdraw.dependencymatrix.persistence">MatrixSettings.Direction</a></span> <span class="element-name">invert</span>()</div>
<div class="block">Gets inverted direction or the sam for BOTH.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>inverted direction</dd>
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
