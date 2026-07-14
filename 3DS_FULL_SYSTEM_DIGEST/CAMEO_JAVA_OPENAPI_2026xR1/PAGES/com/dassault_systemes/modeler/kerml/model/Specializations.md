# JAVA OPENAPI: Specializations (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Specializations.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Specializations.html`
- source_sha256: `9c944c6d9da158b73646c9477b2205306dc51cd75f1b90ff7338a422047e52f6`
- captured_utc: `2026-07-14T16:44:48.345847+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Specializations

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Specializations

@OpenApiAllpublic classSpecializations
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Specialization`](kerml/Specialization.html) and [`Type`](kerml/Type.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Specializations](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Type](kerml/Type.html)`
`[firstSuperTypeMatching](#firstSuperTypeMatching(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Type](kerml/Type.html)> predicate)`
Returns the first supertype of the given type that matches the predicate.
`static <T extends [Type](kerml/Type.html)> 
T`
`[firstSuperTypeMatching](#firstSuperTypeMatching(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate,java.lang.Class))([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Type](kerml/Type.html)> predicate,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> typeClass)`
Returns the first supertype of the given type that matches the predicate
 and is an instance of the specified class.
`static void`
`[forEachSuperType](#forEachSuperType(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Consumer))([Type](kerml/Type.html) type,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Type](kerml/Type.html)> consumer)`
Applies the given consumer to each direct supertype of the specified type.
`static [Type](kerml/Type.html)`
`[getFirstNonImpliedGeneralType](#getFirstNonImpliedGeneralType(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns the first non‑implied general (super) type of the given type.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)>`
`[getSubTypesRecursively](#getSubTypesRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Specialization](kerml/Specialization.html)> specializationKind)`
Returns all subtypes of the given type recursively, excluding the type itself.
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)>`
`[getSubTypesRecursivelyIncludingSelf](#getSubTypesRecursivelyIncludingSelf(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Specialization](kerml/Specialization.html)> specializationKind)`
Returns all subtypes of the given type recursively, including the type itself.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)>`
`[getSuperTypes](#getSuperTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns all direct supertypes of the given type as a list.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Type](kerml/Type.html)>`
`[streamOfSubTypes](#streamOfSubTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class))([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Specialization](kerml/Specialization.html)> specializationKind)`
Returns a stream of subtypes of the given type using the specified specialization kind.
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Type](kerml/Type.html)>`
`[streamOfSuperTypes](#streamOfSuperTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns a stream of all direct supertypes of the given type.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Specializations
public Specializations()
 ============ METHOD DETAIL ========== 
Method Details
streamOfSubTypes
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Type](kerml/Type.html)> streamOfSubTypes([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Specialization](kerml/Specialization.html)> specializationKind)
Returns a stream of subtypes of the given type using the specified specialization kind.
Parameters:
`type` - the type whose subtypes are requested
`specializationKind` - the specialization class to filter by
Returns:
stream of subtypes
firstSuperTypeMatching
@CheckForNullpublic static <T extends [Type](kerml/Type.html)> T firstSuperTypeMatching([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Type](kerml/Type.html)> predicate,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> typeClass)
Returns the first supertype of the given type that matches the predicate
 and is an instance of the specified class.
