# JAVA OPENAPI: RedefiningEObjectEList (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml2/util/RedefiningEObjectEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/RedefiningEObjectEList.html`
- source_sha256: `f8336e223dafd0b7c2f206201a67a30554ca7a96a7b87adc3193eb7fc7ab8f36`
- captured_utc: `2026-07-14T16:46:09.595928+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class RedefiningEObjectEList<E>

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<E>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<E>
[java.util.AbstractSequentialList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html)<E>
org.eclipse.emf.ecore.util.AbstractSequentialInternalEList<E>
org.eclipse.uml2.common.util.DerivedEObjectEList<E>
org.eclipse.uml2.common.util.DerivedSubsetEObjectEList<E>
com.nomagic.magicdraw.uml2.util.RedefiningEObjectEList<E>

All Implemented Interfaces:
`[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<E>`, `[SequencedCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html)<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

public classRedefiningEObjectEList<E>
extends org.eclipse.uml2.common.util.DerivedSubsetEObjectEList<E>

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`protected class`
`[RedefiningEObjectEList.RedefiningEObjectListIterator](RedefiningEObjectEList.RedefiningEObjectListIterator.html)`

`protected class`
`[RedefiningEObjectEList.ResolvingRedefiningEObjectListIterator](RedefiningEObjectEList.ResolvingRedefiningEObjectListIterator.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList
`dataClass, featureID, owner, sourceFeatureIDs`
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[RedefiningEObjectEList](#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int sourceFeatureID)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[add](#add(E))([E](RedefiningEObjectEList.html) e)`
Appends the specified element to the start of this list (optional
 operation).
`boolean`
`[addAll](#addAll(int,java.util.Collection))(int index,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [E](RedefiningEObjectEList.html)> collection)`

`boolean`
`[addAll](#addAll(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [E](RedefiningEObjectEList.html)> collection)`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[E](RedefiningEObjectEList.html)>`
`[basicList](#basicList())()`

`int`
`[getFeatureID](#getFeatureID())()`

`protected org.eclipse.emf.ecore.EClassifier`
`[getFeatureType](#getFeatureType())()`

`protected org.eclipse.emf.ecore.EReference`
`[getInverseEReference](#getInverseEReference())()`

`protected [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?>`
`[getInverseFeatureClass](#getInverseFeatureClass())()`

`protected int`
`[getInverseFeatureID](#getInverseFeatureID())()`

`protected boolean`
`[hasInstanceClass](#hasInstanceClass())()`

`protected boolean`
`[hasNavigableInverse](#hasNavigableInverse())()`

`org.eclipse.emf.common.notify.NotificationChain`
`[inverseAdd](#inverseAdd(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)`

`org.eclipse.emf.common.notify.NotificationChain`
`[inverseRemove](#inverseRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)`

`protected boolean`
`[isContainment](#isContainment())()`

`protected [ListIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html)<[E](RedefiningEObjectEList.html)>`
`[listIterator](#listIterator(int,boolean))(int index,
 boolean resolve)`

`[E](RedefiningEObjectEList.html)`
`[move](#move(int,int))(int newPosition,
 int oldPosition)`
Moves the object from the old position to the new position.
`void`
`[move](#move(int,E))(int newPosition,
 [E](RedefiningEObjectEList.html) object)`
Moves the object to the new position, if is in the list.
`protected [ListIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html)<[E](RedefiningEObjectEList.html)>`
`[newListIterator](#newListIterator())()`

`protected [ListIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html)<[E](RedefiningEObjectEList.html)>`
`[newResolvingListIterator](#newResolvingListIterator())()`
Methods inherited from class org.eclipse.uml2.common.util.DerivedSubsetEObjectEList
`isNotificationRequired, newEmptyListIterator`
Methods inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList
`add, addAllUnique, addUnique, basicListIterator, contains, createNotification, derive, dispatchNotification, doAddAllUnique, get, getEObject, getEStructuralFeature, getEStructuralFeature, isEmpty, isIncluded, isIncluded, isSet, listIterator, remove, set, set, setUnique, size, unset, validate`
Methods inherited from class org.eclipse.emf.ecore.util.AbstractSequentialInternalEList
`addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray`
Methods inherited from class java.util.[AbstractSequentialList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html)
`[get](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html#get(int)), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html#iterator())`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[clear](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#clear()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#hashCode()), [indexOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#indexOf(java.lang.Object)), [lastIndexOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#lastIndexOf(java.lang.Object)), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#listIterator()), [removeRange](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.util.[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)
`[containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#remove(java.lang.Object)), [removeAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#removeAll(java.util.Collection)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#retainAll(java.util.Collection)), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray(T%5B%5D)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList
`addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)
`[addFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)), [addLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)), [clear](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#clear()), [containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [get](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#get(int)), [getFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()), [getLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()), [indexOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#indexOf(java.lang.Object)), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()), [lastIndexOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#lastIndexOf(java.lang.Object)), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [removeAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)), [removeFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()), [removeLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()), [replaceAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()), [sort](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int)), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray(T%5B%5D))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
RedefiningEObjectEList
public RedefiningEObjectEList([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int sourceFeatureID)
 ============ METHOD DETAIL ========== 
Method Details
move
public [E](RedefiningEObjectEList.html) move(int newPosition,
 int oldPosition)
Moves the object from the old position to the new position.
Specified by:
`move` in interface `org.eclipse.emf.common.util.EList<[E](RedefiningEObjectEList.html)>`
Overrides:
`move` in class `org.eclipse.emf.ecore.util.AbstractSequentialInternalEList<[E](RedefiningEObjectEList.html)>`
Parameters:
`newPosition` - the position of the object after the move.
`oldPosition` - the position of the object before the move.
Returns:
the moved object.
add
public boolean add([E](RedefiningEObjectEList.html) e)
Appends the specified element to the start of this list (optional
 operation).
 
Lists that support this operation may place limitations on what
 elements may be added to this list. In particular, some
 lists will refuse to add null elements, and others will impose
 restrictions on the type of elements that may be added. List
 classes should clearly specify in their documentation any restrictions
 on what elements may be added.
 
This implementation calls `add(0, e)`.
 
Note that this implementation throws an
 `UnsupportedOperationException` unless
 `add(int, E)` is overridden.
Specified by:
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#add(E))` in interface `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[E](RedefiningEObjectEList.html)>`
Specified by:
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E))` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[E](RedefiningEObjectEList.html)>`
Overrides:
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#add(E))` in class `[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<[E](RedefiningEObjectEList.html)>`
Parameters:
`e` - element to be appended to this list
Returns:
`true` (as specified by [`Collection.add(E)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#add(E)))
Throws:
`[UnsupportedOperationException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/UnsupportedOperationException.html)` - if the `add` operation
 is not supported by this list
`[ClassCastException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassCastException.html)` - if the class of the specified element
 prevents it from being added to this list
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the specified element is null and this
 list does not permit null elements
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if some property of this element
 prevents it from being added to this list
move
public void move(int newPosition,
 [E](RedefiningEObjectEList.html) object)
Moves the object to the new position, if is in the list.
Specified by:
`move` in interface `org.eclipse.emf.common.util.EList<[E](RedefiningEObjectEList.html)>`
Overrides:
`move` in class `org.eclipse.emf.ecore.util.AbstractSequentialInternalEList<[E](RedefiningEObjectEList.html)>`
Parameters:
`newPosition` - the position of the object after the move.
`object` - the object to move.
addAll
public boolean addAll([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [E](RedefiningEObjectEList.html)> collection)
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#addAll(java.util.Collection))` in interface `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[E](RedefiningEObjectEList.html)>`
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection))` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[E](RedefiningEObjectEList.html)>`
Overrides:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#addAll(java.util.Collection))` in class `[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<[E](RedefiningEObjectEList.html)>`
addAll
public boolean addAll(int index,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [E](RedefiningEObjectEList.html)> collection)
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection))` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[E](RedefiningEObjectEList.html)>`
Overrides:
`addAll` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](RedefiningEObjectEList.html)>`
hasNavigableInverse
protected boolean hasNavigableInverse()
hasInstanceClass
protected boolean hasInstanceClass()
getFeatureType
protected org.eclipse.emf.ecore.EClassifier getFeatureType()
getInverseEReference
protected org.eclipse.emf.ecore.EReference getInverseEReference()
getInverseFeatureID
protected int getInverseFeatureID()
getInverseFeatureClass
protected [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> getInverseFeatureClass()
getFeatureID
public int getFeatureID()
inverseAdd
public org.eclipse.emf.common.notify.NotificationChain inverseAdd([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)
inverseRemove
public org.eclipse.emf.common.notify.NotificationChain inverseRemove([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 org.eclipse.emf.common.notify.NotificationChain notifications)
isContainment
protected boolean isContainment()
newListIterator
protected [ListIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html)<[E](RedefiningEObjectEList.html)> newListIterator()
Overrides:
`newListIterator` in class `org.eclipse.uml2.common.util.DerivedSubsetEObjectEList<[E](RedefiningEObjectEList.html)>`
newResolvingListIterator
protected [ListIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html)<[E](RedefiningEObjectEList.html)> newResolvingListIterator()
Overrides:
`newResolvingListIterator` in class `org.eclipse.uml2.common.util.DerivedSubsetEObjectEList<[E](RedefiningEObjectEList.html)>`
basicList
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[E](RedefiningEObjectEList.html)> basicList()
Specified by:
`basicList` in interface `org.eclipse.emf.ecore.util.InternalEList<[E](RedefiningEObjectEList.html)>`
Overrides:
`basicList` in class `org.eclipse.uml2.common.util.DerivedSubsetEObjectEList<[E](RedefiningEObjectEList.html)>`
listIterator
protected [ListIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html)<[E](RedefiningEObjectEList.html)> listIterator(int index,
 boolean resolve)
Overrides:
`listIterator` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](RedefiningEObjectEList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class RedefiningEObjectEList">Class RedefiningEObjectEList&lt;E&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html" title="class or interface in java.util">java.util.AbstractSequentialList</a>&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.AbstractSequentialInternalEList&lt;E&gt;
<div class="inheritance">org.eclipse.uml2.common.util.DerivedEObjectEList&lt;E&gt;
<div class="inheritance">org.eclipse.uml2.common.util.DerivedSubsetEObjectEList&lt;E&gt;
<div class="inheritance">com.nomagic.magicdraw.uml2.util.RedefiningEObjectEList&lt;E&gt;</div>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html" title="class or interface in java.util">SequencedCollection</a>&lt;E&gt;</code>, <code>org.eclipse.emf.common.util.EList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.EStructuralFeature.Setting</code>, <code>org.eclipse.emf.ecore.util.InternalEList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.util.InternalEList.Unsettable&lt;E&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">RedefiningEObjectEList&lt;E&gt;</span>
<span class="extends-implements">extends org.eclipse.uml2.common.util.DerivedSubsetEObjectEList&lt;E&gt;</span></div>
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
<div class="col-first even-row-color"><code>protected class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="RedefiningEObjectEList.RedefiningEObjectListIterator.html" title="class in com.nomagic.magicdraw.uml2.util">RedefiningEObjectEList.RedefiningEObjectListIterator</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="RedefiningEObjectEList.ResolvingRedefiningEObjectListIterator.html" title="class in com.nomagic.magicdraw.uml2.util">RedefiningEObjectEList.ResolvingRedefiningEObjectListIterator</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.uml2.common.util.DerivedEObjectEList">Fields inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList</h3>
<code>dataClass, featureID, owner, sourceFeatureIDs</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int)">RedefiningEObjectEList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int sourceFeatureID)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(E)">add</a><wbr/>(<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends the specified element to the start of this list (optional
 operation).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAll(int,java.util.Collection)">addAll</a><wbr/>(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt; collection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAll(java.util.Collection)">addAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt; collection)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#basicList()">basicList</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureID()">getFeatureID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected org.eclipse.emf.ecore.EClassifier</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFeatureType()">getFeatureType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected org.eclipse.emf.ecore.EReference</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInverseEReference()">getInverseEReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInverseFeatureClass()">getInverseFeatureClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInverseFeatureID()">getInverseFeatureID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasInstanceClass()">hasInstanceClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasNavigableInverse()">hasNavigableInverse</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.NotificationChain</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#inverseAdd(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">inverseAdd</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.emf.common.notify.NotificationChain</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#inverseRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">inverseRemove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isContainment()">isContainment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a><wbr/>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listIterator(int,boolean)">listIterator</a><wbr/>(int index,
 boolean resolve)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#move(int,int)">move</a><wbr/>(int newPosition,
 int oldPosition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves the object from the old position to the new position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#move(int,E)">move</a><wbr/>(int newPosition,
 <a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Moves the object to the new position, if is in the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a><wbr/>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#newListIterator()">newListIterator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a><wbr/>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#newResolvingListIterator()">newResolvingListIterator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.uml2.common.util.DerivedSubsetEObjectEList">Methods inherited from class org.eclipse.uml2.common.util.DerivedSubsetEObjectEList</h3>
<code>isNotificationRequired, newEmptyListIterator</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.uml2.common.util.DerivedEObjectEList">Methods inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList</h3>
<code>add, addAllUnique, addUnique, basicListIterator, contains, createNotification, derive, dispatchNotification, doAddAllUnique, get, getEObject, getEStructuralFeature, getEStructuralFeature, isEmpty, isIncluded, isIncluded, isSet, listIterator, remove, set, set, setUnique, size, unset, validate</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.AbstractSequentialInternalEList">Methods inherited from class org.eclipse.emf.ecore.util.AbstractSequentialInternalEList</h3>
<code>addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractSequentialList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html" title="class or interface in java.util">AbstractSequentialList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractSequentialList.html#iterator()" title="class or interface in java.util">iterator</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#indexOf(java.lang.Object)" title="class or interface in java.util">indexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#lastIndexOf(java.lang.Object)" title="class or interface in java.util">lastIndexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractCollection">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray()" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray(T%5B%5D)" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toString()" title="class or interface in java.util">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.InternalEList">Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList</h3>
<code>addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)" title="class or interface in java.util">addFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)" title="class or interface in java.util">addLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()" title="class or interface in java.util">getFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()" title="class or interface in java.util">getLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#indexOf(java.lang.Object)" title="class or interface in java.util">indexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#lastIndexOf(java.lang.Object)" title="class or interface in java.util">lastIndexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()" title="class or interface in java.util">removeFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()" title="class or interface in java.util">removeLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray()" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray(T%5B%5D)" title="class or interface in java.util">toArray</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int)">
<h3>RedefiningEObjectEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RedefiningEObjectEList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int sourceFeatureID)</span></div>
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
<section class="detail" id="move(int,int)">
<h3>move</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a></span> <span class="element-name">move</span><wbr/><span class="parameters">(int newPosition,
 int oldPosition)</span></div>
<div class="block">Moves the object from the old position to the new position.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>move</code> in interface <code>org.eclipse.emf.common.util.EList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>move</code> in class <code>org.eclipse.emf.ecore.util.AbstractSequentialInternalEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>newPosition</code> - the position of the object after the move.</dd>
<dd><code>oldPosition</code> - the position of the object before the move.</dd>
<dt>Returns:</dt>
<dd>the moved object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(E)">
<h3 id="add(java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a> e)</span></div>
<div class="block">Appends the specified element to the start of this list (optional
 operation).
 <p></p>
<p>Lists that support this operation may place limitations on what
 elements may be added to this list.  In particular, some
 lists will refuse to add null elements, and others will impose
 restrictions on the type of elements that may be added.  List
 classes should clearly specify in their documentation any restrictions
 on what elements may be added.
 <p></p>
<p>This implementation calls <code>add(0, e)</code>.
 <p></p>
<p>Note that this implementation throws an
 <code>UnsupportedOperationException</code> unless
 <code>add(int, E)</code> is overridden.</p></p></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#add(E)" title="class or interface in java.util">add</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - element to be appended to this list</dd>
<dt>Returns:</dt>
<dd><code>true</code> (as specified by <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util"><code>Collection.add(E)</code></a>)</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/UnsupportedOperationException.html" title="class or interface in java.lang">UnsupportedOperationException</a></code> - if the <code>add</code> operation
                                       is not supported by this list</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassCastException.html" title="class or interface in java.lang">ClassCastException</a></code> - if the class of the specified element
                                       prevents it from being added to this list</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the specified element is null and this
                                       list does not permit null elements</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if some property of this element
                                       prevents it from being added to this list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="move(int,E)">
<h3 id="move(int,java.lang.Object)">move</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">move</span><wbr/><span class="parameters">(int newPosition,
 <a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a> object)</span></div>
<div class="block">Moves the object to the new position, if is in the list.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>move</code> in interface <code>org.eclipse.emf.common.util.EList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>move</code> in class <code>org.eclipse.emf.ecore.util.AbstractSequentialInternalEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>newPosition</code> - the position of the object after the move.</dd>
<dd><code>object</code> - the object to move.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAll(java.util.Collection)">
<h3>addAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt; collection)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAll(int,java.util.Collection)">
<h3>addAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addAll</span><wbr/><span class="parameters">(int index,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt; collection)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>addAll</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNavigableInverse()">
<h3>hasNavigableInverse</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasNavigableInverse</span>()</div>
</section>
</li>
<li>
<section class="detail" id="hasInstanceClass()">
<h3>hasInstanceClass</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasInstanceClass</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getFeatureType()">
<h3>getFeatureType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">org.eclipse.emf.ecore.EClassifier</span> <span class="element-name">getFeatureType</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInverseEReference()">
<h3>getInverseEReference</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">org.eclipse.emf.ecore.EReference</span> <span class="element-name">getInverseEReference</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInverseFeatureID()">
<h3>getInverseFeatureID</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getInverseFeatureID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getInverseFeatureClass()">
<h3>getInverseFeatureClass</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">getInverseFeatureClass</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getFeatureID()">
<h3>getFeatureID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getFeatureID</span>()</div>
</section>
</li>
<li>
<section class="detail" id="inverseAdd(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">
<h3>inverseAdd</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.NotificationChain</span> <span class="element-name">inverseAdd</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</span></div>
</section>
</li>
<li>
<section class="detail" id="inverseRemove(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">
<h3>inverseRemove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.emf.common.notify.NotificationChain</span> <span class="element-name">inverseRemove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 org.eclipse.emf.common.notify.NotificationChain notifications)</span></div>
</section>
</li>
<li>
<section class="detail" id="isContainment()">
<h3>isContainment</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isContainment</span>()</div>
</section>
</li>
<li>
<section class="detail" id="newListIterator()">
<h3>newListIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</span> <span class="element-name">newListIterator</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>newListIterator</code> in class <code>org.eclipse.uml2.common.util.DerivedSubsetEObjectEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="newResolvingListIterator()">
<h3>newResolvingListIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</span> <span class="element-name">newResolvingListIterator</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>newResolvingListIterator</code> in class <code>org.eclipse.uml2.common.util.DerivedSubsetEObjectEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="basicList()">
<h3>basicList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</span> <span class="element-name">basicList</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>basicList</code> in interface <code>org.eclipse.emf.ecore.util.InternalEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>basicList</code> in class <code>org.eclipse.uml2.common.util.DerivedSubsetEObjectEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listIterator(int,boolean)">
<h3>listIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</span> <span class="element-name">listIterator</span><wbr/><span class="parameters">(int index,
 boolean resolve)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>listIterator</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="RedefiningEObjectEList.html" title="type parameter in RedefiningEObjectEList">E</a>&gt;</code></dd>
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
