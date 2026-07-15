# JAVA OPENAPI: SubsetSupersetEObjectWithInverseEList (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml2/util/SubsetSupersetEObjectWithInverseEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/SubsetSupersetEObjectWithInverseEList.html`
- source_sha256: `0ef90ce49e6480a5335bb49ec7e1e9a34024d3d1ca5439d214942cdbb6ec8a50`
- captured_utc: `2026-07-14T16:46:10.168937+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class SubsetSupersetEObjectWithInverseEList<E>

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<E>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<E>
org.eclipse.emf.common.util.AbstractEList<E>
org.eclipse.emf.common.util.BasicEList<E>
org.eclipse.emf.common.notify.impl.NotifyingListImpl<E>
org.eclipse.emf.ecore.util.NotifyingInternalEListImpl<E>
org.eclipse.emf.ecore.util.EcoreEList<E>
org.eclipse.emf.ecore.util.EObjectEList<E>
com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<E>
[com.nomagic.magicdraw.uml2.util.ModelEObjectEList](ModelEObjectEList.html)<E>
[com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEList](SubsetSupersetEObjectEList.html)<E>
com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectWithInverseEList<E>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<E>`, `[RandomAccess](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/RandomAccess.html)`, `[SequencedCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html)<E>`, `org.eclipse.emf.common.notify.NotifyingList<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

Direct Known Subclasses:
`[SubsetSupersetEObjectWithInverseEList.ManyInverse](SubsetSupersetEObjectWithInverseEList.ManyInverse.html)`, `[SubsetSupersetEObjectWithInverseEList.Unsettable](SubsetSupersetEObjectWithInverseEList.Unsettable.html)`, `[SubsetSupersetEObjectWithInverseResolvingEList](SubsetSupersetEObjectWithInverseResolvingEList.html)`

public classSubsetSupersetEObjectWithInverseEList<E>
extends [SubsetSupersetEObjectEList](SubsetSupersetEObjectEList.html)<E>

Since:
1.2
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectWithInverseEList)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[SubsetSupersetEObjectWithInverseEList.ManyInverse](SubsetSupersetEObjectWithInverseEList.ManyInverse.html)<[E](SubsetSupersetEObjectWithInverseEList.ManyInverse.html)>`

`static class`
`[SubsetSupersetEObjectWithInverseEList.Unsettable](SubsetSupersetEObjectWithInverseEList.Unsettable.html)<[E](SubsetSupersetEObjectWithInverseEList.Unsettable.html)>`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected final int`
`[inverseFeatureID](#inverseFeatureID)`
Fields inherited from class com.nomagic.magicdraw.uml2.util.[SubsetSupersetEObjectEList](SubsetSupersetEObjectEList.html)
`[subsetFeatureIDs](SubsetSupersetEObjectEList.html#subsetFeatureIDs), [supersetFeatureIDs](SubsetSupersetEObjectEList.html#supersetFeatureIDs)`
Fields inherited from class org.eclipse.emf.ecore.util.EObjectEList
`featureID`
Fields inherited from class org.eclipse.emf.ecore.util.EcoreEList
`dataClass, owner`
Fields inherited from class org.eclipse.emf.common.util.BasicEList
`data, size`
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SubsetSupersetEObjectWithInverseEList](#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D,int%5B%5D,int))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] supersetFeatureIDs,
 int[] subsetFeatureIDs,
 int inverseFeatureID)`
Creates and initializes a new `SubsetSupersetEObjectWithInverseEList` instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?>`
`[getInverseFeatureClass](#getInverseFeatureClass())()`

`int`
`[getInverseFeatureID](#getInverseFeatureID())()`

`protected boolean`
`[hasInverse](#hasInverse())()`