Type Parameters:
`T` - supertype type
Parameters:
`type` - the type whose supertypes are inspected
`predicate` - condition the supertype must satisfy
`typeClass` - class the supertype must be an instance of
Returns:
the first matching supertype, or null
forEachSuperType
public static void forEachSuperType([Type](kerml/Type.html) type,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Type](kerml/Type.html)> consumer)
Applies the given consumer to each direct supertype of the specified type.
Parameters:
`type` - the type whose supertypes are processed
`consumer` - action applied to each supertype
firstSuperTypeMatching
@CheckForNullpublic static [Type](kerml/Type.html) firstSuperTypeMatching([Type](kerml/Type.html) type,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Type](kerml/Type.html)> predicate)
Returns the first supertype of the given type that matches the predicate.
Parameters:
`type` - the type whose supertypes are inspected
`predicate` - condition the supertype must satisfy
Returns:
the first matching supertype, or null
streamOfSuperTypes
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Type](kerml/Type.html)> streamOfSuperTypes([Type](kerml/Type.html) type)
Returns a stream of all direct supertypes of the given type.
Parameters:
`type` - the type whose supertypes are requested
Returns:
stream of supertypes
getFirstNonImpliedGeneralType
@CheckForNullpublic static [Type](kerml/Type.html) getFirstNonImpliedGeneralType([Type](kerml/Type.html) type)
Returns the first non‑implied general (super) type of the given type.
Parameters:
`type` - the type whose general type is requested
Returns:
the first non‑implied general type, or null
getSubTypesRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)> getSubTypesRecursively([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Specialization](kerml/Specialization.html)> specializationKind)
Returns all subtypes of the given type recursively, excluding the type itself.
Parameters:
`type` - the type whose subtypes are requested
`specializationKind` - the specialization class to filter by
Returns:
collection of recursive subtypes
getSubTypesRecursivelyIncludingSelf
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Type](kerml/Type.html)> getSubTypesRecursivelyIncludingSelf([Type](kerml/Type.html) type,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<? extends [Specialization](kerml/Specialization.html)> specializationKind)
Returns all subtypes of the given type recursively, including the type itself.
Parameters:
`type` - the type whose subtypes are requested
`specializationKind` - the specialization class to filter by
Returns:
collection of recursive subtypes including the type
getSuperTypes
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Type](kerml/Type.html)> getSuperTypes([Type](kerml/Type.html) type)
Returns all direct supertypes of the given type as a list.
Parameters:
`type` - the type whose supertypes are requested
Returns:
list of supertypes

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Specializations">Class Specializations</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Specializations</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Specializations</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Specialization</code></a> and <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Type</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Specializations</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#firstSuperTypeMatching(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">firstSuperTypeMatching</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; predicate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first supertype of the given type that matches the predicate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#firstSuperTypeMatching(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate,java.lang.Class)">firstSuperTypeMatching</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; predicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; typeClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first supertype of the given type that matches the predicate
 and is an instance of the specified class.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#forEachSuperType(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Consumer)">forEachSuperType</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies the given consumer to each direct supertype of the specified type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstNonImpliedGeneralType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getFirstNonImpliedGeneralType</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first non‑implied general (super) type of the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubTypesRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">getSubTypesRecursively</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt; specializationKind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all subtypes of the given type recursively, excluding the type itself.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSubTypesRecursivelyIncludingSelf(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">getSubTypesRecursivelyIncludingSelf</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt; specializationKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all subtypes of the given type recursively, including the type itself.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuperTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getSuperTypes</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all direct supertypes of the given type as a list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfSubTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">streamOfSubTypes</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt; specializationKind)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of subtypes of the given type using the specified specialization kind.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#streamOfSuperTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">streamOfSuperTypes</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of all direct supertypes of the given type.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>Specializations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Specializations</span>()</div>
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
<section class="detail" id="streamOfSubTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>streamOfSubTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">streamOfSubTypes</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt; specializationKind)</span></div>
<div class="block">Returns a stream of subtypes of the given type using the specified specialization kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose subtypes are requested</dd>
<dd><code>specializationKind</code> - the specialization class to filter by</dd>
<dt>Returns:</dt>
<dd>stream of subtypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firstSuperTypeMatching(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate,java.lang.Class)">
<h3>firstSuperTypeMatching</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">firstSuperTypeMatching</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; predicate,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; typeClass)</span></div>
<div class="block">Returns the first supertype of the given type that matches the predicate
 and is an instance of the specified class.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - supertype type</dd>
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose supertypes are inspected</dd>
<dd><code>predicate</code> - condition the supertype must satisfy</dd>
<dd><code>typeClass</code> - class the supertype must be an instance of</dd>
<dt>Returns:</dt>
<dd>the first matching supertype, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forEachSuperType(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Consumer)">
<h3>forEachSuperType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">forEachSuperType</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; consumer)</span></div>
<div class="block">Applies the given consumer to each direct supertype of the specified type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose supertypes are processed</dd>
<dd><code>consumer</code> - action applied to each supertype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firstSuperTypeMatching(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.util.function.Predicate)">
<h3>firstSuperTypeMatching</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">firstSuperTypeMatching</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt; predicate)</span></div>
<div class="block">Returns the first supertype of the given type that matches the predicate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose supertypes are inspected</dd>
<dd><code>predicate</code> - condition the supertype must satisfy</dd>
<dt>Returns:</dt>
<dd>the first matching supertype, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="streamOfSuperTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>streamOfSuperTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">streamOfSuperTypes</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns a stream of all direct supertypes of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose supertypes are requested</dd>
<dt>Returns:</dt>
<dd>stream of supertypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstNonImpliedGeneralType(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getFirstNonImpliedGeneralType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a></span> <span class="element-name">getFirstNonImpliedGeneralType</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the first non‑implied general (super) type of the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose general type is requested</dd>
<dt>Returns:</dt>
<dd>the first non‑implied general type, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubTypesRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>getSubTypesRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getSubTypesRecursively</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt; specializationKind)</span></div>
<div class="block">Returns all subtypes of the given type recursively, excluding the type itself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose subtypes are requested</dd>
<dd><code>specializationKind</code> - the specialization class to filter by</dd>
<dt>Returns:</dt>
<dd>collection of recursive subtypes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSubTypesRecursivelyIncludingSelf(com.dassault_systemes.modeler.kerml.model.kerml.Type,java.lang.Class)">
<h3>getSubTypesRecursivelyIncludingSelf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getSubTypesRecursivelyIncludingSelf</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="kerml/Specialization.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Specialization</a>&gt; specializationKind)</span></div>
<div class="block">Returns all subtypes of the given type recursively, including the type itself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose subtypes are requested</dd>
<dd><code>specializationKind</code> - the specialization class to filter by</dd>
<dt>Returns:</dt>
<dd>collection of recursive subtypes including the type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuperTypes(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getSuperTypes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a>&gt;</span> <span class="element-name">getSuperTypes</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns all direct supertypes of the given type as a list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type whose supertypes are requested</dd>
<dt>Returns:</dt>
<dd>list of supertypes</dd>
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
