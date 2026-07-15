# JAVA OPENAPI: ModifiableDerivedUnionEObjectEList (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml2/util/ModifiableDerivedUnionEObjectEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/ModifiableDerivedUnionEObjectEList.html`
- source_sha256: `9d6ef3e19f8d28fdd9389b922c4c76025d6f443e81eca5caa871d6c17dc6b146`
- captured_utc: `2026-07-14T16:52:16.833944+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class ModifiableDerivedUnionEObjectEList<E>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html)<E>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)<E>
[java.util.AbstractSequentialList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html)<E>
org.eclipse.emf.ecore.util.AbstractSequentialInternalEList<E>
org.eclipse.uml2.common.util.DerivedEObjectEList<E>
org.eclipse.uml2.common.util.DerivedUnionEObjectEList<E>
com.nomagic.magicdraw.uml2.util.ModifiableDerivedUnionEObjectEList<E>

All Implemented Interfaces:
`[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

public classModifiableDerivedUnionEObjectEList<E>
extends org.eclipse.uml2.common.util.DerivedUnionEObjectEList<E>

A derived list representing a union of all the elements from its source
 features. This list is ideal for implementing derived union features.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`class`
`[ModifiableDerivedUnionEObjectEList.DerivedUnionIterator](ModifiableDerivedUnionEObjectEList.DerivedUnionIterator.html)`
Non resolving `DerivedUnionEObjectEStoreEList` iterator.
`class`
`[ModifiableDerivedUnionEObjectEList.DerivedUnionResolvingIterator](ModifiableDerivedUnionEObjectEList.DerivedUnionResolvingIterator.html)`
Resolving `DerivedUnionEObjectEStoreEList` iterator.
`class`
`[ModifiableDerivedUnionEObjectEList.EmptyDerivedUnionListIterator](ModifiableDerivedUnionEObjectEList.EmptyDerivedUnionListIterator.html)`
Empty `DerivedUnionEObjectEStoreEList` iterator.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList
`dataClass, featureID, owner, sourceFeatureIDs`
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ModifiableDerivedUnionEObjectEList](#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] sourceFeatureIDs)`
Creates and initializes a new `DerivedUnionEObjectEStoreEList` from specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[add](#add(E))([E](ModifiableDerivedUnionEObjectEList.html) e)`
Appends the specified element to the end of this list (optional
 operation).
`boolean`
`[contains](#contains(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`
The method is copied from supper and fixed casting to Collection instead of List.
`boolean`
`[isEmpty](#isEmpty())()`

`[E](ModifiableDerivedUnionEObjectEList.html)`
`[move](#move(int,int))(int newPosition,
 int oldPosition)`
Move is not supported however the method returns value at old index.
`void`
`[move](#move(int,E))(int newPosition,
 [E](ModifiableDerivedUnionEObjectEList.html) object)`
Does nothing.
`protected [ListIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
`[newEmptyListIterator](#newEmptyListIterator())()`

`protected [ListIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
`[newListIterator](#newListIterator())()`

`protected [ListIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
`[newResolvingListIterator](#newResolvingListIterator())()`

`boolean`
`[remove](#remove(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
`[snapshot](#snapshot())()`
Methods inherited from class org.eclipse.uml2.common.util.DerivedUnionEObjectEList
`basicList, isIncluded`
Methods inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList
`add, addAll, addAllUnique, addUnique, basicListIterator, createNotification, derive, dispatchNotification, doAddAllUnique, get, getEObject, getEStructuralFeature, getEStructuralFeature, isIncluded, isNotificationRequired, isSet, listIterator, listIterator, remove, set, set, setUnique, size, unset, validate`
Methods inherited from class org.eclipse.emf.ecore.util.AbstractSequentialInternalEList
`addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray`
Methods inherited from class java.util.[AbstractSequentialList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html)
`[get](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html#get(int)), [iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html#iterator())`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[clear](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#clear()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#hashCode()), [indexOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#indexOf(java.lang.Object)), [lastIndexOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#lastIndexOf(java.lang.Object)), [listIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#listIterator()), [removeRange](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.util.[AbstractCollection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html)
`[addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#addAll(java.util.Collection)), [containsAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)), [removeAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#removeAll(java.util.Collection)), [retainAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#retainAll(java.util.Collection)), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#toArray()), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#toArray(T%5B%5D)), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList
`addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)
`[addAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)), [clear](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#clear()), [containsAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [get](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#get(int)), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#hashCode()), [indexOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#indexOf(java.lang.Object)), [iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#iterator()), [lastIndexOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#lastIndexOf(java.lang.Object)), [listIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator()), [removeAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)), [replaceAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [sort](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int)), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#toArray()), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#toArray(T%5B%5D))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModifiableDerivedUnionEObjectEList
public ModifiableDerivedUnionEObjectEList([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] sourceFeatureIDs)
Creates and initializes a new `DerivedUnionEObjectEStoreEList` from specified parameters.
Parameters:
`dataClass` - class of objects which will be stored in the collection.
`owner` - owner of the collection.
`featureID` - feature which value this list represents ID.
`sourceFeatureIDs` - identifiers of features that compose values of this list.
 ============ METHOD DETAIL ========== 
Method Details
add
public boolean add([E](ModifiableDerivedUnionEObjectEList.html) e)
Appends the specified element to the end of this list (optional
 operation).
 
Lists that support this operation may place limitations on what
 elements may be added to this list. In particular, some
 lists will refuse to add null elements, and others will impose
 restrictions on the type of elements that may be added. List
 classes should clearly specify in their documentation any restrictions
 on what elements may be added.
 
This implementation calls `add(size(), e)`.
 
Note that this implementation throws an
 `UnsupportedOperationException` unless
 `add(int, E)` is overridden.
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Overrides:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#add(E))` in class `[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Parameters:
`e` - element to be appended to this list
Returns:
`true` (as specified by [`Collection.add(E)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)))
Throws:
`[UnsupportedOperationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html)` - if the `add` operation
 is not supported by this list
`[ClassCastException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassCastException.html)` - if the class of the specified element
 prevents it from being added to this list
`[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html)` - if the specified element is null and this
 list does not permit null elements
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if some property of this element
 prevents it from being added to this list
move
public [E](ModifiableDerivedUnionEObjectEList.html) move(int newPosition,
 int oldPosition)
Move is not supported however the method returns value at old index.
Specified by:
`move` in interface `org.eclipse.emf.common.util.EList<[E](ModifiableDerivedUnionEObjectEList.html)>`
Overrides:
`move` in class `org.eclipse.emf.ecore.util.AbstractSequentialInternalEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
Parameters:
`newPosition` - new position.
`oldPosition` - old position.
Returns:
value at old position.
move
public void move(int newPosition,
 [E](ModifiableDerivedUnionEObjectEList.html) object)
Does nothing. Move is not supported.
Specified by:
`move` in interface `org.eclipse.emf.common.util.EList<[E](ModifiableDerivedUnionEObjectEList.html)>`
Overrides:
`move` in class `org.eclipse.emf.ecore.util.AbstractSequentialInternalEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
Parameters:
`newPosition` - new position.
`object` - an object to move.
remove
public boolean remove([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#remove(java.lang.Object))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(java.lang.Object))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Overrides:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#remove(java.lang.Object))` in class `[AbstractCollection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
contains
public boolean contains([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
The method is copied from supper and fixed casting to Collection instead of List.
Specified by:
`[contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#contains(java.lang.Object))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Specified by:
`[contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#contains(java.lang.Object))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Overrides:
`contains` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
Parameters:
`object` - an object.
Returns:
true if the collection contains the object, otherwise - false.
newListIterator
protected [ListIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html)<[E](ModifiableDerivedUnionEObjectEList.html)> newListIterator()
Overrides:
`newListIterator` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
newResolvingListIterator
protected [ListIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html)<[E](ModifiableDerivedUnionEObjectEList.html)> newResolvingListIterator()
Overrides:
`newResolvingListIterator` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
newEmptyListIterator
protected [ListIterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html)<[E](ModifiableDerivedUnionEObjectEList.html)> newEmptyListIterator()
Overrides:
`newEmptyListIterator` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
isEmpty
public boolean isEmpty()
Specified by:
`[isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#isEmpty())` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Specified by:
`[isEmpty](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#isEmpty())` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModifiableDerivedUnionEObjectEList.html)>`
Overrides:
`isEmpty` in class `org.eclipse.uml2.common.util.DerivedEObjectEList<[E](ModifiableDerivedUnionEObjectEList.html)>`
snapshot
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[E](ModifiableDerivedUnionEObjectEList.html)> snapshot()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class ModifiableDerivedUnionEObjectEList">Class ModifiableDerivedUnionEObjectEList&lt;E&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html" title="class or interface in java.util">java.util.AbstractSequentialList</a>&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.AbstractSequentialInternalEList&lt;E&gt;
<div class="inheritance">org.eclipse.uml2.common.util.DerivedEObjectEList&lt;E&gt;
<div class="inheritance">org.eclipse.uml2.common.util.DerivedUnionEObjectEList&lt;E&gt;
<div class="inheritance">com.nomagic.magicdraw.uml2.util.ModifiableDerivedUnionEObjectEList&lt;E&gt;</div>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;E&gt;</code>, <code>org.eclipse.emf.common.util.EList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.EStructuralFeature.Setting</code>, <code>org.eclipse.emf.ecore.util.InternalEList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.util.InternalEList.Unsettable&lt;E&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ModifiableDerivedUnionEObjectEList&lt;E&gt;</span>
<span class="extends-implements">extends org.eclipse.uml2.common.util.DerivedUnionEObjectEList&lt;E&gt;</span></div>
<div class="block">A derived list representing a union of all the elements from its source
 features. This list is ideal for implementing derived union features.</div>
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
<div class="col-first even-row-color"><code>class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ModifiableDerivedUnionEObjectEList.DerivedUnionIterator.html" title="class in com.nomagic.magicdraw.uml2.util">ModifiableDerivedUnionEObjectEList.DerivedUnionIterator</a></code></div>
<div class="col-last even-row-color">
<div class="block">Non resolving <code>DerivedUnionEObjectEStoreEList</code> iterator.</div>
</div>
<div class="col-first odd-row-color"><code>class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ModifiableDerivedUnionEObjectEList.DerivedUnionResolvingIterator.html" title="class in com.nomagic.magicdraw.uml2.util">ModifiableDerivedUnionEObjectEList.DerivedUnionResolvingIterator</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Resolving <code>DerivedUnionEObjectEStoreEList</code> iterator.</div>
</div>
<div class="col-first even-row-color"><code>class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ModifiableDerivedUnionEObjectEList.EmptyDerivedUnionListIterator.html" title="class in com.nomagic.magicdraw.uml2.util">ModifiableDerivedUnionEObjectEList.EmptyDerivedUnionListIterator</a></code></div>
<div class="col-last even-row-color">
<div class="block">Empty <code>DerivedUnionEObjectEStoreEList</code> iterator.</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D)">ModifiableDerivedUnionEObjectEList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] sourceFeatureIDs)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>DerivedUnionEObjectEStoreEList</code> from specified parameters.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(E)">add</a><wbr/>(<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends the specified element to the end of this list (optional
 operation).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#contains(java.lang.Object)">contains</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The method is copied from supper and fixed casting to Collection instead of List.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty()">isEmpty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#move(int,int)">move</a><wbr/>(int newPosition,
 int oldPosition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Move is not supported however the method returns value at old index.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#move(int,E)">move</a><wbr/>(int newPosition,
 <a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Does nothing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#newEmptyListIterator()">newEmptyListIterator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#newListIterator()">newListIterator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#newResolvingListIterator()">newResolvingListIterator</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(java.lang.Object)">remove</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#snapshot()">snapshot</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.uml2.common.util.DerivedUnionEObjectEList">Methods inherited from class org.eclipse.uml2.common.util.DerivedUnionEObjectEList</h3>
<code>basicList, isIncluded</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.uml2.common.util.DerivedEObjectEList">Methods inherited from class org.eclipse.uml2.common.util.DerivedEObjectEList</h3>
<code>add, addAll, addAllUnique, addUnique, basicListIterator, createNotification, derive, dispatchNotification, doAddAllUnique, get, getEObject, getEStructuralFeature, getEStructuralFeature, isIncluded, isNotificationRequired, isSet, listIterator, listIterator, remove, set, set, setUnique, size, unset, validate</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.AbstractSequentialInternalEList">Methods inherited from class org.eclipse.emf.ecore.util.AbstractSequentialInternalEList</h3>
<code>addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractSequentialList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html" title="class or interface in java.util">AbstractSequentialList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractSequentialList.html#iterator()" title="class or interface in java.util">iterator</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#indexOf(java.lang.Object)" title="class or interface in java.util">indexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#lastIndexOf(java.lang.Object)" title="class or interface in java.util">lastIndexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractCollection">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#toArray()" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#toArray(T%5B%5D)" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#toString()" title="class or interface in java.util">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.InternalEList">Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList</h3>
<code>addAllUnique, addUnique, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicIterator, basicLastIndexOf, basicListIterator, basicRemove, basicToArray, basicToArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#get(int)" title="class or interface in java.util">get</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#indexOf(java.lang.Object)" title="class or interface in java.util">indexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#lastIndexOf(java.lang.Object)" title="class or interface in java.util">lastIndexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#toArray()" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#toArray(T%5B%5D)" title="class or interface in java.util">toArray</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int[])">
<h3>ModifiableDerivedUnionEObjectEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModifiableDerivedUnionEObjectEList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] sourceFeatureIDs)</span></div>
<div class="block">Creates and initializes a new <code>DerivedUnionEObjectEStoreEList</code> from specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataClass</code> - class of objects which will be stored in the collection.</dd>
<dd><code>owner</code> - owner of the collection.</dd>
<dd><code>featureID</code> - feature which value this list represents ID.</dd>
<dd><code>sourceFeatureIDs</code> - identifiers of features that compose values of this list.</dd>
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
<section class="detail" id="add(E)">
<h3 id="add(java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a> e)</span></div>
<div class="block">Appends the specified element to the end of this list (optional
 operation).
 <p></p>
<p>Lists that support this operation may place limitations on what
 elements may be added to this list.  In particular, some
 lists will refuse to add null elements, and others will impose
 restrictions on the type of elements that may be added.  List
 classes should clearly specify in their documentation any restrictions
 on what elements may be added.
 <p></p>
<p>This implementation calls <code>add(size(), e)</code>.
 <p></p>
<p>Note that this implementation throws an
 <code>UnsupportedOperationException</code> unless
 <code>add(int, E)</code> is overridden.</p></p></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#add(E)" title="class or interface in java.util">add</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>e</code> - element to be appended to this list</dd>
<dt>Returns:</dt>
<dd><code>true</code> (as specified by <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util"><code>Collection.add(E)</code></a>)</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html" title="class or interface in java.lang">UnsupportedOperationException</a></code> - if the <code>add</code> operation
                                       is not supported by this list</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassCastException.html" title="class or interface in java.lang">ClassCastException</a></code> - if the class of the specified element
                                       prevents it from being added to this list</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the specified element is null and this
                                       list does not permit null elements</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if some property of this element
                                       prevents it from being added to this list</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="move(int,int)">
<h3>move</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a></span> <span class="element-name">move</span><wbr/><span class="parameters">(int newPosition,
 int oldPosition)</span></div>
<div class="block">Move is not supported however the method returns value at old index.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>move</code> in interface <code>org.eclipse.emf.common.util.EList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>move</code> in class <code>org.eclipse.emf.ecore.util.AbstractSequentialInternalEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>newPosition</code> - new position.</dd>
<dd><code>oldPosition</code> - old position.</dd>
<dt>Returns:</dt>
<dd>value at old position.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="move(int,E)">
<h3 id="move(int,java.lang.Object)">move</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">move</span><wbr/><span class="parameters">(int newPosition,
 <a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a> object)</span></div>
<div class="block">Does nothing. Move is not supported.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>move</code> in interface <code>org.eclipse.emf.common.util.EList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>move</code> in class <code>org.eclipse.emf.ecore.util.AbstractSequentialInternalEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>newPosition</code> - new position.</dd>
<dd><code>object</code> - an object to move.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(java.lang.Object)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(java.lang.Object)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">The method is copied from supper and fixed casting to Collection instead of List.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>contains</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - an object.</dd>
<dt>Returns:</dt>
<dd>true if the collection contains the object, otherwise - false.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="newListIterator()">
<h3>newListIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</span> <span class="element-name">newListIterator</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>newListIterator</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="newResolvingListIterator()">
<h3>newResolvingListIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</span> <span class="element-name">newResolvingListIterator</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>newResolvingListIterator</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="newEmptyListIterator()">
<h3>newEmptyListIterator</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ListIterator.html" title="class or interface in java.util">ListIterator</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</span> <span class="element-name">newEmptyListIterator</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>newEmptyListIterator</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty()">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#isEmpty()" title="class or interface in java.util">isEmpty</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#isEmpty()" title="class or interface in java.util">isEmpty</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>isEmpty</code> in class <code>org.eclipse.uml2.common.util.DerivedEObjectEList&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="snapshot()">
<h3>snapshot</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="ModifiableDerivedUnionEObjectEList.html" title="type parameter in ModifiableDerivedUnionEObjectEList">E</a>&gt;</span> <span class="element-name">snapshot</span>()</div>
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
