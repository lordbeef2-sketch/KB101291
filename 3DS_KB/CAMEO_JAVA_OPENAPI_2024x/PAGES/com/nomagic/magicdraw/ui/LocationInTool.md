# JAVA OPENAPI: LocationInTool (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/LocationInTool.html
- source_path: `com/nomagic/magicdraw/ui/LocationInTool.html`
- source_sha256: `78059880479a0e1185a91c89cea24edbb709249e57651c5c7659f4ac560a2395`
- captured_utc: `2026-07-14T16:52:02.722756+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Enum Class LocationInTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[LocationInTool](LocationInTool.html)>
com.nomagic.magicdraw.ui.LocationInTool

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[LocationInTool](LocationInTool.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

@OpenApiAllpublic enumLocationInTool
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[LocationInTool](LocationInTool.html)>

Location in MagicDraw tool. Used as invocation information for some actions (Element creation, diagram opening, representation text creation and etc.)

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[application](#application)`
application wide context, i.e a notification or some ui element that is used in many places
`[browser](#browser)`
browser (containment) window
`[diagram](#diagram)`
inside the diagram panel
`[diagram_context_menu](#diagram_context_menu)`
a context menu inside the diagram panel
`[diagram_toolbar](#diagram_toolbar)`
top toolbar bar of the diagram
`[diagram_window_tab_context_menu](#diagram_window_tab_context_menu)`
a context menu for a diagram window tab
`[main_toolbar](#main_toolbar)`
main MD menu and toolbar
`[project_window](#project_window)`
project specific window location, i.e validation results or find usages
`[specification_dialog](#specification_dialog)`
element specification dialog
`[unknown](#unknown)`
undefined context
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [LocationInTool](LocationInTool.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [LocationInTool](LocationInTool.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
unknown
public static final [LocationInTool](LocationInTool.html) unknown
undefined context
application
public static final [LocationInTool](LocationInTool.html) application
application wide context, i.e a notification or some ui element that is used in many places
project_window
public static final [LocationInTool](LocationInTool.html) project_window
project specific window location, i.e validation results or find usages
specification_dialog
public static final [LocationInTool](LocationInTool.html) specification_dialog
element specification dialog
main_toolbar
public static final [LocationInTool](LocationInTool.html) main_toolbar
main MD menu and toolbar
browser
public static final [LocationInTool](LocationInTool.html) browser
browser (containment) window
diagram
public static final [LocationInTool](LocationInTool.html) diagram
inside the diagram panel
diagram_toolbar
public static final [LocationInTool](LocationInTool.html) diagram_toolbar
top toolbar bar of the diagram
diagram_context_menu
public static final [LocationInTool](LocationInTool.html) diagram_context_menu
a context menu inside the diagram panel
diagram_window_tab_context_menu
public static final [LocationInTool](LocationInTool.html) diagram_window_tab_context_menu
a context menu for a diagram window tab
 ============ METHOD DETAIL ========== 
Method Details
values
public static [LocationInTool](LocationInTool.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [LocationInTool](LocationInTool.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
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

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Enum Class LocationInTool">Enum Class LocationInTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.ui.LocationInTool</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public enum </span><span class="element-name type-name-label">LocationInTool</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a>&gt;</span></div>
<div class="block">Location in MagicDraw tool. Used as invocation information for some actions (Element creation, diagram opening, representation text creation and etc.)</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#application">application</a></code></div>
<div class="col-last even-row-color">
<div class="block">application wide context, i.e a notification or some ui element that is used in many places</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#browser">browser</a></code></div>
<div class="col-last odd-row-color">
<div class="block">browser (containment) window</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#diagram">diagram</a></code></div>
<div class="col-last even-row-color">
<div class="block">inside the diagram panel</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#diagram_context_menu">diagram_context_menu</a></code></div>
<div class="col-last odd-row-color">
<div class="block">a context menu inside the diagram panel</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#diagram_toolbar">diagram_toolbar</a></code></div>
<div class="col-last even-row-color">
<div class="block">top toolbar bar of the diagram</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#diagram_window_tab_context_menu">diagram_window_tab_context_menu</a></code></div>
<div class="col-last odd-row-color">
<div class="block">a context menu for a diagram window tab</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#main_toolbar">main_toolbar</a></code></div>
<div class="col-last even-row-color">
<div class="block">main MD menu and toolbar</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#project_window">project_window</a></code></div>
<div class="col-last odd-row-color">
<div class="block">project specific window location, i.e validation results or find usages</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#specification_dialog">specification_dialog</a></code></div>
<div class="col-last even-row-color">
<div class="block">element specification dialog</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#unknown">unknown</a></code></div>
<div class="col-last odd-row-color">
<div class="block">undefined context</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a>[]</code></div>
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
<section class="detail" id="unknown">
<h3>unknown</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">unknown</span></div>
<div class="block">undefined context</div>
</section>
</li>
<li>
<section class="detail" id="application">
<h3>application</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">application</span></div>
<div class="block">application wide context, i.e a notification or some ui element that is used in many places</div>
</section>
</li>
<li>
<section class="detail" id="project_window">
<h3>project_window</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">project_window</span></div>
<div class="block">project specific window location, i.e validation results or find usages</div>
</section>
</li>
<li>
<section class="detail" id="specification_dialog">
<h3>specification_dialog</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">specification_dialog</span></div>
<div class="block">element specification dialog</div>
</section>
</li>
<li>
<section class="detail" id="main_toolbar">
<h3>main_toolbar</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">main_toolbar</span></div>
<div class="block">main MD menu and toolbar</div>
</section>
</li>
<li>
<section class="detail" id="browser">
<h3>browser</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">browser</span></div>
<div class="block">browser (containment) window</div>
</section>
</li>
<li>
<section class="detail" id="diagram">
<h3>diagram</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">diagram</span></div>
<div class="block">inside the diagram panel</div>
</section>
</li>
<li>
<section class="detail" id="diagram_toolbar">
<h3>diagram_toolbar</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">diagram_toolbar</span></div>
<div class="block">top toolbar bar of the diagram</div>
</section>
</li>
<li>
<section class="detail" id="diagram_context_menu">
<h3>diagram_context_menu</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">diagram_context_menu</span></div>
<div class="block">a context menu inside the diagram panel</div>
</section>
</li>
<li>
<section class="detail" id="diagram_window_tab_context_menu">
<h3>diagram_window_tab_context_menu</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">diagram_window_tab_context_menu</span></div>
<div class="block">a context menu for a diagram window tab</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="LocationInTool.html" title="enum class in com.nomagic.magicdraw.ui">LocationInTool</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
