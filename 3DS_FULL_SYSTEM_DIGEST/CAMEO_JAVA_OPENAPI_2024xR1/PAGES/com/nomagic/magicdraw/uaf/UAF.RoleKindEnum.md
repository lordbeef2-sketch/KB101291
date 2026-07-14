# JAVA OPENAPI: UAF.RoleKindEnum (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uaf/UAF.RoleKindEnum.html
- source_path: `com/nomagic/magicdraw/uaf/UAF.RoleKindEnum.html`
- source_sha256: `6918a54b5380e7fc79d826f4f6f8667b224dc919b6a7247a95fe7e0d3afdda8d`
- captured_utc: `2026-07-14T16:51:57.773691+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uaf](package-summary.html)

## Enum Class UAF.RoleKindEnum

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UAF.RoleKindEnum](UAF.RoleKindEnum.html)>
com.nomagic.magicdraw.uaf.UAF.RoleKindEnum

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)<[UAF.RoleKindEnum](UAF.RoleKindEnum.html)>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)`

Enclosing class:
[UAF](UAF.html)

public static enumUAF.RoleKindEnum
extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)<[UAF.RoleKindEnum](UAF.RoleKindEnum.html)>

Enumeration of the possible kinds of roles that a ResourceRole may play in the context of a ResourcePerformer.