`protected boolean`
`[hasNavigableInverse](#hasNavigableInverse())()`
Methods inherited from class com.nomagic.magicdraw.uml2.util.[SubsetSupersetEObjectEList](SubsetSupersetEObjectEList.html)
`[add](SubsetSupersetEObjectEList.html#add(int,E)), [add](SubsetSupersetEObjectEList.html#add(E)), [addAll](SubsetSupersetEObjectEList.html#addAll(int,java.util.Collection)), [addAll](SubsetSupersetEObjectEList.html#addAll(java.util.Collection)), [basicAdd](SubsetSupersetEObjectEList.html#basicAdd(E,org.eclipse.emf.common.notify.NotificationChain)), [basicSet](SubsetSupersetEObjectEList.html#basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain)), [basicSupersetAdd](SubsetSupersetEObjectEList.html#basicSupersetAdd(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)), [didRemove](SubsetSupersetEObjectEList.html#didRemove(int,E)), [enforceSubsetConstraints](SubsetSupersetEObjectEList.html#enforceSubsetConstraints()), [enforceSupersetConstraints](SubsetSupersetEObjectEList.html#enforceSupersetConstraints()), [replaceOrAddToSuperset](SubsetSupersetEObjectEList.html#replaceOrAddToSuperset(java.lang.Object,java.lang.Object)), [resolve](SubsetSupersetEObjectEList.html#resolve(int,org.eclipse.emf.ecore.EObject)), [set](SubsetSupersetEObjectEList.html#set(int,E)), [subsetRemove](SubsetSupersetEObjectEList.html#subsetRemove(java.lang.Object)), [supersetAdd](SubsetSupersetEObjectEList.html#supersetAdd(java.lang.Object))`
Methods inherited from class com.nomagic.magicdraw.uml2.util.[ModelEObjectEList](ModelEObjectEList.html)
`[checkCompatibility](ModelEObjectEList.html#checkCompatibility(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature,E)), [createOperationTimeoutException](ModelEObjectEList.html#createOperationTimeoutException()), [getEventSupporter](ModelEObjectEList.html#getEventSupporter()), [getLockProvider](ModelEObjectEList.html#getLockProvider())`
Methods inherited from class com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList
`addAllUnique, addUnique, addUnique, afterChange, assign, basicContains, basicContainsAll, basicGet, basicIndexOf, basicLastIndexOf, basicList, basicToArray, basicToArray, beforeChange, clear, contains, doMove, doRemove, execute, firePropertyChange, get, getPropertyEventName, hasManyInverse, indexOf, isEmpty, lastIndexOf, move, primitiveGet, remove, removeAll, setUnique, size, startLogEvents, stopLogEvents, validate`
Methods inherited from class org.eclipse.emf.ecore.util.EObjectEList
`canContainNull, getFeatureID, isEObject, isUnique, resolve, useEquals`
Methods inherited from class org.eclipse.emf.ecore.util.EcoreEList
`createNotification, createNotification, dispatchNotification, get, getEObject, getEStructuralFeature, getFeature, getFeatureType, getInverseEReference, getNotifier, hasInstanceClass, hasProxies, inverseAdd, inverseRemove, isContainment, isInstance, isNotificationRequired, isSet, newData, resolve, resolveProxy, set, toArray, toArray, unset`
Methods inherited from class org.eclipse.emf.ecore.util.NotifyingInternalEListImpl
`basicIterator, basicListIterator, basicListIterator`
Methods inherited from class org.eclipse.emf.common.notify.impl.NotifyingListImpl
`addAllUnique, addAllUnique, addAllUnique, basicRemove, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet`
Methods inherited from class org.eclipse.emf.common.util.BasicEList
`clone, data, grow, setData, shrink`
Methods inherited from class org.eclipse.emf.common.util.AbstractEList
`didAdd, didChange, didClear, didMove, didSet, equalObjects, equals, getDuplicates, getNonDuplicates, hashCode, iterator, listIterator, listIterator, move, remove, retainAll, toString`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[removeRange](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.util.[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)
`[containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface org.eclipse.emf.common.util.EList
`move`
Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList
`addAllUnique, basicIterator, basicListIterator, basicListIterator, basicRemove`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)
`[addFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)), [addLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)), [containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [getFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()), [getLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator(int)), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [removeFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()), [removeLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()), [replaceAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()), [sort](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int))`

============ FIELD DETAIL =========== 
Field Details
inverseFeatureID
protected final int inverseFeatureID
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SubsetSupersetEObjectWithInverseEList
public SubsetSupersetEObjectWithInverseEList([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 @CheckForNull
 int[] supersetFeatureIDs,
 @CheckForNull
 int[] subsetFeatureIDs,
 int inverseFeatureID)
Creates and initializes a new `SubsetSupersetEObjectWithInverseEList` instance.
Parameters:
`dataClass` - data class.
`owner` - owner of the setting.
`featureID` - feature id.
`supersetFeatureIDs` - array of superset features.
`subsetFeatureIDs` - array of subset features.
`inverseFeatureID` - if of inverse feature.
 ============ METHOD DETAIL ========== 
Method Details
hasInverse
protected boolean hasInverse()
Overrides:
`hasInverse` in class `com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<[E](SubsetSupersetEObjectWithInverseEList.html)>`
hasNavigableInverse
protected boolean hasNavigableInverse()
Overrides:
`hasNavigableInverse` in class `com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<[E](SubsetSupersetEObjectWithInverseEList.html)>`
getInverseFeatureID
public int getInverseFeatureID()
Overrides:
`getInverseFeatureID` in class `org.eclipse.emf.ecore.util.EcoreEList<[E](SubsetSupersetEObjectWithInverseEList.html)>`
getInverseFeatureClass
public [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> getInverseFeatureClass()
Overrides:
`getInverseFeatureClass` in class `org.eclipse.emf.ecore.util.EcoreEList<[E](SubsetSupersetEObjectWithInverseEList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class SubsetSupersetEObjectWithInverseEList">Class SubsetSupersetEObjectWithInverseEList&lt;E&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.AbstractEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.BasicEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.notify.impl.NotifyingListImpl&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.NotifyingInternalEListImpl&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.EcoreEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.ecore.util.EObjectEList&lt;E&gt;
<div class="inheritance">com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;E&gt;
<div class="inheritance"><a href="ModelEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">com.nomagic.magicdraw.uml2.util.ModelEObjectEList</a>&lt;E&gt;
<div class="inheritance"><a href="SubsetSupersetEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEList</a>&lt;E&gt;
<div class="inheritance">com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectWithInverseEList&lt;E&gt;</div>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;E&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/RandomAccess.html" title="class or interface in java.util">RandomAccess</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html" title="class or interface in java.util">SequencedCollection</a>&lt;E&gt;</code>, <code>org.eclipse.emf.common.notify.NotifyingList&lt;E&gt;</code>, <code>org.eclipse.emf.common.util.EList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.EStructuralFeature.Setting</code>, <code>org.eclipse.emf.ecore.util.InternalEList&lt;E&gt;</code>, <code>org.eclipse.emf.ecore.util.InternalEList.Unsettable&lt;E&gt;</code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="SubsetSupersetEObjectWithInverseEList.ManyInverse.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectWithInverseEList.ManyInverse</a></code>, <code><a href="SubsetSupersetEObjectWithInverseEList.Unsettable.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectWithInverseEList.Unsettable</a></code>, <code><a href="SubsetSupersetEObjectWithInverseResolvingEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectWithInverseResolvingEList</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">SubsetSupersetEObjectWithInverseEList&lt;E&gt;</span>
<span class="extends-implements">extends <a href="SubsetSupersetEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEList</a>&lt;E&gt;</span></div>
<dl class="notes">
<dt>Since:</dt>
<dd>1.2</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectWithInverseEList">Serialized Form</a></li>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="SubsetSupersetEObjectWithInverseEList.ManyInverse.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectWithInverseEList.ManyInverse</a>&lt;<a href="SubsetSupersetEObjectWithInverseEList.ManyInverse.html" title="type parameter in SubsetSupersetEObjectWithInverseEList.ManyInverse">E</a>&gt;</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="SubsetSupersetEObjectWithInverseEList.Unsettable.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectWithInverseEList.Unsettable</a>&lt;<a href="SubsetSupersetEObjectWithInverseEList.Unsettable.html" title="type parameter in SubsetSupersetEObjectWithInverseEList.Unsettable">E</a>&gt;</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#inverseFeatureID">inverseFeatureID</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEList">Fields inherited from class com.nomagic.magicdraw.uml2.util.<a href="SubsetSupersetEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEList</a></h3>
<code><a href="SubsetSupersetEObjectEList.html#subsetFeatureIDs">subsetFeatureIDs</a>, <a href="SubsetSupersetEObjectEList.html#supersetFeatureIDs">supersetFeatureIDs</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.ecore.util.EObjectEList">Fields inherited from class org.eclipse.emf.ecore.util.EObjectEList</h3>
<code>featureID</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.ecore.util.EcoreEList">Fields inherited from class org.eclipse.emf.ecore.util.EcoreEList</h3>
<code>dataClass, owner</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.eclipse.emf.common.util.BasicEList">Fields inherited from class org.eclipse.emf.common.util.BasicEList</h3>
<code>data, size</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int%5B%5D,int%5B%5D,int)">SubsetSupersetEObjectWithInverseEList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 int[] supersetFeatureIDs,
 int[] subsetFeatureIDs,
 int inverseFeatureID)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>SubsetSupersetEObjectWithInverseEList</code> instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInverseFeatureClass()">getInverseFeatureClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInverseFeatureID()">getInverseFeatureID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasInverse()">hasInverse</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasNavigableInverse()">hasNavigableInverse</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml2.util.SubsetSupersetEObjectEList">Methods inherited from class com.nomagic.magicdraw.uml2.util.<a href="SubsetSupersetEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEList</a></h3>
