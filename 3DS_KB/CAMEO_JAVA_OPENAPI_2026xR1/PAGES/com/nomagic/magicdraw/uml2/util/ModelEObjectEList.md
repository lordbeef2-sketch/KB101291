# JAVA OPENAPI: ModelEObjectEList (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml2/util/ModelEObjectEList.html
- source_path: `com/nomagic/magicdraw/uml2/util/ModelEObjectEList.html`
- source_sha256: `b29fefe401f7564c5cc9f0b9154dc872c7ea37ca34adb048335d7138c8db1329`
- captured_utc: `2026-07-14T16:46:09.520926+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class ModelEObjectEList<E>

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
com.nomagic.magicdraw.uml2.util.ModelEObjectEList<E>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<E>`, `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<E>`, `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<E>`, `[RandomAccess](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/RandomAccess.html)`, `[SequencedCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html)<E>`, `org.eclipse.emf.common.notify.NotifyingList<E>`, `org.eclipse.emf.common.util.EList<E>`, `org.eclipse.emf.ecore.EStructuralFeature.Setting`, `org.eclipse.emf.ecore.util.InternalEList<E>`, `org.eclipse.emf.ecore.util.InternalEList.Unsettable<E>`

Direct Known Subclasses:
`[ModelEObjectResolvingEList](ModelEObjectResolvingEList.html)`, `[SubsetSupersetEObjectEList](SubsetSupersetEObjectEList.html)`

public classModelEObjectEList<E>
extends com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<E>

Base class for all transient collections of the model.

Version:
1.0
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.ModelEObjectEList)