=========== ENUM CONSTANT SUMMARY =========== 
Enum Constant Summary
Enum Constants
Enum Constant
Description
`[ARTIFACT_COMPONENT](#ARTIFACT_COMPONENT)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of non human resource that is used as a component in the context of a ResourcePerformer.
`[COMPONENT](#COMPONENT)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Software that is used in the context of a ResourcePerformer.
`[EQUIPMENT](#EQUIPMENT)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of man made resource that is used to accomplish a task or function in the context of a ResourcePerformer.
`[HOSTED_SOFTWARE](#HOSTED_SOFTWARE)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of software that is used in the context of a ResourcePerformer.
`[HUMAN_RESOURCE](#HUMAN_RESOURCE)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of human resource that is used in the context of a ResourcePerformer.
`[NATURAL_RESOURCE_COMPONENT](#NATURAL_RESOURCE_COMPONENT)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of natural resource that is used as a component in the context of a ResourcePerformer.
`[OTHER](#OTHER)`
Indicates that the ResourceRole associated with the ResourceRoleKind is another kind of RoleKind that is not on the enumerated list.
`[PART](#PART)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that is used as a part of another ResourcePerformer.
`[PLATFORM](#PLATFORM)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that represents a platform (e.g.
`[POST_ROLE](#POST_ROLE)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Post that is used in the context of a ResourcePerformer.
`[RESPONSIBILITY_ROLE](#RESPONSIBILITY_ROLE)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Responsibility associated with a role that is used in the context of a ResourcePerformer.
`[SUB_ORGANIZATION](#SUB_ORGANIZATION)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Organization that is typically the parent of another - e.g.
`[SUB_SYSTEM_PART](#SUB_SYSTEM_PART)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of subsystem (represented as a ResourcePerformers) is is part of another ResourcePerformer.
`[SYSTEM](#SYSTEM)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of assembly of ResourcePerformers that is used in the context of another ResourcePerformer.
`[USED_CONFIGURATION](#USED_CONFIGURATION)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing CapabilityConfiguration that is used in the context of a ResourcePerformer.
`[USED_PHYSICAL_ARCHITECTURE](#USED_PHYSICAL_ARCHITECTURE)`
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing PhysicalArchitecture that is used in the context of a ResourcePerformer.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [UAF.RoleKindEnum](UAF.RoleKindEnum.html)`
`[from](#from(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getText](#getText())()`

`static [UAF.RoleKindEnum](UAF.RoleKindEnum.html)`
`[toEnum](#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)`

`static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[toEnumerationLiteral](#toEnumerationLiteral(com.nomagic.magicdraw.uaf.UAF,com.nomagic.magicdraw.uaf.UAF.RoleKindEnum))([UAF](UAF.html) profile,
 [UAF.RoleKindEnum](UAF.RoleKindEnum.html) anEnum)`

`static [UAF.RoleKindEnum](UAF.RoleKindEnum.html)`
`[valueOf](#valueOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Returns the enum constant of this class with the specified name.
`static [UAF.RoleKindEnum](UAF.RoleKindEnum.html)[]`
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
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) PART
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that is used as a part of another ResourcePerformer.
COMPONENT
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) COMPONENT
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Software that is used in the context of a ResourcePerformer.
USED_CONFIGURATION
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) USED_CONFIGURATION
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing CapabilityConfiguration that is used in the context of a ResourcePerformer.
HUMAN_RESOURCE
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) HUMAN_RESOURCE
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of human resource that is used in the context of a ResourcePerformer.
PLATFORM
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) PLATFORM
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that represents a platform (e.g. vessel, aircraft, etc.) that is used in the context of a SystemsResource.
SYSTEM
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) SYSTEM
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of assembly of ResourcePerformers that is used in the context of another ResourcePerformer.
SUB_ORGANIZATION
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) SUB_ORGANIZATION
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Organization that is typically the parent of another - e.g. a squadron may be part of a batallion, that is used in the context of a ResourcePerformer.
POST_ROLE
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) POST_ROLE
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Post that is used in the context of a ResourcePerformer.
RESPONSIBILITY_ROLE
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) RESPONSIBILITY_ROLE
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Responsibility associated with a role that is used in the context of a ResourcePerformer.
EQUIPMENT
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) EQUIPMENT
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of man made resource that is used to accomplish a task or function in the context of a ResourcePerformer.
SUB_SYSTEM_PART
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) SUB_SYSTEM_PART
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of subsystem (represented as a ResourcePerformers) is is part of another ResourcePerformer.
USED_PHYSICAL_ARCHITECTURE
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) USED_PHYSICAL_ARCHITECTURE
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing PhysicalArchitecture that is used in the context of a ResourcePerformer.
HOSTED_SOFTWARE
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) HOSTED_SOFTWARE
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of software that is used in the context of a ResourcePerformer.
ARTIFACT_COMPONENT
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) ARTIFACT_COMPONENT
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of non human resource that is used as a component in the context of a ResourcePerformer.
NATURAL_RESOURCE_COMPONENT
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) NATURAL_RESOURCE_COMPONENT
Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of natural resource that is used as a component in the context of a ResourcePerformer.
OTHER
public static final [UAF.RoleKindEnum](UAF.RoleKindEnum.html) OTHER
Indicates that the ResourceRole associated with the ResourceRoleKind is another kind of RoleKind that is not on the enumerated list.
 ============ METHOD DETAIL ========== 
Method Details
values
public static [UAF.RoleKindEnum](UAF.RoleKindEnum.html)[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.
Returns:
an array containing the constants of this enum class, in the order they are declared
valueOf
public static [UAF.RoleKindEnum](UAF.RoleKindEnum.html) valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
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
@CheckForNullpublic static [UAF.RoleKindEnum](UAF.RoleKindEnum.html) from(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
toEnum
@CheckForNullpublic static [UAF.RoleKindEnum](UAF.RoleKindEnum.html) toEnum([EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) literal)
toEnumerationLiteral
@CheckForNullpublic static [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) toEnumerationLiteral([UAF](UAF.html) profile,
 [UAF.RoleKindEnum](UAF.RoleKindEnum.html) anEnum)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uaf</a></div>
<h1 class="title" title="Enum Class UAF.RoleKindEnum">Enum Class UAF.RoleKindEnum</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.uaf.UAF.RoleKindEnum</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">UAF.RoleKindEnum</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a>&gt;</span></div>
<div class="block">Enumeration of the possible kinds of roles that a ResourceRole may play in the context of a ResourcePerformer.</div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="#ARTIFACT_COMPONENT">ARTIFACT_COMPONENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of non human resource that is used as a component in the context of a ResourcePerformer.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#COMPONENT">COMPONENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Software that is used in the context of a ResourcePerformer.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#EQUIPMENT">EQUIPMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of man made resource that is used to accomplish a task or function in the context of a ResourcePerformer.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#HOSTED_SOFTWARE">HOSTED_SOFTWARE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of software that is used in the context of a ResourcePerformer.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#HUMAN_RESOURCE">HUMAN_RESOURCE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of human resource that is used in the context of a ResourcePerformer.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#NATURAL_RESOURCE_COMPONENT">NATURAL_RESOURCE_COMPONENT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of natural resource that is used as a component in the context of a ResourcePerformer.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#OTHER">OTHER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is another kind of RoleKind that is not on the enumerated list.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#PART">PART</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that is used as a part of another ResourcePerformer.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#PLATFORM">PLATFORM</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that represents  a platform (e.g.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#POST_ROLE">POST_ROLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Post that is used in the context of a ResourcePerformer.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#RESPONSIBILITY_ROLE">RESPONSIBILITY_ROLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Responsibility associated with a role that is used in the context of a ResourcePerformer.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SUB_ORGANIZATION">SUB_ORGANIZATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of  Organization that is typically the parent of another - e.g.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SUB_SYSTEM_PART">SUB_SYSTEM_PART</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of  subsystem (represented as a ResourcePerformers) is is part of another ResourcePerformer.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SYSTEM">SYSTEM</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of assembly of ResourcePerformers that is used in the context of another ResourcePerformer.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#USED_CONFIGURATION">USED_CONFIGURATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing CapabilityConfiguration that is used in the context of a ResourcePerformer.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#USED_PHYSICAL_ARCHITECTURE">USED_PHYSICAL_ARCHITECTURE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing PhysicalArchitecture that is used in the context of a ResourcePerformer.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#from(java.lang.Object)">from</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">toEnum</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toEnumerationLiteral(com.nomagic.magicdraw.uaf.UAF,com.nomagic.magicdraw.uaf.UAF.RoleKindEnum)">toEnumerationLiteral</a><wbr/>(<a href="UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a> profile,
 <a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a> anEnum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a>[]</code></div>
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
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">PART</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that is used as a part of another ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="COMPONENT">
<h3>COMPONENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">COMPONENT</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Software that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="USED_CONFIGURATION">
<h3>USED_CONFIGURATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">USED_CONFIGURATION</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing CapabilityConfiguration that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="HUMAN_RESOURCE">
<h3>HUMAN_RESOURCE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">HUMAN_RESOURCE</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of human resource that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="PLATFORM">
<h3>PLATFORM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">PLATFORM</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that represents  a platform (e.g. vessel, aircraft, etc.) that is used in the context of a SystemsResource.</div>
</section>
</li>
<li>
<section class="detail" id="SYSTEM">
<h3>SYSTEM</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">SYSTEM</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of assembly of ResourcePerformers that is used in the context of another ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="SUB_ORGANIZATION">
<h3>SUB_ORGANIZATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">SUB_ORGANIZATION</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of  Organization that is typically the parent of another - e.g. a squadron may be part of a batallion, that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="POST_ROLE">
<h3>POST_ROLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">POST_ROLE</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Post that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="RESPONSIBILITY_ROLE">
<h3>RESPONSIBILITY_ROLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">RESPONSIBILITY_ROLE</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Responsibility associated with a role that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="EQUIPMENT">
<h3>EQUIPMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">EQUIPMENT</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of man made resource that is used to accomplish a task or function in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="SUB_SYSTEM_PART">
<h3>SUB_SYSTEM_PART</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">SUB_SYSTEM_PART</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of  subsystem (represented as a ResourcePerformers) is is part of another ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="USED_PHYSICAL_ARCHITECTURE">
<h3>USED_PHYSICAL_ARCHITECTURE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">USED_PHYSICAL_ARCHITECTURE</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing PhysicalArchitecture that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="HOSTED_SOFTWARE">
<h3>HOSTED_SOFTWARE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">HOSTED_SOFTWARE</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of software that is used in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="ARTIFACT_COMPONENT">
<h3>ARTIFACT_COMPONENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">ARTIFACT_COMPONENT</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of non human resource that is used as a component in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="NATURAL_RESOURCE_COMPONENT">
<h3>NATURAL_RESOURCE_COMPONENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">NATURAL_RESOURCE_COMPONENT</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of natural resource that is used as a component in the context of a ResourcePerformer.</div>
</section>
</li>
<li>
<section class="detail" id="OTHER">
<h3>OTHER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">OTHER</span></div>
<div class="block">Indicates that the ResourceRole associated with the ResourceRoleKind is another kind of RoleKind that is not on the enumerated list.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">from</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnum(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>toEnum</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a></span> <span class="element-name">toEnum</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> literal)</span></div>
</section>
</li>
<li>
<section class="detail" id="toEnumerationLiteral(com.nomagic.magicdraw.uaf.UAF,com.nomagic.magicdraw.uaf.UAF.RoleKindEnum)">
<h3>toEnumerationLiteral</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">toEnumerationLiteral</span><wbr/><span class="parameters">(<a href="UAF.html" title="class in com.nomagic.magicdraw.uaf">UAF</a> profile,
 <a href="UAF.RoleKindEnum.html" title="enum class in com.nomagic.magicdraw.uaf">UAF.RoleKindEnum</a> anEnum)</span></div>
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
