# JAVA OPENAPI: SubsetSupersetEObjectEStoreWithInverseResolvingEList (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml2/util/SubsetSupersetEObjectEStoreWithInverseResolvingEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/SubsetSupersetEObjectEStoreWithInverseResolvingEList.html`
- source_sha256: `3d92ed505b7862cef054921c1944dfa9032ad8efe1930cb2820cb29b74f16b17`
- captured_utc: `2026-07-14T16:52:27.256083+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class SubsetSupersetEObjectEStoreWithInverseResolvingEList<E>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html)<E>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)<E>
org.eclipse.emf.common.util.AbstractEList<E>
org.eclipse.emf.common.util.DelegatingEList<E>
org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<E>
org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl<E>
org.eclipse.emf.ecore.util.DelegatingEcoreEList<E>
org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic<E>
org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic<E>
com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<E>
[com.nomagic.magicdraw.emf.impl.BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)<E>
[com.nomagic.magicdraw.uml2.util.ModelEStoreEList](ModelEStoreEList.html)<E>
[com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList](SubsetSupersetEObjectEStoreEList.html)<E>
[com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseEList](SubsetSupersetEObjectEStoreWithInverseEList.html)<E>
com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseResolvingEList<E>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<E>`, `org.eclipse.emf.common.notify.NotifyingList<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

Direct Known Subclasses:
`[SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse](SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse.html)`, `[SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable](SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable.html)`

public classSubsetSupersetEObjectEStoreWithInverseResolvingEList<E>
extends [SubsetSupersetEObjectEStoreWithInverseEList](SubsetSupersetEObjectEStoreWithInverseEList.html)<E>

Since:
1.2
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseResolvingEList)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse](SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse.html)<[E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse.html)>`

