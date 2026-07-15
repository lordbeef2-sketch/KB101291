# JAVA OPENAPI: SubsetSupersetEObjectEStoreEList (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/util/SubsetSupersetEObjectEStoreEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/SubsetSupersetEObjectEStoreEList.html`
- source_sha256: `5e5638608ed8d3ea9e87f58373717a3718e76440501c0e0bf83842a83f7d8ae9`
- captured_utc: `2026-07-14T16:56:07.268591+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class SubsetSupersetEObjectEStoreEList<E>

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
com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList<E>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<E>`, `org.eclipse.emf.common.notify.NotifyingList<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

Direct Known Subclasses:
`[SubsetSupersetEObjectEStoreContainmentEList](SubsetSupersetEObjectEStoreContainmentEList.html)`, `[SubsetSupersetEObjectEStoreResolvingEList](SubsetSupersetEObjectEStoreResolvingEList.html)`, `[SubsetSupersetEObjectEStoreWithInverseEList](SubsetSupersetEObjectEStoreWithInverseEList.html)`

public classSubsetSupersetEObjectEStoreEList<E>
extends [ModelEStoreEList](ModelEStoreEList.html)<E>

A list that enforces subset/superset constraints. Specifically, when an
 element is added to a subset, it is also added to the associated superset(s),
 if not already present; when an element is removed from a superset, it is
 also removed from the associated subset(s), if present.

Since:
1.2
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?>`
`[dataClass](#dataClass)`

`protected final int[]`
`[subsetFeatureIDs](#subsetFeatureIDs)`
An array of subset feature identifiers.
`protected final int[]`
`[supersetFeatureIDs](#supersetFeatureIDs)`
An array of superset feature identifiers.
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
`[SubsetSupersetEObjectEStoreEList](#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D,int%5B%5D))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] supersetFeatureIDs,
 int[] subsetFeatureIDs)`
