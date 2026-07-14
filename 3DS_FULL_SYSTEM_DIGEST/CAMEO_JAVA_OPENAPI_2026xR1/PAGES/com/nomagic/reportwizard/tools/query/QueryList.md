# JAVA OPENAPI: QueryList (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/query/QueryList.html
- source_path: `com/nomagic/reportwizard/tools/query/QueryList.html`
- source_sha256: `2077762144ae35d2514282cf116ab369eeceb1f8721d3209ddcb5fcd67abbaea`
- captured_utc: `2026-07-14T16:46:15.939013+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.query](package-summary.html)

## Class QueryList

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
[java.util.AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.reportwizard.tools.query.QueryList

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`, `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`, `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`, `[SequencedCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`

@OpenApiAllpublic classQueryList
extends [AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
implements [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

Query result collection.

Since:
Jan 28, 2013
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.reportwizard.tools.query.QueryList)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[modCount](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#modCount)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[QueryList](#%3Cinit%3E())()`
QueryList constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[add](#add(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e)`

`boolean`
`[addAll](#addAll(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) col)`
Add collection to QueryList.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[first](#first())()`
Return the first element from collection.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[get](#get(int))(int index)`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[last](#last())()`
Return the last element from collection.
`int`
`[size](#size())()`

`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[unique](#unique())()`
return the first element from collection (equivalent to [`first()`](#first()).
Methods inherited from class java.util.[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#add(int,E)), [addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#addAll(int,java.util.Collection)), [clear](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#clear()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#hashCode()), [indexOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#indexOf(java.lang.Object)), [iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#iterator()), [lastIndexOf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#lastIndexOf(java.lang.Object)), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#listIterator()), [listIterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#listIterator(int)), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#remove(int)), [removeRange](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)), [set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#set(int,E)), [subList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int))`
Methods inherited from class java.util.[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)
`[contains](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#contains(java.lang.Object)), [containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#isEmpty()), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#remove(java.lang.Object)), [removeAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#removeAll(java.util.Collection)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#retainAll(java.util.Collection)), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray(T%5B%5D)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface java.util.[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)
`[parallelStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()), [removeIf](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)), [stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction))`
Methods inherited from interface java.lang.[Iterable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html)
`[forEach](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer))`
Methods inherited from interface java.util.[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)
`[addFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)), [addLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)), [contains](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#contains(java.lang.Object)), [containsAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)), [getFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()), [getLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()), [isEmpty](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#isEmpty()), [remove](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)), [removeAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)), [removeFirst](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()), [removeLast](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()), [replaceAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)), [retainAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)), [reversed](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()), [sort](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)), [spliterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray()), [toArray](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray(T%5B%5D))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
QueryList
public QueryList()
QueryList constructor.
 ============ METHOD DETAIL ========== 
Method Details
get
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) get(int index)
Specified by:
`[get](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#get(int))` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Specified by:
`[get](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#get(int))` in class `[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
size
public int size()
Specified by:
`[size](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#size())` in interface `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Specified by:
`[size](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#size())` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Specified by:
`[size](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#size())` in class `[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
add
public boolean add([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) e)
Specified by:
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#add(E))` in interface `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Specified by:
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E))` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Overrides:
`[add](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#add(E))` in class `[AbstractList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
addAll
public boolean addAll([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html) col)
Add collection to QueryList.
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#addAll(java.util.Collection))` in interface `[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Specified by:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection))` in interface `[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Overrides:
`[addAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#addAll(java.util.Collection))` in class `[AbstractCollection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
Parameters:
`col` - collection
Returns:
true after finish add collection
first
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) first()
Return the first element from collection.
Returns:
first element
last
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) last()
Return the last element from collection.
Returns:
last element
unique
public [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) unique()
return the first element from collection (equivalent to [`first()`](#first()).
Returns:
Element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.query</a></div>
<h1 class="title" title="Class QueryList">Class QueryList</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">java.util.AbstractCollection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">java.util.AbstractList</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;
<div class="inheritance">com.nomagic.reportwizard.tools.query.QueryList</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/SequencedCollection.html" title="class or interface in java.util">SequencedCollection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">QueryList</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Query result collection.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 28, 2013</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.reportwizard.tools.query.QueryList">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">QueryList</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">QueryList constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">add</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addAll(java.util.Collection)">addAll</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> col)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add collection to QueryList.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#first()">first</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the first element from collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#get(int)">get</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#last()">last</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return the last element from collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#size()">size</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unique()">unique</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">return the first element from collection (equivalent to <a href="#first()"><code>first()</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractList">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#add(int,E)" title="class or interface in java.util">add</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#addAll(int,java.util.Collection)" title="class or interface in java.util">addAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#clear()" title="class or interface in java.util">clear</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)" title="class or interface in java.util">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#hashCode()" title="class or interface in java.util">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#indexOf(java.lang.Object)" title="class or interface in java.util">indexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#iterator()" title="class or interface in java.util">iterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#lastIndexOf(java.lang.Object)" title="class or interface in java.util">lastIndexOf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#listIterator()" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#listIterator(int)" title="class or interface in java.util">listIterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#remove(int)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#removeRange(int,int)" title="class or interface in java.util">removeRange</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#set(int,E)" title="class or interface in java.util">set</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#subList(int,int)" title="class or interface in java.util">subList</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.AbstractCollection">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray()" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toArray(T%5B%5D)" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#toString()" title="class or interface in java.util">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Collection">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#parallelStream()" title="class or interface in java.util">parallelStream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#removeIf(java.util.function.Predicate)" title="class or interface in java.util">removeIf</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#stream()" title="class or interface in java.util">stream</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#toArray(java.util.function.IntFunction)" title="class or interface in java.util">toArray</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Iterable">Methods inherited from interface java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html" title="class or interface in java.lang">Iterable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Iterable.html#forEach(java.util.function.Consumer)" title="class or interface in java.lang">forEach</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.List">Methods inherited from interface java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addFirst(E)" title="class or interface in java.util">addFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addLast(E)" title="class or interface in java.util">addLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#contains(java.lang.Object)" title="class or interface in java.util">contains</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#containsAll(java.util.Collection)" title="class or interface in java.util">containsAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getFirst()" title="class or interface in java.util">getFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#getLast()" title="class or interface in java.util">getLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#isEmpty()" title="class or interface in java.util">isEmpty</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#remove(java.lang.Object)" title="class or interface in java.util">remove</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeAll(java.util.Collection)" title="class or interface in java.util">removeAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeFirst()" title="class or interface in java.util">removeFirst</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#removeLast()" title="class or interface in java.util">removeLast</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#replaceAll(java.util.function.UnaryOperator)" title="class or interface in java.util">replaceAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#retainAll(java.util.Collection)" title="class or interface in java.util">retainAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#reversed()" title="class or interface in java.util">reversed</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#sort(java.util.Comparator)" title="class or interface in java.util">sort</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#spliterator()" title="class or interface in java.util">spliterator</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray()" title="class or interface in java.util">toArray</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#toArray(T%5B%5D)" title="class or interface in java.util">toArray</a></code></div>
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
<h3>QueryList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">QueryList</span>()</div>
<div class="block">QueryList constructor.</div>
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
<section class="detail" id="get(int)">
<h3>get</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">get</span><wbr/><span class="parameters">(int index)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#get(int)" title="class or interface in java.util">get</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#get(int)" title="class or interface in java.util">get</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="size()">
<h3>size</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">size</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#size()" title="class or interface in java.util">size</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#size()" title="class or interface in java.util">size</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#size()" title="class or interface in java.util">size</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#add(E)" title="class or interface in java.util">add</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html#add(E)" title="class or interface in java.util">add</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractList.html" title="class or interface in java.util">AbstractList</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addAll(java.util.Collection)">
<h3>addAll</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addAll</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> col)</span></div>
<div class="block">Add collection to QueryList.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html#addAll(java.util.Collection)" title="class or interface in java.util">addAll</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/AbstractCollection.html" title="class or interface in java.util">AbstractCollection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></dd>
<dt>Parameters:</dt>
<dd><code>col</code> - collection</dd>
<dt>Returns:</dt>
<dd>true after finish add collection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="first()">
<h3>first</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">first</span>()</div>
<div class="block">Return the first element from collection.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>first element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="last()">
<h3>last</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">last</span>()</div>
<div class="block">Return the last element from collection.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>last element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unique()">
<h3>unique</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">unique</span>()</div>
<div class="block">return the first element from collection (equivalent to <a href="#first()"><code>first()</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Element</dd>
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