`static class`
`[SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable](SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable.html)<[E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable.html)>`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.uml2.util.[SubsetSupersetEObjectEStoreWithInverseEList](SubsetSupersetEObjectEStoreWithInverseEList.html)
`[inverseFeatureID](SubsetSupersetEObjectEStoreWithInverseEList.html#inverseFeatureID)`
Fields inherited from class com.nomagic.magicdraw.uml2.util.[SubsetSupersetEObjectEStoreEList](SubsetSupersetEObjectEStoreEList.html)
`[dataClass](SubsetSupersetEObjectEStoreEList.html#dataClass), [subsetFeatureIDs](SubsetSupersetEObjectEStoreEList.html#subsetFeatureIDs), [supersetFeatureIDs](SubsetSupersetEObjectEStoreEList.html#supersetFeatureIDs)`
Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic
`eStructuralFeature`
Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic
`HAS_INSTANCE_CLASS, HAS_MANY_INVERSE, HAS_NAVIGABLE_INVERSE, HAS_PROXIES, IS_CONTAINER, IS_CONTAINMENT, IS_ENUM, IS_EOBJECT, IS_PRIMITIVE, IS_SET, IS_UNIQUE, IS_UNSETTABLE, kind`
Fields inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList
`owner`
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SubsetSupersetEObjectEStoreWithInverseResolvingEList](#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D,int%5B%5D,int))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] supersetFeatureIDs,
 int[] subsetFeatureIDs,
 int inverseFeatureID)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.html)`
`[resolve](#resolve(int,E))(int index,
 [E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.html) object)`
Methods inherited from class com.nomagic.magicdraw.uml2.util.[SubsetSupersetEObjectEStoreWithInverseEList](SubsetSupersetEObjectEStoreWithInverseEList.html)
`[getInverseFeatureClass](SubsetSupersetEObjectEStoreWithInverseEList.html#getInverseFeatureClass()), [getInverseFeatureID](SubsetSupersetEObjectEStoreWithInverseEList.html#getInverseFeatureID()), [hasInverse](SubsetSupersetEObjectEStoreWithInverseEList.html#hasInverse()), [hasNavigableInverse](SubsetSupersetEObjectEStoreWithInverseEList.html#hasNavigableInverse())`
Methods inherited from class com.nomagic.magicdraw.uml2.util.[SubsetSupersetEObjectEStoreEList](SubsetSupersetEObjectEStoreEList.html)
`[add](SubsetSupersetEObjectEStoreEList.html#add(int,E)), [add](SubsetSupersetEObjectEStoreEList.html#add(E)), [addAll](SubsetSupersetEObjectEStoreEList.html#addAll(int,java.util.Collection)), [addAll](SubsetSupersetEObjectEStoreEList.html#addAll(java.util.Collection)), [basicAdd](SubsetSupersetEObjectEStoreEList.html#basicAdd(E,org.eclipse.emf.common.notify.NotificationChain)), [basicSet](SubsetSupersetEObjectEStoreEList.html#basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain)), [didRemove](SubsetSupersetEObjectEStoreEList.html#didRemove(int,E)), [enforceSubsetConstraints](SubsetSupersetEObjectEStoreEList.html#enforceSubsetConstraints()), [enforceSupersetConstraints](SubsetSupersetEObjectEStoreEList.html#enforceSupersetConstraints()), [replaceOrAddToSuperset](SubsetSupersetEObjectEStoreEList.html#replaceOrAddToSuperset(java.lang.Object,java.lang.Object)), [resolve](SubsetSupersetEObjectEStoreEList.html#resolve(int,org.eclipse.emf.ecore.EObject)), [set](SubsetSupersetEObjectEStoreEList.html#set(int,E)), [subsetRemove](SubsetSupersetEObjectEStoreEList.html#subsetRemove(java.lang.Object)), [supersetAdd](SubsetSupersetEObjectEStoreEList.html#supersetAdd(java.lang.Object))`
Methods inherited from class com.nomagic.magicdraw.uml2.util.[ModelEStoreEList](ModelEStoreEList.html)
`[addAllUnique](ModelEStoreEList.html#addAllUnique(int,java.util.Collection)), [addUnique](ModelEStoreEList.html#addUnique(int,E)), [addUnique](ModelEStoreEList.html#addUnique(E)), [afterChange](ModelEStoreEList.html#afterChange()), [basicRemove](ModelEStoreEList.html#basicRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)), [beforeChange](ModelEStoreEList.html#beforeChange()), [firePropertyChange](ModelEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)), [firePropertyChange](ModelEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int,int)), [getPropertyEventName](ModelEStoreEList.html#getPropertyEventName(java.lang.Object)), [hasProxies](ModelEStoreEList.html#hasProxies()), [indexOf](ModelEStoreEList.html#indexOf(java.lang.Object)), [lastIndexOf](ModelEStoreEList.html#lastIndexOf(java.lang.Object)), [move](ModelEStoreEList.html#move(int,int)), [remove](ModelEStoreEList.html#remove(int)), [removeAll](ModelEStoreEList.html#removeAll(java.util.Collection)), [setUnique](ModelEStoreEList.html#setUnique(int,E)), [validate](ModelEStoreEList.html#validate(int,E))`
Methods inherited from class com.nomagic.magicdraw.emf.impl.[BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)
`[createOperationTimeoutException](../../emf/impl/BasicEStoreEList.html#createOperationTimeoutException()), [getLockProvider](../../emf/impl/BasicEStoreEList.html#getLockProvider())`
Methods inherited from class com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList
`delegateAdd, delegateAdd, delegateBasicList, delegateClear, delegateContains, delegateContainsAll, delegateEquals, delegateGet, delegateHashCode, delegateIndexOf, delegateIsEmpty, delegateIterator, delegateLastIndexOf, delegateList, delegateListIterator, delegateMove, delegateRemove, delegateSet, delegateSize, delegateToArray, delegateToArray, delegateToString, eStore, execute, getEStructuralFeature, makeLastInCollection, snapshot`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic
`canContainNull, didChange, hasInstanceClass, hasManyInverse, isContainer, isContainment, isEObject, isSet, isUnique, isUnsettable, kind, unset, useEquals`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList
`contains, containsAll, createNotification, createNotification, dispatchNotification, get, getEObject, getFeature, getFeatureID, getFeatureType, getInverseEReference, getNotifier, inverseAdd, inverseRemove, isInstance, isNotificationRequired, resolve, resolveProxy, set, toArray, toArray`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl
`basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray`
Methods inherited from class org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl
`addAllUnique, addAllUnique, addAllUnique, clear, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doMove, doRemove, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet`
Methods inherited from class org.eclipse.emf.common.util.DelegatingEList
`doClear, equals, get, hashCode, isEmpty, primitiveGet, remove, retainAll, size, toString`
Methods inherited from class org.eclipse.emf.common.util.AbstractEList
`didAdd, didClear, didMove, didSet, equalObjects, getDuplicates, getNonDuplicates, iterator, listIterator, listIterator, move`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[removeRange](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface org.eclipse.emf.common.util.EList
`move`
Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList
`addAllUnique, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)
`[clear](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#clear()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [get](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#get(int)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#hashCode()), [isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#isEmpty()), [iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#iterator()), [listIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator(int)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [replaceAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#size()), [sort](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SubsetSupersetEObjectEStoreWithInverseResolvingEList
public SubsetSupersetEObjectEStoreWithInverseResolvingEList([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 @CheckForNull
 int[] supersetFeatureIDs,
 @CheckForNull
 int[] subsetFeatureIDs,
 int inverseFeatureID)
 ============ METHOD DETAIL ========== 
Method Details
resolve
protected [E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.html) resolve(int index,
 [E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.html) object)
Overrides:
`resolve` in class `org.eclipse.emf.ecore.util.DelegatingEcoreEList<[E](SubsetSupersetEObjectEStoreWithInverseResolvingEList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class SubsetSupersetEObjectEStoreWithInverseResolvingEList">Class SubsetSupersetEObjectEStoreWithInverseResolvingEList&lt;E&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.AbstractEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.DelegatingEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingEcoreEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.DelegatingEcoreEList.Dynamic&lt;E&gt;
<div class="inheritance">com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;E&gt;
<div class="inheritance"><a href="../../emf/impl/BasicEStoreEList.html" title="class in com.nomagic.magicdraw.emf.impl">com.nomagic.magicdraw.emf.impl.BasicEStoreEList</a>&lt;E&gt;
<div class="inheritance"><a href="ModelEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">com.nomagic.magicdraw.uml2.util.ModelEStoreEList</a>&lt;E&gt;
<div class="inheritance"><a href="SubsetSupersetEObjectEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList</a>&lt;E&gt;
<div class="inheritance"><a href="SubsetSupersetEObjectEStoreWithInverseEList.html" title="class in com.nomagic.magicdraw.uml2.util">com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseEList</a>&lt;E&gt;
<div class="inheritance">com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseResolvingEList&lt;E&gt;</div>
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
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;E&gt;</code>, <code>org.eclipse.emf.common.notify.NotifyingList&lt;E&gt;</code>, <code>org.eclipse.emf.common.util.EList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.EStructuralFeature.Setting</code>, <code>org.eclipse.emf.ecore.util.InternalEList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.util.InternalEList.Unsettable&lt;E&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse</a></code>, <code><a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">SubsetSupersetEObjectEStoreWithInverseResolvingEList&lt;E&gt;</span>
<span class="extends-implements">extends <a href="SubsetSupersetEObjectEStoreWithInverseEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseEList</a>&lt;E&gt;</span></div>
<dl class="notes">
<dt>Since:</dt>
<dd>1.2</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseResolvingEList">Serialized Form</a></li>
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
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse</a>&lt;<a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList.ManyInverse">E</a>&gt;</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable</a>&lt;<a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList.Unsettable">E</a>&gt;</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseEList">Fields inherited from class com.nomagic.magicdraw.uml2.util.<a href="SubsetSupersetEObjectEStoreWithInverseEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseEList</a></h3>
<code><a href="SubsetSupersetEObjectEStoreWithInverseEList.html#inverseFeatureID">inverseFeatureID</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList">Fields inherited from class com.nomagic.magicdraw.uml2.util.<a href="SubsetSupersetEObjectEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreEList</a></h3>
<code><a href="SubsetSupersetEObjectEStoreEList.html#dataClass">dataClass</a>, <a href="SubsetSupersetEObjectEStoreEList.html#subsetFeatureIDs">subsetFeatureIDs</a>, <a href="SubsetSupersetEObjectEStoreEList.html#supersetFeatureIDs">supersetFeatureIDs</a></code></div>
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
<h3 id="fields-inherited-from-class-java.util.AbstractList">Fields inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#modCount" title="class or interface in java.util">modCount</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D,int%5B%5D,int)">SubsetSupersetEObjectEStoreWithInverseResolvingEList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] supersetFeatureIDs,
 int[] subsetFeatureIDs,
 int inverseFeatureID)</code></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList">E</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resolve(int,E)">resolve</a><wbr/>(int index,
 <a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreWithInverseEList">Methods inherited from class com.nomagic.magicdraw.uml2.util.<a href="SubsetSupersetEObjectEStoreWithInverseEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseEList</a></h3>
<code><a href="SubsetSupersetEObjectEStoreWithInverseEList.html#getInverseFeatureClass()">getInverseFeatureClass</a>, <a href="SubsetSupersetEObjectEStoreWithInverseEList.html#getInverseFeatureID()">getInverseFeatureID</a>, <a href="SubsetSupersetEObjectEStoreWithInverseEList.html#hasInverse()">hasInverse</a>, <a href="SubsetSupersetEObjectEStoreWithInverseEList.html#hasNavigableInverse()">hasNavigableInverse</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList">Methods inherited from class com.nomagic.magicdraw.uml2.util.<a href="SubsetSupersetEObjectEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreEList</a></h3>
<code><a href="SubsetSupersetEObjectEStoreEList.html#add(int,E)">add</a>, <a href="SubsetSupersetEObjectEStoreEList.html#add(E)">add</a>, <a href="SubsetSupersetEObjectEStoreEList.html#addAll(int,java.util.Collection)">addAll</a>, <a href="SubsetSupersetEObjectEStoreEList.html#addAll(java.util.Collection)">addAll</a>, <a href="SubsetSupersetEObjectEStoreEList.html#basicAdd(E,org.eclipse.emf.common.notify.NotificationChain)">basicAdd</a>, <a href="SubsetSupersetEObjectEStoreEList.html#basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain)">basicSet</a>, <a href="SubsetSupersetEObjectEStoreEList.html#didRemove(int,E)">didRemove</a>, <a href="SubsetSupersetEObjectEStoreEList.html#enforceSubsetConstraints()">enforceSubsetConstraints</a>, <a href="SubsetSupersetEObjectEStoreEList.html#enforceSupersetConstraints()">enforceSupersetConstraints</a>, <a href="SubsetSupersetEObjectEStoreEList.html#replaceOrAddToSuperset(java.lang.Object,java.lang.Object)">replaceOrAddToSuperset</a>, <a href="SubsetSupersetEObjectEStoreEList.html#resolve(int,org.eclipse.emf.ecore.EObject)">resolve</a>, <a href="SubsetSupersetEObjectEStoreEList.html#set(int,E)">set</a>, <a href="SubsetSupersetEObjectEStoreEList.html#subsetRemove(java.lang.Object)">subsetRemove</a>, <a href="SubsetSupersetEObjectEStoreEList.html#supersetAdd(java.lang.Object)">supersetAdd</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml2.util.ModelEStoreEList">Methods inherited from class com.nomagic.magicdraw.uml2.util.<a href="ModelEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">ModelEStoreEList</a></h3>
<code><a href="ModelEStoreEList.html#addAllUnique(int,java.util.Collection)">addAllUnique</a>, <a href="ModelEStoreEList.html#addUnique(int,E)">addUnique</a>, <a href="ModelEStoreEList.html#addUnique(E)">addUnique</a>, <a href="ModelEStoreEList.html#afterChange()">afterChange</a>, <a href="ModelEStoreEList.html#basicRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">basicRemove</a>, <a href="ModelEStoreEList.html#beforeChange()">beforeChange</a>, <a href="ModelEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)">firePropertyChange</a>, <a href="ModelEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int,int)">firePropertyChange</a>, <a href="ModelEStoreEList.html#getPropertyEventName(java.lang.Object)">getPropertyEventName</a>, <a href="ModelEStoreEList.html#hasProxies()">hasProxies</a>, <a href="ModelEStoreEList.html#indexOf(java.lang.Object)">indexOf</a>, <a href="ModelEStoreEList.html#lastIndexOf(java.lang.Object)">lastIndexOf</a>, <a href="ModelEStoreEList.html#move(int,int)">move</a>, <a href="ModelEStoreEList.html#remove(int)">remove</a>, <a href="ModelEStoreEList.html#removeAll(java.util.Collection)">removeAll</a>, <a href="ModelEStoreEList.html#setUnique(int,E)">setUnique</a>, <a href="ModelEStoreEList.html#validate(int,E)">validate</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emf.impl.BasicEStoreEList">Methods inherited from class com.nomagic.magicdraw.emf.impl.<a href="../../emf/impl/BasicEStoreEList.html" title="class in com.nomagic.magicdraw.emf.impl">BasicEStoreEList</a></h3>
<code><a href="../../emf/impl/BasicEStoreEList.html#createOperationTimeoutException()">createOperationTimeoutException</a>, <a href="../../emf/impl/BasicEStoreEList.html#getLockProvider()">getLockProvider</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList">Methods inherited from class com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList</h3>
<code>delegateAdd, delegateAdd, delegateBasicList, delegateClear, delegateContains, delegateContainsAll, delegateEquals, delegateGet, delegateHashCode, delegateIndexOf, delegateIsEmpty, delegateIterator, delegateLastIndexOf, delegateList, delegateListIterator, delegateMove, delegateRemove, delegateSet, delegateSize, delegateToArray, delegateToArray, delegateToString, eStore, execute, getEStructuralFeature, makeLastInCollection, snapshot</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic</h3>
<code>canContainNull, didChange, hasInstanceClass, hasManyInverse, isContainer, isContainment, isEObject, isSet, isUnique, isUnsettable, kind, unset, useEquals</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList</h3>
<code>contains, containsAll, createNotification, createNotification, dispatchNotification, get, getEObject, getFeature, getFeatureID, getFeatureType, getInverseEReference, getNotifier, inverseAdd, inverseRemove, isInstance, isNotificationRequired, resolve, resolveProxy, set, toArray, toArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingNotifyingInternalEListImpl</h3>
<code>basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl">Methods inherited from class org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl</h3>
<code>addAllUnique, addAllUnique, addAllUnique, clear, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doMove, doRemove, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.DelegatingEList">Methods inherited from class org.eclipse.emf.common.util.DelegatingEList</h3>
<code>doClear, equals, get, hashCode, isEmpty, primitiveGet, remove, retainAll, size, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEList">Methods inherited from class org.eclipse.emf.common.util.AbstractEList</h3>
<code>didAdd, didClear, didMove, didSet, equalObjects, getDuplicates, getNonDuplicates, iterator, listIterator, listIterator, move</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.EList">Methods inherited from interface org.eclipse.emf.common.util.EList</h3>
<code>move</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.InternalEList">Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList</h3>
<code>addAllUnique, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#size()" title="class or interface in java.util">size</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int[],int[],int)">
<h3>SubsetSupersetEObjectEStoreWithInverseResolvingEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SubsetSupersetEObjectEStoreWithInverseResolvingEList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 @CheckForNull
 int[] supersetFeatureIDs,
 @CheckForNull
 int[] subsetFeatureIDs,
 int inverseFeatureID)</span></div>
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
<section class="detail" id="resolve(int,E)">
<h3 id="resolve(int,java.lang.Object)">resolve</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList">E</a></span> <span class="element-name">resolve</span><wbr/><span class="parameters">(int index,
 <a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList">E</a> object)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>resolve</code> in class <code>org.eclipse.emf.ecore.util.DelegatingEcoreEList&lt;<a href="SubsetSupersetEObjectEStoreWithInverseResolvingEList.html" title="type parameter in SubsetSupersetEObjectEStoreWithInverseResolvingEList">E</a>&gt;</code></dd>
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
