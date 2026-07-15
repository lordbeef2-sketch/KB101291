# JAVA OPENAPI: ModelEStoreEList (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/util/ModelEStoreEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/ModelEStoreEList.html`
- source_sha256: `0034190a97b24b9a59e8e48af16ebe907be81e30909c8978d4cba2dea13fc772`
- captured_utc: `2026-07-14T16:52:18.724969+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class ModelEStoreEList<E>

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
com.nomagic.magicdraw.uml2.util.ModelEStoreEList<E>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<E>`, `org.eclipse.emf.common.notify.NotifyingList<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

Direct Known Subclasses:
`[NoNullModelEStoreEList](NoNullModelEStoreEList.html)`, `[SubsetSupersetEObjectEStoreEList](SubsetSupersetEObjectEStoreEList.html)`

public classModelEStoreEList<E>
extends [BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)<E>

A list that delegates to a store.

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.ModelEStoreEList)

=========== FIELD SUMMARY =========== 
Field Summary
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
`[ModelEStoreEList](#%3Cinit%3E(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature))(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)`
Creates and initializes a new `ModelEStoreEList` instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[add](#add(int,E))(int index,
 [E](ModelEStoreEList.html) object)`
Adds the object at the given index in the list.
`boolean`
`[addAllUnique](#addAllUnique(int,java.util.Collection))(int index,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [E](ModelEStoreEList.html)> collection)`
Adds each object of the collection at each successive index in the list
 and returns whether any objects were added;
 it does no ranging checking or uniqueness checking.
`void`
`[addUnique](#addUnique(int,E))(int index,
 [E](ModelEStoreEList.html) object)`
Adds the object at the given index in the list;
 it does no ranging checking or uniqueness checking.
`void`
`[addUnique](#addUnique(E))([E](ModelEStoreEList.html) object)`
Adds the object at the end of the list;
 it does no uniqueness checking.
`protected final void`
`[afterChange](#afterChange())()`
The method will be invoked after specified property.
`org.eclipse.emf.common.notify.NotificationChain`
`[basicRemove](#basicRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)`

`protected final void`
`[beforeChange](#beforeChange())()`
The method will be invoked before specified property change.
`protected void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index)`
Implementation must fire property change event.
`protected void`
`[firePropertyChange](#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index,
 int newIndex)`
Implementation must fire property change event.
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyEventName](#getPropertyEventName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`
Returns name of the property change event.
`protected boolean`
`[hasProxies](#hasProxies())()`

`int`
`[indexOf](#indexOf(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`

`int`
`[lastIndexOf](#lastIndexOf(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`

`[E](ModelEStoreEList.html)`
`[move](#move(int,int))(int targetIndex,
 int sourceIndex)`
Moves the object at the source index of the list to the target index of the list
 and returns the moved object.
`[E](ModelEStoreEList.html)`
`[remove](#remove(int))(int index)`
Removes the object at the index from the list and returns it.
`boolean`
`[removeAll](#removeAll(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection)`
Removes each object of the collection from the list and returns whether any object was actually contained by the list.
`[E](ModelEStoreEList.html)`
`[setUnique](#setUnique(int,E))(int index,
 [E](ModelEStoreEList.html) object)`
Sets the object at the index
 and returns the old object at the index;
 it does no ranging checking or uniqueness checking.
`protected [E](ModelEStoreEList.html)`
`[validate](#validate(int,E))(int index,
 [E](ModelEStoreEList.html) object)`
Validates a new content object and returns the validated object.
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
`addAllUnique, addAllUnique, addAllUnique, basicAdd, basicSet, clear, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doMove, doRemove, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet`
Methods inherited from class org.eclipse.emf.common.util.DelegatingEList
`doClear, equals, get, hashCode, isEmpty, primitiveGet, remove, retainAll, size, toString`
Methods inherited from class org.eclipse.emf.common.util.AbstractEList
`add, addAll, addAll, didAdd, didClear, didMove, didRemove, didSet, equalObjects, getDuplicates, getNonDuplicates, iterator, listIterator, listIterator, move, set`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[removeRange](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface org.eclipse.emf.common.util.EList
`move`
Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList
`addAllUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E)), [addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)), [addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)), [clear](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#clear()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [get](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#get(int)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#hashCode()), [isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#isEmpty()), [iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#iterator()), [listIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator(int)), [remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [replaceAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#set(int,E)), [size](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#size()), [sort](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModelEStoreEList
public ModelEStoreEList(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)
Creates and initializes a new `ModelEStoreEList` instance.
Parameters:
`owner` - owner of the collection.
`eStructuralFeature` - feature that values is hold by this collection.
 ============ METHOD DETAIL ========== 
Method Details
getPropertyEventName
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyEventName([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
Returns name of the property change event.
Overrides:
`getPropertyEventName` in class `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList<[E](ModelEStoreEList.html)>`
Parameters:
`value` - property that changed value.
Returns:
property name.
beforeChange
protected final void beforeChange()
The method will be invoked before specified property change.
Overrides:
`[beforeChange](../../emf/impl/BasicEStoreEList.html#beforeChange())` in class `[BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)<[E](ModelEStoreEList.html)>`
afterChange
protected final void afterChange()
Description copied from class: `com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList`
The method will be invoked after specified property.
Overrides:
`[afterChange](../../emf/impl/BasicEStoreEList.html#afterChange())` in class `[BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)<[E](ModelEStoreEList.html)>`
firePropertyChange
protected void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index)
Implementation must fire property change event.
Overrides:
`[firePropertyChange](../../emf/impl/BasicEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int))` in class `[BasicEStoreEList](../../emf/impl/BasicEStoreEList.html)<[E](ModelEStoreEList.html)>`
Parameters:
`propertyName` - name of the changed property.
`oldValue` - old value of the property.
`newValue` - new value of the property.
`index` - index of the new value.
firePropertyChange
protected void firePropertyChange([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) propertyName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) oldValue,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) newValue,
 int index,
 int newIndex)
Implementation must fire property change event.
Parameters:
`propertyName` - name of the changed property.
`oldValue` - old value of the property.
`newValue` - new value of the property.
`index` - index of the new value.
`newIndex` - new index of the value
add
public void add(int index,
 [E](ModelEStoreEList.html) object)
Adds the object at the given index in the list.
 If `uniqueness` is required,
 duplicates will be ignored.
 This implementation delegates to [`addUnique(int, E)`](#addUnique(int,E))
 after uniqueness checking.
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(int,E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModelEStoreEList.html)>`
Overrides:
`add` in class `org.eclipse.emf.common.util.AbstractEList<[E](ModelEStoreEList.html)>`
Parameters:
`object` - the object to be added.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if `uniqueness` is required,
 and the object is a duplicate.
See Also:
[`addUnique(int, Object)`](#addUnique(int,E))
validate
protected [E](ModelEStoreEList.html) validate(int index,
 [E](ModelEStoreEList.html) object)
Validates a new content object and returns the validated object.
 This implementation checks for null, if `necessary` and returns the argument object.
 Clients may throw additional types of runtime exceptions
 in order to handle constraint violations.
Overrides:
`validate` in class `org.eclipse.emf.ecore.util.DelegatingEcoreEList<[E](ModelEStoreEList.html)>`
Parameters:
`index` - the position of the new content.
`object` - the new content.
Returns:
the validated content.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if a constraint prevents the object from being added.
addUnique
public void addUnique([E](ModelEStoreEList.html) object)
Adds the object at the end of the list;
 it does no uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as `required`
 and delegates to `inverseAdd` as `required`.
Specified by:
`addUnique` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](ModelEStoreEList.html)>`
Overrides:
`addUnique` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`object` - the object to be added.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
`DelegatingEcoreEList.Generic.hasInverse()`
`DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)`
addUnique
public void addUnique(int index,
 [E](ModelEStoreEList.html) object)
Adds the object at the given index in the list;
 it does no ranging checking or uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as `required`
 and delegates to `inverseAdd` as `required`.
Specified by:
`addUnique` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](ModelEStoreEList.html)>`
Overrides:
`addUnique` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`object` - the object to be added.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
`DelegatingEcoreEList.Generic.hasInverse()`
`DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)`
setUnique
public [E](ModelEStoreEList.html) setUnique(int index,
 [E](ModelEStoreEList.html) object)
Sets the object at the index
 and returns the old object at the index;
 it does no ranging checking or uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as `required`
 and delegates to `inverseAdd` and `inverseRemove` as `required`.
Specified by:
`setUnique` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](ModelEStoreEList.html)>`
Overrides:
`setUnique` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`index` - the position in question.
`object` - the object to set.
Returns:
the old object at the index.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
`DelegatingEcoreEList.Generic.hasInverse()`
`DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)`
`DelegatingEcoreEList.inverseRemove(E, org.eclipse.emf.common.notify.NotificationChain)`
move
public [E](ModelEStoreEList.html) move(int targetIndex,
 int sourceIndex)