<code><a href="SubsetSupersetEObjectEList.html#add(int,E)">add</a>, <a href="SubsetSupersetEObjectEList.html#add(E)">add</a>, <a href="SubsetSupersetEObjectEList.html#addAll(int,java.util.Collection)">addAll</a>, <a href="SubsetSupersetEObjectEList.html#addAll(java.util.Collection)">addAll</a>, <a href="SubsetSupersetEObjectEList.html#basicAdd(E,org.eclipse.emf.common.notify.NotificationChain)">basicAdd</a>, <a href="SubsetSupersetEObjectEList.html#basicSet(int,E,org.eclipse.emf.common.notify.NotificationChain)">basicSet</a>, <a href="SubsetSupersetEObjectEList.html#basicSupersetAdd(java.lang.Object,org.eclipse.emf.common.notify.NotificationChain)">basicSupersetAdd</a>, <a href="SubsetSupersetEObjectEList.html#didRemove(int,E)">didRemove</a>, <a href="SubsetSupersetEObjectEList.html#enforceSubsetConstraints()">enforceSubsetConstraints</a>, <a href="SubsetSupersetEObjectEList.html#enforceSupersetConstraints()">enforceSupersetConstraints</a>, <a href="SubsetSupersetEObjectEList.html#replaceOrAddToSuperset(java.lang.Object,java.lang.Object)">replaceOrAddToSuperset</a>, <a href="SubsetSupersetEObjectEList.html#resolve(int,org.eclipse.emf.ecore.EObject)">resolve</a>, <a href="SubsetSupersetEObjectEList.html#set(int,E)">set</a>, <a href="SubsetSupersetEObjectEList.html#subsetRemove(java.lang.Object)">subsetRemove</a>, <a href="SubsetSupersetEObjectEList.html#supersetAdd(java.lang.Object)">supersetAdd</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml2.util.ModelEObjectEList">Methods inherited from class com.nomagic.magicdraw.uml2.util.<a href="ModelEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">ModelEObjectEList</a></h3>
<code><a href="ModelEObjectEList.html#checkCompatibility(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature,E)">checkCompatibility</a>, <a href="ModelEObjectEList.html#createOperationTimeoutException()">createOperationTimeoutException</a>, <a href="ModelEObjectEList.html#getEventSupporter()">getEventSupporter</a>, <a href="ModelEObjectEList.html#getLockProvider()">getLockProvider</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList">Methods inherited from class com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList</h3>
<code>addAllUnique, addUnique, addUnique, afterChange, assign, basicContains, basicContainsAll, basicGet, basicIndexOf, basicLastIndexOf, basicList, basicToArray, basicToArray, beforeChange, clear, contains, doMove, doRemove, execute, firePropertyChange, get, getPropertyEventName, hasManyInverse, indexOf, isEmpty, lastIndexOf, move, primitiveGet, remove, removeAll, setUnique, size, startLogEvents, stopLogEvents, validate</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.EObjectEList">Methods inherited from class org.eclipse.emf.ecore.util.EObjectEList</h3>
<code>canContainNull, getFeatureID, isEObject, isUnique, resolve, useEquals</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.EcoreEList">Methods inherited from class org.eclipse.emf.ecore.util.EcoreEList</h3>
<code>createNotification, createNotification, dispatchNotification, get, getEObject, getEStructuralFeature, getFeature, getFeatureType, getInverseEReference, getNotifier, hasInstanceClass, hasProxies, inverseAdd, inverseRemove, isContainment, isInstance, isNotificationRequired, isSet, newData, resolve, resolveProxy, set, toArray, toArray, unset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.NotifyingInternalEListImpl">Methods inherited from class org.eclipse.emf.ecore.util.NotifyingInternalEListImpl</h3>
<code>basicIterator, basicListIterator, basicListIterator</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.impl.NotifyingListImpl">Methods inherited from class org.eclipse.emf.common.notify.impl.NotifyingListImpl</h3>
<code>addAllUnique, addAllUnique, addAllUnique, basicRemove, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.BasicEList">Methods inherited from class org.eclipse.emf.common.util.BasicEList</h3>
<code>clone, data, grow, setData, shrink</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEList">Methods inherited from class org.eclipse.emf.common.util.AbstractEList</h3>
<code>didAdd, didChange, didClear, didMove, didSet, equalObjects, equals, getDuplicates, getNonDuplicates, hashCode, iterator, listIterator, listIterator, move, remove, retainAll, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractCollection">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.EList">Methods inherited from interface org.eclipse.emf.common.util.EList</h3>
<code>move</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.InternalEList">Methods inherited from interface org.eclipse.emf.ecore.util.InternalEList</h3>
<code>addAllUnique, basicIterator, basicListIterator, basicListIterator, basicRemove</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)" title="class or interface in java.util">addFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)" title="class or interface in java.util">addLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()" title="class or interface in java.util">getFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()" title="class or interface in java.util">getLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()" title="class or interface in java.util">removeFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()" title="class or interface in java.util">removeLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
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
<section class="detail" id="inverseFeatureID">
<h3>inverseFeatureID</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">int</span> <span class="element-name">inverseFeatureID</span></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int,int[],int[],int)">
<h3>SubsetSupersetEObjectWithInverseEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SubsetSupersetEObjectWithInverseEList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID,
 @CheckForNull
 int[] supersetFeatureIDs,
 @CheckForNull
 int[] subsetFeatureIDs,
 int inverseFeatureID)</span></div>
