# JAVA OPENAPI: UPDMProfile.RuleKindEnum (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/updm/utils/UPDMProfile.RuleKindEnum.html
- source_path: `com/nomagic/updm/utils/UPDMProfile.RuleKindEnum.html`
- source_sha256: `8532780ea053b2d9946ad079af8b5dca29794080fb9d65ba74f415ffc096ad08`
- captured_utc: `2026-07-14T16:59:12.760695+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.updm.utils](package-summary.html)

## Enum Class UPDMProfile.RuleKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)>
com.nomagic.updm.utils.UPDMProfile.RuleKindEnum

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html)<[UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
`[UPDMProfile](UPDMProfile.html)`

public static enumUPDMProfile.RuleKindEnum
extends [Enum](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)>

Enumeration of possible kinds for constraints.

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[ACTIONASSERTION](#ACTIONASSERTION)`
Statement that concerns some dynamic aspect of the business.
`[AGREEMENT](#AGREEMENT)`
A consent among parties regarding the terms and conditions of activities that said parties participate in.
`[CONSTRAINT](#CONSTRAINT)`
Business Rule, Rule, Restraint, Operational Limitation.
`[DERIVATION](#DERIVATION)`
Rule derived from another rule.
`[GUIDANCE](#GUIDANCE)`
An authoritative statement intended to lead or steer the execution of actions.
`[SECURITYPOLICY](#SECURITYPOLICY)`
An OperationalConstraint that specifies policy for information handling, physical security, encryption, etc.
`[STRUCTURALASSERTION](#STRUCTURALASSERTION)`
Statement that something of importance to the business either exists as a concept of interest or exists in relationship to another thing of interest.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)`
`[from](#from(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`

`static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)`
`[toEnum](#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[toEnumerationLiteral](#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.RuleKindEnum))([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) anEnum)`

`static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
STRUCTURALASSERTION
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) STRUCTURALASSERTION
Statement that something of importance to the business either exists as a concept of interest or exists in relationship to another thing of interest.
ACTIONASSERTION
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) ACTIONASSERTION
Statement that concerns some dynamic aspect of the business.
DERIVATION
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) DERIVATION
Rule derived from another rule.
AGREEMENT
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) AGREEMENT
A consent among parties regarding the terms and conditions of activities that said parties participate in.
CONSTRAINT
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) CONSTRAINT
Business Rule, Rule, Restraint, Operational Limitation.
GUIDANCE
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) GUIDANCE
An authoritative statement intended to lead or steer the execution of actions.
SECURITYPOLICY
public static final [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) SECURITYPOLICY
An OperationalConstraint that specifies policy for information handling, physical security, encryption, etc.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) valueOf([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Returns the enum constant of this class with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this class. (Extraneous whitespace characters are 
not permitted.)
Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if this enum class has no constant with the specified name
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the argument is null
getText
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getText()
from
@CheckForNullpublic static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) from(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
toEnum
@CheckForNullpublic static [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) toEnum([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
toEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) toEnumerationLiteral([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.RuleKindEnum](UPDMProfile.RuleKindEnum.html) anEnum)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.updm.utils</a></div>
<h1 class="title" title="Enum Class UPDMProfile.RuleKindEnum">Enum Class UPDMProfile.RuleKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a>&gt;
<div class="inheritance">com.nomagic.updm.utils.UPDMProfile.RuleKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">UPDMProfile.RuleKindEnum</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a>&gt;</span></div>
<div class="block">Enumeration of possible kinds for constraints.</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#ACTIONASSERTION">ACTIONASSERTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Statement that concerns some dynamic aspect of the business.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#AGREEMENT">AGREEMENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A consent among parties regarding the terms and conditions of activities that said parties participate in.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#CONSTRAINT">CONSTRAINT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Business Rule, Rule, Restraint, Operational Limitation.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#DERIVATION">DERIVATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Rule derived from another rule.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#GUIDANCE">GUIDANCE</a></code></div>
<div class="col-last even-row-color">
<div class="block">An authoritative statement intended to lead or steer the execution of actions.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SECURITYPOLICY">SECURITYPOLICY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An OperationalConstraint that specifies policy for information handling, physical security, encryption, etc.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#STRUCTURALASSERTION">STRUCTURALASSERTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Statement that something of importance to the business either exists as a concept of interest or exists in relationship to another thing of interest.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#from(java.lang.Object)">from</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">toEnum</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.RuleKindEnum)">toEnumerationLiteral</a><wbr/>(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a> anEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="STRUCTURALASSERTION">
<h3>STRUCTURALASSERTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">STRUCTURALASSERTION</span></div>
<div class="block">Statement that something of importance to the business either exists as a concept of interest or exists in relationship to another thing of interest.</div>
</section>
</li>
<li>
<section class="detail" id="ACTIONASSERTION">
<h3>ACTIONASSERTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">ACTIONASSERTION</span></div>
<div class="block">Statement that concerns some dynamic aspect of the business.</div>
</section>
</li>
<li>
<section class="detail" id="DERIVATION">
<h3>DERIVATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">DERIVATION</span></div>
<div class="block">Rule derived from another rule.</div>
</section>
</li>
<li>
<section class="detail" id="AGREEMENT">
<h3>AGREEMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">AGREEMENT</span></div>
<div class="block">A consent among parties regarding the terms and conditions of activities that said parties participate in.</div>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINT">
<h3>CONSTRAINT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">CONSTRAINT</span></div>
<div class="block">Business Rule, Rule, Restraint, Operational Limitation.</div>
</section>
</li>
<li>
<section class="detail" id="GUIDANCE">
<h3>GUIDANCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">GUIDANCE</span></div>
<div class="block">An authoritative statement intended to lead or steer the execution of actions.</div>
</section>
</li>
<li>
<section class="detail" id="SECURITYPOLICY">
<h3>SECURITYPOLICY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">SECURITYPOLICY</span></div>
<div class="block">An OperationalConstraint that specifies policy for information handling, physical security, encryption, etc.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
</section>
</li>
<li>
<section class="detail" id="from(java.lang.Object)">
<h3>from</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">from</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>toEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a></span> <span class="element-name">toEnum</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.RuleKindEnum)">
<h3>toEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">toEnumerationLiteral</span><wbr/><span class="parameters">(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.RuleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RuleKindEnum</a> anEnum)</span></div>
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
