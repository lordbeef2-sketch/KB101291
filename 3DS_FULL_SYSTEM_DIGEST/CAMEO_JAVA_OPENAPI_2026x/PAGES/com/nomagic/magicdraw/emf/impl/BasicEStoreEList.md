# JAVA OPENAPI: BasicEStoreEList (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/emf/impl/BasicEStoreEList.html
- source_path: `com/nomagic/magicdraw/emf/impl/BasicEStoreEList.html`
- source_sha256: `84a9bb1d0baa05935431fd3ff36382651057ca368925b6818ebe2995c4941579`
- captured_utc: `2026-07-14T16:57:56.046514+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emf.impl](package-summary.html)

## Class BasicEStoreEList<E>

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<E>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<E>
org.eclipse.emf.common.util.AbstractEList<E>
org.eclipse.emf.common.util.DelegatingEList<E>
org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<E>
org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl<E>
org.eclipse.emf.ecore.util.DelegatingEcoreEList<E>
org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic<E>
org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic<E>
com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<E>
com.nomagic.magicdraw.emf.impl.BasicEStoreEList<E>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<E>`, `[SequencedCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html)<E>`, `org.eclipse.emf.common.notify.NotifyingList<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

Direct Known Subclasses:
`[ModelEStoreEList](../../uml2/util/ModelEStoreEList.html)`

public classBasicEStoreEList<E>
extends com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<E>

A list that delegates to a store.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.emf.impl.BasicEStoreEList)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic
`eStructuralFeature`
Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic
`HAS_INSTANCE_CLASS, HAS_MANY_INVERSE, HAS_NAVIGABLE_INVERSE, HAS_PROXIES, IS_CONTAINER, IS_CONTAINMENT, IS_ENUM, IS_EOBJECT, IS_PRIMITIVE, IS_SET, IS_UNIQUE, IS_UNSETTABLE, kind`
Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList
`owner`
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BasicEStoreEList](#%3Cinit%3E(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[afterChange](#afterChange())()`
The method will be invoked after specified property.
`protected void`
`[beforeChange](#beforeChange())()`
The method will be invoked before specified property change.
`protected [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)`
`[createOperationTimeoutException](#createOperationTimeoutException())()`

`protected void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue,
 int index)`
Fire property change event.
`protected com.dassault_systemes.modeler.foundation.util.ModelLockProvider`
`[getLockProvider](#getLockProvider())()`
Methods inherited from class com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList
`delegateAdd, delegateAdd, delegateBasicList, delegateClear, delegateContains, delegateContainsAll, delegateEquals, delegateGet, delegateHashCode, delegateIndexOf, delegateIsEmpty, delegateIterator, delegateLastIndexOf, delegateList, delegateListIterator, delegateMove, delegateRemove, delegateSet, delegateSize, delegateToArray, delegateToArray, delegateToString, eStore, execute, getEStructuralFeature, getPropertyEventName, makeLastInCollection, snapshot`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic
`canContainNull, didChange, hasInstanceClass, hasInverse, hasManyInverse, hasNavigableInverse, hasProxies, isContainer, isContainment, isEObject, isSet, isUnique, isUnsettable, kind, unset, useEquals`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList
`contains, containsAll, createNotification, createNotification, dispatchNotification, get, getEObject, getFeature, getFeatureID, getFeatureType, getInverseEReference, getInverseFeatureClass, getInverseFeatureID, getNotifier, indexOf, inverseAdd, inverseRemove, isInstance, isNotificationRequired, lastIndexOf, resolve, resolve, resolveProxy, set, toArray, toArray, validate`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl
`basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray`
Methods inherited from class org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl
`addAllUnique, addAllUnique, addAllUnique, addAllUnique, addUnique, addUnique, basicAdd, basicRemove, basicSet, clear, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doMove, doRemove, doRemoveAll, doSetUnique, getFeatureID, hasShadow, move, remove, removeAll, setUnique, shadowAdd, shadowRemove, shadowSet`
Methods inherited from class org.eclipse.emf.common.util.DelegatingEList
`doClear, equals, get, hashCode, isEmpty, primitiveGet, remove, retainAll, size, toString`
Methods inherited from class org.eclipse.emf.common.util.AbstractEList
`add, add, addAll, addAll, didAdd, didClear, didMove, didRemove, didSet, equalObjects, getDuplicates, getNonDuplicates, iterator, listIterator, listIterator, move, set`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[removeRange](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface org.eclipse.emf.common.util.EList
`move, move`
Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList
`addAllUnique, addAllUnique, addUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicRemove, basicToArray, basicToArray, setUnique`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(int,E)), [add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E)), [addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)), [addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)), [addFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)), [addLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)), [clear](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#clear()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [get](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#get(int)), [getFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()), [getLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#isEmpty()), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator(int)), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(int)), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [removeAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)), [removeFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()), [removeLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()), [replaceAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()), [set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#set(int,E)), [size](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#size()), [sort](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BasicEStoreEList
public BasicEStoreEList(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)
 ============ METHOD DETAIL ========== 
Method Details
beforeChange
protected void beforeChange()
Description copied from class: `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList`
The method will be invoked before specified property change.
Specified by:
`beforeChange` in class `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<[E](BasicEStoreEList.html)>`
afterChange
protected void afterChange()
Description copied from class: `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList`
The method will be invoked after specified property.
Specified by:
`afterChange` in class `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<[E](BasicEStoreEList.html)>`
firePropertyChange
protected void firePropertyChange([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) oldValue,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) newValue,
 int index)
