# JAVA OPENAPI: UMLCopier (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml2/util/UMLCopier.html
- source_path: `com/nomagic/magicdraw/uml2/util/UMLCopier.html`
- source_sha256: `e1ed62ced9329a9aee2a5040be760554d34f30ddc99a1816233ba92c4c606983`
- captured_utc: `2026-07-14T16:56:00.476515+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class UMLCopier

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html)<K,V>
[java.util.HashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html)<K,V>
[java.util.LinkedHashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html)<org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject>
org.eclipse.emf.ecore.util.EcoreUtil.Copier
com.nomagic.magicdraw.uml2.util.UMLCopier

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject>`

public classUMLCopier
extends org.eclipse.emf.ecore.util.EcoreUtil.Copier

Utility class that should be used to copy UML model objects.

Version:
1.0
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.UMLCopier)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`protected static class`
`[UMLCopier.IndexTracker](UMLCopier.IndexTracker.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class org.eclipse.emf.ecore.util.EcoreUtil.Copier
`resolveProxies, useOriginalReferences`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[UMLCopier](#%3Cinit%3E())()`
Creates an instance.
`[UMLCopier](#%3Cinit%3E(boolean))(boolean resolveProxies)`
Creates an instance that resolves proxies or not as specified.
`[UMLCopier](#%3Cinit%3E(boolean,boolean))(boolean resolveProxies,
 boolean useOriginalReferences)`