<div class="block">Creates and initializes a new <code>SubsetSupersetEObjectWithInverseEList</code> instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataClass</code> - data class.</dd>
<dd><code>owner</code> - owner of the setting.</dd>
<dd><code>featureID</code> - feature id.</dd>
<dd><code>supersetFeatureIDs</code> - array of superset features.</dd>
<dd><code>subsetFeatureIDs</code> - array of subset features.</dd>
<dd><code>inverseFeatureID</code> - if of inverse feature.</dd>
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
<section class="detail" id="hasInverse()">
<h3>hasInverse</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasInverse</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>hasInverse</code> in class <code>com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;<a href="SubsetSupersetEObjectWithInverseEList.html" title="type parameter in SubsetSupersetEObjectWithInverseEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasNavigableInverse()">
<h3>hasNavigableInverse</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">hasNavigableInverse</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>hasNavigableInverse</code> in class <code>com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;<a href="SubsetSupersetEObjectWithInverseEList.html" title="type parameter in SubsetSupersetEObjectWithInverseEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInverseFeatureID()">
<h3>getInverseFeatureID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getInverseFeatureID</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getInverseFeatureID</code> in class <code>org.eclipse.emf.ecore.util.EcoreEList&lt;<a href="SubsetSupersetEObjectWithInverseEList.html" title="type parameter in SubsetSupersetEObjectWithInverseEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInverseFeatureClass()">
<h3>getInverseFeatureClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">getInverseFeatureClass</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getInverseFeatureClass</code> in class <code>org.eclipse.emf.ecore.util.EcoreEList&lt;<a href="SubsetSupersetEObjectWithInverseEList.html" title="type parameter in SubsetSupersetEObjectWithInverseEList">E</a>&gt;</code></dd>
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