Description copied from class: `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList`
Fire property change event.
Specified by:
`firePropertyChange` in class `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<[E](BasicEStoreEList.html)>`
Parameters:
`propertyName` - name of the changed property.
`oldValue` - old value of the property.
`newValue` - new value of the property.
`index` - index of the new value.
getLockProvider
@CheckForNullprotected com.dassault_systemes.modeler.foundation.util.ModelLockProvider getLockProvider()
Specified by:
`getLockProvider` in class `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<[E](BasicEStoreEList.html)>`
createOperationTimeoutException
protected [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html) createOperationTimeoutException()
Specified by:
`createOperationTimeoutException` in class `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<[E](BasicEStoreEList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emf.impl</a></div>
<h1 class="title" title="Class BasicEStoreEList">Class BasicEStoreEList&lt;E&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.AbstractEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.DelegatingEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingEcoreEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic&lt;E&gt;
<div class="inheritance">com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;E&gt;
<div class="inheritance">com.nomagic.magicdraw.emf.impl.BasicEStoreEList&lt;E&gt;</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html" title="class or interface in java.util">SequencedCollection</a>&lt;E&gt;</code>, <code>org.eclipse.emf.common.notify.NotifyingList&lt;E&gt;</code>, <code>org.eclipse.emf.common.util.EList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.EStructuralFeature.Setting</code>, <code>org.eclipse.emf.ecore.util.InternalEList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.util.InternalEList.Unsettable&lt;E&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../uml2/util/ModelEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">ModelEStoreEList</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">BasicEStoreEList&lt;E&gt;</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;E&gt;</span></div>
<div class="block">A list that delegates to a store.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.emf.impl.BasicEStoreEList">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic">Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic</h3>
<code>eStructuralFeature</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic">Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic</h3>
<code>HAS_INSTANCE_CLASS, HAS_MANY_INVERSE, HAS_NAVIGABLE_INVERSE, HAS_PROXIES, IS_CONTAINER, IS_CONTAINMENT, IS_ENUM, IS_EOBJECT, IS_PRIMITIVE, IS_SET, IS_UNIQUE, IS_UNSETTABLE, kind</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList">Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList</h3>
<code>owner</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.util.AbstractList">Fields inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount" title="class or interface in java.util">modCount</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature)">BasicEStoreEList</a><wbr/>(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterChange()">afterChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method will be invoked after specified property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeChange()">beforeChange</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method will be invoked before specified property change.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationTimeoutException()">createOperationTimeoutException</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Fire property change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.dassault_systemes.modeler.foundation.util.ModelLockProvider</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockProvider()">getLockProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList">Methods inherited from class com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList</h3>
<code>delegateAdd, delegateAdd, delegateBasicList, delegateClear, delegateContains, delegateContainsAll, delegateEquals, delegateGet, delegateHashCode, delegateIndexOf, delegateIsEmpty, delegateIterator, delegateLastIndexOf, delegateList, delegateListIterator, delegateMove, delegateRemove, delegateSet, delegateSize, delegateToArray, delegateToArray, delegateToString, eStore, execute, getEStructuralFeature, getPropertyEventName, makeLastInCollection, snapshot</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic</h3>
<code>canContainNull, didChange, hasInstanceClass, hasInverse, hasManyInverse, hasNavigableInverse, hasProxies, isContainer, isContainment, isEObject, isSet, isUnique, isUnsettable, kind, unset, useEquals</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList</h3>
<code>contains, containsAll, createNotification, createNotification, dispatchNotification, get, getEObject, getFeature, getFeatureID, getFeatureType, getInverseEReference, getInverseFeatureClass, getInverseFeatureID, getNotifier, indexOf, inverseAdd, inverseRemove, isInstance, isNotificationRequired, lastIndexOf, resolve, resolve, resolveProxy, set, toArray, toArray, validate</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl</h3>
<code>basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl">Methods inherited from class org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl</h3>
<code>addAllUnique, addAllUnique, addAllUnique, addAllUnique, addUnique, addUnique, basicAdd, basicRemove, basicSet, clear, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doMove, doRemove, doRemoveAll, doSetUnique, getFeatureID, hasShadow, move, remove, removeAll, setUnique, shadowAdd, shadowRemove, shadowSet</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.DelegatingEList">Methods inherited from class org.eclipse.emf.common.util.DelegatingEList</h3>
<code>doClear, equals, get, hashCode, isEmpty, primitiveGet, remove, retainAll, size, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEList">Methods inherited from class org.eclipse.emf.common.util.AbstractEList</h3>
<code>add, add, addAll, addAll, didAdd, didClear, didMove, didRemove, didSet, equalObjects, getDuplicates, getNonDuplicates, iterator, listIterator, listIterator, move, set</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.EList">Methods inherited from interface org.eclipse.emf.common.util.EList</h3>
<code>move, move</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.InternalEList">Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList</h3>
<code>addAllUnique, addAllUnique, addUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicRemove, basicToArray, basicToArray, setUnique</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(int,E)" title="class or interface in java.util">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)" title="class or interface in java.util">addFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)" title="class or interface in java.util">addLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()" title="class or interface in java.util">getFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()" title="class or interface in java.util">getLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(int)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()" title="class or interface in java.util">removeFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()" title="class or interface in java.util">removeLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#set(int,E)" title="class or interface in java.util">set</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#size()" title="class or interface in java.util">size</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
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
<section class="detail" id="&lt;init&gt;(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature)">
<h3>BasicEStoreEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BasicEStoreEList</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</span></div>
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
<section class="detail" id="beforeChange()">
<h3>beforeChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">beforeChange</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList</code></span></div>
<div class="block">The method will be invoked before specified property change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>beforeChange</code> in class <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;<a href="BasicEStoreEList.html" title="type parameter in BasicEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterChange()">
<h3>afterChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterChange</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList</code></span></div>
<div class="block">The method will be invoked after specified property.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>afterChange</code> in class <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;<a href="BasicEStoreEList.html" title="type parameter in BasicEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList</code></span></div>
<div class="block">Fire property change event.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>firePropertyChange</code> in class <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;<a href="BasicEStoreEList.html" title="type parameter in BasicEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>propertyName</code> - name of the changed property.</dd>
<dd><code>oldValue</code> - old value of the property.</dd>
<dd><code>newValue</code> - new value of the property.</dd>
<dd><code>index</code> - index of the new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLockProvider()">
<h3>getLockProvider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type">com.dassault_systemes.modeler.foundation.util.ModelLockProvider</span> <span class="element-name">getLockProvider</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getLockProvider</code> in class <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;<a href="BasicEStoreEList.html" title="type parameter in BasicEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationTimeoutException()">
<h3>createOperationTimeoutException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span> <span class="element-name">createOperationTimeoutException</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>createOperationTimeoutException</code> in class <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;<a href="BasicEStoreEList.html" title="type parameter in BasicEStoreEList">E</a>&gt;</code></dd>
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