Creates an instance that resolves proxies or not and uses non-copied references or not as specified.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[addToTargetWhenBidirectional](#addToTargetWhenBidirectional(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.util.InternalEList,org.eclipse.emf.ecore.EReference,int,org.eclipse.emf.ecore.EObject,com.nomagic.magicdraw.uml2.util.UMLCopier.IndexTracker))(org.eclipse.emf.ecore.EObject copyEObject,
 org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> targetList,
 org.eclipse.emf.ecore.EReference eOpposite,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject,
 [UMLCopier.IndexTracker](UMLCopier.IndexTracker.html) indexTracker)`

`org.eclipse.emf.ecore.EObject`
`[copy](#copy(org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EObject eObject)`
Returns a copy of the given eObject.
`protected void`
`[copyContainment](#copyContainment(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)`
Called to handle the copying of a containment feature;
 this adds a list of copies or sets a single copy as appropriate for the multiplicity.
`protected void`
`[copyReference](#copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject))(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)`
Called to handle the copying of a cross reference;
 this adds values or sets a single value as appropriate for the multiplicity
 while omitting any bidirectional reference that isn't in the copy map.
`void`
`[copyReferences](#copyReferences())()`
Hooks up cross references; it delegates to [`copyReference`](#copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)).
`protected [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<org.eclipse.emf.ecore.EObject>`
`[getSourceIterator](#getSourceIterator(org.eclipse.emf.ecore.util.InternalEList))(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> source)`
Methods inherited from class org.eclipse.emf.ecore.util.EcoreUtil.Copier
`copyAll, copyAttribute, copyAttributeValue, copyFeatureMap, copyProxyURI, createCopy, getTarget, getTarget, getTarget, getTarget`
Methods inherited from class java.util.[LinkedHashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html)
`[clear](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#clear()), [containsValue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#containsValue(java.lang.Object)), [entrySet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#entrySet()), [forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#forEach(java.util.function.BiConsumer)), [get](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#get(java.lang.Object)), [getOrDefault](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#getOrDefault(java.lang.Object,V)), [keySet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#keySet()), [removeEldestEntry](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#removeEldestEntry(java.util.Map.Entry)), [replaceAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#replaceAll(java.util.function.BiFunction)), [values](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#values())`
Methods inherited from class java.util.[HashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#clone()), [compute](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#compute(K,java.util.function.BiFunction)), [computeIfAbsent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#computeIfAbsent(K,java.util.function.Function)), [computeIfPresent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#computeIfPresent(K,java.util.function.BiFunction)), [containsKey](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#containsKey(java.lang.Object)), [isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#isEmpty()), [merge](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#merge(K,V,java.util.function.BiFunction)), [put](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#put(K,V)), [putAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#putAll(java.util.Map)), [putIfAbsent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#putIfAbsent(K,V)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#remove(java.lang.Object)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#remove(java.lang.Object,java.lang.Object)), [replace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#replace(K,V)), [replace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#replace(K,V,V)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#size())`
Methods inherited from class java.util.[AbstractMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html#equals(java.lang.Object)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html#hashCode()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)
`[compute](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#compute(K,java.util.function.BiFunction)), [computeIfAbsent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfAbsent(K,java.util.function.Function)), [computeIfPresent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfPresent(K,java.util.function.BiFunction)), [containsKey](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#containsKey(java.lang.Object)), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#equals(java.lang.Object)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#hashCode()), [isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#isEmpty()), [merge](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#merge(K,V,java.util.function.BiFunction)), [put](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#put(K,V)), [putAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putAll(java.util.Map)), [putIfAbsent](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putIfAbsent(K,V)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object,java.lang.Object)), [replace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V)), [replace](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V,V)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#size())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
UMLCopier
public UMLCopier()
Creates an instance.
UMLCopier
public UMLCopier(boolean resolveProxies)
Creates an instance that resolves proxies or not as specified.
Parameters:
`resolveProxies` - whether proxies should be resolved while copying.
UMLCopier
public UMLCopier(boolean resolveProxies,
 boolean useOriginalReferences)
Creates an instance that resolves proxies or not and uses non-copied references or not as specified.
Parameters:
`resolveProxies` - whether proxies should be resolved while copying.
`useOriginalReferences` - whether non-copied references should be used while copying.
 ============ METHOD DETAIL ========== 
Method Details
copy
public org.eclipse.emf.ecore.EObject copy(org.eclipse.emf.ecore.EObject eObject)
Returns a copy of the given eObject.
Overrides:
`copy` in class `org.eclipse.emf.ecore.util.EcoreUtil.Copier`
Parameters:
`eObject` - the object to copy.
Returns:
the copy.
copyReferences
public void copyReferences()
Hooks up cross references; it delegates to [`copyReference`](#copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)).
Overrides:
`copyReferences` in class `org.eclipse.emf.ecore.util.EcoreUtil.Copier`
copyContainment
protected void copyContainment(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)
Called to handle the copying of a containment feature;
 this adds a list of copies or sets a single copy as appropriate for the multiplicity.
Overrides:
`copyContainment` in class `org.eclipse.emf.ecore.util.EcoreUtil.Copier`
Parameters:
`eReference` - the feature to copy.
`eObject` - the object from which to copy.
`copyEObject` - the object to copy to.
copyReference
protected void copyReference(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)
Called to handle the copying of a cross reference;
 this adds values or sets a single value as appropriate for the multiplicity
 while omitting any bidirectional reference that isn't in the copy map.
Overrides:
`copyReference` in class `org.eclipse.emf.ecore.util.EcoreUtil.Copier`
Parameters:
`eReference` - the reference to copy.
`eObject` - the object from which to copy.
`copyEObject` - the object to copy to.
getSourceIterator
protected [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<org.eclipse.emf.ecore.EObject> getSourceIterator(org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> source)
addToTargetWhenBidirectional
protected void addToTargetWhenBidirectional(org.eclipse.emf.ecore.EObject copyEObject,
 org.eclipse.emf.ecore.util.InternalEList<org.eclipse.emf.ecore.EObject> targetList,
 org.eclipse.emf.ecore.EReference eOpposite,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject,
 [UMLCopier.IndexTracker](UMLCopier.IndexTracker.html) indexTracker)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class UMLCopier">Class UMLCopier</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html" title="class or interface in java.util">java.util.AbstractMap</a>&lt;K,<wbr/>V&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html" title="class or interface in java.util">java.util.HashMap</a>&lt;K,<wbr/>V&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html" title="class or interface in java.util">java.util.LinkedHashMap</a>&lt;org.eclipse.emf.ecore.EObject,<wbr/>org.eclipse.emf.ecore.EObject&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.EcoreUtil.Copier
<div class="inheritance">com.nomagic.magicdraw.uml2.util.UMLCopier</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;org.eclipse.emf.ecore.EObject,<wbr/>org.eclipse.emf.ecore.EObject&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">UMLCopier</span>
<span class="extends-implements">extends org.eclipse.emf.ecore.util.EcoreUtil.Copier</span></div>
<div class="block">Utility class that should be used to copy UML model objects.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.UMLCopier">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="UMLCopier.IndexTracker.html" title="class in com.nomagic.magicdraw.uml2.util">UMLCopier.IndexTracker</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.ecore.util.EcoreUtil.Copier">Fields inherited from class org.eclipse.emf.ecore.util.EcoreUtil.Copier</h3>
<code>resolveProxies, useOriginalReferences</code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">UMLCopier</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean)">UMLCopier</a><wbr/>(boolean resolveProxies)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance that resolves proxies or not as specified.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,boolean)">UMLCopier</a><wbr/>(boolean resolveProxies,
 boolean useOriginalReferences)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance that resolves proxies or not and uses non-copied references or not as specified.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToTargetWhenBidirectional(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.util.InternalEList,org.eclipse.emf.ecore.EReference,int,org.eclipse.emf.ecore.EObject,com.nomagic.magicdraw.uml2.util.UMLCopier.IndexTracker)">addToTargetWhenBidirectional</a><wbr/>(org.eclipse.emf.ecore.EObject copyEObject,
 org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; targetList,
 org.eclipse.emf.ecore.EReference eOpposite,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject,
 <a href="UMLCopier.IndexTracker.html" title="class in com.nomagic.magicdraw.uml2.util">UMLCopier.IndexTracker</a> indexTracker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.ecore.EObject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(org.eclipse.emf.ecore.EObject)">copy</a><wbr/>(org.eclipse.emf.ecore.EObject eObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a copy of the given eObject.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copyContainment(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)">copyContainment</a><wbr/>(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called to handle the copying of a containment feature;
 this adds a list of copies or sets a single copy as appropriate for the multiplicity.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)">copyReference</a><wbr/>(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called to handle the copying of a cross reference;
 this adds values or sets a single value as appropriate for the multiplicity
 while omitting any bidirectional reference that isn't in the copy map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copyReferences()">copyReferences</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hooks up cross references; it delegates to <a href="#copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)"><code>copyReference</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;org.eclipse.emf.ecore.EObject&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceIterator(org.eclipse.emf.ecore.util.InternalEList)">getSourceIterator</a><wbr/>(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.EcoreUtil.Copier">Methods inherited from class org.eclipse.emf.ecore.util.EcoreUtil.Copier</h3>
<code>copyAll, copyAttribute, copyAttributeValue, copyFeatureMap, copyProxyURI, createCopy, getTarget, getTarget, getTarget, getTarget</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.LinkedHashMap">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html" title="class or interface in java.util">LinkedHashMap</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#containsValue(java.lang.Object)" title="class or interface in java.util">containsValue</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#entrySet()" title="class or interface in java.util">entrySet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#forEach(java.util.function.BiConsumer)" title="class or interface in java.util">forEach</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#get(java.lang.Object)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#getOrDefault(java.lang.Object,V)" title="class or interface in java.util">getOrDefault</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#keySet()" title="class or interface in java.util">keySet</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#removeEldestEntry(java.util.Map.Entry)" title="class or interface in java.util">removeEldestEntry</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#replaceAll(java.util.function.BiFunction)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashMap.html#values()" title="class or interface in java.util">values</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.HashMap">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html" title="class or interface in java.util">HashMap</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#clone()" title="class or interface in java.util">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#compute(K,java.util.function.BiFunction)" title="class or interface in java.util">compute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#computeIfAbsent(K,java.util.function.Function)" title="class or interface in java.util">computeIfAbsent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#computeIfPresent(K,java.util.function.BiFunction)" title="class or interface in java.util">computeIfPresent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#containsKey(java.lang.Object)" title="class or interface in java.util">containsKey</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#merge(K,V,java.util.function.BiFunction)" title="class or interface in java.util">merge</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#put(K,V)" title="class or interface in java.util">put</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#putAll(java.util.Map)" title="class or interface in java.util">putAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#putIfAbsent(K,V)" title="class or interface in java.util">putIfAbsent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#remove(java.lang.Object,java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#replace(K,V)" title="class or interface in java.util">replace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#replace(K,V,V)" title="class or interface in java.util">replace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html#size()" title="class or interface in java.util">size</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractMap">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html" title="class or interface in java.util">AbstractMap</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractMap.html#toString()" title="class or interface in java.util">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Map">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#compute(K,java.util.function.BiFunction)" title="class or interface in java.util">compute</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfAbsent(K,java.util.function.Function)" title="class or interface in java.util">computeIfAbsent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#computeIfPresent(K,java.util.function.BiFunction)" title="class or interface in java.util">computeIfPresent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#containsKey(java.lang.Object)" title="class or interface in java.util">containsKey</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#merge(K,V,java.util.function.BiFunction)" title="class or interface in java.util">merge</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#put(K,V)" title="class or interface in java.util">put</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putAll(java.util.Map)" title="class or interface in java.util">putAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#putIfAbsent(K,V)" title="class or interface in java.util">putIfAbsent</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#remove(java.lang.Object,java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V)" title="class or interface in java.util">replace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#replace(K,V,V)" title="class or interface in java.util">replace</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#size()" title="class or interface in java.util">size</a></code></div>
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
<h3>UMLCopier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UMLCopier</span>()</div>
<div class="block">Creates an instance.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>UMLCopier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UMLCopier</span><wbr/><span class="parameters">(boolean resolveProxies)</span></div>
<div class="block">Creates an instance that resolves proxies or not as specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resolveProxies</code> - whether proxies should be resolved while copying.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean,boolean)">
<h3>UMLCopier</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">UMLCopier</span><wbr/><span class="parameters">(boolean resolveProxies,
 boolean useOriginalReferences)</span></div>
<div class="block">Creates an instance that resolves proxies or not and uses non-copied references or not as specified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resolveProxies</code> - whether proxies should be resolved while copying.</dd>
<dd><code>useOriginalReferences</code> - whether non-copied references should be used while copying.</dd>
</dl>
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
<section class="detail" id="copy(org.eclipse.emf.ecore.EObject)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.ecore.EObject</span> <span class="element-name">copy</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject eObject)</span></div>
<div class="block">Returns a copy of the given eObject.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>copy</code> in class <code>org.eclipse.emf.ecore.util.EcoreUtil.Copier</code></dd>
<dt>Parameters:</dt>
<dd><code>eObject</code> - the object to copy.</dd>
<dt>Returns:</dt>
<dd>the copy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyReferences()">
<h3>copyReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">copyReferences</span>()</div>
<div class="block">Hooks up cross references; it delegates to <a href="#copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)"><code>copyReference</code></a>.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>copyReferences</code> in class <code>org.eclipse.emf.ecore.util.EcoreUtil.Copier</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyContainment(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)">
<h3>copyContainment</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">copyContainment</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)</span></div>
<div class="block">Called to handle the copying of a containment feature;
 this adds a list of copies or sets a single copy as appropriate for the multiplicity.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>copyContainment</code> in class <code>org.eclipse.emf.ecore.util.EcoreUtil.Copier</code></dd>
<dt>Parameters:</dt>
<dd><code>eReference</code> - the feature to copy.</dd>
<dd><code>eObject</code> - the object from which to copy.</dd>
<dd><code>copyEObject</code> - the object to copy to.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyReference(org.eclipse.emf.ecore.EReference,org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.EObject)">
<h3>copyReference</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">copyReference</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EReference eReference,
 org.eclipse.emf.ecore.EObject eObject,
 org.eclipse.emf.ecore.EObject copyEObject)</span></div>
<div class="block">Called to handle the copying of a cross reference;
 this adds values or sets a single value as appropriate for the multiplicity
 while omitting any bidirectional reference that isn't in the copy map.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>copyReference</code> in class <code>org.eclipse.emf.ecore.util.EcoreUtil.Copier</code></dd>
<dt>Parameters:</dt>
<dd><code>eReference</code> - the reference to copy.</dd>
<dd><code>eObject</code> - the object from which to copy.</dd>
<dd><code>copyEObject</code> - the object to copy to.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceIterator(org.eclipse.emf.ecore.util.InternalEList)">
<h3>getSourceIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;org.eclipse.emf.ecore.EObject&gt;</span> <span class="element-name">getSourceIterator</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; source)</span></div>
</section>
</li>
<li>
<section class="detail" id="addToTargetWhenBidirectional(org.eclipse.emf.ecore.EObject,org.eclipse.emf.ecore.util.InternalEList,org.eclipse.emf.ecore.EReference,int,org.eclipse.emf.ecore.EObject,com.nomagic.magicdraw.uml2.util.UMLCopier.IndexTracker)">
<h3>addToTargetWhenBidirectional</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addToTargetWhenBidirectional</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EObject copyEObject,
 org.eclipse.emf.ecore.util.InternalEList&lt;org.eclipse.emf.ecore.EObject&gt; targetList,
 org.eclipse.emf.ecore.EReference eOpposite,
 int index,
 org.eclipse.emf.ecore.EObject copyReferencedEObject,
 <a href="UMLCopier.IndexTracker.html" title="class in com.nomagic.magicdraw.uml2.util">UMLCopier.IndexTracker</a> indexTracker)</span></div>
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