=========== FIELD SUMMARY =========== 
Field Summary
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
`[ModelEObjectEList](#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID)`
Creates and initializes a new `ModelEObjectEList` instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[checkCompatibility](#checkCompatibility(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature,E))(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 [E](ModelEObjectEList.html) object)`

`protected [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)`
`[createOperationTimeoutException](#createOperationTimeoutException())()`

`protected [EventSupporter](EventSupporter.html)`
`[getEventSupporter](#getEventSupporter())()`

`protected com.dassault_systemes.modeler.foundation.util.ModelLockProvider`
`[getLockProvider](#getLockProvider())()`
Methods inherited from class com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList
`addAllUnique, addUnique, addUnique, afterChange, assign, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicLastIndexOf, basicList, basicToArray, basicToArray, beforeChange, clear, contains, doMove, doRemove, execute, firePropertyChange, get, getPropertyEventName, hasInverse, hasManyInverse, hasNavigableInverse, indexOf, isEmpty, lastIndexOf, move, primitiveGet, remove, removeAll, setUnique, size, startLogEvents, stopLogEvents, validate`
Methods inherited from class org.eclipse.emf.ecore.util.EObjectEList
`canContainNull, getFeatureID, isEObject, isUnique, resolve, useEquals`
Methods inherited from class org.eclipse.emf.ecore.util.EcoreEList
`createNotification, createNotification, dispatchNotification, get, getEObject, getEStructuralFeature, getFeature, getFeatureType, getInverseEReference, getInverseFeatureClass, getInverseFeatureID, getNotifier, hasInstanceClass, hasProxies, inverseAdd, inverseRemove, isContainment, isInstance, isNotificationRequired, isSet, newData, resolve, resolve, resolveProxy, set, toArray, toArray, unset`
Methods inherited from class org.eclipse.emf.ecore.util.NotifyingInternalEListImpl
`basicIterator, basicListIterator, basicListIterator`
Methods inherited from class org.eclipse.emf.common.notify.impl.NotifyingListImpl
`addAllUnique, addAllUnique, addAllUnique, basicRemove, basicSet, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet`
Methods inherited from class org.eclipse.emf.common.util.BasicEList
`clone, data, grow, setData, shrink`
Methods inherited from class org.eclipse.emf.common.util.AbstractEList
`add, add, addAll, addAll, didAdd, didChange, didClear, didMove, didRemove, didSet, equalObjects, equals, getDuplicates, getNonDuplicates, hashCode, iterator, listIterator, listIterator, move, remove, retainAll, set, toString`
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
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(int,E)), [add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E)), [addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)), [addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)), [addFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)), [addLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)), [containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)), [getFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()), [getLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator(int)), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [removeFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()), [removeLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()), [replaceAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()), [set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#set(int,E)), [sort](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ModelEObjectEList
public ModelEObjectEList([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID)
Creates and initializes a new `ModelEObjectEList` instance.
Parameters:
`dataClass` - data class.
`owner` - owner of the setting.
`featureID` - feature id.
 ============ METHOD DETAIL ========== 
Method Details
getEventSupporter
protected [EventSupporter](EventSupporter.html) getEventSupporter()
Specified by:
`getEventSupporter` in class `com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<[E](ModelEObjectEList.html)>`
getLockProvider
@CheckForNullprotected com.dassault_systemes.modeler.foundation.util.ModelLockProvider getLockProvider()
Specified by:
`getLockProvider` in class `com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<[E](ModelEObjectEList.html)>`
createOperationTimeoutException
protected [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html) createOperationTimeoutException()
Specified by:
`createOperationTimeoutException` in class `com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<[E](ModelEObjectEList.html)>`
checkCompatibility
protected void checkCompatibility(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 [E](ModelEObjectEList.html) object)
Specified by:
`checkCompatibility` in class `com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList<[E](ModelEObjectEList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class ModelEObjectEList">Class ModelEObjectEList&lt;E&gt;</h1>
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
<div class="inheritance">com.nomagic.magicdraw.uml2.util.ModelEObjectEList&lt;E&gt;</div>
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
<dd><code><a href="ModelEObjectResolvingEList.html" title="class in com.nomagic.magicdraw.uml2.util">ModelEObjectResolvingEList</a></code>, <code><a href="SubsetSupersetEObjectEList.html" title="class in com.nomagic.magicdraw.uml2.util">SubsetSupersetEObjectEList</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">ModelEObjectEList&lt;E&gt;</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;E&gt;</span></div>
<div class="block">Base class for all transient collections of the model.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.ModelEObjectEList">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int)">ModelEObjectEList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>ModelEObjectEList</code> instance.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkCompatibility(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature,E)">checkCompatibility</a><wbr/>(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 <a href="ModelEObjectEList.html" title="type parameter in ModelEObjectEList">E</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOperationTimeoutException()">createOperationTimeoutException</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="EventSupporter.html" title="interface in com.nomagic.magicdraw.uml2.util">EventSupporter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEventSupporter()">getEventSupporter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.dassault_systemes.modeler.foundation.util.ModelLockProvider</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLockProvider()">getLockProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList">Methods inherited from class com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList</h3>
<code>addAllUnique, addUnique, addUnique, afterChange, assign, basicAdd, basicContains, basicContainsAll, basicGet, basicIndexOf, basicLastIndexOf, basicList, basicToArray, basicToArray, beforeChange, clear, contains, doMove, doRemove, execute, firePropertyChange, get, getPropertyEventName, hasInverse, hasManyInverse, hasNavigableInverse, indexOf, isEmpty, lastIndexOf, move, primitiveGet, remove, removeAll, setUnique, size, startLogEvents, stopLogEvents, validate</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.EObjectEList">Methods inherited from class org.eclipse.emf.ecore.util.EObjectEList</h3>
<code>canContainNull, getFeatureID, isEObject, isUnique, resolve, useEquals</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.EcoreEList">Methods inherited from class org.eclipse.emf.ecore.util.EcoreEList</h3>
<code>createNotification, createNotification, dispatchNotification, get, getEObject, getEStructuralFeature, getFeature, getFeatureType, getInverseEReference, getInverseFeatureClass, getInverseFeatureID, getNotifier, hasInstanceClass, hasProxies, inverseAdd, inverseRemove, isContainment, isInstance, isNotificationRequired, isSet, newData, resolve, resolve, resolveProxy, set, toArray, toArray, unset</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.ecore.util.NotifyingInternalEListImpl">Methods inherited from class org.eclipse.emf.ecore.util.NotifyingInternalEListImpl</h3>
<code>basicIterator, basicListIterator, basicListIterator</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.notify.impl.NotifyingListImpl">Methods inherited from class org.eclipse.emf.common.notify.impl.NotifyingListImpl</h3>
<code>addAllUnique, addAllUnique, addAllUnique, basicRemove, basicSet, createNotification, createNotificationChain, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddAllUnique, doAddUnique, doAddUnique, doClear, doRemoveAll, doSetUnique, getFeatureID, hasShadow, shadowAdd, shadowRemove, shadowSet</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.BasicEList">Methods inherited from class org.eclipse.emf.common.util.BasicEList</h3>
<code>clone, data, grow, setData, shrink</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEList">Methods inherited from class org.eclipse.emf.common.util.AbstractEList</h3>
<code>add, add, addAll, addAll, didAdd, didChange, didClear, didMove, didRemove, didSet, equalObjects, equals, getDuplicates, getNonDuplicates, hashCode, iterator, listIterator, listIterator, move, remove, retainAll, set, toString</code></div>
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
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(int,E)" title="class or interface in java.util">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(int,java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)" title="class or interface in java.util">addFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)" title="class or interface in java.util">addLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()" title="class or interface in java.util">getFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()" title="class or interface in java.util">getLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()" title="class or interface in java.util">removeFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()" title="class or interface in java.util">removeLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#set(int,E)" title="class or interface in java.util">set</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.Class,org.eclipse.emf.ecore.InternalEObject,int)">
<h3>ModelEObjectEList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ModelEObjectEList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; dataClass,
 org.eclipse.emf.ecore.InternalEObject owner,
 int featureID)</span></div>
<div class="block">Creates and initializes a new <code>ModelEObjectEList</code> instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataClass</code> - data class.</dd>
<dd><code>owner</code> - owner of the setting.</dd>
<dd><code>featureID</code> - feature id.</dd>
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
<section class="detail" id="getEventSupporter()">
<h3>getEventSupporter</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="EventSupporter.html" title="interface in com.nomagic.magicdraw.uml2.util">EventSupporter</a></span> <span class="element-name">getEventSupporter</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getEventSupporter</code> in class <code>com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;<a href="ModelEObjectEList.html" title="type parameter in ModelEObjectEList">E</a>&gt;</code></dd>
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
<dd><code>getLockProvider</code> in class <code>com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;<a href="ModelEObjectEList.html" title="type parameter in ModelEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOperationTimeoutException()">
<h3>createOperationTimeoutException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span> <span class="element-name">createOperationTimeoutException</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>createOperationTimeoutException</code> in class <code>com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;<a href="ModelEObjectEList.html" title="type parameter in ModelEObjectEList">E</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkCompatibility(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature,E)">
<h3 id="checkCompatibility(org.eclipse.emf.ecore.InternalEObject,org.eclipse.emf.ecore.EStructuralFeature,java.lang.Object)">checkCompatibility</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">checkCompatibility</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.InternalEObject owner,
 org.eclipse.emf.ecore.EStructuralFeature feature,
 <a href="ModelEObjectEList.html" title="type parameter in ModelEObjectEList">E</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>checkCompatibility</code> in class <code>com.dassault_systemes.modeler.foundation.util.AbstractModelEObjectEList&lt;<a href="ModelEObjectEList.html" title="type parameter in ModelEObjectEList">E</a>&gt;</code></dd>
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