Moves the object at the source index of the list to the target index of the list
 and returns the moved object.
 In addition to the normal effects,
 this override implementation generates notifications as `required`.
Specified by:
`move` in interface `org.eclipse.emf.common.util.EList<[E](ModelEStoreEList.html)>`
Overrides:
`move` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`targetIndex` - the new position for the object in the list.
`sourceIndex` - the old position of the object in the list.
Returns:
the moved object.
Throws:
`[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)` - if either index isn't within the size range.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
addAllUnique
public boolean addAllUnique(int index,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [E](ModelEStoreEList.html)> collection)
Adds each object of the collection at each successive index in the list
 and returns whether any objects were added;
 it does no ranging checking or uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as `required`
 and delegates to `inverseAdd` as `required`.
Specified by:
`addAllUnique` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](ModelEStoreEList.html)>`
Overrides:
`addAllUnique` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`index` - the index at which to add.
`collection` - the collection of objects to be added.
Returns:
whether any objects were added.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
`DelegatingEcoreEList.Generic.hasInverse()`
`DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)`
remove
public [E](ModelEStoreEList.html) remove(int index)
Removes the object at the index from the list and returns it.
 In addition to the normal effects,
 this override implementation generates notifications as `required`
 and delegates to `inverseRemove` as `required`.
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(int))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModelEStoreEList.html)>`
Overrides:
`remove` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`index` - the position of the object to remove.
Returns:
the removed object.
Throws:
`[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)` - if the index isn't within the size range.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
`DelegatingEcoreEList.Generic.hasInverse()`
`DelegatingEcoreEList.inverseRemove(E, org.eclipse.emf.common.notify.NotificationChain)`
removeAll
public boolean removeAll([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection)
Removes each object of the collection from the list and returns whether any object was actually contained by the list.
 In addition to the normal effects,
 this override implementation generates notifications as `required`
 and delegates to `inverseRemove` as `required`.
Specified by:
`[removeAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeAll(java.util.Collection))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](ModelEStoreEList.html)>`
Specified by:
`[removeAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModelEStoreEList.html)>`
Overrides:
`removeAll` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`
Parameters:
`collection` - the collection of objects to be removed.
Returns:
whether any object was actually contained by the list.
See Also:
`DelegatingEcoreEList.isNotificationRequired()`
`DelegatingEcoreEList.Generic.hasInverse()`
`DelegatingEcoreEList.inverseRemove(E, org.eclipse.emf.common.notify.NotificationChain)`
indexOf
public int indexOf([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Specified by:
`[indexOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#indexOf(java.lang.Object))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModelEStoreEList.html)>`
Overrides:
`indexOf` in class `org.eclipse.emf.ecore.util.DelegatingEcoreEList<[E](ModelEStoreEList.html)>`
lastIndexOf
public int lastIndexOf([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Specified by:
`[lastIndexOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#lastIndexOf(java.lang.Object))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModelEStoreEList.html)>`
Overrides:
`lastIndexOf` in class `org.eclipse.emf.ecore.util.DelegatingEcoreEList<[E](ModelEStoreEList.html)>`
hasProxies
protected boolean hasProxies()
Overrides:
`hasProxies` in class `org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic<[E](ModelEStoreEList.html)>`
basicRemove
public org.eclipse.emf.common.notify.NotificationChain basicRemove([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)
Specified by:
`basicRemove` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](ModelEStoreEList.html)>`
Overrides:
`basicRemove` in class `org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl<[E](ModelEStoreEList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class ModelEStoreEList">Class ModelEStoreEList&lt;E&gt;</h1>
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
<div class="inheritance">com.nomagic.magicdraw.uml2.util.ModelEStoreEList&lt;E&gt;</div>
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
<dd><code><a href="NoNullModelEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">NoNullModelEStoreEList</a></code>, <code><a href="SubsetSupersetEObjectEStoreEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEStoreEList</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ModelEStoreEList&lt;E&gt;</span>
<span class="extends-implements">extends <a href="../../emf/impl/BasicEStoreEList.html" title="class in com.nomagic.magicdraw.emf.impl">BasicEStoreEList</a>&lt;E&gt;</span></div>
<div class="block">A list that delegates to a store.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.ModelEStoreEList">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature)">ModelEStoreEList</a><wbr/>(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>ModelEStoreEList</code> instance.</div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(int,E)">add</a><wbr/>(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the object at the given index in the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAllUnique(int,java.util.Collection)">addAllUnique</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds each object of the collection at each successive index in the list
 and returns whether any objects were added;
 it does no ranging checking or uniqueness checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addUnique(int,E)">addUnique</a><wbr/>(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the object at the given index in the list;
 it does no ranging checking or uniqueness checking.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addUnique(E)">addUnique</a><wbr/>(<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds the object at the end of the list;
 it does no uniqueness checking.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterChange()">afterChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method will be invoked after specified property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.NotificationChain</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#basicRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">basicRemove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeChange()">beforeChange</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method will be invoked before specified property change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Implementation must fire property change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int,int)">firePropertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index,
 int newIndex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Implementation must fire property change event.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyEventName(java.lang.Object)">getPropertyEventName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns name of the property change event.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasProxies()">hasProxies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#indexOf(java.lang.Object)">indexOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#lastIndexOf(java.lang.Object)">lastIndexOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#move(int,int)">move</a><wbr/>(int targetIndex,
 int sourceIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves the object at the source index of the list to the target index of the list
 and returns the moved object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(int)">remove</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the object at the index from the list and returns it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAll(java.util.Collection)">removeAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes each object of the collection from the list and returns whether any object was actually contained by the list.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUnique(int,E)">setUnique</a><wbr/>(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the object at the index
 and returns the old object at the index;
 it does no ranging checking or uniqueness checking.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#validate(int,E)">validate</a><wbr/>(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validates a new content object and returns the validated object.</div>
</div>
</div>
</div>
</div>
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
<code>addAllUnique, addAllUnique, addAllUnique, basicAdd, basicSet, clear, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doMove, doRemove, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.DelegatingEList">Methods inherited from class org.eclipse.emf.common.util.DelegatingEList</h3>
<code>doClear, equals, get, hashCode, isEmpty, primitiveGet, remove, retainAll, size, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEList">Methods inherited from class org.eclipse.emf.common.util.AbstractEList</h3>
<code>add, addAll, addAll, didAdd, didClear, didMove, didRemove, didSet, equalObjects, getDuplicates, getNonDuplicates, iterator, listIterator, listIterator, move, set</code></div>
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
<code>addAllUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicList, basicListIterator, basicListIterator, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#set(int,E)" title="class or interface in java.util">set</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#size()" title="class or interface in java.util">size</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
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
<h3>ModelEStoreEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModelEStoreEList</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature eStructuralFeature)</span></div>
<div class="block">Creates and initializes a new <code>ModelEStoreEList</code> instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - owner of the collection.</dd>
<dd><code>eStructuralFeature</code> - feature that values is hold by this collection.</dd>
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
<section class="detail" id="getPropertyEventName(java.lang.Object)">
<h3>getPropertyEventName</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyEventName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Returns name of the property change event.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getPropertyEventName</code> in class <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - property that changed value.</dd>
<dt>Returns:</dt>
<dd>property name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="beforeChange()">
<h3>beforeChange</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">beforeChange</span>()</div>
<div class="block">The method will be invoked before specified property change.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../emf/impl/BasicEStoreEList.html#beforeChange()">beforeChange</a></code> in class <code><a href="../../emf/impl/BasicEStoreEList.html" title="class in com.nomagic.magicdraw.emf.impl">BasicEStoreEList</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterChange()">
<h3>afterChange</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">afterChange</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.dassault_systemes.modeler.foundation.emf.impl.AbstractEStoreEList</code></span></div>
<div class="block">The method will be invoked after specified property.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../emf/impl/BasicEStoreEList.html#afterChange()">afterChange</a></code> in class <code><a href="../../emf/impl/BasicEStoreEList.html" title="class in com.nomagic.magicdraw.emf.impl">BasicEStoreEList</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index)</span></div>
<div class="block">Implementation must fire property change event.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../emf/impl/BasicEStoreEList.html#firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int)">firePropertyChange</a></code> in class <code><a href="../../emf/impl/BasicEStoreEList.html" title="class in com.nomagic.magicdraw.emf.impl">BasicEStoreEList</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>propertyName</code> - name of the changed property.</dd>
<dd><code>oldValue</code> - old value of the property.</dd>
<dd><code>newValue</code> - new value of the property.</dd>
<dd><code>index</code> - index of the new value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="firePropertyChange(java.lang.String,java.lang.Object,java.lang.Object,int,int)">
<h3>firePropertyChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">firePropertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> oldValue,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> newValue,
 int index,
 int newIndex)</span></div>
<div class="block">Implementation must fire property change event.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - name of the changed property.</dd>
<dd><code>oldValue</code> - old value of the property.</dd>
<dd><code>newValue</code> - new value of the property.</dd>
<dd><code>index</code> - index of the new value.</dd>
<dd><code>newIndex</code> - new index of the value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(int,E)">
<h3 id="add(int,java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</span></div>
<div class="block">Adds the object at the given index in the list.
 If <code>uniqueness</code> is required,
 duplicates will be ignored.
 This implementation delegates to <a href="#addUnique(int,E)"><code>addUnique(int, E)</code></a>
 after uniqueness checking.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(int,E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>add</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - the object to be added.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if <code>uniqueness</code> is required,
                                  and the object is a duplicate.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#addUnique(int,E)"><code>addUnique(int, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="validate(int,E)">
<h3 id="validate(int,java.lang.Object)">validate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></span> <span class="element-name">validate</span><wbr/><span class="parameters">(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</span></div>
<div class="block">Validates a new content object and returns the validated object.
 This implementation checks for null, if <code>necessary</code> and returns the argument object.
 Clients may throw additional types of runtime exceptions
 in order to handle constraint violations.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>validate</code> in class <code>org.eclipse.emf.ecore.util.DelegatingEcoreEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - the position of the new content.</dd>
<dd><code>object</code> - the new content.</dd>
<dt>Returns:</dt>
<dd>the validated content.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if a constraint prevents the object from being added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addUnique(E)">
<h3 id="addUnique(java.lang.Object)">addUnique</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addUnique</span><wbr/><span class="parameters">(<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</span></div>
<div class="block">Adds the object at the end of the list;
 it does no uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>
 and delegates to <code>inverseAdd</code> as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addUnique</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>addUnique</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - the object to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
<li><code>DelegatingEcoreEList.Generic.hasInverse()</code></li>
<li><code>DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addUnique(int,E)">
<h3 id="addUnique(int,java.lang.Object)">addUnique</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addUnique</span><wbr/><span class="parameters">(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</span></div>
<div class="block">Adds the object at the given index in the list;
 it does no ranging checking or uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>
 and delegates to <code>inverseAdd</code> as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addUnique</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>addUnique</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - the object to be added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
<li><code>DelegatingEcoreEList.Generic.hasInverse()</code></li>
<li><code>DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUnique(int,E)">
<h3 id="setUnique(int,java.lang.Object)">setUnique</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></span> <span class="element-name">setUnique</span><wbr/><span class="parameters">(int index,
 <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a> object)</span></div>
<div class="block">Sets the object at the index
 and returns the old object at the index;
 it does no ranging checking or uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>
 and delegates to <code>inverseAdd</code> and <code>inverseRemove</code> as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setUnique</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>setUnique</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - the position in question.</dd>
<dd><code>object</code> - the object to set.</dd>
<dt>Returns:</dt>
<dd>the old object at the index.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
<li><code>DelegatingEcoreEList.Generic.hasInverse()</code></li>
<li><code>DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
<li><code>DelegatingEcoreEList.inverseRemove(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="move(int,int)">
<h3>move</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></span> <span class="element-name">move</span><wbr/><span class="parameters">(int targetIndex,
 int sourceIndex)</span></div>
<div class="block">Moves the object at the source index of the list to the target index of the list
 and returns the moved object.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>move</code> in interface <code>org.eclipse.emf.common.util.EList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>move</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>targetIndex</code> - the new position for the object in the list.</dd>
<dd><code>sourceIndex</code> - the old position of the object in the list.</dd>
<dt>Returns:</dt>
<dd>the moved object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></code> - if either index isn't within the size range.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAllUnique(int,java.util.Collection)">
<h3>addAllUnique</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addAllUnique</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt; collection)</span></div>
<div class="block">Adds each object of the collection at each successive index in the list
 and returns whether any objects were added;
 it does no ranging checking or uniqueness checking.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>
 and delegates to <code>inverseAdd</code> as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>addAllUnique</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>addAllUnique</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - the index at which to add.</dd>
<dd><code>collection</code> - the collection of objects to be added.</dd>
<dt>Returns:</dt>
<dd>whether any objects were added.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
<li><code>DelegatingEcoreEList.Generic.hasInverse()</code></li>
<li><code>DelegatingEcoreEList.inverseAdd(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(int)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a></span> <span class="element-name">remove</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block">Removes the object at the index from the list and returns it.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>
 and delegates to <code>inverseRemove</code> as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(int)" title="class or interface in java.util">remove</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>remove</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>index</code> - the position of the object to remove.</dd>
<dt>Returns:</dt>
<dd>the removed object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></code> - if the index isn't within the size range.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
<li><code>DelegatingEcoreEList.Generic.hasInverse()</code></li>
<li><code>DelegatingEcoreEList.inverseRemove(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeAll(java.util.Collection)">
<h3>removeAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection)</span></div>
<div class="block">Removes each object of the collection from the list and returns whether any object was actually contained by the list.
 In addition to the normal effects,
 this override implementation generates notifications as <code>required</code>
 and delegates to <code>inverseRemove</code> as <code>required</code>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>removeAll</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>collection</code> - the collection of objects to be removed.</dd>
<dt>Returns:</dt>
<dd>whether any object was actually contained by the list.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><code>DelegatingEcoreEList.isNotificationRequired()</code></li>
<li><code>DelegatingEcoreEList.Generic.hasInverse()</code></li>
<li><code>DelegatingEcoreEList.inverseRemove(E, org.eclipse.emf.common.notify.NotificationChain)</code></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="indexOf(java.lang.Object)">
<h3>indexOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">indexOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#indexOf(java.lang.Object)" title="class or interface in java.util">indexOf</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>indexOf</code> in class <code>org.eclipse.emf.ecore.util.DelegatingEcoreEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lastIndexOf(java.lang.Object)">
<h3>lastIndexOf</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">lastIndexOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#lastIndexOf(java.lang.Object)" title="class or interface in java.util">lastIndexOf</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>lastIndexOf</code> in class <code>org.eclipse.emf.ecore.util.DelegatingEcoreEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasProxies()">
<h3>hasProxies</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasProxies</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>hasProxies</code> in class <code>org.eclipse.emf.ecore.util.DelegatingEcoreEList.Generic&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="basicRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">
<h3>basicRemove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.NotificationChain</span> <span class="element-name">basicRemove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>basicRemove</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>basicRemove</code> in class <code>org.eclipse.emf.common.notify.impl.DelegatingNotifyingListImpl&lt;<a href="ModelEStoreEList.html" title="type parameter in ModelEStoreEList">E</a>&gt;</code></dd>
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
