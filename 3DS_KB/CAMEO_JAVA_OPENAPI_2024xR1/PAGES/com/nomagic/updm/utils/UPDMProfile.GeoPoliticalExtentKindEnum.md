# JAVA OPENAPI: UPDMProfile.GeoPoliticalExtentKindEnum (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/updm/utils/UPDMProfile.GeoPoliticalExtentKindEnum.html
- source_path: `com/nomagic/updm/utils/UPDMProfile.GeoPoliticalExtentKindEnum.html`
- source_sha256: `348182da7bcfc98f65e61d6910503f61f4070b61269db3a5f45784bb46f88ee2`
- captured_utc: `2026-07-14T16:53:18.466700+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.updm.utils](package-summary.html)

## Enum Class UPDMProfile.GeoPoliticalExtentKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)>
com.nomagic.updm.utils.UPDMProfile.GeoPoliticalExtentKindEnum

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
[UPDMProfile](UPDMProfile.html)

public static enumUPDMProfile.GeoPoliticalExtentKindEnum
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)>

Enumeration of geopolitical extent kinds, used to support the geoPoliticalExtentKind tag of the geoPoliticalExtent stereotype.

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[COUNTRY](#COUNTRY)`
A political state or nation or its territory.
`[FACILITY](#FACILITY)`
A real property entity consisting of underlying land and one or more of the following: a building, a structure (including linear structures), a utility system, or pavement.
`[GEOFEATURE](#GEOFEATURE)`
An object that encompasses meteorological, geographic, and control features mission significance.
`[INSTALLATION](#INSTALLATION)`
A base, camp, post, station, yard, center, or other activity, including leased facilities, without regard to the duration of operational control.
`[OTHER](#OTHER)`
Other GeoPoliticalExtent kind that is not on the enumerated list.
`[REGIONOFCOUNTRY](#REGIONOFCOUNTRY)`
A large, usually continuous segment of a political state or nation or its territory.
`[REGIONOFWORLD](#REGIONOFWORLD)`
A large, usually continuous segment of a surface or space; area.
`[SITE](#SITE)`
Physical (geographic) location that is or was owned by, leased to, or otherwise possessed.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)`
`[from](#from(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`

`static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)`
`[toEnum](#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[toEnumerationLiteral](#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.GeoPoliticalExtentKindEnum))([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) anEnum)`

`static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
GEOFEATURE
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) GEOFEATURE
An object that encompasses meteorological, geographic, and control features mission significance.
REGIONOFCOUNTRY
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) REGIONOFCOUNTRY
A large, usually continuous segment of a political state or nation or its territory.
COUNTRY
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) COUNTRY
A political state or nation or its territory.
REGIONOFWORLD
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) REGIONOFWORLD
A large, usually continuous segment of a surface or space; area.
FACILITY
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) FACILITY
A real property entity consisting of underlying land and one or more of the following: a building, a structure (including linear structures), a utility system, or pavement.
SITE
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) SITE
Physical (geographic) location that is or was owned by, leased to, or otherwise possessed. Each site is assigned to a single installation. A site may exist in one of three forms: (1) Land only, where there are no facilities present and where the land consists of either a single land parcel or two or more contiguous land parcels. (2) Facility or facilities only, where the underlying land is neither owned nor controlled by the government. A stand-alone facility can be a site. If a facility is not a stand-alone facility, it must be assigned to a site. (3). Land and all the facilities thereon, where the land consists of either a single land parcel or two or more contiguous land parcels.
INSTALLATION
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) INSTALLATION
A base, camp, post, station, yard, center, or other activity, including leased facilities, without regard to the duration of operational control. An installation may include one or more sites.
OTHER
public static final [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) OTHER
Other GeoPoliticalExtent kind that is not on the enumerated list.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
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
@CheckForNullpublic static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) from(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
toEnum
@CheckForNullpublic static [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) toEnum([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
toEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) toEnumerationLiteral([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.GeoPoliticalExtentKindEnum](UPDMProfile.GeoPoliticalExtentKindEnum.html) anEnum)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.updm.utils</a></div>
<h1 class="title" title="Enum Class UPDMProfile.GeoPoliticalExtentKindEnum">Enum Class UPDMProfile.GeoPoliticalExtentKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a>&gt;
<div class="inheritance">com.nomagic.updm.utils.UPDMProfile.GeoPoliticalExtentKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">UPDMProfile.GeoPoliticalExtentKindEnum</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a>&gt;</span></div>
<div class="block">Enumeration of geopolitical extent kinds, used to support the geoPoliticalExtentKind tag of the geoPoliticalExtent stereotype.</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#COUNTRY">COUNTRY</a></code></div>
<div class="col-last even-row-color">
<div class="block">A political state or nation or its territory.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#FACILITY">FACILITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A real property entity consisting of underlying land and one or more of the following: a building, a structure (including linear structures), a utility system, or pavement.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#GEOFEATURE">GEOFEATURE</a></code></div>
<div class="col-last even-row-color">
<div class="block">An object that encompasses meteorological, geographic, and control features mission significance.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#INSTALLATION">INSTALLATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A base, camp, post, station, yard, center, or other activity, including leased facilities, without regard to the duration of operational control.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#OTHER">OTHER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Other GeoPoliticalExtent kind that is not on the enumerated list.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#REGIONOFCOUNTRY">REGIONOFCOUNTRY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A large, usually continuous segment of a political state or nation or its territory.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#REGIONOFWORLD">REGIONOFWORLD</a></code></div>
<div class="col-last even-row-color">
<div class="block">A large, usually continuous segment of a surface or space; area.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SITE">SITE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Physical (geographic) location that is or was owned by, leased to, or otherwise possessed.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#from(java.lang.Object)">from</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">toEnum</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.GeoPoliticalExtentKindEnum)">toEnumerationLiteral</a><wbr/>(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a> anEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a>[]</code></div>
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
<section class="detail" id="GEOFEATURE">
<h3>GEOFEATURE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">GEOFEATURE</span></div>
<div class="block">An object that encompasses meteorological, geographic, and control features mission significance.</div>
</section>
</li>
<li>
<section class="detail" id="REGIONOFCOUNTRY">
<h3>REGIONOFCOUNTRY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">REGIONOFCOUNTRY</span></div>
<div class="block">A large, usually continuous segment of a political state or nation or its territory.</div>
</section>
</li>
<li>
<section class="detail" id="COUNTRY">
<h3>COUNTRY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">COUNTRY</span></div>
<div class="block">A political state or nation or its territory.</div>
</section>
</li>
<li>
<section class="detail" id="REGIONOFWORLD">
<h3>REGIONOFWORLD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">REGIONOFWORLD</span></div>
<div class="block">A large, usually continuous segment of a surface or space; area.</div>
</section>
</li>
<li>
<section class="detail" id="FACILITY">
<h3>FACILITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">FACILITY</span></div>
<div class="block">A real property entity consisting of underlying land and one or more of the following: a building, a structure (including linear structures), a utility system, or pavement.</div>
</section>
</li>
<li>
<section class="detail" id="SITE">
<h3>SITE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">SITE</span></div>
<div class="block">Physical (geographic) location that is or was owned by, leased to, or otherwise possessed. Each site is assigned to a single installation. A site may exist in one of three forms: (1) Land only, where there are no facilities present and where the land consists of either a single land parcel or two or more contiguous land parcels. (2) Facility or facilities only, where the underlying land is neither owned nor controlled by the government. A stand-alone facility can be a site. If a facility is not a stand-alone facility, it must be assigned to a site. (3). Land and all the facilities thereon, where the land consists of either a single land parcel or two or more contiguous land parcels.</div>
</section>
</li>
<li>
<section class="detail" id="INSTALLATION">
<h3>INSTALLATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">INSTALLATION</span></div>
<div class="block">A base, camp, post, station, yard, center, or other activity, including leased facilities, without regard to the duration of operational control. An installation may include one or more sites.</div>
</section>
</li>
<li>
<section class="detail" id="OTHER">
<h3>OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">OTHER</span></div>
<div class="block">Other GeoPoliticalExtent kind that is not on the enumerated list.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">from</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>toEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a></span> <span class="element-name">toEnum</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.GeoPoliticalExtentKindEnum)">
<h3>toEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">toEnumerationLiteral</span><wbr/><span class="parameters">(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.GeoPoliticalExtentKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.GeoPoliticalExtentKindEnum</a> anEnum)</span></div>
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
