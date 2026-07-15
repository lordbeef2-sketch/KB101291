# JAVA OPENAPI: UAF.LocationTypeKindEnum (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uaf/UAF.LocationTypeKindEnum.html
- source_path: `com/nomagic/magicdraw/uaf/UAF.LocationTypeKindEnum.html`
- source_sha256: `8d52255c8fbac706a4bd58811caa5a6b335ea7ece7546ef2a89bf6dd73e42e86`
- captured_utc: `2026-07-14T16:51:53.147629+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uaf](package-summary.html)

## Enum Class UAF.LocationTypeKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)>
com.nomagic.magicdraw.uaf.UAF.LocationTypeKindEnum

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
[UAF](UAF.html)

public static enumUAF.LocationTypeKindEnum
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)>

Enumeration of the possible kinds of location type that are applicable to a Location.

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[CIRCULARAREATYPE](#CIRCULARAREATYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a circle.
`[ELIPTICALAREATYPE](#ELIPTICALAREATYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by an ellipse.
`[GEOSTATIONARYPOINTTYPE](#GEOSTATIONARYPOINTTYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.
`[LINETYPE](#LINETYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of geometric figure formed by a point moving along a fixed direction and the reverse direction.
`[OTHERTYPE](#OTHERTYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of is a LocationKindType that is not on the enumerated list.
`[PLANARSURFACETYPE](#PLANARSURFACETYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of is a two-dimensional portion of space.
`[POINTTYPE](#POINTTYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.
`[POLYGONAREATYPE](#POLYGONAREATYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a polygon.
`[RECTANGULARAREATYPE](#RECTANGULARAREATYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a rectangle.
`[SOLIDVOLUMETYPE](#SOLIDVOLUMETYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.
`[SURFACETYPE](#SURFACETYPE)`
Indicates that the Location associated with the LocationTypeKind describes a type of portion of space having length and breadth but no thickness or regards to time.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)`
`[from](#from(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`

`static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)`
`[toEnum](#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[toEnumerationLiteral](#toEnumerationLiteral(com.nomagic.magicdraw.uaf.UAF,com.nomagic.magicdraw.uaf.UAF.LocationTypeKindEnum))([UAF](UAF.html) profile,
 [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) anEnum)`

`static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
SOLIDVOLUMETYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) SOLIDVOLUMETYPE
Indicates that the Location associated with the LocationTypeKind describes a type of amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.
SURFACETYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) SURFACETYPE
Indicates that the Location associated with the LocationTypeKind describes a type of portion of space having length and breadth but no thickness or regards to time.
LINETYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) LINETYPE
Indicates that the Location associated with the LocationTypeKind describes a type of geometric figure formed by a point moving along a fixed direction and the reverse direction.
POINTTYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) POINTTYPE
Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.
GEOSTATIONARYPOINTTYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) GEOSTATIONARYPOINTTYPE
Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.
PLANARSURFACETYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) PLANARSURFACETYPE
Indicates that the Location associated with the LocationTypeKind describes a type of is a two-dimensional portion of space.
POLYGONAREATYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) POLYGONAREATYPE
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a polygon.
RECTANGULARAREATYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) RECTANGULARAREATYPE
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a rectangle.
ELIPTICALAREATYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) ELIPTICALAREATYPE
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by an ellipse.
CIRCULARAREATYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) CIRCULARAREATYPE
Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a circle.
OTHERTYPE
public static final [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) OTHERTYPE
Indicates that the Location associated with the LocationTypeKind describes a type of is a LocationKindType that is not on the enumerated list.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
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
@CheckForNullpublic static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) from(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
toEnum
@CheckForNullpublic static [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) toEnum([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
toEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) toEnumerationLiteral([UAF](UAF.html) profile,
 [UAF.LocationTypeKindEnum](UAF.LocationTypeKindEnum.html) anEnum)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uaf</a></div>
<h1 class="title" title="Enum Class UAF.LocationTypeKindEnum">Enum Class UAF.LocationTypeKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.uaf.UAF.LocationTypeKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">UAF.LocationTypeKindEnum</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a>&gt;</span></div>
<div class="block">Enumeration of the possible kinds of location type that are applicable to a Location.</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#CIRCULARAREATYPE">CIRCULARAREATYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a circle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#ELIPTICALAREATYPE">ELIPTICALAREATYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by an ellipse.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#GEOSTATIONARYPOINTTYPE">GEOSTATIONARYPOINTTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#LINETYPE">LINETYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of geometric figure formed by a point moving along a fixed direction and the reverse direction.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#OTHERTYPE">OTHERTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of is a LocationKindType that is not on the enumerated list.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#PLANARSURFACETYPE">PLANARSURFACETYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of is a two-dimensional portion of space.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#POINTTYPE">POINTTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#POLYGONAREATYPE">POLYGONAREATYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a polygon.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#RECTANGULARAREATYPE">RECTANGULARAREATYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a rectangle.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SOLIDVOLUMETYPE">SOLIDVOLUMETYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SURFACETYPE">SURFACETYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of portion of space having length and breadth but no thickness or regards to time.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#from(java.lang.Object)">from</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">toEnum</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnumerationLiteral(com.nomagic.magicdraw.uaf.UAF,com.nomagic.magicdraw.uaf.UAF.LocationTypeKindEnum)">toEnumerationLiteral</a><wbr/>(<a href="UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a> profile,
 <a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a> anEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a>[]</code></div>
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
<section class="detail" id="SOLIDVOLUMETYPE">
<h3>SOLIDVOLUMETYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">SOLIDVOLUMETYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of amount of space occupied by a three-dimensional object of definite shape; not liquid or gaseous.</div>
</section>
</li>
<li>
<section class="detail" id="SURFACETYPE">
<h3>SURFACETYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">SURFACETYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of portion of space having length and breadth but no thickness or regards to time.</div>
</section>
</li>
<li>
<section class="detail" id="LINETYPE">
<h3>LINETYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">LINETYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of geometric figure formed by a point moving along a fixed direction and the reverse direction.</div>
</section>
</li>
<li>
<section class="detail" id="POINTTYPE">
<h3>POINTTYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">POINTTYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.</div>
</section>
</li>
<li>
<section class="detail" id="GEOSTATIONARYPOINTTYPE">
<h3>GEOSTATIONARYPOINTTYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">GEOSTATIONARYPOINTTYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of unidimensional Individual.</div>
</section>
</li>
<li>
<section class="detail" id="PLANARSURFACETYPE">
<h3>PLANARSURFACETYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">PLANARSURFACETYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of is a two-dimensional portion of space.</div>
</section>
</li>
<li>
<section class="detail" id="POLYGONAREATYPE">
<h3>POLYGONAREATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">POLYGONAREATYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a polygon.</div>
</section>
</li>
<li>
<section class="detail" id="RECTANGULARAREATYPE">
<h3>RECTANGULARAREATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">RECTANGULARAREATYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a rectangle.</div>
</section>
</li>
<li>
<section class="detail" id="ELIPTICALAREATYPE">
<h3>ELIPTICALAREATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">ELIPTICALAREATYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by an ellipse.</div>
</section>
</li>
<li>
<section class="detail" id="CIRCULARAREATYPE">
<h3>CIRCULARAREATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">CIRCULARAREATYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of space enclosed by a circle.</div>
</section>
</li>
<li>
<section class="detail" id="OTHERTYPE">
<h3>OTHERTYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">OTHERTYPE</span></div>
<div class="block">Indicates that the Location associated with the LocationTypeKind describes a type of is a LocationKindType that is not on the enumerated list.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">from</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>toEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a></span> <span class="element-name">toEnum</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnumerationLiteral(com.nomagic.magicdraw.uaf.UAF,com.nomagic.magicdraw.uaf.UAF.LocationTypeKindEnum)">
<h3>toEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">toEnumerationLiteral</span><wbr/><span class="parameters">(<a href="UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a> profile,
 <a href="UAF.LocationTypeKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.LocationTypeKindEnum</a> anEnum)</span></div>
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
