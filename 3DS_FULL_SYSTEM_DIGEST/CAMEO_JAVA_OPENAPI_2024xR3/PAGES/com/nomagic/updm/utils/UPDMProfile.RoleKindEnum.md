# JAVA OPENAPI: UPDMProfile.RoleKindEnum (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/updm/utils/UPDMProfile.RoleKindEnum.html
- source_path: `com/nomagic/updm/utils/UPDMProfile.RoleKindEnum.html`
- source_sha256: `72d7cd8621c735124dc5ee2ce657a625c15e95640e83bf8051229ee00f52f794`
- captured_utc: `2026-07-14T16:56:38.435941+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.updm.utils](package-summary.html)

## Enum Class UPDMProfile.RoleKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)>
com.nomagic.updm.utils.UPDMProfile.RoleKindEnum

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
[UPDMProfile](UPDMProfile.html)

public static enumUPDMProfile.RoleKindEnum
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)>

Enumeration of the roles that a ResourceRole may play in the context of a CapabilityConfiguration or System, used to support the RoleKind tag of a ResourceRole.

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[COMPONENT](#COMPONENT)`
(MODAF SoftwareComponent) Asserts that Software is a component of another Software.
`[EQUIPMENT](#EQUIPMENT)`
UPDM: Equipment is a physical resource that is used to accomplish a task or function in a system or an environment.
`[HOSTED_SOFTWARE](#HOSTED_SOFTWARE)`
Asserts that Software is hosted on a ResourceArtifact (which means the artifact is some kind of computer system).
`[HUMAN_RESOURCE](#HUMAN_RESOURCE)`
The role of an OrganizationalResource in a PhysicalArchitecture.
`[OTHER](#OTHER)`
Other MODAF Role kind that is not on the enumerated list.
`[PART](#PART)`
Usage of a ResourceArtifact as a part of another ResourceArtifact.
`[PLATFORM](#PLATFORM)`
Usage of a ResourceArtifact as a platform (e.g.
`[POST_ROLE](#POST_ROLE)`
(MODAF Post) Asserts that a Post exists in an OrganizationType of the type specified by the related PostType.
`[RESPONSIBILITY_ROLE](#RESPONSIBILITY_ROLE)`
(MODAF Role) A ResourceUsage that asserts a given PostType has a RoleType.
`[SERVICE_ACCESS_ROLE](#SERVICE_ACCESS_ROLE)`
A ResourceUsage that asserts a given ServiceAccess is used in the context of a particular service usage.
`[SUB_ORGANIZATION](#SUB_ORGANIZATION)`
Asserts that one OrganizationType is typically the parent of another - e.g.
`[SUB_SYSTEM_PART](#SUB_SYSTEM_PART)`
UPDM: Indicates that a (sub)system is part of another system.
`[SYSTEM](#SYSTEM)`
The usage of a ResourceArtifact as a System in a PhysicalArchitecture.
`[USED_CONFIGURATION](#USED_CONFIGURATION)`
The usage of a PhysicalArchitecture in another PhysicalArchitecture.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)`
`[from](#from(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`

`static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)`
`[toEnum](#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[toEnumerationLiteral](#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.RoleKindEnum))([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) anEnum)`

`static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)[]`
`[values](#values())()`
Returns an array containing the constants of this enum class, in
the order they are declared.
Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ ENUM CONSTANT DETAIL =========== 
Enum Constant Details
PART
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) PART
Usage of a ResourceArtifact as a part of another ResourceArtifact.
COMPONENT
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) COMPONENT
(MODAF SoftwareComponent) Asserts that Software is a component of another Software.
USED_CONFIGURATION
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) USED_CONFIGURATION
The usage of a PhysicalArchitecture in another PhysicalArchitecture.
HUMAN_RESOURCE
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) HUMAN_RESOURCE
The role of an OrganizationalResource in a PhysicalArchitecture.
PLATFORM
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) PLATFORM
Usage of a ResourceArtifact as a platform (e.g. vessel, aircraft, etc.) in a particular PhysicalArchitecture.
SYSTEM
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) SYSTEM
The usage of a ResourceArtifact as a System in a PhysicalArchitecture.
SUB_ORGANIZATION
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) SUB_ORGANIZATION
Asserts that one OrganizationType is typically the parent of another - e.g. a squadron may be part of a batallion.
POST_ROLE
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) POST_ROLE
(MODAF Post) Asserts that a Post exists in an OrganizationType of the type specified by the related PostType.
RESPONSIBILITY_ROLE
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) RESPONSIBILITY_ROLE
(MODAF Role) A ResourceUsage that asserts a given PostType has a RoleType.
SERVICE_ACCESS_ROLE
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) SERVICE_ACCESS_ROLE
A ResourceUsage that asserts a given ServiceAccess is used in the context of a particular service usage.
EQUIPMENT
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) EQUIPMENT
UPDM: Equipment is a physical resource that is used to accomplish a task or function in a system or an environment.
 MODAF: (MODAF::PhysicalAsset): Usage of an ResourceArtifact (MODAF::Artefact) as a component of a ResourceConfiguration.
 DoDAF: NA
