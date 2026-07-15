# JAVA OPENAPI: UPDMProfile.LocationKindEnum (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/updm/utils/UPDMProfile.LocationKindEnum.html
- source_path: `com/nomagic/updm/utils/UPDMProfile.LocationKindEnum.html`
- source_sha256: `3b86366243f3278a3937d1a3d254442b56ecf01e5ff2cee459ed233e8c46df8f`
- captured_utc: `2026-07-14T16:56:34.193892+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.updm.utils](package-summary.html)

## Enum Class UPDMProfile.LocationKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)>
com.nomagic.updm.utils.UPDMProfile.LocationKindEnum

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
[UPDMProfile](UPDMProfile.html)

public static enumUPDMProfile.LocationKindEnum
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)>

Enumeration of location kinds, used to support the locationKind tag of the LocationKind stereotype.

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[CIRCULARAREA](#CIRCULARAREA)`
The space enclosed by a circle.
`[ELIPTICALAREA](#ELIPTICALAREA)`
The space enclosed by an ellipse.
`[GEOSTATIONARYPOINT](#GEOSTATIONARYPOINT)`
Unidimensional Individual (dimensionless in space, existent over all time).
`[LINE](#LINE)`
A geometric figure formed by a point moving along a fixed direction and the reverse direction.
`[OTHER](#OTHER)`
Other Location kind that is not on the enumerated list.
`[PLANARSURFACE](#PLANARSURFACE)`
A two-dimensional portion of space.
`[POINT](#POINT)`
Unidimensional Individual (dimensionless in space, existent over all time).
`[POLYGONAREA](#POLYGONAREA)`
The space enclosed by a polygon.
`[RECTANGULARAREA](#RECTANGULARAREA)`
The space enclosed by a rectangle.
`[SOLIDVOLUME](#SOLIDVOLUME)`
The amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.
`[SURFACE](#SURFACE)`
A portion of space having length and breadth but no thickness or regards to time.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)`
`[from](#from(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`

`static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)`
`[toEnum](#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[toEnumerationLiteral](#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.LocationKindEnum))([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) anEnum)`

`static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
SOLIDVOLUME
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) SOLIDVOLUME
The amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.
SURFACE
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) SURFACE
A portion of space having length and breadth but no thickness or regards to time.
LINE
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) LINE
A geometric figure formed by a point moving along a fixed direction and the reverse direction.
POINT
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) POINT
Unidimensional Individual (dimensionless in space, existent over all time).
GEOSTATIONARYPOINT
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) GEOSTATIONARYPOINT
Unidimensional Individual (dimensionless in space, existent over all time).
PLANARSURFACE
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) PLANARSURFACE
A two-dimensional portion of space.
POLYGONAREA
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) POLYGONAREA
The space enclosed by a polygon.
RECTANGULARAREA
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) RECTANGULARAREA
The space enclosed by a rectangle.
ELIPTICALAREA
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) ELIPTICALAREA
The space enclosed by an ellipse.
CIRCULARAREA
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) CIRCULARAREA
The space enclosed by a circle.
OTHER
public static final [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) OTHER
Other Location kind that is not on the enumerated list.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
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
getText
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getText()
from
@CheckForNullpublic static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) from(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
toEnum
@CheckForNullpublic static [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) toEnum([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
toEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) toEnumerationLiteral([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.LocationKindEnum](UPDMProfile.LocationKindEnum.html) anEnum)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.updm.utils</a></div>
<h1 class="title" title="Enum Class UPDMProfile.LocationKindEnum">Enum Class UPDMProfile.LocationKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a>&gt;
<div class="inheritance">com.nomagic.updm.utils.UPDMProfile.LocationKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">UPDMProfile.LocationKindEnum</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a>&gt;</span></div>
<div class="block">Enumeration of location kinds, used to support the locationKind tag of the LocationKind stereotype.</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#CIRCULARAREA">CIRCULARAREA</a></code></div>
<div class="col-last even-row-color">
<div class="block">The space enclosed by a circle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#ELIPTICALAREA">ELIPTICALAREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The space enclosed by an ellipse.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#GEOSTATIONARYPOINT">GEOSTATIONARYPOINT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unidimensional Individual (dimensionless in space, existent over all time).</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#LINE">LINE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A geometric figure formed by a point moving along a fixed direction and the reverse direction.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#OTHER">OTHER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Other Location kind that is not on the enumerated list.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#PLANARSURFACE">PLANARSURFACE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A two-dimensional portion of space.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#POINT">POINT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unidimensional Individual (dimensionless in space, existent over all time).</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#POLYGONAREA">POLYGONAREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The space enclosed by a polygon.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#RECTANGULARAREA">RECTANGULARAREA</a></code></div>
<div class="col-last even-row-color">
<div class="block">The space enclosed by a rectangle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SOLIDVOLUME">SOLIDVOLUME</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SURFACE">SURFACE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A portion of space having length and breadth but no thickness or regards to time.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#from(java.lang.Object)">from</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">toEnum</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.LocationKindEnum)">toEnumerationLiteral</a><wbr/>(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a> anEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a>[]</code></div>
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
<section class="detail" id="SOLIDVOLUME">
<h3>SOLIDVOLUME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">SOLIDVOLUME</span></div>
<div class="block">The amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.</div>
</section>
</li>
<li>
<section class="detail" id="SURFACE">
<h3>SURFACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">SURFACE</span></div>
<div class="block">A portion of space having length and breadth but no thickness or regards to time.</div>
</section>
</li>
<li>
<section class="detail" id="LINE">
<h3>LINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">LINE</span></div>
<div class="block">A geometric figure formed by a point moving along a fixed direction and the reverse direction.</div>
</section>
</li>
<li>
<section class="detail" id="POINT">
<h3>POINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">POINT</span></div>
<div class="block">Unidimensional Individual (dimensionless in space, existent over all time).</div>
</section>
</li>
<li>
<section class="detail" id="GEOSTATIONARYPOINT">
<h3>GEOSTATIONARYPOINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">GEOSTATIONARYPOINT</span></div>
<div class="block">Unidimensional Individual (dimensionless in space, existent over all time).</div>
</section>
</li>
<li>
<section class="detail" id="PLANARSURFACE">
<h3>PLANARSURFACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">PLANARSURFACE</span></div>
<div class="block">A two-dimensional portion of space.</div>
</section>
</li>
<li>
<section class="detail" id="POLYGONAREA">
<h3>POLYGONAREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">POLYGONAREA</span></div>
<div class="block">The space enclosed by a polygon.</div>
</section>
</li>
<li>
<section class="detail" id="RECTANGULARAREA">
<h3>RECTANGULARAREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">RECTANGULARAREA</span></div>
<div class="block">The space enclosed by a rectangle.</div>
</section>
</li>
<li>
<section class="detail" id="ELIPTICALAREA">
<h3>ELIPTICALAREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">ELIPTICALAREA</span></div>
<div class="block">The space enclosed by an ellipse.</div>
</section>
</li>
<li>
<section class="detail" id="CIRCULARAREA">
<h3>CIRCULARAREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">CIRCULARAREA</span></div>
<div class="block">The space enclosed by a circle.</div>
</section>
</li>
<li>
<section class="detail" id="OTHER">
<h3>OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">OTHER</span></div>
<div class="block">Other Location kind that is not on the enumerated list.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
</section>
</li>
<li>
<section class="detail" id="from(java.lang.Object)">
<h3>from</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">from</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>toEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a></span> <span class="element-name">toEnum</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.LocationKindEnum)">
<h3>toEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">toEnumerationLiteral</span><wbr/><span class="parameters">(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.LocationKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.LocationKindEnum</a> anEnum)</span></div>
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
