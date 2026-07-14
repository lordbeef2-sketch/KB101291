# JAVA OPENAPI: Elements (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Elements.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Elements.html`
- source_sha256: `e5e93461c8775a64e79b23df708d6d3cc8fabf08052aba65d1593497f1348be4`
- captured_utc: `2026-07-14T16:44:47.380835+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Elements

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Elements

@OpenApiAllpublic classElements
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Element`](kerml/Element.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Elements](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[applyRecursively](#applyRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Function))([Element](kerml/Element.html) element,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Element](kerml/Element.html),[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)> function)`
Recursively applies the function to the element and its owned elements
 until the function returns false.
`static void`
`[consumeRecursively](#consumeRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Consumer))([Element](kerml/Element.html) element,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Element](kerml/Element.html)> consumer)`
Recursively applies the consumer to the element and all its owned elements.
`static void`
`[consumeRecursively](#consumeRecursively(java.util.Collection,java.util.function.Consumer))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Element](kerml/Element.html)> consumer)`
Recursively applies the consumer to each element in the collection.
`static void`
`[dispose](#dispose(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements)`
Disposes the given elements using `ElementDisposer`, ensuring
 that disposal is performed on a stable array snapshot.
`static [Element](kerml/Element.html)`
`[findOwner](#findOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate))([Element](kerml/Element.html) element,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](kerml/Element.html)> condition)`
Finds the first owner in the containment chain that satisfies the condition.
`static [Element](kerml/Element.html)`
`[getContainer](#getContainer(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Returns the EMF container of the element if it is also a KerML [`Element`](kerml/Element.html).
`static void`
`[selfDispose](#selfDispose(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements)`
Calls [`ModelElement.selfDispose()`](../../foundation/model/ModelElement.html#selfDispose()) on each element in the collection.
`static void`
`[selfDisposeOwningRelationship](#selfDisposeOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Disposes the owning relationship of the given element, if present.
`static void`
`[selfDisposeUnsettingOwningRelationship](#selfDisposeUnsettingOwningRelationship(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements)`
Unsets the owning relationship of each element and then disposes it.
`static void`
`[setOwningElement](#setOwningElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element,
 [Element](kerml/Element.html) owning)`
Sets the owning element of the given element.
`static <M extends [OwningMembership](kerml/OwningMembership.html)> 
M`
`[setOwningMembership](#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,org.eclipse.emf.ecore.EClass))([Element](kerml/Element.html) member,
 [Namespace](kerml/Namespace.html) namespace,
 org.eclipse.emf.ecore.EClass preferredMembershipEClass)`
Establish preferred [`OwningMembership`](kerml/OwningMembership.html) between a member and given namespace.
`static <M extends [OwningMembership](kerml/OwningMembership.html)> 
M`
`[setOwningMembership](#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,org.eclipse.emf.ecore.EClass,boolean))([Element](kerml/Element.html) member,
 [Namespace](kerml/Namespace.html) namespace,
 org.eclipse.emf.ecore.EClass membershipEClass,
 boolean preferredMembershipClass)`
Establish preferred [`OwningMembership`](kerml/OwningMembership.html) between a member and given namespace.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Elements
public Elements()
 ============ METHOD DETAIL ========== 
Method Details
dispose
public static void dispose([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements)
Disposes the given elements using `ElementDisposer`, ensuring
 that disposal is performed on a stable array snapshot.
Parameters:
`elements` - elements to dispose
selfDispose
public static void selfDispose([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements)
Calls [`ModelElement.selfDispose()`](../../foundation/model/ModelElement.html#selfDispose()) on each element in the collection.
Parameters:
`elements` - elements to dispose
selfDisposeUnsettingOwningRelationship
public static void selfDisposeUnsettingOwningRelationship([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements)
Unsets the owning relationship of each element and then disposes it.
Parameters:
`elements` - elements to dispose
selfDisposeOwningRelationship
public static void selfDisposeOwningRelationship([Element](kerml/Element.html) element)
Disposes the owning relationship of the given element, if present.
Parameters:
`element` - element whose owning relationship should be disposed
getContainer
@CheckForNullpublic static [Element](kerml/Element.html) getContainer([Element](kerml/Element.html) element)
Returns the EMF container of the element if it is also a KerML [`Element`](kerml/Element.html).
Parameters:
`element` - element
Returns:
container element, or null
setOwningMembership
@CheckForNullpublic static <M extends [OwningMembership](kerml/OwningMembership.html)> M setOwningMembership([Element](kerml/Element.html) member,
 @CheckForNull
 [Namespace](kerml/Namespace.html) namespace,
 @CheckForNull
 org.eclipse.emf.ecore.EClass preferredMembershipEClass)
Establish preferred [`OwningMembership`](kerml/OwningMembership.html) between a member and given namespace.
 Current membership will be used(if valid) and if preferred is unspecified.
 Ignores preferred membership kind if it is more general than the current one.
 Default membership kind will be used if current/preferred is invalid or unspecified.
Parameters:
`member` - member
`namespace` - namespace
`preferredMembershipEClass` - kind of preferred OwningMembership
setOwningMembership
@CheckForNullpublic static <M extends [OwningMembership](kerml/OwningMembership.html)> M setOwningMembership([Element](kerml/Element.html) member,
 @CheckForNull
 [Namespace](kerml/Namespace.html) namespace,
 @CheckForNull
 org.eclipse.emf.ecore.EClass membershipEClass,
 boolean preferredMembershipClass)
Establish preferred [`OwningMembership`](kerml/OwningMembership.html) between a member and given namespace.
 Current membership will be used(if valid) and if preferred is unspecified.
 Ignores preferred membership kind if it is more general than the current one.
 Default membership kind will be used if current/preferred is invalid or unspecified.
Parameters:
`member` - member
`namespace` - namespace
`membershipEClass` - OwningMembership kind
`preferredMembershipClass` - true if membershipEClass should be treated as preferred, false if as exact
setOwningElement
public static void setOwningElement([Element](kerml/Element.html) element,
 @CheckForNull
 [Element](kerml/Element.html) owning)
Sets the owning element of the given element. Depending on the type of
 the owning element, this may create an annotation, set an owning
 relationship, or assign a standard owner.
Parameters:
`element` - element to update
`owning` - new owning element, or null
consumeRecursively
public static void consumeRecursively([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](kerml/Element.html)> elements,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Element](kerml/Element.html)> consumer)
Recursively applies the consumer to each element in the collection.
Parameters:
`elements` - elements to traverse
`consumer` - consumer applied to each element
consumeRecursively
public static void consumeRecursively([Element](kerml/Element.html) element,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<[Element](kerml/Element.html)> consumer)
Recursively applies the consumer to the element and all its owned elements.
Parameters:
`element` - root element
`consumer` - consumer applied to each element
applyRecursively
public static void applyRecursively([Element](kerml/Element.html) element,
 [Function](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html)<[Element](kerml/Element.html),[Boolean](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html)> function)
Recursively applies the function to the element and its owned elements
 until the function returns false.
Parameters:
`element` - root element
`function` - function returning true to continue recursion
findOwner
@CheckForNullpublic static [Element](kerml/Element.html) findOwner([Element](kerml/Element.html) element,
 [Predicate](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html)<[Element](kerml/Element.html)> condition)
Finds the first owner in the containment chain that satisfies the condition.
Parameters:
`element` - starting element
`condition` - predicate applied to owners
Returns:
matching owner, or null

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Elements">Class Elements</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Elements</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Elements</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Elements</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#applyRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Function)">applyRecursively</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; function)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Recursively applies the function to the element and its owned elements
 until the function returns false.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#consumeRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Consumer)">consumeRecursively</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; consumer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Recursively applies the consumer to the element and all its owned elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#consumeRecursively(java.util.Collection,java.util.function.Consumer)">consumeRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Recursively applies the consumer to each element in the collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose(java.util.Collection)">dispose</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disposes the given elements using <code>ElementDisposer</code>, ensuring
 that disposal is performed on a stable array snapshot.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate)">findOwner</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; condition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Finds the first owner in the containment chain that satisfies the condition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getContainer(com.dassault_systemes.modeler.kerml.model.kerml.Element)">getContainer</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the EMF container of the element if it is also a KerML <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#selfDispose(java.util.Collection)">selfDispose</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calls <a href="../../foundation/model/ModelElement.html#selfDispose()"><code>ModelElement.selfDispose()</code></a> on each element in the collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#selfDisposeOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)">selfDisposeOwningRelationship</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disposes the owning relationship of the given element, if present.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#selfDisposeUnsettingOwningRelationship(java.util.Collection)">selfDisposeUnsettingOwningRelationship</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Unsets the owning relationship of each element and then disposes it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwningElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element)">setOwningElement</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> owning)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the owning element of the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;M extends <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a>&gt;<br/>M</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,org.eclipse.emf.ecore.EClass)">setOwningMembership</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> member,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace,
 org.eclipse.emf.ecore.EClass preferredMembershipEClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Establish preferred <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OwningMembership</code></a> between a member and given namespace.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;M extends <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a>&gt;<br/>M</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,org.eclipse.emf.ecore.EClass,boolean)">setOwningMembership</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> member,
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace,
 org.eclipse.emf.ecore.EClass membershipEClass,
 boolean preferredMembershipClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Establish preferred <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OwningMembership</code></a> between a member and given namespace.</div>
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
<h3>Elements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Elements</span>()</div>
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
<section class="detail" id="dispose(java.util.Collection)">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">dispose</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements)</span></div>
<div class="block">Disposes the given elements using <code>ElementDisposer</code>, ensuring
 that disposal is performed on a stable array snapshot.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to dispose</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selfDispose(java.util.Collection)">
<h3>selfDispose</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">selfDispose</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements)</span></div>
<div class="block">Calls <a href="../../foundation/model/ModelElement.html#selfDispose()"><code>ModelElement.selfDispose()</code></a> on each element in the collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to dispose</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selfDisposeUnsettingOwningRelationship(java.util.Collection)">
<h3>selfDisposeUnsettingOwningRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">selfDisposeUnsettingOwningRelationship</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements)</span></div>
<div class="block">Unsets the owning relationship of each element and then disposes it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to dispose</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="selfDisposeOwningRelationship(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>selfDisposeOwningRelationship</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">selfDisposeOwningRelationship</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Disposes the owning relationship of the given element, if present.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element whose owning relationship should be disposed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContainer(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>getContainer</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">getContainer</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns the EMF container of the element if it is also a KerML <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Element</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>container element, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,org.eclipse.emf.ecore.EClass)">
<h3>setOwningMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;M extends <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a>&gt;</span> <span class="return-type">M</span> <span class="element-name">setOwningMembership</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> member,
 @CheckForNull
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace,
 @CheckForNull
 org.eclipse.emf.ecore.EClass preferredMembershipEClass)</span></div>
<div class="block">Establish preferred <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OwningMembership</code></a> between a member and given namespace.
 Current membership will be used(if valid) and if preferred is unspecified.
 Ignores preferred membership kind if it is more general than the current one.
 Default membership kind will be used if current/preferred is invalid or unspecified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>member</code> - member</dd>
<dd><code>namespace</code> - namespace</dd>
<dd><code>preferredMembershipEClass</code> - kind of preferred OwningMembership</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningMembership(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Namespace,org.eclipse.emf.ecore.EClass,boolean)">
<h3>setOwningMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;M extends <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">OwningMembership</a>&gt;</span> <span class="return-type">M</span> <span class="element-name">setOwningMembership</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> member,
 @CheckForNull
 <a href="kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> namespace,
 @CheckForNull
 org.eclipse.emf.ecore.EClass membershipEClass,
 boolean preferredMembershipClass)</span></div>
<div class="block">Establish preferred <a href="kerml/OwningMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>OwningMembership</code></a> between a member and given namespace.
 Current membership will be used(if valid) and if preferred is unspecified.
 Ignores preferred membership kind if it is more general than the current one.
 Default membership kind will be used if current/preferred is invalid or unspecified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>member</code> - member</dd>
<dd><code>namespace</code> - namespace</dd>
<dd><code>membershipEClass</code> - OwningMembership kind</dd>
<dd><code>preferredMembershipClass</code> - true if membershipEClass should be treated as preferred, false if as exact</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOwningElement(com.dassault_systemes.modeler.kerml.model.kerml.Element,com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>setOwningElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setOwningElement</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 @CheckForNull
 <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> owning)</span></div>
<div class="block">Sets the owning element of the given element. Depending on the type of
 the owning element, this may create an annotation, set an owning
 relationship, or assign a standard owner.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to update</dd>
<dd><code>owning</code> - new owning element, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="consumeRecursively(java.util.Collection,java.util.function.Consumer)">
<h3>consumeRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">consumeRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; consumer)</span></div>
<div class="block">Recursively applies the consumer to each element in the collection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to traverse</dd>
<dd><code>consumer</code> - consumer applied to each element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="consumeRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Consumer)">
<h3>consumeRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">consumeRecursively</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; consumer)</span></div>
<div class="block">Recursively applies the consumer to the element and all its owned elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - root element</dd>
<dd><code>consumer</code> - consumer applied to each element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyRecursively(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Function)">
<h3>applyRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">applyRecursively</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; function)</span></div>
<div class="block">Recursively applies the function to the element and its owned elements
 until the function returns false.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - root element</dd>
<dd><code>function</code> - function returning true to continue recursion</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findOwner(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.function.Predicate)">
<h3>findOwner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a></span> <span class="element-name">findOwner</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Predicate.html" title="class or interface in java.util.function">Predicate</a>&lt;<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; condition)</span></div>
<div class="block">Finds the first owner in the containment chain that satisfies the condition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - starting element</dd>
<dd><code>condition</code> - predicate applied to owners</dd>
<dt>Returns:</dt>
<dd>matching owner, or null</dd>
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