SUB_SYSTEM_PART
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) SUB_SYSTEM_PART
UPDM: Indicates that a (sub)system is part of another system.
 MODAF: Usage of an Artefact (UPDM::ResourceArtifact) as a part of another Artefact (UPDM::ResourceArtifact), equates to a MODAF::Part
 DoDAF: NA
HOSTED_SOFTWARE
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) HOSTED_SOFTWARE
Asserts that Software is hosted on a ResourceArtifact (which means the artifact is some kind of computer system).
OTHER
public static final [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) OTHER
Other MODAF Role kind that is not on the enumerated list.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
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
@CheckForNullpublic static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) from(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
toEnum
@CheckForNullpublic static [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) toEnum([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
toEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) toEnumerationLiteral([UPDMProfile](UPDMProfile.html) profile,
 [UPDMProfile.RoleKindEnum](UPDMProfile.RoleKindEnum.html) anEnum)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.updm.utils</a></div>
<h1 class="title" title="Enum Class UPDMProfile.RoleKindEnum">Enum Class UPDMProfile.RoleKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a>&gt;
<div class="inheritance">com.nomagic.updm.utils.UPDMProfile.RoleKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">UPDMProfile.RoleKindEnum</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a>&gt;</span></div>
<div class="block">Enumeration of the roles that a ResourceRole may play in the context of a CapabilityConfiguration or System, used to support the RoleKind tag of a ResourceRole.</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#COMPONENT">COMPONENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">(MODAF SoftwareComponent) Asserts that Software is a component of another Software.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#EQUIPMENT">EQUIPMENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">UPDM: Equipment is a physical resource that is used to accomplish a task or function in a system or an environment.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#HOSTED_SOFTWARE">HOSTED_SOFTWARE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Asserts that Software is hosted on a ResourceArtifact (which means the artifact is some kind of computer system).</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#HUMAN_RESOURCE">HUMAN_RESOURCE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The role of an OrganizationalResource in a PhysicalArchitecture.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#OTHER">OTHER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Other MODAF Role kind that is not on the enumerated list.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#PART">PART</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Usage of a ResourceArtifact as a part of another ResourceArtifact.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#PLATFORM">PLATFORM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Usage of a ResourceArtifact as a platform (e.g.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#POST_ROLE">POST_ROLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">(MODAF Post) Asserts that a Post exists in an OrganizationType of the type specified by the related PostType.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#RESPONSIBILITY_ROLE">RESPONSIBILITY_ROLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">(MODAF Role) A ResourceUsage that asserts a given PostType has a RoleType.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SERVICE_ACCESS_ROLE">SERVICE_ACCESS_ROLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A ResourceUsage that asserts a given ServiceAccess is used in the context of a particular service usage.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SUB_ORGANIZATION">SUB_ORGANIZATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Asserts that one OrganizationType is typically the parent of another - e.g.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SUB_SYSTEM_PART">SUB_SYSTEM_PART</a></code></div>
<div class="col-last odd-row-color">
<div class="block">UPDM: Indicates that a (sub)system is part of another system.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SYSTEM">SYSTEM</a></code></div>
<div class="col-last even-row-color">
<div class="block">The usage of a ResourceArtifact as a System in a PhysicalArchitecture.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#USED_CONFIGURATION">USED_CONFIGURATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The usage of a PhysicalArchitecture in another PhysicalArchitecture.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#from(java.lang.Object)">from</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">toEnum</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.RoleKindEnum)">toEnumerationLiteral</a><wbr/>(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a> anEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a>[]</code></div>
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
<section class="detail" id="PART">
<h3>PART</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">PART</span></div>
<div class="block">Usage of a ResourceArtifact as a part of another ResourceArtifact.</div>
</section>
</li>
<li>
<section class="detail" id="COMPONENT">
<h3>COMPONENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">COMPONENT</span></div>
<div class="block">(MODAF SoftwareComponent) Asserts that Software is a component of another Software.</div>
</section>
</li>
<li>
<section class="detail" id="USED_CONFIGURATION">
<h3>USED_CONFIGURATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">USED_CONFIGURATION</span></div>
<div class="block">The usage of a PhysicalArchitecture in another PhysicalArchitecture.</div>
</section>
</li>
<li>
<section class="detail" id="HUMAN_RESOURCE">
<h3>HUMAN_RESOURCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">HUMAN_RESOURCE</span></div>
<div class="block">The role of an OrganizationalResource in a PhysicalArchitecture.</div>
</section>
</li>
<li>
<section class="detail" id="PLATFORM">
<h3>PLATFORM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">PLATFORM</span></div>
<div class="block">Usage of a ResourceArtifact as a platform (e.g. vessel, aircraft, etc.) in a particular PhysicalArchitecture.</div>
</section>
</li>
<li>
<section class="detail" id="SYSTEM">
<h3>SYSTEM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">SYSTEM</span></div>
<div class="block">The usage of a ResourceArtifact as a System in a PhysicalArchitecture.</div>
</section>
</li>
<li>
<section class="detail" id="SUB_ORGANIZATION">
<h3>SUB_ORGANIZATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">SUB_ORGANIZATION</span></div>
<div class="block">Asserts that one OrganizationType is typically the parent of another - e.g. a squadron may be part of a batallion.</div>
</section>
</li>
<li>
<section class="detail" id="POST_ROLE">
<h3>POST_ROLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">POST_ROLE</span></div>
<div class="block">(MODAF Post) Asserts that a Post exists in an OrganizationType of the type specified by the related PostType.</div>
</section>
</li>
<li>
<section class="detail" id="RESPONSIBILITY_ROLE">
<h3>RESPONSIBILITY_ROLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">RESPONSIBILITY_ROLE</span></div>
<div class="block">(MODAF Role) A ResourceUsage that asserts a given PostType has a RoleType.</div>
</section>
</li>
<li>
<section class="detail" id="SERVICE_ACCESS_ROLE">
<h3>SERVICE_ACCESS_ROLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">SERVICE_ACCESS_ROLE</span></div>
<div class="block">A ResourceUsage that asserts a given ServiceAccess is used in the context of a particular service usage.</div>
</section>
</li>
<li>
<section class="detail" id="EQUIPMENT">
<h3>EQUIPMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">EQUIPMENT</span></div>
<div class="block">UPDM: Equipment is a physical resource that is used to accomplish a task or function in a system or an environment.
                 MODAF: (MODAF::PhysicalAsset): Usage of an ResourceArtifact (MODAF::Artefact) as a component of a ResourceConfiguration.
                 DoDAF: NA</div>
</section>
</li>
<li>
<section class="detail" id="SUB_SYSTEM_PART">
<h3>SUB_SYSTEM_PART</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">SUB_SYSTEM_PART</span></div>
<div class="block">UPDM: Indicates that a (sub)system is part of another system.
                 MODAF: Usage of an Artefact (UPDM::ResourceArtifact) as a part of another Artefact (UPDM::ResourceArtifact), equates to a MODAF::Part
                 DoDAF: NA</div>
</section>
</li>
<li>
<section class="detail" id="HOSTED_SOFTWARE">
<h3>HOSTED_SOFTWARE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">HOSTED_SOFTWARE</span></div>
<div class="block">Asserts that Software is hosted on a ResourceArtifact (which means the artifact is some kind of computer system).</div>
</section>
</li>
<li>
<section class="detail" id="OTHER">
<h3>OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">OTHER</span></div>
<div class="block">Other MODAF Role kind that is not on the enumerated list.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">from</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>toEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a></span> <span class="element-name">toEnum</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnumerationLiteral(com.nomagic.updm.utils.UPDMProfile,com.nomagic.updm.utils.UPDMProfile.RoleKindEnum)">
<h3>toEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">toEnumerationLiteral</span><wbr/><span class="parameters">(<a href="UPDMProfile.html" title="class in com.nomagic.updm.utils">UPDMProfile</a> profile,
 <a href="UPDMProfile.RoleKindEnum.html" title="enum class in com.nomagic.updm.utils">UPDMProfile.RoleKindEnum</a> anEnum)</span></div>
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
