# JAVA OPENAPI: FastContainsList (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml2/util/FastContainsList.html
- source_path: `com/nomagic/magicdraw/uml2/util/FastContainsList.html`
- source_sha256: `fb9afd5d2382590c4739bc7fb53b40601e4ca5504974fb3df34b3cbc964e366e`
- captured_utc: `2026-07-14T16:56:06.631583+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Class FastContainsList<T>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html)<E>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)<E>
org.eclipse.emf.common.util.AbstractEList<E>
org.eclipse.emf.common.util.BasicEList<E>
org.eclipse.emf.common.util.UniqueEList<E>
org.eclipse.emf.common.util.UniqueEList.FastCompare<T>
com.nomagic.magicdraw.uml2.util.FastContainsList<T>

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)<T>`, `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T>`, `[RandomAccess](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/RandomAccess.html)`, `org.eclipse.emf.common.util.EList<T>`

public classFastContainsList<T>
extends org.eclipse.emf.common.util.UniqueEList.FastCompare<T>

Unique value list that supports fast contains method.

Version:
1.0
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.FastContainsList)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class org.eclipse.emf.common.util.BasicEList
`data, size`
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FastContainsList](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[add](#add(int,T))(int index,
 [T](FastContainsList.html) object)`

`boolean`
`[add](#add(T))([T](FastContainsList.html) object)`

`boolean`
`[contains](#contains(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)`

`[T](FastContainsList.html)`
`[remove](#remove(int))(int index)`

`[T](FastContainsList.html)`
`[set](#set(int,T))(int index,
 [T](FastContainsList.html) object)`

`protected [T](FastContainsList.html)`
`[validate](#validate(int,T))(int index,
 [T](FastContainsList.html) object)`
Methods inherited from class org.eclipse.emf.common.util.UniqueEList.FastCompare
`useEquals`
Methods inherited from class org.eclipse.emf.common.util.UniqueEList
`isUnique`
Methods inherited from class org.eclipse.emf.common.util.BasicEList
`addAllUnique, addAllUnique, addAllUnique, addAllUnique, addUnique, addUnique, assign, basicGet, basicList, clear, clone, data, get, grow, indexOf, isEmpty, lastIndexOf, move, newData, primitiveGet, setData, setUnique, shrink, size, toArray, toArray`
Methods inherited from class org.eclipse.emf.common.util.AbstractEList
`addAll, addAll, basicIterator, basicListIterator, basicListIterator, canContainNull, didAdd, didChange, didClear, didMove, didRemove, didSet, equalObjects, equals, getDuplicates, getNonDuplicates, hashCode, iterator, listIterator, listIterator, move, remove, removeAll, resolve, retainAll, toString`
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html)
`[removeRange](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.util.[AbstractCollection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html)
`[containsAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)
`[containsAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [replaceAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [sort](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()), [subList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FastContainsList
public FastContainsList()
 ============ METHOD DETAIL ========== 
Method Details
add
public boolean add([T](FastContainsList.html) object)
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[T](FastContainsList.html)>`
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[T](FastContainsList.html)>`
Overrides:
`add` in class `org.eclipse.emf.common.util.AbstractEList<[T](FastContainsList.html)>`
add
public void add(int index,
 [T](FastContainsList.html) object)
Specified by:
`[add](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(int,E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[T](FastContainsList.html)>`
Overrides:
`add` in class `org.eclipse.emf.common.util.AbstractEList<[T](FastContainsList.html)>`
set
public [T](FastContainsList.html) set(int index,
 [T](FastContainsList.html) object)
Specified by:
`[set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#set(int,E))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[T](FastContainsList.html)>`
Overrides:
`set` in class `org.eclipse.emf.common.util.AbstractEList<[T](FastContainsList.html)>`
remove
@CheckForNullpublic [T](FastContainsList.html) remove(int index)
Specified by:
`[remove](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(int))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[T](FastContainsList.html)>`
Overrides:
`remove` in class `org.eclipse.emf.common.util.BasicEList<[T](FastContainsList.html)>`
contains
public boolean contains([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) object)
Specified by:
`[contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#contains(java.lang.Object))` in interface `[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[T](FastContainsList.html)>`
Specified by:
`[contains](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#contains(java.lang.Object))` in interface `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[T](FastContainsList.html)>`
Overrides:
`contains` in class `org.eclipse.emf.common.util.BasicEList<[T](FastContainsList.html)>`
validate
protected [T](FastContainsList.html) validate(int index,
 [T](FastContainsList.html) object)
Overrides:
`validate` in class `org.eclipse.emf.common.util.AbstractEList<[T](FastContainsList.html)>`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Class FastContainsList">Class FastContainsList&lt;T&gt;</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;E&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.AbstractEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.BasicEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.UniqueEList&lt;E&gt;
<div class="inheritance">org.eclipse.emf.common.util.UniqueEList.FastCompare&lt;T&gt;
<div class="inheritance">com.nomagic.magicdraw.uml2.util.FastContainsList&lt;T&gt;</div>
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
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;T&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/RandomAccess.html" title="class or interface in java.util">RandomAccess</a></code>, <code>org.eclipse.emf.common.util.EList&lt;T&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">FastContainsList&lt;T&gt;</span>
<span class="extends-implements">extends org.eclipse.emf.common.util.UniqueEList.FastCompare&lt;T&gt;</span></div>
<div class="block">Unique value list that supports fast contains method.</div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.uml2.util.FastContainsList">Serialized Form</a></li>
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
<h3 id="fields-inherited-from-class-org.eclipse.emf.common.util.BasicEList">Fields inherited from class org.eclipse.emf.common.util.BasicEList</h3>
<code>data, size</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FastContainsList</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(int,T)">add</a><wbr/>(int index,
 <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(T)">add</a><wbr/>(<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#contains(java.lang.Object)">contains</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FastContainsList.html" title="type parameter in FastContainsList">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(int)">remove</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FastContainsList.html" title="type parameter in FastContainsList">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#set(int,T)">set</a><wbr/>(int index,
 <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#validate(int,T)">validate</a><wbr/>(int index,
 <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.UniqueEList.FastCompare">Methods inherited from class org.eclipse.emf.common.util.UniqueEList.FastCompare</h3>
<code>useEquals</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.UniqueEList">Methods inherited from class org.eclipse.emf.common.util.UniqueEList</h3>
<code>isUnique</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.BasicEList">Methods inherited from class org.eclipse.emf.common.util.BasicEList</h3>
<code>addAllUnique, addAllUnique, addAllUnique, addAllUnique, addUnique, addUnique, assign, basicGet, basicList, clear, clone, data, get, grow, indexOf, isEmpty, lastIndexOf, move, newData, primitiveGet, setData, setUnique, shrink, size, toArray, toArray</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.eclipse.emf.common.util.AbstractEList">Methods inherited from class org.eclipse.emf.common.util.AbstractEList</h3>
<code>addAll, addAll, basicIterator, basicListIterator, basicListIterator, canContainNull, didAdd, didChange, didClear, didMove, didRemove, didSet, equalObjects, equals, getDuplicates, getNonDuplicates, hashCode, iterator, listIterator, listIterator, move, remove, removeAll, resolve, retainAll, toString</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractCollection">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
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
<h3>FastContainsList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FastContainsList</span>()</div>
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
<section class="detail" id="add(T)">
<h3 id="add(java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>add</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(int,T)">
<h3 id="add(int,java.lang.Object)">add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(int index,
 <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#add(int,E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>add</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="set(int,T)">
<h3 id="set(int,java.lang.Object)">set</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="FastContainsList.html" title="type parameter in FastContainsList">T</a></span> <span class="element-name">set</span><wbr/><span class="parameters">(int index,
 <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#set(int,E)" title="class or interface in java.util">set</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>set</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(int)">
<h3>remove</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="FastContainsList.html" title="type parameter in FastContainsList">T</a></span> <span class="element-name">remove</span><wbr/><span class="parameters">(int index)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#remove(int)" title="class or interface in java.util">remove</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>remove</code> in class <code>org.eclipse.emf.common.util.BasicEList&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(java.lang.Object)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code>contains</code> in class <code>org.eclipse.emf.common.util.BasicEList&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="validate(int,T)">
<h3 id="validate(int,java.lang.Object)">validate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="FastContainsList.html" title="type parameter in FastContainsList">T</a></span> <span class="element-name">validate</span><wbr/><span class="parameters">(int index,
 <a href="FastContainsList.html" title="type parameter in FastContainsList">T</a> object)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>validate</code> in class <code>org.eclipse.emf.common.util.AbstractEList&lt;<a href="FastContainsList.html" title="type parameter in FastContainsList">T</a>&gt;</code></dd>
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