Creates and initializes a new `SubsetSupersetEObjectEStoreEList` instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[add](#add(int,E))(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) object)`
Adds the object at the given index in the list.
`boolean`
`[add](#add(E))([E](SubsetSupersetEObjectEStoreEList.html) object)`

`boolean`
`[addAll](#addAll(int,java.util.Collection))(int index,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [E](SubsetSupersetEObjectEStoreEList.html)> collection)`

`boolean`
`[addAll](#addAll(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [E](SubsetSupersetEObjectEStoreEList.html)> collection)`

`org.eclipse.emf.common.notify.NotificationChain`
`[basicAdd](#basicAdd(E,org.eclipse.emf.common.notify.NotificationChain))([E](SubsetSupersetEObjectEStoreEList.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)`

`org.eclipse.emf.common.notify.NotificationChain`
`[basicSet](#basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain))(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)`

`protected void`
`[didRemove](#didRemove(int,E))(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) oldObject)`

`protected boolean`
`[enforceSubsetConstraints](#enforceSubsetConstraints())()`
Indicates whether subset constraints should be enforced.
`protected boolean`
`[enforceSupersetConstraints](#enforceSupersetConstraints())()`
Indicates whether superset constraints should be enforced.
`protected void`
`[replaceOrAddToSuperset](#replaceOrAddToSuperset(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldObject,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
Replaces the specified value or adds ir to the superset if new value is not already added.
`protected org.eclipse.emf.ecore.EObject`
`[resolve](#resolve(int,org.eclipse.emf.ecore.EObject))(int index,
 org.eclipse.emf.ecore.EObject eObject)`

`[E](SubsetSupersetEObjectEStoreEList.html)`
`[set](#set(int,E))(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) object)`

`protected void`
`[subsetRemove](#subsetRemove(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
Removes the specified element from the subset(s).
`protected void`
`[supersetAdd](#supersetAdd(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
Adds the specified element to the superset(s).
Methods inherited from class com.nomagic.magicdraw.uml2.util.[ModelEStoreEList](ModelEStoreEList.html)
`[addAllUnique](ModelEStoreEList.html#addAllUnique(int,java.util.Collection)), [addUnique](ModelEStoreEList.html#addUnique(int,E)), [addUnique](ModelEStoreEList.html#addUnique(E)), [afterChange](ModelEStoreEList.html#afterChange()), [basicRemove](ModelEStoreEList.html#basicRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)), [beforeChange](ModelEStoreEList.html#beforeChange()), [firePropertyChange](ModelEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)), [firePropertyChange](ModelEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int,int)), [getPropertyEventName](ModelEStoreEList.html#getPropertyEventName(java.lang.Object)), [hasProxies](ModelEStoreEList.html#hasProxies()), [indexOf](ModelEStoreEList.html#indexOf(java.lang.Object)), [lastIndexOf](ModelEStoreEList.html#lastIndexOf(java.lang.Object)), [move](ModelEStoreEList.html#move(int,int)), [remove](ModelEStoreEList.html#remove(int)), [removeAll](ModelEStoreEList.html#removeAll(java.util.Collection)), [setUnique](ModelEStoreEList.html#setUnique(int,E)), [validate](ModelEStoreEList.html#validate(int,E))`
Methods inherited from class com.nomagic.magicdraw.emf.impl.[BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)
`[createOperationTimeoutException](../../emf/impl/BasicEStoreEList.html#createOperationTimeoutException()), [getLockProvider](../../emf/impl/BasicEStoreEList.html#getLockProvider())`
Methods inherited from class com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList
`delegateAdd, delegateAdd, delegateBasicList, delegateClear, delegateContains, delegateContainsAll, delegateEquals, delegateGet, delegateHashCode, delegateIndexOf, delegateIsEmpty, delegateIterator, delegateLastIndexOf, delegateList, delegateListIterator, delegateMove, delegateRemove, delegateSet, delegateSize, delegateToArray, delegateToArray, delegateToString, eStore, execute, getEStructuralFeature, makeLastInCollection, snapshot`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic
`canContainNull, didChange, hasInstanceClass, hasInverse, hasManyInverse, hasNavigableInverse, isContainer, isContainment, isEObject, isSet, isUnique, isUnsettable, kind, unset, useEquals`
Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList
`contains, containsAll, createNotification, createNotification, dispatchNotification, get, getEObject, getFeature, getFeatureID, getFeatureType, getInverseEReference, getInverseFeatureClass, getInverseFeatureID, getNotifier, inverseAdd, inverseRemove, isInstance, isNotificationRequired, resolve, resolve, resolveProxy, set, toArray, toArray`
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

============ FIELD DETAIL =========== 
Field Details
supersetFeatureIDs
protected final int[] supersetFeatureIDs
An array of superset feature identifiers.
subsetFeatureIDs
protected final int[] subsetFeatureIDs
An array of subset feature identifiers.
dataClass
protected [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SubsetSupersetEObjectEStoreEList
public SubsetSupersetEObjectEStoreEList([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 @CheckForNull
 int[] supersetFeatureIDs,
 @CheckForNull
 int[] subsetFeatureIDs)
Creates and initializes a new `SubsetSupersetEObjectEStoreEList` instance.
Parameters:
`dataClass` - class of data type.
`owner` - owner of the collection.
`featureID` - feature id of that values is hold by this collection.
`supersetFeatureIDs` - array of superset features.
`subsetFeatureIDs` - array of subset features.
 ============ METHOD DETAIL ========== 
Method Details
enforceSubsetConstraints
protected boolean enforceSubsetConstraints()
Indicates whether subset constraints should be enforced.
Returns:
`true` if subset constraints should be enforced;
 `false` otherwise.
supersetAdd
protected void supersetAdd([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Adds the specified element to the superset(s).
Parameters:
`object` - The element to be added.
replaceOrAddToSuperset
protected void replaceOrAddToSuperset([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldObject,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Replaces the specified value or adds ir to the superset if new value is not already added.
Parameters:
`oldObject` - old value.
`object` - new value.
enforceSupersetConstraints
protected boolean enforceSupersetConstraints()
Indicates whether superset constraints should be enforced.
Returns:
`true` if superset constraints should be enforced;
 `false` otherwise.
subsetRemove
protected void subsetRemove([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Removes the specified element from the subset(s).
Parameters:
`object` - The element to be removed.
basicAdd
public org.eclipse.emf.common.notify.NotificationChain basicAdd([E](SubsetSupersetEObjectEStoreEList.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)
Specified by:
`basicAdd` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](SubsetSupersetEObjectEStoreEList.html)>`
Overrides:
`basicAdd` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](SubsetSupersetEObjectEStoreEList.html)>`
basicSet
public org.eclipse.emf.common.notify.NotificationChain basicSet(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)
Overrides:
`basicSet` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](SubsetSupersetEObjectEStoreEList.html)>`
add
public void add(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) object)
Description copied from class: `[ModelEStoreEList](ModelEStoreEList.html#add(int,E))`
Adds the object at the given index in the list.
 If `uniqueness` is required,
 duplicates will be ignored.
 This implementation delegates to [`addUnique(int, E)`](ModelEStoreEList.html#addUnique(int,E))
 after uniqueness checking.
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(int,E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Overrides:
`[add](ModelEStoreEList.html#add(int,E))` in class `[ModelEStoreEList](ModelEStoreEList.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
`object` - the object to be added.
See Also:
[`ModelEStoreEList.addUnique(int, Object)`](ModelEStoreEList.html#addUnique(int,E))
add
public boolean add([E](SubsetSupersetEObjectEStoreEList.html) object)
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Overrides:
`add` in class `org.eclipse.emf.common.util.AbstractEList<[E](SubsetSupersetEObjectEStoreEList.html)>`
addAll
public boolean addAll([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [E](SubsetSupersetEObjectEStoreEList.html)> collection)
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#addAll(java.util.Collection))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(java.util.Collection))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Overrides:
`addAll` in class `org.eclipse.emf.common.util.AbstractEList<[E](SubsetSupersetEObjectEStoreEList.html)>`
addAll
public boolean addAll(int index,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [E](SubsetSupersetEObjectEStoreEList.html)> collection)
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Overrides:
`addAll` in class `org.eclipse.emf.common.util.AbstractEList<[E](SubsetSupersetEObjectEStoreEList.html)>`
set
public [E](SubsetSupersetEObjectEStoreEList.html) set(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) object)
Specified by:
`[set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#set(int,E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](SubsetSupersetEObjectEStoreEList.html)>`
Overrides:
`set` in class `org.eclipse.emf.common.util.AbstractEList<[E](SubsetSupersetEObjectEStoreEList.html)>`
didRemove
protected void didRemove(int index,
 [E](SubsetSupersetEObjectEStoreEList.html) oldObject)
Overrides:
`didRemove` in class `org.eclipse.emf.common.util.AbstractEList<[E](SubsetSupersetEObjectEStoreEList.html)>`
resolve
protected org.eclipse.emf.ecore.EObject resolve(int index,
 org.eclipse.emf.ecore.EObject eObject)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class SubsetSupersetEObjectEStoreEList">Class SubsetSupersetEObjectEStoreEList&lt;E&gt;</h1>
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
<div class="inheritance">com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList&lt;E&gt;</div>
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
<dd><code><a href="SubsetSupersetEObjectEStoreContainmentEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreContainmentEList</a></code>, <code><a href="SubsetSupersetEObjectEStoreResolvingEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreResolvingEList</a></code>, <code><a href="SubsetSupersetEObjectEStoreWithInverseEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreWithInverseEList</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">SubsetSupersetEObjectEStoreEList&lt;E&gt;</span>
<span class="extends-implements">extends <a href="ModelEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">ModelEStoreEList</a>&lt;E&gt;</span></div>
<div class="block">A list that enforces subset/superset constraints. Specifically, when an
 element is added to a subset, it is also added to the associated superset(s),
 if not already present; when an element is removed from a superset, it is
 also removed from the associated subset(s), if present.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>1.2</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEStoreEList">Serialized Form</a></li>
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
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#dataClass">dataClass</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected final int[]</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#subsetFeatureIDs">subsetFeatureIDs</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An array of subset feature identifiers.</div>
</div>
<div class="col-first even-row-color"><code>protected final int[]</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#supersetFeatureIDs">supersetFeatureIDs</a></code></div>
<div class="col-last even-row-color">
<div class="block">An array of superset feature identifiers.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D,int%5B%5D)">SubsetSupersetEObjectEStoreEList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] supersetFeatureIDs,
 int[] subsetFeatureIDs)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>SubsetSupersetEObjectEStoreEList</code> instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(int,E)">add</a><wbr/>(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the object at the given index in the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(E)">add</a><wbr/>(<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAll(int,java.util.Collection)">addAll</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAll(java.util.Collection)">addAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.NotificationChain</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#basicAdd(E,org.eclipse.emf.common.notify.NotificationChain)">basicAdd</a><wbr/>(<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.NotificationChain</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain)">basicSet</a><wbr/>(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#didRemove(int,E)">didRemove</a><wbr/>(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> oldObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enforceSubsetConstraints()">enforceSubsetConstraints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether subset constraints should be enforced.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enforceSupersetConstraints()">enforceSupersetConstraints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates whether superset constraints should be enforced.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceOrAddToSuperset(java.lang.Object,java.lang.Object)">replaceOrAddToSuperset</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replaces the specified value or adds ir to the superset if new value is not already added.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected org.eclipse.emf.ecore.EObject</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resolve(int,org.eclipse.emf.ecore.EObject)">resolve</a><wbr/>(int index,
 org.eclipse.emf.ecore.EObject eObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#set(int,E)">set</a><wbr/>(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#subsetRemove(java.lang.Object)">subsetRemove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the specified element from the subset(s).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#supersetAdd(java.lang.Object)">supersetAdd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the specified element to the superset(s).</div>
</div>
</div>
</div>
</div>
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
<code>canContainNull, didChange, hasInstanceClass, hasInverse, hasManyInverse, hasNavigableInverse, isContainer, isContainment, isEObject, isSet, isUnique, isUnsettable, kind, unset, useEquals</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.DelegatingEcoreEList">Methods inherited from class org.eclipse.emf.ecore.util.DelegatingEcoreEList</h3>
<code>contains, containsAll, createNotification, createNotification, dispatchNotification, get, getEObject, getFeature, getFeatureID, getFeatureType, getInverseEReference, getInverseFeatureClass, getInverseFeatureID, getNotifier, inverseAdd, inverseRemove, isInstance, isNotificationRequired, resolve, resolve, resolveProxy, set, toArray, toArray</code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="supersetFeatureIDs">
<h3>supersetFeatureIDs</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">int[]</span> <span class="element-name">supersetFeatureIDs</span></div>
<div class="block">An array of superset feature identifiers.</div>
</section>
</li>
<li>
<section class="detail" id="subsetFeatureIDs">
<h3>subsetFeatureIDs</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">int[]</span> <span class="element-name">subsetFeatureIDs</span></div>
<div class="block">An array of subset feature identifiers.</div>
</section>
</li>
<li>
<section class="detail" id="dataClass">
<h3>dataClass</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">dataClass</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int[],int[])">
<h3>SubsetSupersetEObjectEStoreEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SubsetSupersetEObjectEStoreEList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 @CheckForNull
 int[] supersetFeatureIDs,
 @CheckForNull
 int[] subsetFeatureIDs)</span></div>
<div class="block">Creates and initializes a new <code>SubsetSupersetEObjectEStoreEList</code> instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataClass</code> - class of data type.</dd>
<dd><code>owner</code> - owner of the collection.</dd>
<dd><code>featureID</code> - feature id of that values is hold by this collection.</dd>
<dd><code>supersetFeatureIDs</code> - array of superset features.</dd>
<dd><code>subsetFeatureIDs</code> - array of subset features.</dd>
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
<section class="detail" id="enforceSubsetConstraints()">
<h3>enforceSubsetConstraints</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">enforceSubsetConstraints</span>()</div>
<div class="block">Indicates whether subset constraints should be enforced.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if subset constraints should be enforced;
         <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="supersetAdd(java.lang.Object)">
<h3>supersetAdd</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">supersetAdd</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Adds the specified element to the superset(s).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The element to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceOrAddToSuperset(java.lang.Object,java.lang.Object)">
<h3>replaceOrAddToSuperset</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">replaceOrAddToSuperset</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Replaces the specified value or adds ir to the superset if new value is not already added.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldObject</code> - old value.</dd>
<dd><code>object</code> - new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enforceSupersetConstraints()">
<h3>enforceSupersetConstraints</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">enforceSupersetConstraints</span>()</div>
<div class="block">Indicates whether superset constraints should be enforced.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> if superset constraints should be enforced;
         <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="subsetRemove(java.lang.Object)">
<h3>subsetRemove</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">subsetRemove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Removes the specified element from the subset(s).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>object</code> - The element to be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="basicAdd(E,org.eclipse.emf.common.notify.NotificationChain)">
<h3 id="basicAdd(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">basicAdd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.NotificationChain</span> <span class="element-name">basicAdd</span><wbr/><span class="parameters">(<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>basicAdd</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>basicAdd</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain)">
<h3 id="basicSet(int,java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">basicSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.NotificationChain</span> <span class="element-name">basicSet</span><wbr/><span class="parameters">(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>basicSet</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(int,E)">
<h3 id="add(int,java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="ModelEStoreEList.html#add(int,E)">ModelEStoreEList</a></code></span></div>
<div class="block">Adds the object at the given index in the list.
 If <code>uniqueness</code> is required,
 duplicates will be ignored.
 This implementation delegates to <a href="ModelEStoreEList.html#addUnique(int,E)"><code>addUnique(int, E)</code></a>
 after uniqueness checking.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(int,E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a href="ModelEStoreEList.html#add(int,E)">add</a></code> in class <code><a href="ModelEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">ModelEStoreEList</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dd><code>object</code> - the object to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="ModelEStoreEList.html#addUnique(int,E)"><code>ModelEStoreEList.addUnique(int, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(E)">
<h3 id="add(java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>add</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAll(java.util.Collection)">
<h3>addAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt; collection)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>addAll</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAll(int,java.util.Collection)">
<h3>addAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addAll</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt; collection)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>addAll</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="set(int,E)">
<h3 id="set(int,java.lang.Object)">set</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a></span> <span class="element-name">set</span><wbr/><span class="parameters">(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#set(int,E)" title="class or interface in java.util">set</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>set</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="didRemove(int,E)">
<h3 id="didRemove(int,java.lang.Object)">didRemove</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">didRemove</span><wbr/><span class="parameters">(int index,
 <a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a> oldObject)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>didRemove</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="SubsetSupersetEObjectEStoreEList.html" title="type parameter in SubsetSupersetEObjectEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resolve(int,org.eclipse.emf.ecore.EObject)">
<h3>resolve</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">org.eclipse.emf.ecore.EObject</span> <span class="element-name">resolve</span><wbr/><span class="parameters">(int index,
 org.eclipse.emf.ecore.EObject eObject)</span></div>
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
